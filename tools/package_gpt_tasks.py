#!/usr/bin/env python3
"""Package the current manuscript and research context for two GPT tasks."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "outputs" / "gpt"
EXTENSIONS = {".md", ".tex", ".bib", ".pdf", ".png", ".svg", ".yaml"}
LICENSE_FILES = {"LICENSE", "NOTICE", "COMMERCIAL.md", "TRADEMARK.md"}


def package(task, prompt):
    files = [ROOT / "README.md", ROOT / "CLAUDE.md"]
    for directory in ("overleaf", "literature"):
        for path in sorted((ROOT / directory).rglob("*")):
            if not path.is_file():
                continue
            if path.suffix not in EXTENSIONS and path.name not in LICENSE_FILES:
                continue
            if "prompts" in path.parts and path.name != prompt:
                continue
            files.append(path)
    output = DEST / f"dca-{task}.zip"
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())
        archive.writestr(
            "START_HERE.txt",
            f"任务指令：overleaf/notes/prompts/{prompt}\n"
            "先读 overleaf/notes/progress/PROJECT_STATUS.md 与\n"
            "overleaf/notes/project/lower-bound-research-direction.md。\n"
            "包内保留材料相对路径。历史讨论中的旧绝对路径仅供追溯。\n",
        )
    print(f"{output.relative_to(ROOT)}: {len(files)} files, {output.stat().st_size:,} bytes")


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    package("literature", "gptpro-literature-research-prompt.md")
    package("refine", "gptpro-draft-review-prompt.md")
