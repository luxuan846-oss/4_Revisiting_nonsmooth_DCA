# 论文结构（2026-10-16 讨论后，第二版）

编号约定：问题按在论文中出现的顺序编号为 Q0–Q3。状态标记：【已证】【推导待核】【草稿】【未证】【初稿已有】。

## 一、全文一句话

> 失去弱凸性以后，确定性方法并不必然失效（Kong–Lewis 已在方向 oracle 下对 DC 的 Goldstein 目标给出确定性上界；本文的增量是普通分量 oracle、紧界与目标的刻画）。对分量有界的 DC 问题，同点近似 DC 临界在有限时间内不可达；由 DCA 下降机制导出的值松弛临界点（VAC）在负侧光滑时推出 Moreau 驻点，它与真正驻点之间的差距是 DC 临界固有的、换分解无法消除；VAC 的确定性最优复杂度为 $\Theta(\varepsilon^{-4})$，与弱凸情形相同。确定性方法能否越过 VAC 达到与分解无关的目标，是本文提出的边界问题。

## 二、四个问题（按出现顺序）

| 编号 | 问题 | 回答 | 章节 | 状态 |
|---|---|---|---|---|
| Q0 | 两侧都非光滑时，同点近似 DC 临界能达到吗？ | 不能，有限时间内不可达；正侧值松弛不可缺少 | §3 | 推导待核 |
| Q1 | VAC 对目标函数保证了什么？它的缺陷是它自己造成的吗？ | 负侧光滑时推出 Moreau 驻点，确定 $\delta\sim\varepsilon^2$；伪临界是 DC 临界固有的，二维起换分解也无法消除 | §5 | $F_0$ 已证，校准与一维结论待核 |
| Q2 | 超出弱凸后，确定性方法达到 VAC 的最优代价是多少？ | $\Theta(\varepsilon^{-4})$，与弱凸相同；成对给出完整次微分也不能更快 | §6–§7 | 上界待核，下界草稿 |
| Q3 | 在 DC 方法实际使用的普通分量 oracle 下，确定性方法能达到的最强目标在哪一层？ | 未知；关键是同点配对的 Goldstein 能否达到 | §8 | 未证 |

## 三、逻辑主线与过渡（按论文顺序）

| 步 | 内容 | 过渡到下一步 |
|---|---|---|
| 背景（已有结果） | 弱凸类的确定性复杂度已定为 $\Theta(\varepsilon^{-4})$。失去弱凸后：同点近驻点与 Moreau/NAS 目标不可达；一般 Lipschitz 上，确定性求 Goldstein 驻点需指数代价。DC 文献把同点近似 DC 临界当作目标与停机准则，已有速率依赖负侧光滑或按精确子问题计数，两侧非光滑时它能否达到没有人问过 | DC 类比弱凸大、比一般 Lipschitz 有结构。确定性方法在这里还剩下什么？先看 DC 文献的标准目标 |
| Q0（§3） | 同点近似 DC 临界在有限时间内不可达；$\delta_\phi\to0$ 一端也不可达 | 必须放松。凸分析中有空间松弛（附近点的次梯度）与值松弛（$\varepsilon$-次微分）两种经典工具；DCA 的下降恒等式控制的是 Fenchel 间隙，即函数值误差，所以 DCA 的证书应当用值松弛来写 |
| VAC（§4） | 从单步恒等式读出三个误差来源，构造 VAC | VAC 依赖分解。它对 $F$ 保证了什么？缺陷是它自己造成的吗？ |
| Q1（§5） | 交集与包含的差距只在 $g$ 的折痕处；负侧光滑时 VAC 推出 Moreau 驻点；“换个好分解就能修好”在一维成立，二维 $F_0$ 推翻它 | VAC 只继承 DC 临界的固有缺陷，并在负侧光滑时与 Li–Pan 的目标对齐。在 $\delta=\varepsilon^2$ 这个尺度上，确定性代价是多少？ |
| Q2 上界（§6） | 不精确近端 DCA，确定性、普通分量 oracle、计入内层成本、不需强凸：$O(\Delta B^2\delta^{-1}\varepsilon^{-2})$ | 换成任何算法，能否少于 $\varepsilon^{-4}$？给出两个分量的完整次微分有没有帮助？ |
| Q2 下界（§7） | 成对返回完整次微分时仍需 $\Omega(\varepsilon^{-4})$ | 负侧非光滑没有增加确定性代价。但 VAC 仍会被伪临界骗，而 Q1 说明只能换目标。同样的信息下，确定性方法能达到更强的目标吗？ |
| Q3（§8） | 目标阶梯 L0/L1/L2；L0 可达；L2 在方向 oracle 下可达；普通分量 oracle 下 L1、L2 未知 | 回答“DC 分解消除了哪些障碍、留下了哪些信息损失”，并引出随机推论与讨论 |

