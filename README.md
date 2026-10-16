# Revisiting Nonsmooth DCA

与苏文藻老师合作的非光滑 DC 优化论文。当前阶段是**已有初稿的文献定位与文章完善**。目标期刊为 **Mathematical Programming 或 JMLR**，投稿顺序尚未由用户最终确定。

- **研究重点**：[非光滑到 DC 的下界路线](overleaf/notes/project/lower-bound-research-direction.md)
- **当前状态**：[PROJECT_STATUS.md](overleaf/notes/progress/PROJECT_STATUS.md)
- **正文入口**：[overleaf/main.tex](overleaf/main.tex)
- **任务一**：[给 GPT 的文献调研指令](overleaf/notes/prompts/gptpro-literature-research-prompt.md)
- **任务二**：[给 GPT 的初稿 refine 指令](overleaf/notes/prompts/gptpro-draft-review-prompt.md)
- **讨论与会话**：[材料时间线](overleaf/notes/project/research-context.md)、[Codex 记录](overleaf/notes/conversations/README.md)
- **Codex / Claude**：[AGENTS.md](AGENTS.md)、[CLAUDE.md](CLAUDE.md)
- **项目技能**：[技能入口](overleaf/notes/skills/README.md)

## 目录

```text
AGENTS.md                     Codex 入口
CLAUDE.md                     两个助手共用的研究约定
overleaf/
  main.tex                    唯一活动正文入口
  sections/                   从现有初稿按章节整理
  appendix/                   正文实际调用的附录
  tools/                      宏与 BibTeX
  figure/                     论文图及生成源文件
  slides/                     2026 年 7 月汇报与 8 月讨论
  notes/
    project/                  研究问题、背景与文献定位
    progress/                 当前状态与整理记录
    prompts/                  两个 GPT 任务、Codex / Claude 启动指令
    conversations/            指定的两条 Codex 会话
    gpt-proofs/                历史证明与审阅材料
    skills/                   DCA 技能与研究评议方法
literature/                   已有调研记录与引用信息
oldversion/                   有差异的历史副本
tools/                        附件打包工具
```

参考仓库：[3-DDLALM](https://github.com/luxuan846-oss/3-DDLALM)，其默认分支为 `master`。本项目沿用 `overleaf/notes/` 的工作组织方式，数学主题与判断规则针对 DCA 编写。目标远端：[4_Revisiting_nonsmooth_DCA](https://github.com/luxuan846-oss/4_Revisiting_nonsmooth_DCA)。

## 使用

在本目录启动 Codex 或 Claude Code。两个助手均先读取当前状态，再执行相应任务。技能正文集中在 `overleaf/notes/skills/`；项目发现入口位于 `.agents/skills/` 和 `.claude/skills/`。

编译正文：

```bash
cd overleaf
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

生成两个 GPT 附件包：

```bash
python3 tools/package_gpt_tasks.py
```

输出位于 `outputs/gpt/`。将对应 ZIP 解压后上传给 GPT，并粘贴该任务的指令。附件含未发表稿件与项目讨论，仅用于本次研究协作。

原工作目录中的材料保持原位。迁移来源与未纳入项见 [整理记录](overleaf/notes/progress/REORGANIZATION_20261016.md)。


# Stochastic DCAM

## Project Focus

This project currently focuses on the following research directions:

- Zotero literature related to **stochastic** optimization.
- **Stochastic DC programming** and stochastic difference-of-convex methods.
- **DC programming** for nonsmooth and composite optimization.
- **Nonsmooth optimization**, especially stationarity, convergence, and complexity analysis.

## Reading Priority

When reviewing papers or notes for this project, prioritize work connected to:

- stochastic approximation and stochastic first-order methods;
- DC decomposition, majorization-minimization, and proximal updates;
- Clarke stationarity, limiting stationarity, and weak convexity;
- unconstrained nonconvex nonsmooth and composite optimization.
