# Codex / Claude 启动指令

在仓库根目录启动，先读 `CLAUDE.md` 和 `overleaf/notes/progress/PROJECT_STATUS.md`。

文献任务：

```text
使用 dca-literature 技能，执行 overleaf/notes/prompts/gptpro-literature-research-prompt.md。
先读稿件、2026-08-21 讨论及指定会话，再核对最接近文献。
交付文献报告与 BibTeX，将实际完成事项写入 PROJECT_STATUS.md。
```

初稿任务：

```text
使用 dca-refine 技能，执行 overleaf/notes/prompts/gptpro-draft-review-prompt.md。
以 overleaf/main.tex 为入口，完整读取章节与附录。
先确认核心结果和待验证主张，再实施必要的理论、结构和写作完善。
说明变更、验证结果和剩余问题，并更新 PROJECT_STATUS.md。
```

Codex 可调用 `$dca-literature` / `$dca-refine`，Claude Code 可调用 `/dca-literature` / `/dca-refine`。客户端未自动发现时，直接读取 `overleaf/notes/skills/` 下相应 `SKILL.md`。