## 四、章节结构

### 1. Introduction　【改写】`sections/introduction.tex`

**1.1 背景：非光滑非凸优化中的确定性复杂度**
- 弱凸类：Davis–Drusvyatskiy (SIOPT 2019) 给出 Moreau 驻点的 $O(\varepsilon^{-4})$ 上界；Li–Pan (arXiv 2608.03246) 给出确定性 $\Omega(\varepsilon^{-4})$ 下界。确定性复杂度定为 $\Theta(\varepsilon^{-4})$。
- 失去弱凸性后的三类负面结果：
  - 同点近驻点不可达：Zhang 等 (ICML 2020)；凸函数上也不可达：Kornowski–Shamir (arXiv 2209.10346)。
  - NAS（Moreau 型近驻点）在弱凸参数无界时不可达：Tian–So (ICML 2021 workshop)。
  - Goldstein 驻点：随机算法 $\Theta(\delta^{-1}\varepsilon^{-3})$（Zhang 等 2020；Cutkosky 等 ICML 2023；Kornowski arXiv 2609.17780）；确定性算法无法维数无关（Jordan 等 COLT 2023；Tian–So MP 2024），代价为 $(1/\varepsilon)^{\Omega(d)}$（Kornowski arXiv 2609.23837）。
- DC 类介于两者之间：负侧非光滑时不再弱凸，但保留凸分解。Kong–Lewis (MOR 2024) 在方向次梯度 oracle 下给出确定性 Goldstein 的 $O(\delta^{-1}\varepsilon^{-4})$。

**1.2 核心问题**
> 在分量有界的 DC 类上，确定性方法能否保住弱凸情形的最优复杂度？能达到什么目标，代价是多少，失去了什么？

**1.3 已有目标为何不够**
- 同点近似 DC 临界：DC 文献的标准目标与停机准则；已有速率依赖负侧光滑，或按精确子问题计数；两侧非光滑时能否达到没有人回答（Q0 证明不可达）。
- Moreau/NAS：负侧非光滑时不可达。
- Goldstein：需要随机化，或需要比 DC 方法常用信息更强的方向 oracle；与 DCA 的模型机制无关。
- DCA-PAGE 的单侧 gap：只控制旧点负侧见证的误差。精确 DCA 每步正侧间隙恒为零，单侧读数不足以说明临界。

**1.4 本文的回答**
- Q0：两侧非光滑时，同点近似 DC 临界在有限时间内不可达，正侧值松弛不可缺少。
- 由 DCA 的单步恒等式导出值松弛临界点 VAC。
- Q1：负侧光滑时 VAC 推出 Moreau 驻点；伪临界是 DC 临界固有的，二维起换分解也无法消除。
- Q2：VAC 的确定性最优复杂度为 $\Theta(\varepsilon^{-4})$，与弱凸相同；成对给出完整次微分也不能更快。
- Q3：提出确定性边界问题——普通分量 oracle 下，确定性方法能否越过 VAC。

**1.5 贡献**
1. 不可达性（Q0）：本文提出的问题与针对 DC 临界的结论；证明借用 Kornowski–Shamir 的凸困难族，通过 DC 嵌入完成；需与 Tian–So 2021（某些 DC 程序上 NAS 的困难性）区分。
2. VAC：由 DCA 单步恒等式导出的三参数联合证书 $(\delta_\phi,\delta_g,\varepsilon)$，三项分别对应内层求解误差、负侧运输误差、对偶不匹配；负侧运输间隙 $\Psi_g(x^{k+1},v^k)$ 是判断精确 DCA 是否接近临界的关键量。
3. VAC 的含义（Q1）：负侧光滑时的 Moreau 校准；伪临界只出现在 $g$ 的折痕处；一维中换分解总能消除，二维 $F_0$ 在原点对所有分解都 DC 临界却不是 Clarke 驻点。
4. 确定性最优复杂度（Q2，主结果）：上界由函数值不精确的近端 DCA 给出，按基本查询计数、计入内层成本、不需强凸；下界由 Li–Pan 实例加有界凸化项给出，成对 oracle 不泄露信息。
5. 确定性边界（Q3）：目标阶梯；由 Kong–Lewis 推出 Kornowski 的指数困难实例不在有界 DC 类中；普通分量 oracle 下同点配对 Goldstein 的可达性（证出为定理，否则为开放问题）。

