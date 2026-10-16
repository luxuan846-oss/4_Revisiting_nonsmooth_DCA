# 非光滑结构、DC 信息与下界的研究问题

更新：2026-10-16，依据用户本次补充。**研究起点是理解非光滑性产生的计算难度，以及 DC 结构和 DCA 能利用什么信息。** 用户目前最想推进的是下界证明思路。

## 用户直觉

最初受到 2020 年非光滑复杂度论文启发，随后关注 2026 年 8 月弱凸下界，以及近期带约束的非光滑随机优化。用户希望找到这些理论与 DC/DCA 的实质联系。

暂将 2020 年论文定位为 Zhang、Lin、Jegelka、Sra、Jadbabaie 的 ICML 论文，依据当前项目收藏和研究脉络。该定位属于待用户后续确认的推断，不影响先沿此线索阅读。

核心问题：**固定 DC 问题类、查询接口和驻点目标后，非光滑性是否带来额外的信息成本？分量信息或精确凸子问题能减少哪部分成本？DCA 能达到什么界？**

## 阅读主线

| 文献 | 对本问题的用途 | 来源 |
|---|---|---|
| Zhang et al., ICML 2020, *Complexity of Finding Stationary Points of Nonconvex Nonsmooth Functions* | 从同点驻点困难性转向可计算的近似驻点目标 | [PMLR](https://proceedings.mlr.press/v119/zhang20p.html)、[arXiv](https://arxiv.org/abs/2002.04130)、[DBLP](https://dblp.org/rec/conf/icml/ZhangLJSJ20.html) |
| Li–Pan, 2026, *Optimal Deterministic Oracle Complexity for Weakly Convex Optimization* | 弱凸函数类、完整次微分 oracle、Moreau 驻点下界与 generalized zero-chain 构造 | [arXiv:2608.03246](https://arxiv.org/abs/2608.03246)、[正文](https://arxiv.org/html/2608.03246v1) |
| Liu–Chen–Luo–Low, ICML 2024, *Zeroth-Order Methods for Constrained Nonconvex Nonsmooth Stochastic Optimization* | 闭凸约束上的 Goldstein 型判据与零阶方法 | [PMLR](https://proceedings.mlr.press/v235/liu24j.html)、[DBLP](https://dblp.org/rec/conf/icml/LiuCLL24.html) |
| Buzaglo–Kornowski, 2026, *Optimal Algorithms for Nonsmooth Nonconvex Stochastic Optimization with Constraints* | 约束驻点、online-to-nonconvex 转换，以及从光滑困难实例得到下界的方法 | [arXiv:2610.13787](https://arxiv.org/abs/2610.13787)、[正文 §7、§8.6](https://arxiv.org/html/2610.13787v1) |
| 2026-09-27 周报中的下界线索 | Nemirovski–Yudin 信息复杂度；Carmon 等的 zero-chain；Li–Pan 弱凸下界；Pan–Zheng–Li minimax 下界 | [周报](../../slides/20260927周报_润色.pdf)、[arXiv:2609.14235](https://arxiv.org/abs/2609.14235) |

2610.13787 的作者是 Buzaglo 与 Kornowski，文中的 Liu et al. [2024] 是上一行的 ICML 论文。本轮已核对新论文摘要、正文相关段落、参考文献及 Liu 论文正式发表页和 DBLP。Li–Pan 的研究设定与主定理由摘要、正文定义 1–6、定理 3 交叉核对；尚未逐行审阅整个困难实例证明。

## 问题类下界与 DCA 的关系

问题类 oracle 下界考察：在规定信息接口下，所有允许算法中最好的方法，面对函数类中的最难实例，仍需多少次查询。DCA 是候选算法。若研究仅限 DCA 更新规则，则得到算法或算法族的下界。

当前 slides 的 minimax 设定对应前者。若 DCA 通过相同的一阶接口实施，并将内层工作计入成本，问题类下界便能约束它。若每步直接调用精确凸子问题求解器，则需要另外说明这一操作的信息和计算成本。

## 值得先推导的联系

**候选路线 A：将弱凸困难实例写成规范 DC 分解。** 对已知弱凸参数 $\rho$，取

$$
\phi(x)=F(x)+\frac{\rho}{2}\lVert x\rVert^2,
\qquad g(x)=\frac{\rho}{2}\lVert x\rVert^2.
$$

两分量均凸，且 $F=\phi-g$。对弱凸 $F$，标准次微分满足

$$
\partial\phi(x)=\partial F(x)+\rho x,
\qquad \partial g(x)=\{\rho x\}.
$$

这是直接的代数联系：给定 $\rho$，一次 $F$ 的函数值和完整次微分查询足以模拟该分解的分量查询。它提供了一条实际归约入口。

下一步推导两个环节：本文 VAC 精度如何推出 Li–Pan 使用的 Moreau 精度；这个分解怎样满足本文选择的函数类。二次分量在全空间没有统一有界次梯度，因此若保留全局分量界，应尝试有界区域构造、合适延拓或另一种分解。**这是构造要解决的数学问题。**

**候选路线 B：从光滑困难实例进入 DC。** 光滑非凸函数在适当曲率界下也有二次 DC 分解。参照近期约束论文的处理，研究原有困难实例的驻点障碍怎样变成本文证书的障碍。若换算导致精度或分量常数变化，把这些变化纳入最终界。

**候选路线 C：直接保留非光滑困难构造的信息隐藏机制。** 阅读 Zhang 2020、Li–Pan 的构造后，尝试让两个凸分量同时满足本文大小界，并让每次分量查询仍只能揭示有限的新信息。以候选引理和小实例推进，判断哪一步需要新构造。

这些是可推进的证明路线，目前尚未证明它们给出本项目目标函数类下的完整下界。

## 给 GPT 的主要要求

1. 先说明用户直觉指向的科学问题，独立判断哪个联系最值得深化。
2. 沿上述文献解释困难实例怎样隐藏信息，给出能用于 DC 的构造或归约。
3. 优先尝试完成一个关键引理：oracle 模拟、证书转换或函数类嵌入，明确它对总下界的作用。
4. 最后联系 DCA：哪个实现提供上界，内层代价如何计入，能否与问题类下界匹配。

用户希望探索真实机制与证明方案。报告围绕有希望的路线展开，必要条件随推导说明，避免将研究任务写成大批限制条款。
