# 三问的定理表述与文献对比（2026-10-16 草案）

状态标记：【已核】表示助手已逐步核对；【待审】表示目前只有 GPT Pro 证明稿，尚未独立审核。常数取自 `gpt-proofs/` 中的报告。

## 0. Setting

**Function class.** $\mathcal D(G_\phi,G_g,\Delta)$ consists of pairs $(\phi,g)$ of finite convex functions on $\mathbb R^n$ with $\operatorname{Lip}(\phi)\le G_\phi$, $\operatorname{Lip}(g)\le G_g$, and $F(x^0)-\inf F\le\Delta$, where $F=\phi-g$. Write $B=G_\phi+G_g$.

**Oracle.** The component oracle $\mathcal O_{\mathrm{comp}}$ returns, at a query $x$, the values $\phi(x)$, $g(x)$ and some $u\in\partial\phi(x)$, $v\in\partial g(x)$ chosen adversarially.

**Algorithms.** Deterministic algorithms in the exact real-arithmetic query model; complexity is the worst-case number of oracle calls.

**Targets.**

- $(\delta_\phi,\delta_g,\varepsilon)$-VAC: there are $u\in\partial_{\delta_\phi}\phi(x)$ and $v\in\partial_{\delta_g}g(x)$ with $\|u-v\|\le\varepsilon$.
- $(r,\varepsilon)$-L1: $\operatorname{dist}\bigl(0,\operatorname{conv}\bigcup_{y\in\overline B_r(x)}(\partial\phi(y)-\partial g(y))\bigr)\le\varepsilon$.
- $(r,\varepsilon)$-L2, i.e. Goldstein stationarity of $F$: $\operatorname{dist}\bigl(0,\partial_rF(x)\bigr)\le\varepsilon$, where $\partial_rF(x)=\operatorname{conv}\bigcup_{y\in\overline B_r(x)}\partial_CF(y)$.

## Q1. What does the DCA descent certify, and at what cost?

**Proposition 1.1 (positive-side relaxation is necessary).** There exist absolute constants $G_\phi^0,G_g^0,\Delta^0,\varepsilon_0>0$ with the following property. For every budget $T$, every deterministic algorithm making $T$ queries, and every $\delta_g\ge0$, some instance in $\mathcal D(G_\phi^0,G_g^0,\Delta^0)$ admits no queried or output point that is a $(0,\delta_g,\varepsilon_0)$-VAC point. 【待审：基于 Kornowski–Shamir 凸困难族的归约，量词按原文】

**Theorem 1.2 (explicit certificate with one exact side).** For all $\delta\in(0,\Delta]$ and $\varepsilon\in(0,B]$, there is a deterministic algorithm that uses only $\mathcal O_{\mathrm{comp}}$ and outputs $(x,u,v)$ together with a computable number $\widehat\Psi$ such that

$$
\Psi_\phi(x,u)\le\widehat\Psi\le\delta,\qquad v\in\partial g(x),\qquad \|u-v\|\le\varepsilon .
$$

Its query count is $O\bigl((1+\Delta/\delta)(1+B^2/\varepsilon^2)\bigr)$. 【待审】

**Theorem 1.3 (matching lower bound).** There exist absolute constants $c,\varepsilon_1>0$ and a fixed class $\mathcal D(G_\phi^1,G_g^1,\Delta^1)$ such that, for every $\varepsilon\in(0,\varepsilon_1)$, every deterministic algorithm that outputs an $(\varepsilon^2,\varepsilon^2,\varepsilon)$-VAC point on all instances needs at least $c\,\varepsilon^{-4}$ queries. This holds even if each query returns the full subdifferentials $\partial\phi(x)$ and $\partial g(x)$. 【待审：Li–Pan 实例加有界凸化项与成对抵抗 oracle】

**Corollary 1.4.** On a fixed class, the deterministic complexity of $(\varepsilon^2,0,\varepsilon)$-VAC is $\Theta(\varepsilon^{-4})$.

**Proposition 1.5 (calibration).** If $g$ is convex and $\rho$-smooth, every $(\delta_\phi,\delta_g,\varepsilon)$-VAC point $x$ satisfies

$$
\|\nabla F_{1/(2\rho)}(x)\|\le b+\sqrt{b^2+4\rho\delta_\phi},\qquad b=\varepsilon+\sqrt{2\rho\delta_g}.
$$