**1.6 给两类读者的启发**
- 非光滑非凸：
  1. “失去弱凸后确定性方法失效”有适用范围：有界 DC 结构下，确定性方法仍以 $\Theta(\varepsilon^{-4})$ 达到 VAC。
  2. 确定性代价由负侧的凹结构（$g$ 的 Lipschitz 常数，或 Kong–Lewis 的非凸模）决定，而非由非光滑性本身决定。
  3. Q3 将回答随机化具体提供了哪部分信息。
- 非光滑 DC：
  1. 两侧非光滑时，同点近似临界这一标准停机准则没有有限时间保证。
  2. 真实成本为 $\Theta(\varepsilon^{-4})$ 次基本查询；按子问题次数报告的 $\varepsilon^{-2}$ 来自“每步精确求解凸子问题”的能力，分解本身不带来加速。
  3. 伪临界是 DC 临界的固有现象；一维直觉会误导，换分解无法消除。
  4. DCA 用旧点的 $v$ 与新点的 $u$ 跨点配对，这可能是它保持确定性的原因（Q3 检验）。

**1.7 相关工作**
- DCA 复杂度：Faust–Fawzi–Saunderson (AISTATS 2023) 的 Bregman 单步分解；Nguyen 等 DCA-PAGE (arXiv 2509.11657) 的单侧 gap；不精确 DCA（tPLDCA, Optimization 2024；de Oliveira–Tcheou InDCA, SVVA 2019；InmBDCA, JOTA 2025）用 $\varepsilon$-次微分设计算法，无下界、无联合证书。
- d-stationarity：Pang–Razaviyayn–Alvarado (MOR 2017)；2026 年 Feng–Yuan、Niu、Le Thi 等的随机/扰动 DCA 几乎必然收敛；Tian–So (SODA 2025) 的检验困难性；Tian–So (SPM 2026) 关于分解依赖的论述。
- 非光滑非凸驻点复杂度：1.1 节列出的 Goldstein 线与 Kong–Lewis。
- 弱凸下界：Li–Pan。
- 差别：本文在分量有界的 DC 类上同时给出不可达性、目标构造、含义刻画和确定性紧界。

**1.8 结构安排**：§2 设定，§3 Q0，§4 VAC，§5 Q1，§6–§7 Q2，§8 Q3，§9 随机推论，§10 讨论。

### 2. Problem Class, Oracle, and Success Criteria　【改写】`sections/preliminaries.tex`

- 函数类 $\mathcal D(G_\phi,G_g,\Delta)$：$\phi,g:\mathbb R^n\to\mathbb R$ 凸、全空间有限值，$\operatorname{Lip}(\phi)\le G_\phi$，$\operatorname{Lip}(g)\le G_g$，$F(x^0)-\inf F\le\Delta$；维数允许随精度增长。删去原稿的强凸假设（与有界次梯度不相容）。
- oracle：成对分量查询返回 $\bigl(\phi(x),g(x),u\in\partial\phi(x),v\in\partial g(x)\bigr)$，次梯度由 oracle 任选；下界允许返回完整次微分。精确凸子问题调用与近端调用另列，单独计数，不与基本查询混用。
- 成功判据：输出一个满足证书的点；输出可核查的对偶见证另作说明（负侧间隙可由查询值计算，正侧需内层原始–对偶信息）。
- 算法类：确定性算法；随机算法仅在 §9 讨论。
- **过渡**：在这个设定下，DC 文献的标准目标能否达到？

### 3. Exact Same-Point Criticality Is Unreachable (Q0)　【改写】替换 `appendix/Finite_Time_Barriers_of_DC.tex`

