# GPT 任务一：文献调研与下界证明路线

状态：待执行。准备日期：2026-10-16。运行 `python3 tools/package_gpt_tasks.py` 生成 `outputs/gpt/dca-literature.zip`，上传解压后的材料，并发送下列任务。

## 阅读材料

路径相对仓库根目录。先读当前状态与研究问题，再读正文和讨论。

- `overleaf/notes/progress/PROJECT_STATUS.md`
- `overleaf/notes/project/lower-bound-research-direction.md`
- `overleaf/main.tex` 及 `sections/`、`appendix/`、`tools/`
- `overleaf/slides/llx_nonsmooth.tex` 与 PDF，2026-08-21
- `overleaf/slides/discussion_llx_July.pdf`，2026-07-29
- `overleaf/slides/20260927周报_润色.pdf`
- `overleaf/notes/conversations/`，含两条指定会话及摘要
- `literature/jmlr_reference_check_2026-10-10/` 的已有文献报告
- 按需读随机讨论稿、证明材料及 `dca-literature` 技能

## 可直接发送的任务

请作为熟悉非光滑优化、DC 结构与 oracle 复杂度的研究合作者，为我们与苏文藻老师合作的已有初稿做文献调研。中文写报告，BibTeX 用英文。目标期刊为 Mathematical Programming 或 JMLR。本文聚焦无约束的双侧非光滑 DC 优化，文献比较与证明路线均围绕这一范围展开。

**我们的核心直觉：非光滑性增加了多少计算难度？DC 结构能减少哪部分难度？DCA 能否利用这种结构？** 当前最需要帮助的是下界怎么证明，以及一般非光滑和弱凸优化的结果怎样用于 DC。

先读初稿与合作讨论，提炼最值得深化的科学问题，再决定检索重点。请贡献独立判断、具体推导和证明路线。

### 阅读主线

1. Zhang et al. 2020，非光滑非凸驻点复杂度：用户最初的启发来源，暂据项目材料定位为 https://proceedings.mlr.press/v119/zhang20p.html 。
2. Li–Pan 2026，弱凸最优确定性 oracle 复杂度：https://arxiv.org/abs/2608.03246 。
3. Buzaglo–Kornowski 2026：https://arxiv.org/abs/2610.13787 ，及其引用的 Liu–Chen–Luo–Low 2024：https://proceedings.mlr.press/v235/liu24j.html 。重点借鉴其中可用于无约束 DC 问题的驻点概念与复杂度分析方法。
4. 9 月 27 日周报中的 Nemirovski–Yudin、Carmon zero-chain、Pan–Zheng–Li minimax 下界：https://arxiv.org/abs/2609.14235 。
5. 直接相关的 DCA-PAGE、Bregman DCA、MDCA、随机与非精确 DCA、DC envelope 等工作。

### 要解决的问题

- 这些困难实例怎样隐藏信息？哪些机制可以迁移到 DC 分量信息接口？
- 从弱凸函数的规范二次 DC 分解出发，能否完成 oracle 模拟、本文证书到 Moreau 驻点的转换，以及函数类嵌入？请实际尝试至少一个关键引理。
- 固定分量大小界时，怎样调整已有困难实例？有哪些值得尝试的有界区域、延拓或直接构造？
- 问题类下界怎样约束 DCA 的一阶实现？精确子问题求解与外层迭代又对应什么复杂度？
- 本文同点两侧值松弛证书，相比已有单侧 gap 和 Bregman 分析增加了什么能力？
- 2026 年 8 月之后有哪些实质相关新结果？检索到实际执行日期，并说明它们如何改变证明路线与贡献定位。

比较时说明函数类、oracle、成功判据、误差参数和计算单位。关键文献通过原文、版本/出版记录和独立来源交叉核对；尚不清楚的地方给出待验证问题与下一步。

### 上下文

8 月 21 日讨论是最新合作材料，7 月汇报提供演变背景。两条 10 月 10 日会话已有文本附件：

- codex://threads/01a1253d-200f-72b0-b568-afdb6057295c
- codex://threads/01a12739-2eab-7ec3-ad50-5a1a39c0c393

用户确定 MP 或 JMLR。历史助手的具体投稿顺序供参考。现有下界进展以实际定理和证明为依据，研究设想继续向前推导。

### 交付

1. `literature-review.md`：核心判断、关键文献比较、可迁移的机制和最有希望的证明路线。
2. `lower-bound-route.md`：候选定理、归约或困难实例、已完成的关键引理，以及下一步最值得解决的问题。
3. `new-entries.bib` 与 `corrections.bib`：新增和更正条目，注明来源 URL。
4. 对论文贡献定位与 MP/JMLR 的具体建议。

报告围绕数学联系与推进方案展开。先讲有价值的发现，再说明成立条件和剩余工作。
