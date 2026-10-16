# 全文叙事：转折版（2026-10-16）

状态：助手提出的叙事建议，待用户与合作者确认。Q3 的 $\widetilde O(n)$ 上界与 $\Omega(n)$ 下界来自 GPT Pro 证明稿，尚未入库，也未经审核；本节凡涉及 Q3 定理处均以此为前提。

## 读者需要先看到的地图

| 函数类 | 随机算法 | 确定性算法 |
|---|---|---|
| 弱凸 | — | Moreau 驻点 $\Theta(\varepsilon^{-4})$：Davis–Drusvyatskiy 上界，Li–Pan 下界 |
| 一般 Lipschitz | Goldstein 驻点，维数无关（Zhang 等 2020；Davis 等 2022） | Goldstein 驻点需维数指数代价（Kornowski 2609.23837） |
| 分量有界 DC | 扰动后分量几乎必然可微，回到随机情形 | **本文** |

核心问题：DC 类比弱凸类大得多，结构却远比一般 Lipschitz 函数丰富。只用 DCA 实际调用的信息，弱凸世界里的确定性结论还能保住多少？保不住的部分，代价究竟是多少？

## 四个转折

**Q0。** DCA 自 1980 年代提出以来，一直以近似 DC 临界作为标准目标和停机准则，已有速率要么假设负侧光滑，要么按精确子问题计数。然而两个分量都非光滑时，这个准则在有限时间内不可达（Kornowski–Shamir 凸困难族的 DC 嵌入）。

**VAC。** 同点目标虽然不可达，DCA 的单步 Fenchel 间隙恒等式却直接给出了应当放松什么。由此得到三参数值松弛证书 VAC，三个容差依次对应子问题误差、负侧运输误差和对偶不匹配，不需要强凸。

**Q1。** Tian–So 已经指出，坏的分解能把任意点变成临界点。反方向的问题是：好的分解能否总把伪临界消除？一维可以（Jordan 分解）。然而从二维起，$F_0=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}$ 在原点对**所有**凸分解都 DC 临界，却不是 Clarke 驻点。因此这一缺陷属于 DC 临界本身，不是 VAC 造成的。负侧光滑时，VAC 推出 Moreau 驻点，并确定校准尺度 $\delta\sim\varepsilon^2$。

**Q2。** 失去弱凸后，确定性方法一般要付出高昂代价；然而在分量有界的 DC 类上，确定性方法以 $\Theta(\varepsilon^{-4})$ 次基本查询达到 VAC，与弱凸情形相同。即使每次返回两个分量的完整次微分，也不能更快（Li–Pan 实例加有界凸化项 $c_N$，不泄露隐藏坐标）。DC 文献中的 $\varepsilon^{-2}$ 计的是精确子问题次数，分解本身不带来加速。

**Q3。**
1. 在一般 Lipschitz 函数上，随机化带来指数级优势。DC 结构几乎能把这份优势全部收回：Kong–Lewis 的方向 oracle 算法在统一有界的 DC 类上与维数无关。与 Kornowski 合起来可知，指数困难族不能保持统一的分量界。这一结构性认识归功于 Kong–Lewis。
2. 然而，这一收回依赖一项 DCA 从不调用的能力：按外层指定的方向，在并列次梯度中作选择（direction-aware tie-breaking）。潜变量结构化 SVM 的推断模块只返回一个 argmax，并不提供这项能力。
3. 我们证明，放弃这项能力、只用普通分量查询，确定性方法仍能达到原目标的 Goldstein 驻点（局部纯化），维数代价为 $\widetilde O(n)$；同时 $\Omega(n)$ 不可避免。
4. 合起来：DC 类上，随机算法的维数代价为 0；确定性算法配合方向选择，维数代价也为 0；确定性算法面对对抗性选择，代价为 $\widetilde\Theta(n)$；一般 Lipschitz 类上为指数级。随机扰动起作用的方式正是让并列消失，所以**在 DC 类上，确定性的维数代价恰好等于挑选并列次梯度的代价，量级是线性的。**

## 中文摘要草稿

