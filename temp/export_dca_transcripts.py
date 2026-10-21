"""Export all DCA Claude Code transcripts as one Markdown file (dialogue text only).

Merges every JSONL snapshot of the project, deduplicates records by uuid, rebuilds
the message tree, prints the main line first and every other branch (forks,
rewinds, edited messages) afterwards with its branch point.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set

SKIP_PREFIXES = ("<", "Base directory for this skill", "[Request interrupted")
SKIP_TEXTS = {"No response requested."}

SOURCE_LABELS = {
    "c6c2c528": "主线：DCA证书与复杂度分析",
    "e55ca344": "Fork：DCA证书与复杂度分析 (fork)",
    "ba2d95f1": "Fork：btw: 这个显然吗？",
    "c9600c4d": "独立会话：DC算法维数复杂度分析",
}
MAIN_LEAF_FILE = "c6c2c528"
EXCLUDED_FILES = {"c67bc4cf"}  # today's export-only session


@dataclass
class Record:
    uuid: str
    parent: Optional[str]
    role: str
    time: str
    text: str
    files: Set[str] = field(default_factory=set)


def _text_of(d: dict) -> str:
    content = d.get("message", {}).get("content")
    if isinstance(content, str):
        return content
    parts = [
        x.get("text", "")
        for x in (content or [])
        if isinstance(x, dict) and x.get("type") == "text"
    ]
    return "\n\n".join(p for p in parts if p)


def load_records(folder: Path) -> Dict[str, Record]:
    records: Dict[str, Record] = {}
    for path in sorted(folder.glob("*.jsonl")):
        tag = path.name[:8]
        if tag in EXCLUDED_FILES:
            continue
        for line in path.open(encoding="utf-8"):
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            uid = d.get("uuid")
            if not uid:
                continue
            if uid in records:
                records[uid].files.add(tag)
                continue
            text = ""
            if d.get("type") in ("user", "assistant") and not d.get("isMeta") \
                    and not d.get("isCompactSummary"):
                text = _text_of(d).strip()
                if text.startswith(SKIP_PREFIXES) or text in SKIP_TEXTS:
                    text = ""
            records[uid] = Record(
                uuid=uid,
                parent=d.get("parentUuid") or d.get("logicalParentUuid"),
                role=d.get("type", ""),
                time=d.get("timestamp", ""),
                text=text,
                files={tag},
            )
    return records


def visible_parent(records: Dict[str, Record], uid: str) -> Optional[str]:
    cur = records[uid].parent
    while cur and cur in records and not records[cur].text:
        cur = records[cur].parent
    return cur if cur in records else None


def local_time(ts: str) -> str:
    if not ts:
        return ""
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
    return dt.strftime("%Y-%m-%d %H:%M")


def demote_headings(text: str) -> str:
    """Push message-internal headings below the export's own section level."""
    lines, in_code = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("#"):
            line = "##" + line
        lines.append(line)
    return "\n".join(lines)


def render_chain(chain: List[Record], out: List[str],
                 turn_no: Optional[Dict[str, int]] = None) -> None:
    prev_role = None
    for rec in chain:
        if rec.role != prev_role or rec.role == "user":
            who = "老大" if rec.role == "user" else "Claude"
            num = f"第 {turn_no[rec.uuid]} 轮 · " if turn_no and rec.role == "user" else ""
            out.append(f"\n---\n\n**{who}** · {num}{local_time(rec.time)}\n")
        out.append(demote_headings(rec.text) + "\n")
        prev_role = rec.role


def main(folder: Path, out_path: Path) -> None:
    records = load_records(folder)
    vis = {u: r for u, r in records.items() if r.text}
    vparent = {u: visible_parent(records, u) for u in vis}
    children: Dict[Optional[str], List[str]] = {}
    for u, p in vparent.items():
        children.setdefault(p, []).append(u)
    for kids in children.values():
        kids.sort(key=lambda k: vis[k].time)

    def leaf_of(tag: str) -> str:
        cand = [r for r in vis.values() if tag in r.files]
        return max(cand, key=lambda r: r.time).uuid

    def path_to(uid: str) -> List[str]:
        chain: List[str] = []
        cur: Optional[str] = uid
        while cur:
            chain.append(cur)
            cur = vparent[cur]
        return chain[::-1]

    main_path = path_to(leaf_of(MAIN_LEAF_FILE))
    done: Set[str] = set(main_path)
    turn_no = {}
    n = 0
    for u in main_path:
        if vis[u].role == "user":
            n += 1
        turn_no[u] = n

    out: List[str] = ["# Revisiting Nonsmooth DCA：Claude Code 对话全记录\n"]
    out.append(
        "导出自本地 Claude Code 记录，仅保留对话正文，工具调用与系统消息已删除。"
        "时间为本地时间。第 1 部分是主线；第 2 部分起是 fork、回退或改写产生的分支，"
        "注明接在主线哪一轮之后。\n"
    )
    out.append(f"\n## 1. {SOURCE_LABELS[MAIN_LEAF_FILE]}\n")
    render_chain([vis[u] for u in main_path], out, turn_no)

    section = 1
    # branches: walk all visible nodes in time order; any unrendered node whose
    # visible parent is rendered (or None) starts a branch.
    for start in sorted(vis, key=lambda u: vis[u].time):
        if start in done:
            continue
        p = vparent[start]
        if p is not None and p not in done:
            continue
        chain: List[str] = []
        cur: Optional[str] = start
        while cur:
            chain.append(cur)
            done.add(cur)
            nxt = [k for k in children.get(cur, []) if k not in done]
            cur = nxt[-1] if nxt else None
        tags = set().union(*(vis[u].files for u in chain))
        label = next(
            (SOURCE_LABELS[t] for t in ("e55ca344", "ba2d95f1", "c9600c4d") if t in tags),
            "主线中被回退或改写的分支",
        )
        section += 1
        if p is None:
            anchor = "独立会话，从头开始"
        elif p in turn_no:
            anchor = f"接在主线第 {turn_no[p]} 轮之后"
        else:
            anchor = "接在上面某个分支之后"
        out.append(f"\n## {section}. {label}（{anchor}）\n")
        render_chain([vis[u] for u in chain], out)
        # remaining unrendered children of this chain are picked up by the loop
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {out_path}: {section} sections, {len(vis)} text records, main turns {n}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
