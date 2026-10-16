# 全文叙事：转折版（2026-10-16，第二版）

状态：助手提出的叙事建议，待用户与合作者确认。编号沿用 GPT Pro 会话中的三问结构（Q1 可验算证书，Q2 不可消除的伪临界，Q3 确定性边界），与 `paper-structure-2026-10-16.md` 中的 Q0–Q3 编号不同；后者尚未更新。Q3 结论依据 [Q3 证明报告](../gpt-proofs/Q3-deterministic-frontier-proof-report-2026-10-16.md)，该报告尚未独立审核。

第一版把 Q3 写成“按方向挑选并列次梯度值一个线性因子”。这一说法错误，已撤回，原因见文末。

## 主线

所有问题围绕一个问题展开：**DCA 停下来报告“已接近临界”，这个信号有多可信？**

- Q1：能可靠地算出来，代价最优。
- Q2：算得再准，信号本身也可能是错的，换分解也没用。
- Q3：同样的分量信息里，还藏着能纠正这种错误的东西；纠正的代价是近线性维数，而且省不掉。

## 读者需要先看到的地图

| 函数类 | 随机 | 确定性 |
|---|---|---|
| 弱凸 | — | $\Theta(\varepsilon^{-4})$ |
| 一般 Lipschitz | Goldstein 维数无关 | 维数指数代价（Kornowski 2609.23837） |
| 分量有界 DC，普通分量查询 | 扰动后几乎必然可微，维数无关 | **L1 维数无关；L2 为 $\widetilde\Theta(n)$（本文）** |

## 三个转折

**Q1。** 两个分量都非光滑时，同点精确次微分残差没有统一的有限查询保证；Xu 等已经用例子指出这一困难，并改用附近点目标。然而不必放弃同点：只放松正侧的支撑值误差，负侧保持精确，就能以 $\Theta(\varepsilon^{-4})$ 次确定性查询显式输出可验算的 $(\varepsilon^2,0,\varepsilon)$ 证书，代价与弱凸情形相同。上界依靠旧点认证：下降恒等式直接控制旧点的正侧间隙，省掉了线性运输估计带来的多余 $\varepsilon^{-1}$。下界在固定分量界下成立，即使每次返回两个完整次微分也成立。Xu 等对双侧非光滑问题也计入了内层成本，但对象是固定点映射，既不是这一证书，也没有下界。

**Q2。** 证书误差降到零，伪临界仍然存在。Tian–So 已经指出，坏分解能把任意点变成临界点。反方向的问题是：好分解能否总把伪临界救回来？一维可以，而且只需一个分解，就能在所有点同时还原 Clarke 次微分，并保持原分量界。然而从二维起不行：$F_0+3(\lVert x\rVert-1)_+\in\mathcal D(4,1,1)$，它在原点对所有凸分解都 DC 临界，对每个 $0<r<1$，Goldstein 残差都固定为 $1/\sqrt2$。几何机制来自经典极小对理论（Grzybowski–Urbański），必须引用；本文的贡献在于把它读成优化结论，并给出定量分离。

**Q3。** Q2 说明判据本身丢了信息，换分解也无济于事。但是丢掉的信息仍然藏在生成判据的分量查询里。Kong–Lewis 已有确定性 DC Goldstein 算法，然而它要求 oracle 直接给出原目标 $F$ 的方向导数和属于 $\partial_C F$ 的相容向量（Prop. 2.4 的选择）。本文只用 $\phi,g$ 的值与对抗选择的任意次梯度。

- 方法：研究 $\phi-g$，却用凸函数 $\phi+g$ 来控制。$\operatorname{width}_i(\partial\phi-\partial g)=\operatorname{width}_i(\partial\phi+\partial g)$，凸函数次梯度的单调性允许逐坐标二分。算法不去挑选有利的回答，而是寻找一个位置，让所有合法回答都可靠（局部纯化）。
- 代价：L1（分量差的邻域证书）维数无关；L2（$F$ 的 Goldstein）满足 $\Omega(n)\le N\le O(n\log n)$。
- 联系：$\Omega(n)$ 下界的困难实例，正是 Q2 的 $F_0$ 藏进算法未探测的二维子空间。同一个几何障碍，同时解释了表示失真和计算代价。
- 全景：随机化在一般 Lipschitz 函数上值指数级；在 DC 类上，用普通分量查询时只值近线性的维数因子，而且恰好就是越过伪临界缺口（从 L1 到 L2）的价格。不越过时，确定性方法不付维数代价。

## 中文摘要草稿