DCA 以近似 DC 临界作为标准目标与停机准则。尽管这一准则沿用已久，但是当两个凸分量都非光滑时，我们证明它在有限时间内不可达。为此，我们从 DCA 自身的下降恒等式读出值松弛临界证书 VAC，三个容差分别对应子问题误差、负侧运输误差与对偶不匹配。VAC 会被伪临界点满足。通常认为换一个更好的分解就能修复这一点；然而我们证明，这在一维成立，从二维起失效：存在对所有凸分解都 DC 临界、却不是 Clarke 驻点的点，因此缺陷属于 DC 临界本身。失去弱凸性后，确定性方法一般要付出高昂代价；但是在分量有界的 DC 类上，确定性方法以 $\Theta(\varepsilon^{-4})$ 次基本查询达到 VAC，与弱凸情形相同，即使给出两个分量的完整次微分也不能更快。最后，我们刻画随机化在 DC 类上的价值。在一般 Lipschitz 函数上，确定性代价随维数指数增长；在 DC 类上，只要能按方向挑选并列次梯度，确定性方法就与维数无关。DCA 的普通分量查询不具备这项能力。我们用局部纯化，仅凭两个分量的函数值与任意次梯度，确定性地达到原目标的 Goldstein 驻点，维数代价为 $\widetilde O(n)$，并证明 $\Omega(n)$ 不可避免。

## 英文开头草稿

Losing weak convexity is widely believed to doom deterministic methods: for general Lipschitz functions, determinism costs exponentially in the dimension. We show that difference-of-convex structure reverses most of this picture, and we pin down exactly what remains lost. The standard DC stopping rule is unreachable in finite time once both components are nonsmooth, yet a certificate read off the DCA descent identity is reachable at the weakly convex rate $\Theta(\varepsilon^{-4})$. For Goldstein stationarity, the whole dimensional price of determinism is the price of breaking ties among component subgradients, and that price is linear.

## 对 GPT Pro 核验的判断

- 第 1 节的分解代数正确：$\min_i h_i=S-Q$，$\max\{L(S-Q),-\Delta\}=\max\{LS,LQ-\Delta\}-LQ$，常数 $LT$ 与 $L(T-1)$。前提（最终构造的形式、$h_i$ 凸且 1-Lipschitz）待对照原文。
- 第 2 节的一维推导在其前提下正确：$q'_+(s_{i+1})\ge q'_-(s_{i+1})\ge q'_+(s_i)+L$，于是 $\operatorname{Lip}(g)\ge L(T-1)/2$。薄弱处在前提：需要各中心附近的局部斜率都沿同一方向 $\mathbf e_1$ 取 $L$。如果构造在不同查询点使用不同（如近正交）的梯度方向，推导就不成立。该节不是必需的，正文不宜依赖它。
- 第 3 节才是一般论证，即原 K7：若局部 oracle 能模拟方向 oracle（Tian–So Remark 1，待核），则 Kornowski 对 Kong–Lewis 算法构造的困难实例不能落在常数固定的 DC 类中。此前“两者 oracle 不同、不存在矛盾”的更正本身有误；K7 在上述条件下成立。
- 由此推出的叙事后果正确：“指数降到线性”不能写成本文贡献，结构性收回属于 Kong–Lewis。普通分量 oracle 与 $F$ 的方向 oracle 确实不可比；把对照改成“同一分量 oracle，只差是否按方向挑选并列次梯度”，两者就成为嵌套关系，分离结论也就干净了。

## 待核

1. Kong–Lewis Oracle 2.5 是否要求返回向量属于 $\partial_C F(x)$。若不要求，$G=u_d-v_d$（$u_d\in\operatorname{argmax}_{u\in\partial\phi(x)}\langle u,d\rangle$，$v_d$ 同理）即可实现它，“方向选择下维数无关”直接成立；若要求，需另证。
2. Tian–So Remark 1 与 Kornowski 局部 oracle 的包含关系。
3. Q3 上下界证明稿入库并审核；$\Omega(n)$ 适用的参数范围。
4. Kornowski 2609.23837 第 4 节构造的具体形式。
