# GPT Pro 任务：普通分量 oracle 下确定性方法的边界（Q3）

使用方式：整段发给 GPT Pro。可附上 `overleaf/notes/project/paper-structure-2026-10-16.md` 与 `overleaf/notes/gpt-proofs/irremovable-pseudo-criticality-2026-10-16.md` 作为背景。第 8 节是审核用的第二个 prompt。

---

## 0. 角色与总要求

你是非光滑非凸优化复杂度方向的研究者。本任务要求证明或否证下面的命题，不要求写论文正文。

- 每个结论标注状态：**已证明**（附完整证明）／**否证**（附反例或反构造）／**部分结果**（写清已证部分与缺口）／**未解决**。
- 引用文献时写出定理编号、假设与 oracle 模型，并核对它与本任务的模型是否一致；不一致时说明差别如何影响结论。
- 猜想不得写成定理。证明中的每个“显然”都要展开。
- 不得为了得到正面结果而改变 oracle 模型（例如假设 oracle 返回极端次梯度、完整次微分或方向导数），也不得使用随机化，除非明确声明是在讨论对照模型。

## 1. 设定

**函数类** $\mathcal D(G_\phi,G_g,\Delta)$：$\phi,g:\mathbb R^n\to\mathbb R$ 凸、全空间有限值，$\operatorname{Lip}(\phi)\le G_\phi$，$\operatorname{Lip}(g)\le G_g$，$F=\phi-g$，$F(x^0)-\inf F\le\Delta$。记 $B=G_\phi+G_g$。维数 $n$ 任意。

**oracle**
- $\mathcal O_{\mathrm{comp}}$（普通分量 oracle）：查询 $x$，返回 $\phi(x)$、$g(x)$、某个 $u\in\partial\phi(x)$、某个 $v\in\partial g(x)$。$u,v$ 由对抗 oracle 选择，只要求与某个 $(\phi,g)\in\mathcal D$ 一致。注意 $F(x)=\phi(x)-g(x)$ 的值是精确可得的。
- $\mathcal O_{\mathrm{dir}}$（Kong–Lewis, MOR 2024, Oracle 2.5）：对 $F$ 的方向次梯度 oracle。
- $\mathcal O_{\mathrm{loc}}$（Kornowski, arXiv 2609.23837）：局部 oracle，揭示 $F$ 在查询点邻域内的全部信息。

**算法**：确定性算法；复杂度为查询次数。区分两种正面结果：
- (a) 维数无关：$\operatorname{poly}(1/r,1/\varepsilon,B,\Delta)$；
- (b) 依赖维数：$\operatorname{poly}(n,1/r,1/\varepsilon,B,\Delta)$。

**目标阶梯**
- L0（VAC）：存在 $u\in\partial_{\delta_\phi}\phi(x)$、$v\in\partial_{\delta_g}g(x)$，$\lVert u-v\rVert\le\varepsilon$。
- L1（同点配对的 Goldstein）：$\operatorname{dist}\Bigl(0,\ \operatorname{conv}\bigcup_{y\in B_r(x)}\bigl(\partial\phi(y)-\partial g(y)\bigr)\Bigr)\le\varepsilon$。
- L2（$F$ 的 Goldstein）：$\operatorname{dist}\Bigl(0,\ \operatorname{conv}\bigcup_{y\in B_r(x)}\partial_C F(y)\Bigr)\le\varepsilon$。

蕴含关系：L2 ⟹ L1（因 $\partial_C F(y)\subseteq\partial\phi(y)-\partial g(y)$）⟹ L0，容差 $\delta_\phi=2G_\phi r$、$\delta_g=2G_g r$（因 $\operatorname{conv}\partial\phi(B_r(x))\subseteq\partial_{2G_\phi r}\phi(x)$）。请核对这两步。

## 2. 已知结果与已有推导（先核对，再使用）

- **K1（L0 上界）**：函数值不精确的近端 DCA。固定 $x$、$v\in\partial g(x)$、$\eta>0$，$M(y)=\phi(y)-\langle v,y\rangle+\frac{1}{2\eta}\lVert y-x\rVert^2$，$z=\arg\min M$，$M(y)-M(z)\le\sigma$。取 $u=v-(z-x)/\eta$，有

$$
\Psi_g(y,v)+\tfrac{\eta}{2}\lVert u-v\rVert^2\le F(x)-F(y)+\sigma ,
$$

  由此在 $\mathcal O_{\mathrm{comp}}$ 下确定性地以 $O(\Delta B^2\delta^{-1}\varepsilon^{-2})$ 次查询达到 L0。请核对。
