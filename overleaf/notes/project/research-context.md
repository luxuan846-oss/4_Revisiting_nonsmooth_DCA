# 研究背景与材料时间线

研究对象为两个凸分量之差，两个分量均允许非光滑。工作重点是有限时间证书、驻点关系与 DCA 类算法复杂度。当前原稿标题是 *Revisiting DC Optimization: A Unified Notion of Criticality with Optimal Complexity*；其中最优性用语仍需按具体信息模型核对。

## 材料顺序

| 日期 | 材料 | 在当前任务中的用途 |
|---|---|---|
| 2026-06-29 | `single-loop-subgradient-dca-20260629.md` | 早期单循环可行性讨论 |
| 2026 年 7 月 | `stochastic_dc_discussion.md` | 共同二次移位、两侧证书、随机估计器与平滑参数的讨论；文件没有可靠的单一会话日期 |
| 2026-07-29 | `../../slides/discussion_llx_July.pdf` | 与苏老师讨论的上一阶段汇报，日期已从封面确认 |
| 2026-08-19 | `../gpt-proofs/PROOF_AUDIT.md` | 历史 slides 审阅，不能直接沿用其当前缺口状态 |
| 2026-08-21 | `../../slides/llx_nonsmooth.tex` | 用户指定的最新合作进展，日期来自源码；含 oracle 模型与尚未完成的下界问题 |
| 2026-10-10 | 两条 Codex 会话及根目录 `literature/` 报告 | 新颖性担忧、同期工作、MP/JMLR 定位与执行路线讨论 |
| 2026-10-16 | 当前整理 | 确立正文入口、归纳材料、准备两个 GPT 任务及助手配置 |

## 当前科学问题

1. 同点值松弛证书比已有 DC gap 多表达了什么？两个分量的误差和向量残差分别起什么作用？
2. 驻点概念之间在哪些条件下有定量蕴含？哪些反方向失败？
3. 精确 DCA、非精确 DCA、proximal DCA 和随机方法在相同误差口径下能给出什么保证？
4. 计算费用来自外层迭代、精确凸子问题、prox 调用还是实际一阶查询？
5. 固定分量大小界时，确定性 DC 信息模型的下界还缺少什么？已有一般 Lipschitz 下界能否迁移？

## 现有材料的角色

`research-background-original.md` 包含作者其他项目的介绍，只用于背景。不得将 MoSSP、DDLALM 或 DualHash 的定理直接列为本文成果。

`innovation-points-historical.md` 提供候选贡献线索。`dc-goldstein-fenchel-discussion.md` 与随机讨论稿保留推理过程。正文、讨论稿和会话不一致时，先标注版本及假设差别，再判断当前论文应采用什么表述。

材料里的苏老师英文姓名为 Anthony Man-Cho So。合作者背景不代表其已经逐项批准当前全部主张。