Hence the scale $\delta=\varepsilon^2$ corresponds to $O(\varepsilon)$-Moreau stationarity, the weakly convex target. 【待审】

**Remark 1.6 (meaning for DCA).** With $m_x(y)=\phi(y)-g(x)-\langle v,y-x\rangle$, a $(\delta,0,\varepsilon)$-VAC certificate gives $m_x(x)-\inf_{\|y-x\|\le R}m_x(y)\le\delta+\varepsilon R$: the current convex model of DCA is solved to accuracy $\delta+\varepsilon R$ on radius $R$. 【已核】

## Q2. Does an exact certificate under the best decomposition imply stationarity?

**Lemma 2.1 (shared kinks).** If $\phi$ or $g$ is differentiable at $x$, then $\partial\phi(x)-\partial g(x)=\partial_CF(x)$. Consequently, exact DC criticality and Clarke stationarity can differ only at points where both components are nondifferentiable. 【已核：凸函数在可微点严格可微，Clarke 和法则取等号】

**Theorem 2.2 (one dimension: a canonical decomposition).** Let $n=1$. For every $(\phi,g)\in\mathcal D(G_\phi,G_g,\Delta)$ there is $(\Phi,\Gamma)\in\mathcal D(G_\phi,G_g,\Delta)$ with $\Phi-\Gamma=\phi-g$ and $\partial\Phi(x)-\partial\Gamma(x)=\partial_CF(x)$ for every $x\in\mathbb R$. In particular, DC criticality and Clarke stationarity coincide everywhere. 【待审：二阶导数测度的 Jordan 分解】

**Theorem 2.3 (two dimensions: an irremovable pseudo-critical point).** Let $F(x)=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}+3(\|x\|-1)_+$ on $\mathbb R^2$. Then:

1. $F$ admits a decomposition in $\mathcal D(4,1,1)$;
2. every decomposition $F=\phi-g$ into finite convex functions satisfies $\partial\phi(0)\cap\partial g(0)\neq\varnothing$;
3. for every $r\in(0,1)$, $\operatorname{dist}\bigl(0,\partial_rF(0)\bigr)=1/\sqrt2$, and $F'(0;-e_1)=-1$;
4. for every decomposition, some admissible subgradient selection keeps exact DCA at the origin.

The same holds in $\mathbb R^n$, $n\ge2$, after composing with a projection. 【已核：极小对理论（Grzybowski–Urbański Thm 7.1、7.2、7.4；Scholtes 1992），须引用】

## Q3. Can ordinary component information reach decomposition-free stationarity?

**Proposition 3.1 (target ladder).** $(r,\varepsilon)$-L2 implies $(r,\varepsilon)$-L1, which implies $(2G_\phi r,2G_gr,\varepsilon)$-VAC. The converse of the first implication fails: the origin in Theorem 2.3 satisfies L1 exactly but has L2 residual $1/\sqrt2$. 【已核】

**Theorem 3.2 (L1 is dimension-free).** A deterministic algorithm using only $\mathcal O_{\mathrm{comp}}$ outputs an $(r,\varepsilon)$-L1 point with

$$
O\Bigl[\bigl(1+\tfrac{\Delta}{r\varepsilon}\bigr)\bigl(1+\tfrac{B^2}{\varepsilon^2}\bigr)\bigl(1+\tfrac{G_g}{\varepsilon}\bigr)\Bigr]
$$

queries, independently of $n$. 【待审】

**Lemma 3.3 (local purification).** For any $z\in\mathbb R^n$, $\tau>0$ and $s\in(0,B]$, a deterministic procedure finds $y\in B_\tau(z)$ such that every $u\in\partial\phi(y)$ and $v\in\partial g(y)$ satisfy $\operatorname{dist}\bigl(u-v,\partial_CF(y)\bigr)\le s$. It uses at most $n\bigl(\lceil\log_2(4B\lceil\sqrt n\rceil/s)\rceil+2\bigr)+1$ queries. 【待审：核心引理】

**Theorem 3.4 (L2 is reachable).** A deterministic algorithm using only $\mathcal O_{\mathrm{comp}}$ outputs a Goldstein $(r,\varepsilon)$-stationary point of $F$ with

$$
O\Bigl[\bigl(1+\tfrac{\Delta}{r\varepsilon}\bigr)\bigl(1+\tfrac{B^2}{\varepsilon^2}\bigr)\Bigl(1+\tfrac{B}{\varepsilon}+n\log\bigl(2+\tfrac{B\sqrt n}{\varepsilon}\bigr)\Bigr)\Bigr]
$$

