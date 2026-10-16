# 当前项目状态

更新：2026-10-16。**已有初稿；本轮完成项目整理与任务准备。尚未执行新一轮完整文献调研或全文数学审阅。**

## 本次新增研究重点

用户希望理解一般非光滑、弱凸优化与 DC/DCA 的联系，核心困难是下界怎样证明。优先沿 2020 非光滑驻点、Li–Pan 2026 弱凸下界、Buzaglo–Kornowski 2026 及 Liu et al. 2024 中可用于无约束 DC 问题的方法推进。详见 [研究问题与候选路线](../project/lower-bound-research-direction.md)。指令按用户要求精简，以主动推导和推进方案为主。

## 2026-10-16 候选研究问题核查

依据 GPT Pro 评议和后续讨论，做了一轮定向文献核查，报告见 [候选问题文献核查](../../../literature/question_selection_2026-10-16/候选问题文献核查.md)。

- N2（DCA 避开伪临界点）：2026 年 Feng–Yuan、Niu、Le Thi 等三篇已证明随机化 DCA 几乎必然收敛到 d-stationary 点，放弃。
- N1（交集与包含）：检验侧已由 Tian–So (SODA 2025) 解决，并入问题一。
- GPT Pro 主推的 $\Theta(\varepsilon^{-4})$（VAC 两类相同）属于预期结果，降为基线。
- 助手建议的主问题（待用户确认）：问题一，分解无关性的价格（VAC 对比 Goldstein，有界 DC 类）；问题二，DC 类上的确定性价格（Kong–Lewis 的 $\varepsilon^{-1}$ 差距）。
- “VAC 是最强可计算目标”不成立：Goldstein 驻点严格更强，且在 DC 类上有限时间可算。
- 结合 GPT Pro 第二轮评议后调整：主线改为“普通分量 oracle 下 DC 结构能否打破确定性 Goldstein 的指数障碍”。助手推导两点（待核）：(1) Kornowski 2609.23837 的指数困难实例不在有界 DC 类中，否则与 Kong–Lewis 的维数无关上界矛盾；(2) $F_0=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}$ 在原点对**所有**凸分解都 DC 临界，但不是 Clarke 驻点，证明见 [gpt-proofs](../gpt-proofs/irremovable-pseudo-criticality-2026-10-16.md)。
- 讨论后的论文结构（主线：确定性方法在弱凸之外能否保住 $\Theta(\varepsilon^{-4})$；Q0 不可达 → VAC → Q1 含义 → Q2 确定性上下界 → Q3 确定性边界，按出现顺序编号）见 [论文结构](../project/paper-structure-2026-10-16.md)。尚待用户与合作者确认。全文逻辑与新见解核查 prompt：[gptpro-logic-and-insight-audit-prompt](../prompts/gptpro-logic-and-insight-audit-prompt.md)。
- GPT 关于 Q3 的对话（待独立审核）已归档，见 [对话记录](../conversations/chatgpt-6ad27f37-q3-deterministic-frontier.md)。GPT 给出的主张：普通分量 oracle 下 L1 有维数无关的确定性上界；固定分量常数时 L2 有 $n-2$ 次查询下界，同时有 $O(n\log n)$ 的确定性上界，靠局部纯化引理实现。它还修正了上面第 (1) 点：Kornowski 的困难实例是 DC，但分量 Lipschitz 常数随实例长度增长。证明报告附件尚未取回。

## 用户已确定的方向

- 与苏文藻老师合作本篇非光滑 DC 论文。
- 本文研究范围为无约束 DC 优化；本次仅更新任务指令与范围说明。
- GPT 的两个任务：文献调研、已有初稿 refine。
- 目标期刊：Mathematical Programming 或 JMLR。2026-10-10 用户原话：“定下来了。这篇文章MP或者JMLR 告诉我最小执行线路”。
- 2026 年 8 月形成主要结果，当时尚未公开。该信息来自 10 月 10 日用户说明，不能推断之后的公开状态。
- 最新合作讨论材料按用户指定采用 2026-08-21 的 `slides/llx_nonsmooth.tex`；上一阶段汇报为 2026-07-29 的 `slides/discussion_llx_July.pdf`。

## 活动正文与版本边界

正文由原 `cdc2026_template/sample.tex` 按章节整理为 `main.tex` 与 `sections/*.tex`。数学内容保持原样，仅调整路径与章节引用。原 `overleaf_nonsmooth_discussion/paper/main/sample.tex` 的内容不同，归为历史副本。

8 月汇报和两条 10 月会话提供研究背景。8 月 19 日审阅针对更早版 slides，其行号和问题状态必须重新对应。`innovation-points-historical.md` 是原创新点总结，不等同于独立证明审查结果。

## 已识别的待处理事项

| 事项 | 当前证据 | 下一步 |
|---|---|---|
| 贡献定位 | 初稿有三参数同点证书、驻点关系、确定性及随机分析 | 对照 DCA-PAGE、Bregman DCA 等原文，识别实质增量 |
| 固定分量界下界 | 8 月 slides 的 Current status 明写困难实例仍缺失；原创新总结只支持有限预算限制 | 按函数类、oracle、判据核对各版本，不能写成已完成匹配下界 |
| 现有表述 | 引言写光滑非凸问题可由凸分量模型取 `g=0` 得到；正文标题保留 Optimal Complexity | 核对数学表述与最优性依据后修订 |
| 投稿路线 | 用户选择 MP 或 JMLR；旧助手建议 JMLR 优先 | GPT 独立评议两个方向所需的实质增量；不预设顺序 |
| 文献时效 | 已有 2026-10-10 文献重叠报告 | 调研执行时补检该日期之后的新版本，并复核关键结论 |
| 文本残留 | 结论尚未完成，致谢和参考文献说明含模板文本 | refine 时按论文实际内容处理，不填造资助或作者信息 |

这里记录的是可定位的整理发现，不是整稿数学审阅结论。

## 下一步

1. 执行文献任务，交付非光滑到 DC 的下界路线、关键引理、文献比较与 BibTeX。
2. 执行初稿 refine 任务，先判定主定理与开放问题，再输出具体修订。
3. 将被采纳的结论和已完成事项更新到本文件。保持证明与文献报告的执行日期。

## 不作为已定要求

历史助手提出的“JMLR 先投”“必须补三组实验”“MP 必须匹配下界”均属于历史建议。它们不能代表用户最终决定或期刊官方标准。作者署名与顺序沿用原稿，合作背景不自动转化为署名调整。

## 本轮交付验证

正文结构整理已通过内容一致性核对与 LaTeX 编译，当前 PDF 为 47 页。两个 DCA 技能格式有效。两个 GPT 附件包由根目录打包脚本生成。现有行宽警告列入后续排版工作。
