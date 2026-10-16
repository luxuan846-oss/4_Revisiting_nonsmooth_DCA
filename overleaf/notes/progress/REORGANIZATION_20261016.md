# 项目整理记录

日期：2026-10-16。参考 `luxuan846-oss/3-DDLALM` 的 `master` 分支和本地工作区，沿用 `overleaf/notes/{project,progress,prompts,conversations,gpt-proofs,skills}`。

## 材料迁移

来源路径相对原工作目录 `4_nonsmooth_DCAM`。

| 来源 | 新位置与处理 |
|---|---|
| `cdc2026_template/sample.tex` | `overleaf/main.tex` 与七个 `sections/*.tex`；按原顶层章节划分，只调整路径与引用 |
| 原正文调用的 `Finite_Time_Barriers_of_DC.tex`、`lowerbound.tex` | `overleaf/appendix/` |
| `tools/*.tex`、`tools/*.bib` | `overleaf/tools/` |
| `figure/` | `overleaf/figure/`，图与生成源文件 |
| `nonsmooth_discussion_su/llx_nonsmooth.tex` 及 PDF | `overleaf/slides/`，2026-08-21 |
| `nonsmooth_discussion_su/discussion_llx_July.pdf` | `overleaf/slides/`，封面日期 2026-07-29 |
| `nonsmooth_discussion_su/llx/llx_research_model (1).md` | `notes/project/research-background-original.md` |
| 随机、Fenchel/Goldstein、6 月单循环讨论 | `notes/project/`，保留原推理记录 |
| 创新点、证明与审阅 | `notes/project/` 或 `notes/gpt-proofs/`，注明历史状态 |
| 2026-10-10 文献报告与 BibTeX | 根目录 `literature/jmlr_reference_check_2026-10-10/` |
| 两条指定 Codex 会话 | `notes/conversations/`，用户/助手文本、摘要与原链接 |
| 旧 Overleaf 正文与 slides | `oldversion/`，保存有差异的版本 |

正文入口依据实际章节和差异选择，未单凭修改时间判断。数学内容保持原样不代表本轮已经证明。讨论日期与正文编辑日期分开记录。

## 保留在原目录

`4_DC_penalty/`、MoSSP/约束扩展旧稿、第三方论文 PDF、Zotero 上传缓存、临时编译文件和旧 Overleaf 的 `.git/` 保持原位。这里只导入两个任务直接需要的材料。

文献报告中的旧绝对路径和部分 PDF/网页缓存仍指向原工作区。可移植附件包利用报告内文献链接定位原文，不宣称未复制的文件已随包提供。

## Git 与发布

新工作区在原目录内的 `4_Revisiting_nonsmooth_DCA/`，独立管理 Git，保留旧工作区和其历史。目标 GitHub 仓库本次检查时为公开且无文件。

原始资料保留。此次整理不替代文献调研或全文数学审阅。待发布内容含未发表初稿、合作讨论与会话，发布范围需与用户选择一致。

## 本轮验证

- 七个章节重新拼接后与原稿正文逐字一致，两个附录与来源文件逐字节一致。
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` 成功，生成 47 页 `overleaf/main.pdf`。
- 最终日志无未定义引用或文献警告；仍有页边注范围与若干行宽警告，留给正文排版完善。
- 两个新 DCA 技能通过 skill-creator 的格式验证，Codex/Claude 的八个技能链接均可定位正文。
- 补入用户指定的 2026-09-27 周报，新增非光滑到 DC 的下界研究问题，两个 GPT 任务围绕该问题更新。

正文数学内容保持原样；本轮验证覆盖结构与编译，不代表完整理论审阅。