queries. 【待审：纯化与线搜索的衔接】

**Theorem 3.5 (the dimension dependence is necessary).** Fix $r\in(0,1)$ and $\varepsilon\in(0,1/\sqrt2)$. For every $n\ge3$ and every deterministic algorithm making at most $n-3$ queries, there is $(\phi,g)\in\mathcal D(3,1,1)$, consistent with all oracle answers, whose output $\hat x$ satisfies $0\in\partial\phi(\hat x)\cap\partial g(\hat x)$ but $\operatorname{dist}\bigl(0,\partial_rF(\hat x)\bigr)\ge1/\sqrt2$. 【已核：把 Theorem 2.3 的结构嵌入未探测的二维子空间】

**Corollary 3.6.** With $r,\varepsilon,B,\Delta$ fixed, $N_{\mathrm{L1}}(n)=O(1)$, while $\Omega(n)\le N_{\mathrm{L2}}(n)\le O(n\log n)$. When $n\lesssim B/(\varepsilon\log)$, the bound of Theorem 3.4 has the same order as the Kong–Lewis bound, which requires a directional oracle with Clarke-compatible vectors.

## 与已有工作的对比：解决了什么局限

**Q1。** 弱凸类的确定性复杂度已定为 $\Theta(\varepsilon^{-4})$（Davis–Drusvyatskiy 上界，Li–Pan 下界）；两侧非光滑的 DC 类不弱凸，此前不知道认证代价是否会因此上升。DCA 的复杂度分析多数假设负侧光滑，或按精确凸子问题计数（DCA-PAGE、Faust 等的 Bregman 分析）。Xu 等（ICML 2019）在两侧非光滑时计入了内层成本，但目标是不动点映射，没有可验算的同点证书，也没有下界。不精确 DCA 的一类工作（tPLDCA、InDCA、InmBDCA）使用 $\varepsilon$-次微分，同样没有下界。**本文给出一张可显式验算的同点证书：负侧保持精确，确定性代价为 $\Theta(\varepsilon^{-4})$，下界在给出完整次微分时依然成立。** 结论是：超出弱凸的部分不增加认证代价，正侧的值松弛不可缺少，负侧的则可以去掉。

**Q2。** Pang–Razaviyayn–Alvarado 区分了 DC 临界与 d-stationarity；Tian–So（SPM 2026）指出坏的分解能让任意点成为临界点，这是存在性的一面。反方向的问题一直没有回答：好的分解能否总把伪临界消除？**本文回答：一维总能，一个规范分解在所有点同时消除伪临界，并保持分量界；从二维起不能，存在在每个分解下都临界、Goldstein 残差却固定为 $1/\sqrt2$ 的点。** 问题只出在公共折点上。二维的几何机制来自极小对理论；本文的贡献是给出它的优化含义、一维到二维的门槛和定量分离，说明证书的缺陷属于 DC 临界本身，不是求解精度或分解选择造成的。

**Q3。** 原目标的 Goldstein 驻点是这个领域的标准目标。随机方法（Zhang 等 2020；Davis 等 2022）与维数无关，但依赖随机扰动。对一般 Lipschitz 函数，确定性方法不能与维数无关（Jordan 等 2023；Tian–So 2024），代价为维数指数级（Kornowski 2026）。Kong–Lewis（MOR 2024）在 DC 等非凸模有界的类上给出确定性、与维数无关的方法，但要求 oracle 返回原目标的方向导数和 Clarke 相容向量；DCA 拥有的分量次梯度之差在公共折点上不提供这种信息，因此不能直接接入他们的算法。Tian–So（SODA 2025）需要分段仿射表示和精确的驻点检验 oracle。**“确定性方法 × DCA 的普通分量信息 × 原目标 Goldstein 驻点”这一格此前是空的。本文证明它可以达到：局部纯化用凸函数 $\phi+g$ 控制 $\phi-g$ 的次梯度失真，确定性地得到原目标的 Goldstein 驻点；中等维数下与强 oracle 方法同阶，维数依赖近似最优。** 只要求分量配对证书时，代价与维数无关；要求原目标驻点时，线性维数依赖不可避免，其困难实例正是 Q2 的不可消除伪临界结构。

方法新颖性待核：须与 Nesterov 2005 的字典序微分、Khan–Barton 的 LD 导数比较，二者用方向导数逐方向得到 Clarke 型元素。