- 3.1 目标：同点近似 DC 临界，即存在 $u\in\partial\phi(x)$、$v\in\partial g(x)$ 使 $\lVert u-v\rVert\le\varepsilon$。
- 3.2 定理：对固定常数 $G_\phi,G_g,\Delta$ 与任意有限预算，存在 $\mathcal D$ 中实例，使算法的所有迭代点都不满足 3.1 的条件。证明为凸归约：取 Kornowski–Shamir 的一维凸困难族 $q$，令

$$
\phi_q(x,y)=q(x)+\lvert y\rvert+\lvert y-1\rvert,\qquad g_q(x,y)=\lvert y-1\rvert,\qquad F_q=q(x)+\lvert y\rvert,
$$

  则 $\operatorname{dist}\bigl(\partial\phi_q,\partial g_q\bigr)\ge\operatorname{dist}(0,\partial q(x))$，一次成对查询只需一次 $q$ 的查询，分量 Lipschitz 常数不超过 $\sqrt5$ 与 $1$。量词顺序按 Kornowski–Shamir 原文。
- 3.3 推论：取 $g=0$，VAC$(0,\delta_g,\varepsilon)$ 化为凸函数的同点小次梯度，同样不可达；正侧值松弛不可缺少。
- 3.4 附带观察：在 $q$ 的极小点 $x_*$，$(x_*,1)$ 是 DC 临界点，而 $F_q$ 沿 $y$ 方向仍可下降，为 §5 的伪临界预告。
- **过渡**：目标必须放松。空间松弛与值松弛是两种经典工具；DCA 的下降恒等式控制的是函数值误差，因此用值松弛写 DCA 的证书。

### 4. A Certificate Read Off the DCA Descent Identity　【初稿已有，压缩】`criticality.tex` 170–480、`deterministic_dca.tex` 213–277

- 4.1 单步恒等式：对 $v^k\in\partial g(x^k)$，

$$
F(x^k)-F(x^{k+1})=\Psi_\phi(x^k,v^k)+\Psi_g(x^{k+1},v^k)-\Psi_\phi(x^{k+1},v^k),
$$

  其中 $\Psi_h(x,v)=h(x)+h^*(v)-\langle v,x\rangle$。三项对应：当前子问题的求解误差、旧负侧次梯度运到新点的误差、新点的正侧误差。精确 DCA 有 $\Psi_\phi(x^{k+1},v^k)=0$，判断临界需要 $\Psi_g(x^{k+1},v^k)$。不依赖强凸。
- 4.2 定义 VAC：$u\in\partial_{\delta_\phi}\phi(x)$，$v\in\partial_{\delta_g}g(x)$，$\lVert u-v\rVert\le\varepsilon$；等价于 $\Psi_\phi(x,u)\le\delta_\phi$，$\Psi_g(x,v)\le\delta_g$，$\lVert u-v\rVert\le\varepsilon$。值松弛工具本身是经典的，联合证书属于本文。
- 4.3 与已有概念的关系：恢复 $\varepsilon$-critical、nearly $\varepsilon$-critical、nearly $\varepsilon$-stationary（初稿 483–660）；反向嵌入的平方根损失（Brøndsted–Rockafellar，初稿 661–766）；Goldstein ⟹ VAC，容差为 $2G r$，反向不成立（初稿 768–890）。长证明移入附录 B。
- **过渡**：VAC 依赖分解。它对 $F$ 保证了什么？它的缺陷是它自己造成的吗？

### 5. What VAC Certifies (Q1)　【以新增为主】

- 5.1 DC 临界从哪里来：DCA 的不动点条件等价于 $\partial\phi(x)\cap\partial g(x)\neq\emptyset$（交集）；$F$ 在 $x$ 处无下降方向等价于 $\partial g(x)\subseteq\partial\phi(x)$（包含）。$g$ 在 $x$ 可微时，$\partial_C F(x)=\partial\phi(x)-\nabla g(x)$，交集与包含一致，没有伪临界。差距只出现在 $g$ 的折痕处。【已证，标准】
- 5.2 负侧光滑时的校准：$g$ 凸且 $\rho$-光滑时，VAC 给出 $\operatorname{dist}(\nabla g(x),\partial_{\delta_\phi}\phi(x))\le\varepsilon+\sqrt{2\rho\delta_g}$（初稿 `prop:reverse-smooth`），进一步