DCA 停止时报告的近似临界性，究竟能保证什么？尽管两个凸分量都非光滑时，标准的同点临界准则在有限时间内不可达，但是我们证明，只需放松正侧、保持负侧精确，确定性方法就能以 $\Theta(\varepsilon^{-4})$ 次查询显式输出可验算的证书，与弱凸情形的最优代价相同。然而证书再精确也可能误导：通常认为伪临界可以通过换分解消除，我们证明这在一维成立，从二维起失效，存在对所有凸分解都 DC 临界、却远离 Goldstein 驻点的点。即便如此，DCA 使用的普通分量查询仍然足以越过这一缺口。已有确定性方法依赖原目标的方向与 Clarke 信息，我们则利用凸函数 $\phi+g$ 控制差函数 $\phi-g$ 的次梯度失真，仅凭两个分量的函数值与任意次梯度，确定性地达到原目标的 Goldstein 驻点。固定其余参数时，维数代价为 $O(n\log n)$，而 $\Omega(n)$ 不可避免；其困难实例正是上述二维伪临界结构。在一般 Lipschitz 函数上，确定性的代价是维数的指数；在 DC 类上，这一代价降为近线性，并且恰好等于越过伪临界缺口的价格。

## 英文开头草稿

When DCA stops and reports near-criticality, what has it certified? We show that the answer can be computed at the weakly convex optimal rate, that it can be wrong under every convex decomposition from dimension two on, and that the very component queries DCA uses already contain the information needed to correct it. Correcting it costs a near-linear factor in the dimension, and no deterministic method can avoid a linear factor. For general Lipschitz functions, determinism costs exponentially in the dimension; for DC functions, its entire dimensional price is the price of crossing the pseudo-critical gap.

## 第一版的错误：按方向挑选并列次梯度不能消除维数代价

在 $\Omega(n)$ 的困难实例中，查询点满足 $Px=0$，此时 $\partial\phi(x)=\operatorname{conv}\{0,a,b\}$，$\partial g(x)=\operatorname{conv}\{0,-a,-b\}$。如果对抗者把 $a,b$ 选成同时与全部查询点和全部指定方向 $d$ 正交，那么按 $d$ 逐分量挑选时，两边都是平局，返回 $u=v=0$ 仍然合法，算法同样被骗。Kong–Lewis 的 L2 保证要求返回的向量属于 $\partial_C F(x)=\operatorname{conv}\{a,b,a+b\}$；这样的向量不能由分量层面的方向选择得到。因此，$\widetilde\Theta(n)$ 是“从分量差得到忠实于 $\partial_C F$ 的信息”的价格，而不是方向选择的价格。潜变量 SVM 的应用动机相应改为：推断程序给出分量次梯度，却不提供原目标的 Clarke 信息。

## 对 GPT Pro K7 核验的判断

- 显式分解的代数正确；$\operatorname{Lip}(g)\ge L(T-1)/2$ 的一维推导，依赖各中心局部斜率沿同一方向这一前提，正文不宜依赖它。
- 真正的一般论证是：局部 oracle 能给出 Prop. 2.4 意义下属于 Clarke 次微分的方向相容向量（Q3 报告第 723 行附近给出这一读法），因此 Kornowski 针对 Kong–Lewis 算法构造的困难实例，不能落在常数固定的 DC 类中。此前“oracle 不同、不存在矛盾”的更正有误。
- 叙事后果：“DC 结构打破指数障碍”归功于 Kong–Lewis；本文的增量在于普通分量查询、局部纯化，以及 L1/L2 的维数分离。

## 待核

1. Q1 速率已由[全文逻辑核查](../gpt-proofs/dca-logic-audit-summary-2026-10-16.md)更新为 $\Theta(\varepsilon^{-4})$，旧点认证去掉了多余的 $\varepsilon^{-1}$。`paper-structure-2026-10-16.md` §6.4 中的 $\varepsilon^{-5}$ 已过时；`appendix/lowerbound.tex` 仍是旧归约，需要替换。
5. 优先权表述需删改：“此前没人问过同点临界”（Xu 等）；“首个弱凸之外的紧确定性复杂度”（Tian–So 已有非凸模的紧性结果）；“正侧 gap 恒为零”的批评（MDCA v2 Remark 1）。
2. Q3 证明报告的独立审核：纯化引理，以及纯化与线搜索的衔接。
3. 一维 Jordan 分解的结论仍标为待核。
4. Kong–Lewis Oracle 2.5 与 Prop. 2.4 原文；Kornowski 2609.23837 第 4 节构造。