- **K2（Kong–Lewis, MOR 2024）**：在 $\mathcal O_{\mathrm{dir}}$ 下，Algorithm 4.1 确定性地达到 L2。我们从 PDF 文本推断其 Theorem 6.6 的界为 $O(\Delta L^2\Lambda(r)\,r^{-1}\varepsilon^{-4})$（抽取时丢失了 $\varepsilon$，请按原文核对指数）；Prop 6.3 给出 $\Lambda(r)\le\operatorname{Lip}(g)$。请核对 Oracle 2.5 是否要求返回的向量属于 $\partial_C F$。
- **K3（Kornowski, arXiv 2609.23837, Theorem 3.1）**：对一般 Lipschitz 函数，确定性局部算法达到 L2 需 $(L/(32\varepsilon))^{d/2}$ 次查询。
- **K4（Kornowski, arXiv 2609.17780）**：$\Omega(r^{-1}\varepsilon^{-3})$，对 zero-respecting 算法（含随机）。
- **K5（Jordan 等, COLT 2023；Tian–So, MP 2024）**：确定性算法不能维数无关；Jordan 等指出确定性算法需要函数值。
- **K6（随机对照）**：在 $\mathcal O_{\mathrm{comp}}$ 下，对查询点做随机扰动后，$\phi,g$ 几乎必然可微，于是 $u-v=\nabla F$。所以随机算法下 $\mathcal O_{\mathrm{comp}}$ 与 $F$ 的梯度 oracle 等价，L2 可在 $O(r^{-1}\varepsilon^{-3})$ 内达到。差距完全来自确定性。请核对。
- **K7（待核观察）**：Kornowski 的指数困难实例不在常数适中的有界 DC 类中。理由：$\mathcal O_{\mathrm{loc}}$ 可以模拟 $\mathcal O_{\mathrm{dir}}$；若这些实例的非凸模有界，K2 会与 K3 矛盾。请检查 K2 的全部假设（方向半光滑性、Hadamard 方向可微、$L$-有界方向次梯度映射）在 Kornowski 的构造上是否成立，以及模拟是否严格。
- **K8（背景，已证）**：$F_0(x)=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}$ 在原点对任意分解都满足 $0\in\partial\phi(0)-\partial g(0)$，而 $\operatorname{dist}(0,\partial_C F_0(0))=1/\sqrt2$。因此 L1 与 L0 都会被这类伪临界点满足，L2 不会。

## 3. 待验证的假设

**H1（L1 在 $\mathcal O_{\mathrm{comp}}$ 下确定性、维数无关地可达）。** 候选路线：

- 关键事实：对凸 $\phi$、$u\in\partial\phi(y)$、单位向量 $e$，记 $p(t)=\phi(y+te)$，则

$$
\langle u,e\rangle\in\bigl[p'_-(0),\,p'_+(0)\bigr].
$$

  同理记 $q(t)=g(y+te)$，$h=p-q$，于是

$$
\langle u-v,e\rangle\in\bigl[p'_-(0)-q'_+(0),\ p'_+(0)-q'_-(0)\bigr],
$$

  与 $h$ 的单侧导数之差不超过 $p,q$ 在该点的一维跳跃。沿任一线段，$p'$ 与 $q'$ 的总跳跃不超过 $2G_\phi$ 与 $2G_g$。
- 设想：把 Kong–Lewis Algorithm 4.1 中的 $G(x,e)$ 换成 $\mathcal O_{\mathrm{comp}}$ 返回的 $u-v$，线搜索的二分用精确的 $F$ 值维护平均斜率。证明二分失败次数不超过 $1+2(\Lambda+G_\phi)/\sigma$ 或类似量；最小范数元的下降引理对 $\lVert w\rVert\le B$ 的伪向量仍成立；终止时得到的是 L1 证书。
- 任务：写出算法，证明线搜索引理与总复杂度，或指出这条路线失败的具体位置。

**H2（L2 在 $\mathcal O_{\mathrm{comp}}$ 下确定性困难）。** 候选构造：

- 对抗者向 $\phi$ 和 $g$ 同时加入一个凸函数 $c$（在 $F$ 中抵消），使 $c$ 的不可微集合经过所有查询点，从而 $u-v$ 偏离 $\partial_C F$。
- 必须处理的障碍：$\operatorname{Lip}(c)$ 有界；与全部历史回答一致；$F$ 的值精确可得且看不到 $c$；算法可以用 $F$ 的差商检验 $\langle u-v,d\rangle$ 是否一致；底层的 $F$ 本身必须保证 L2 在查询点处不成立。
- 可借鉴 Kornowski 2609.23837 中近正交方向与支撑函数延拓的技术。
- 任务：在 (a) 维数无关与 (b) $\operatorname{poly}(n)$ 两种意义下，分别给出下界构造，或说明构造为何失败。