$$
\lVert\nabla F_{1/(2\rho)}(x)\rVert\le b+\sqrt{b^2+4\rho\delta_\phi},\qquad b=\varepsilon+\sqrt{2\rho\delta_g}.
$$

  因此 $\delta_\phi,\delta_g=O(\varepsilon^2/\rho)$ 对应 $O(\varepsilon)$ 的 Moreau 驻点，确定 §6–§7 使用的尺度。【推导待核】
- 5.3 伪临界的两个来源：
  - 人为加入的公共折痕：$\phi=\lvert x\rvert+\lvert x-1\rvert$，$g=\lvert x\rvert$，$F=\lvert x-1\rvert$，原点 DC 临界而 $F'(0)=-1$；Tian–So (SPM 2026) 用同一手法说明任意点都能被分解成临界点。
  - 凹折痕处的局部极大：$F=-\lvert x\rvert$，$\phi=0$，$g=\lvert x\rvert$。
- 5.4 换分解能修好吗：
  - 一维：取 $F'$ 的 Jordan 分解（正变差给 $\phi'$，负变差给 $g'$），在这一个分解下每一点都有 DC 临界 ⟺ Clarke 驻点，所有非 Clarke 伪临界点同时消除。【推导待核】
  - 二维：$F_0(x)=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}$。三条凹折痕迫使任何分解的 $\partial g(0)$ 含有长度下界的面，于是对每个方向 $d$ 都有 $w_{\partial g(0)}(d)\ge-F_0(d)$，原点对所有分解都 DC 临界；而 $\partial_C F_0(0)=\operatorname{conv}\{e_1,e_2,(1,1)\}$，$\operatorname{dist}(0,\partial_C F_0(0))=1/\sqrt2$。加上 $3\max\{\lVert x\rVert-1,0\}$ 得到分量有界、目标下有界的版本。【已证，新意待查拟微分与极小对文献】
- 5.5 小结：VAC 在容差为零时就是精确 DC 临界，只继承 DC 临界的固有缺陷；负侧光滑时它与 Moreau 目标对齐。初稿 907–1078 的分解依赖内容压缩并入本节。
- **过渡**：在 $\delta=\varepsilon^2$ 这个尺度上，确定性方法达到 VAC 要多少代价？

### 6. Deterministic Upper Bound (Q2)　【改写】`sections/deterministic_dca.tex`

- 6.1 函数值不精确的近端步：固定 $x$、$v\in\partial g(x)$、$\eta>0$，

$$
M(y)=\phi(y)-\langle v,y\rangle+\tfrac{1}{2\eta}\lVert y-x\rVert^2,\qquad z=\arg\min M,\qquad M(y)-M(z)\le\sigma .
$$

  分析见证 $u=v-(z-x)/\eta\in\partial\phi(z)$ 满足 $M(y)-M(z)=\Psi_\phi(y,u)+\tfrac{1}{2\eta}\lVert y-z\rVert^2$，故 $u\in\partial_\sigma\phi(y)$，并有联合下降不等式

$$
\Psi_g(y,v)+\tfrac{\eta}{2}\lVert u-v\rVert^2\le F(x)-F(y)+\sigma .
$$

- 6.2 定理：选观察到的下降最小的一步输出，得到 $\bigl(\sigma,\ \Delta/K+\sigma,\ \sqrt{(2/\eta)(\Delta/K+\sigma)}\bigr)$ 证书。内层用强凸次梯度法，成本 $O(1+\eta B^2/\sigma)$，$B=G_\phi+G_g$。取 $\eta=\delta/\varepsilon^2$、$\sigma=\delta/4$、$K=\lceil4\Delta/\delta\rceil$，总成本 $O(\Delta B^2\delta^{-1}\varepsilon^{-2})$；$\delta=\varepsilon^2/\rho$ 时为 $O(\rho\Delta B^2\varepsilon^{-4})$。算法确定性，只用普通分量 oracle。【推导待核】
- 6.3 推论（按子问题调用计数）：精确 DCA 给 $(0,\Delta/K,0)$；函数值不精确 DCA 给 $(\sigma,\Delta/K+\sigma,0)$；精确近端 DCA 给 $\bigl(0,\Delta/K,\sqrt{\Delta/(\eta K)}\bigr)$。说明 $O(\varepsilon^{-2})$ 次子问题调用与 $O(\varepsilon^{-4})$ 次基本查询描述的是同一实现的外层与总成本。【初稿已有，压缩】
- 6.4 注记：容差不对称。在旧点输出可得 $\delta_g=0$，代价为 $O(\Delta B^2\delta_\phi^{-1}\varepsilon^{-3})$；而 $\delta_\phi=0$ 由 §3 不可达。【推导待核】
- 6.5 删除与修正：删去初稿 373–405 的 “matching lower bound”；1466 起的平滑部分改为读出原分解的值证书，负侧平滑常数不进入步长。
- **过渡**：换成任何算法，能否少于 $\varepsilon^{-4}$？给出两个分量的完整次微分有没有帮助？

### 7. Matching Lower Bound (Q2)　【新增】替换 `appendix/lowerbound.tex`

- 7.1 困难族：Li–Pan 的未缩放实例 $\bar F$（$M\times N$ 坐标、平滑进度函数）。有界凸化项

$$
c_N(t)=\begin{cases}0,&t\le0,\\ \tfrac38t^2-\tfrac{N}{16}t^3,&0<t<2/N,\\ \tfrac{3}{4N}t-\tfrac{1}{2N^2},&t\ge2/N,\end{cases}
$$

  $C_N(z)=\sum_{m,j}c_N(z^m_j)$，$\bar g=C_N$，$\bar\phi=\bar F+C_N$。$0\le c_N'\le\tfrac{3}{4N}$，$0\le c_N''\le\tfrac34$，覆盖 $\bar F$ 所需负曲率；$\operatorname{Lip}(\bar g)\le\tfrac34\sqrt{M/N}$，$\operatorname{Lip}(\bar\phi)\le1+\tfrac34\sqrt{M/N}$，由 $M\le N/12$ 为常数。
- 7.2 不泄露：$c_N'(0)=0$，只用已显露坐标的点处 $\nabla C_N$ 也只涉及这些坐标，两个分量的完整次微分不跳过隐藏层；抵抗 oracle 的不变量同时作用于两个分量，新坐标方向与历史查询正交。
- 7.3 定理：在固定常数的类上，任意确定性算法要输出 $(\varepsilon^2,\varepsilon^2,\varepsilon)$-VAC 点，需要 $\Omega(\varepsilon^{-4})$ 次成对查询，即使每次返回两个完整次微分。由 §5.2 的 Moreau 归约传递 Li–Pan 下界；$N=\Theta(\varepsilon^{-2})$，$M=\Theta(N)$。【草稿】
- 7.4 两侧都非光滑的版本：$\tilde\phi=\bar\phi+2\lvert t\rvert$，$\tilde g=\bar g+\lvert t\rvert$。
- 7.5 解读：与 §6 合起来为 $\Theta(\varepsilon^{-4})$；负侧非光滑没有增加确定性代价；按子问题计数的 $\varepsilon^{-2}$ 来自精确求解能力，分解本身不带来加速。随机化下界与三个容差的完整依赖不在本文范围内。
- **过渡**：VAC 以最优代价可达，但仍会被伪临界骗；§5 说明只能换目标。同样的信息下，确定性方法能达到更强的目标吗？

### 8. The Deterministic Frontier (Q3)　【新增】

- 8.1 目标阶梯：
  - L0：VAC，两侧各自做值松弛，可来自不同的点。
  - L1：同点配对的 Goldstein，$\operatorname{conv}\bigcup_{y\in B_r(x)}\bigl(\partial\phi(y)-\partial g(y)\bigr)$ 中有范数不超过 $\varepsilon$ 的元素；普通分量 oracle 返回的 $u_y-v_y$ 恰是这类向量；仍会被 $F_0$ 型伪临界骗。
  - L2：$F$ 的 Goldstein，$\operatorname{conv}\bigcup_{y\in B_r(x)}\partial_C F(y)$；与分解无关。
  - 蕴含关系：L2 ⟹ L1 ⟹ L0（容差约 $2Gr$）。