**H3（L2 在 $\mathcal O_{\mathrm{comp}}$ 下确定性可达）。** 候选路线：

- 凸函数在某点可微当且仅当各偏导数存在（Rockafellar, Convex Analysis, Theorem 25.2）。定量版本：$\partial f(y)$ 落在一个盒子里，各边长等于沿各坐标方向的一维跳跃。
- 寻找使 $\phi$ 与 $g$ 沿各坐标方向跳跃都很小的点；或用 $F$ 的差商检测并修正伪向量；或给出确定性的“纯化”过程：在半径 $\tau$ 内找到 $y$ 及与 $\partial_C F(y)$ 距离不超过 $s$ 的向量。
- 任务：确定能否达到 (a) 或 (b)，给出复杂度。

## 4. 执行步骤

1. **Stage A**：形式化三个 oracle 与对抗 oracle 的一致性条件；逐条核对 K1–K7，写出所依据的定理编号。
2. **Stage B**：H1 的完整证明，或指出失败位置并给出反例。
3. **Stage C**：H2 的下界尝试，分 (a)、(b) 两种意义。
4. **Stage D**：H3 的上界尝试，分 (a)、(b) 两种意义。
5. **Stage E**：综合 C 与 D，给出 L2 在 $\mathcal O_{\mathrm{comp}}$ 下的判断。
6. **Stage F（自审）**：逐项检查量词顺序（先固定算法，再构造实例）、自适应性、对抗回答与某个 $(\phi,g)\in\mathcal D$ 的一致性、修改后的 Lipschitz 常数、$F$ 下有界、维数依赖；用一个小规模例子尝试推翻自己的每个主要证明。

## 5. 交付格式

1. 状态表：K7、H1、H2(a)、H2(b)、H3(a)、H3(b) 各一行，写状态与一句话结论。
2. 每个已证明结论的精确陈述，包括常数、量词与 oracle。
3. 完整证明或反例，放在附录形式的小节中。
4. 文献核查：2024–2026 年是否已有工作覆盖 H1、H2 或 H3（至少检查 Kong–Lewis 之后引用它的工作、Kornowski 2026 两篇、Tian–So 系列）。
5. 一段解释：在 $\mathcal O_{\mathrm{comp}}$ 下，确定性方法能认证的目标是否恰好停在伪临界缺口（L1 与 L2 之间）；若不是，边界在哪里。

## 6. 本任务的背景动机（供理解，不需要论证）

我们已有：同点近似 DC 临界在有限时间内不可达；VAC（L0）由 DCA 的下降恒等式导出，确定性最优复杂度为 $\Theta(\varepsilon^{-4})$（下界为草稿）；伪临界在二维起不可通过换分解消除（K8）。本任务要回答：在 DC 方法实际使用的信息下，确定性方法能否越过伪临界，达到与分解无关的驻点。

## 7. 禁止事项

- 混用 L1 与 L2。
- 使用随机化或更强的 oracle 而不声明。
- 把依赖未核对文献的步骤写成已证明。

---

## 8. 审核 prompt（把 GPT Pro 的回答交给另一个模型或另一个会话）

> 下面是一份关于“普通分量 oracle 下确定性 Goldstein 驻点可达性”的证明报告。请只做审核，不要重写结论。逐项检查：
> 1. oracle 模型是否始终是“返回 $\phi(x),g(x)$ 与对抗选择的 $u\in\partial\phi(x)$、$v\in\partial g(x)$”，有没有在某一步悄悄使用方向导数、完整次微分或极端次梯度；
> 2. 下界构造中，对抗回答是否与某个满足 Lipschitz 界的凸对 $(\phi,g)$ 一致，修改后常数是否仍与精度无关；
> 3. 量词顺序是否为“对任意确定性算法，存在实例”；
> 4. 上界中的线搜索引理是否真的只用到一维跳跃，伪向量 $u-v$ 是否被当成 $\partial_C F$ 的元素误用；
> 5. 结论属于 L1 还是 L2；
> 6. 维数依赖是否与声明一致。
> 对每一项给出“通过 / 有问题（指出行）/ 无法判断”，最后列出必须由人工核对的三个关键步骤。