- 8.2 已知：L0 确定性可达（§6–§7）；L2 在方向次梯度 oracle 下确定性可达，$O(\Delta L^2G_g\,r^{-1}\varepsilon^{-4})$（Kong–Lewis，非凸模 $\Lambda\le G_g$）。由于 Kornowski 的局部 oracle 能模拟方向 oracle，他的指数困难实例必然不在有界 DC 类中。【推导待核】
- 8.3 核心问题：普通分量 oracle 下，确定性方法能否以多项式代价达到 L1？关键引理（纯化）：能否只用函数值与任意次梯度，在半径 $\tau$ 内确定性地找到点 $y$ 及距 $\partial_C F(y)$ 不超过 $s$ 的向量，代价 $\operatorname{poly}(G/s)$；可用结构是沿任一直线 $g$ 的凹折痕总量不超过 $2G_g$。
  - 若 L1 不可达：VAC 恰在确定性边界上；DCA 的跨点配对正是绕开同点配对障碍的方式。
  - 若可达：问题移到 L1 与 L2 之间，即纯化引理本身。
- 8.4 定位对照（只作定位，不作主张）：随机/确定 × VAC/Goldstein × 弱凸/DC 的已知速率。
- 8.5 写法：8.3 证出则为主定理之一；否则写成开放问题并给出两个方向的部分证据。【未证】
- **过渡**：同一机制在随机情形下的推论。

### 9. Stochastic Extension　【改写，压缩】`sections/stochastic_dca.tex`

- 随机 PS-DCA 模板：路径级下降与误差分离；有界方差下 $O(\varepsilon^{-4})$，作为 §6 的推论。
- 修正：已构造的正侧见证属于精确 $\partial\phi$，写 $\delta_\phi=0$；含噪声项的界只说明该界不能保证任意小精度；MVR 误差递推改用新样本条件与均方光滑性。
- 其余（动量变体、MVR 细节）移入附录 C。

### 10. Discussion　【新增】替换 `sections/conclusion.tex`

**10.1 给非光滑非凸研究者**
1. “失去弱凸后确定性方法失效”有适用范围：有界 DC 结构下，确定性方法仍以 $\Theta(\varepsilon^{-4})$ 达到 VAC。
2. 确定性代价由负侧凹结构决定：Kornowski 的指数实例不在有界 DC 类中。
3. 值松弛与空间松弛是比较驻点目标的一条新坐标轴；Q3 将回答随机化提供了哪部分信息。

**10.2 给非光滑 DC 研究者**
1. 两侧非光滑时，同点近似临界的停机准则没有有限时间保证。
2. 真实成本为 $\Theta(\varepsilon^{-4})$ 次基本查询；$\varepsilon^{-2}$ 是按子问题计数。
3. 伪临界是 DC 临界的固有现象，换分解无法消除。

**10.3 算法设计原则**
- 非光滑非凸：有 DC 结构时用凸模型步代替 Goldstein 采样；用 $G_g$ 而非 $\rho$ 度量非凸性；停机判据用可直接计算的值松弛；随机化只用于逃离负侧折痕处的伪临界（依赖 Q3）。
- 非光滑 DC：按证书分配内层精度（$\sigma\sim\delta_\phi$，$\eta=\delta/\varepsilon^2$）；正则项放进子问题，不强凸化分量；内层求解器返回原始–对偶对；不依赖选分解避开伪临界，需要时显式加入逃离机制并计入预算；平滑负侧后读原分解的值证书；保持跨点配对。

**10.4 开放问题**
1. 普通分量 oracle 下 L1、L2 的确定性可达性（若 §8 未解决）。
2. 高维中“对所有分解都 DC 临界”的点的刻画（与极小拟微分对的关系）。
3. 从给定 DC 临界点出发寻找下降点的信息代价，及其与 $\partial g(x)$ 几何的关系。
4. 随机化下界，以及 $(\delta_\phi,\delta_g,\varepsilon)$ 三参数的完整最优依赖。

### 附录
- A：§3、§6、§7（及 §8 若有定理）的完整证明。
- B：§4.3 关系结果的长证明。
- C：随机部分细节。

### 删去
`sections/constrained_dc.tex` 全节；原标题中的 “Optimal Complexity” 表述（由 §7 的下界支撑后再使用）；摘要、致谢中的模板残留。

## 五、执行顺序

1. §3、§5、§6 先落稿（已有推导，风险低）。
2. §7 下界逐步核对（主结果的关键）。
3. §8 试证纯化引理，同时准备开放问题的写法。
4. §9 压缩；§1、§10 最后统一改写。
5. 投稿前核查：Tian–So 2021 原文；拟微分与极小对文献；“联合证书”与“弱凸之外首个紧确定性界”的提法。
