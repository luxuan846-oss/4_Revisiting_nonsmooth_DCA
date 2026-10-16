# GPT Pro 任务：全文逻辑与“新见解”核查

使用方式：整段发给 GPT Pro，并附上：
- `overleaf/notes/project/paper-structure-2026-10-16.md`（论文结构）
- `overleaf/notes/gpt-proofs/irremovable-pseudo-criticality-2026-10-16.md`（$F_0$ 与一维 Jordan 推导）
- 当前初稿 PDF（`overleaf/main.tex` 编译结果）

Q3（确定性边界）已有单独任务 `gptpro-q3-deterministic-frontier-prompt.md`，本任务只核查 Q3 的定位与 K7 观察，不要求证明 Q3。

---

## 0. 角色与要求

你是非光滑非凸优化与 DC 规划复杂度方向的研究者，也是 MP/JMLR 的严格审稿人。任务有两件：

1. **逐步核对逻辑**：下面的论文主线由若干断言组成，逐条判断是否成立、依据是否充分、量词与假设是否写对。
2. **检验新见解**：我们希望论文给读者带来“还能这么想”“竟然反直觉”“为什么我没想到”的感觉。第 4 节列出我们认为具有这种效果的点。请判断它们是否真的成立、是否已被前人得到、能否加强，并提供能支撑它们的材料（定理、证明、反例、文献原文定位）。

要求：
- 每条断言给出判定：**成立**／**需修正**（给出修正后的精确表述）／**不成立**（给出反例）／**无法判定**（说明缺什么）。
- 文献结论写出定理编号、函数类、oracle、算法类（确定性/随机/zero-respecting）、成功判据，并核对与本文设定是否一致。
- 修正表述时写成精确的数学陈述：补上假设、量词和常数依赖即可，不要加免责性的措辞。结论能正面陈述的就正面陈述。
- 区分三类内容：已有文献结果；我们的新结果；我们的猜想。
- 对“新意”的判断要说明检索了哪些文献线索；未找到先例时，给出最接近的工作以及差别所在。

## 1. 设定与记号

- 函数类 $\mathcal D(G_\phi,G_g,\Delta)$：$\phi,g:\mathbb R^n\to\mathbb R$ 凸、全空间有限值，$\operatorname{Lip}(\phi)\le G_\phi$，$\operatorname{Lip}(g)\le G_g$，$F=\phi-g$，$F(x^0)-\inf F\le\Delta$；$B=G_\phi+G_g$；维数允许随精度增长。
- 成对分量 oracle：查询 $x$ 返回 $\phi(x)$、$g(x)$、某个 $u\in\partial\phi(x)$、某个 $v\in\partial g(x)$；次梯度由 oracle 任选。下界允许返回完整次微分。精确凸子问题调用、近端调用单独计数。
- Fenchel 间隙：$\Psi_h(x,v)=h(x)+h^*(v)-\langle v,x\rangle$；$\Psi_h(x,v)\le\delta\iff v\in\partial_\delta h(x)$。
- **VAC**（值松弛临界点，本文提出）：存在 $u,v$ 使

$$
\Psi_\phi(x,u)\le\delta_\phi,\qquad\Psi_g(x,v)\le\delta_g,\qquad\lVert u-v\rVert\le\varepsilon .
$$

- 同点近似 DC 临界：存在 $u\in\partial\phi(x)$、$v\in\partial g(x)$，$\lVert u-v\rVert\le\varepsilon$。
- $(r,\varepsilon)$-Goldstein：$\operatorname{dist}\bigl(0,\operatorname{conv}\bigcup_{y\in B_r(x)}\partial_C F(y)\bigr)\le\varepsilon$。

## 2. 全文主线（按论文顺序）

> **一句话**：失去弱凸性以后，确定性方法并不必然失效（Kong–Lewis 已在方向 oracle 下对 DC 的 Goldstein 目标给出确定性上界）。对分量有界的 DC 问题，同点近似 DC 临界在有限时间内不可达；由 DCA 下降机制导出的 VAC 在负侧光滑时推出 Moreau 驻点；它与真正驻点之间的差距是 DC 临界固有的，一维中一个规范分解即可消除，二维起任何分解都消除不了；VAC 的确定性最优复杂度为 $\Theta(\varepsilon^{-4})$，与弱凸情形相同。确定性方法能否在同样的信息下越过 VAC，是本文提出的边界问题。

| 步 | 断言 | 过渡 |
|---|---|---|
| 背景 | 弱凸类确定性复杂度为 $\Theta(\varepsilon^{-4})$；失去弱凸后同点近驻点与 NAS 不可达，一般 Lipschitz 上确定性 Goldstein 需指数代价；DC 文献把同点近似 DC 临界当作目标与停机准则，两侧非光滑时它能否达到未被研究 | 先看 DC 的标准目标 |
| Q0 | 两侧非光滑时同点近似 DC 临界在有限时间内不可达；$\delta_\phi\to0$ 也不可达 | 必须放松；DCA 恒等式控制函数值误差，故用值松弛 |
| VAC | 由单步恒等式读出三个误差来源，构造 VAC | VAC 依赖分解，它保证了什么？ |
| Q1 | 伪临界只在 $g$ 的折痕处；负侧光滑时 VAC 推出 Moreau 驻点；一维规范分解消除全部非 Clarke 伪临界，二维 $F_0$ 不可消除 | 在 $\delta=\varepsilon^2$ 尺度上代价是多少？ |
| Q2 | 确定性上界 $O(\Delta B^2\delta^{-1}\varepsilon^{-2})$；成对完整次微分下界 $\Omega(\varepsilon^{-4})$；合为 $\Theta(\varepsilon^{-4})$ | VAC 仍会被伪临界骗；同样信息下能否达到更强目标？ |
| Q3 | 目标阶梯 L0（VAC）/ L1（同点配对 Goldstein）/ L2（$F$ 的 Goldstein）；普通分量 oracle 下 L1、L2 的确定性可达性未知 | 讨论与开放问题 |

## 3. 逐条核对清单

### B. 背景断言

- **B1** Li–Pan (arXiv 2608.03246)：弱凸类确定性 $\Omega(\varepsilon^{-4})$ 下界，Moreau 驻点目标，完整次微分 oracle。核对函数类与 oracle。
- **B2** Tian–So (ICML 2021 BFOM workshop)：对任意有限预算 $T$ 存在 $\rho(T)$，$\rho(T)$-弱凸函数的 NAS 难以计算；标题中的 “certain DC programs” 具体是哪一类？是否覆盖同点近似 DC 临界？这直接影响 Q0 的新意。
- **B3** Jordan 等 (COLT 2023)、Tian–So (MP 2024)、Kornowski (arXiv 2609.23837 Thm 3.1)：确定性 Goldstein 无法维数无关，代价 $(1/\varepsilon)^{\Omega(d)}$。核对算法类与 oracle（局部 oracle）。
- **B4** Kornowski (arXiv 2609.17780)：$\Omega(\delta^{-1}\varepsilon^{-3})$，算法类是 zero-respecting（含随机），梯度确定性。核对是否覆盖一般确定性算法。
- **B5** Kong–Lewis (MOR 2024, Thm 6.6, Prop 6.3)：方向次梯度 oracle 下确定性达到 Goldstein，界的 $\varepsilon,\delta$ 指数（我们推断为 $O(\Delta L^2\Lambda(\delta)\delta^{-1}\varepsilon^{-4})$，DC 情形 $\Lambda\le\operatorname{Lip}(g)$；PDF 抽取丢失了 $\varepsilon$，请按原文核对）。
- **B6** “DC 文献把同点近似 DC 临界作为停机准则，已有复杂度依赖负侧光滑或按精确子问题计数”：请举出代表性文献（Moudafi、Sun 等、Yao 等、Xu 等、DCA-PAGE、Faust 等）核对此概括是否准确。

### Q0. 不可达性

- **Q0.1** 定理：对固定常数 $G_\phi,G_g,\Delta$ 与任意有限预算，存在 $\mathcal D$ 中实例使所有迭代点都不满足同点近似 DC 临界。证明为凸归约：Kornowski–Shamir (arXiv 2209.10346，GPT 前一轮称 Theorem 5) 的一维凸困难族 $q$，令

$$
\phi_q=q(x)+\lvert y\rvert+\lvert y-1\rvert,\quad g_q=\lvert y-1\rvert,\quad F_q=q(x)+\lvert y\rvert ,
$$

  声称 $\operatorname{dist}(\partial\phi_q,\partial g_q)\ge\operatorname{dist}(0,\partial q(x))$，分量常数为 $\sqrt5$、$1$。请核对：不等式是否成立；Kornowski–Shamir 定理的量词（确定性/随机、是否“任意有限时间”）；归约是否保持这些量词。
- **Q0.2** 取 $g=0$，VAC$(0,\delta_g,\varepsilon)$ 化为凸函数同点小次梯度，故不可达。核对 $\partial_{\delta}0=\{0\}$ 的使用是否无误。
- **Q0.3** 新意：DC 文献中是否已有人指出同点近似 DC 临界在两侧非光滑时不可达？与 B2 的关系如何？

### V. VAC 的来源

- **V1** 单步恒等式（$v^k\in\partial g(x^k)$，$x^{k+1}$ 为 DCA 子问题解）：

$$
F(x^k)-F(x^{k+1})=\Psi_\phi(x^k,v^k)+\Psi_g(x^{k+1},v^k)-\Psi_\phi(x^{k+1},v^k),
$$

  不需要强凸。核对。
- **V2** 精确 DCA 有 $\Psi_\phi(x^{k+1},v^k)=0$，因此判断临界的信息在 $\Psi_g(x^{k+1},v^k)$。请查 DCA-PAGE (Nguyen 等, arXiv 2509.11657) Definition 12 的确切定义：沿精确 DCA，它是否恒为零或平凡满足？若是，这是一个尖锐的观察；若否，说明它与 $\Psi_g$ 的关系。
- **V3** 新意：三参数联合证书相对于 $\varepsilon$-次微分型不精确 DCA（Sun 等；tPLDCA, Optimization 2024；de Oliveira–Tcheou InDCA, SVVA 2019；InmBDCA, JOTA 2025）与 Faust–Fawzi–Saunderson (AISTATS 2023) 的 Bregman 分解，是否构成实质增量？是否已有文献定义过同样的联合证书？

### Q1. VAC 保证了什么

- **Q1.1** DCA 不动点 ⟺ $\partial\phi(x)\cap\partial g(x)\ne\emptyset$；无下降方向 ⟺ $\partial g(x)\subseteq\partial\phi(x)$；$g$ 在 $x$ 可微时 $\partial_C F(x)=\partial\phi(x)-\nabla g(x)$，两者一致。核对。
- **Q1.2** 校准：$g$ 凸且 $\rho$-光滑时

$$
\lVert\nabla F_{1/(2\rho)}(x)\rVert\le b+\sqrt{b^2+4\rho\delta_\phi},\qquad b=\varepsilon+\sqrt{2\rho\delta_g}.
$$

  请给出完整证明或修正常数。问：该结论在弱凸文献中是否已知？反方向（Moreau 驻点 ⟹ 某个 VAC）是否成立、损失多少？
- **Q1.3** 一维：取 $F'$ 的 Jordan 分解（正变差给 $\phi'$，负变差给 $g'$），则每一点 DC 临界 ⟺ Clarke 驻点，且分量界不超过原分量界的常数倍。请核对，包括 $F'$ 同时有跳跃和连续变差的点、以及分量全局 Lipschitz 有界的保持。
- **Q1.4** 二维：$F_0(x)=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}$。论证：$F_0$ 在单位圆上于方向 $(1,0)$、$(0,1)$、$(-1,-1)/\sqrt2$ 有大小为 $1,1,\sqrt2$ 的凹折痕；任何分解中 $\phi'(0;\cdot)=F_0+\sigma_{\partial g(0)}$ 必须是支撑函数，因此 $\partial g(0)$ 在这三个法向上暴露的面长度至少为 $1,1,\sqrt2$，从而宽度 $w_{\partial g(0)}(d)\ge\max\{\lvert a\rvert,\lvert b\rvert,\lvert a-b\rvert\}\ge-F_0(d)$，推出 $0\in\partial\phi(0)-\partial g(0)$；而 $\partial_C F_0(0)=\operatorname{conv}\{e_1,e_2,(1,1)\}$，距原点 $1/\sqrt2$。请逐步核对，特别是“$h+h''$ 的原子等于暴露面长度”这一步，以及加上 $3\max\{\lVert x\rVert-1,0\}$ 后的全局版本。
- **Q1.5** 新意：拟微分理论（Demyanov–Rubinov）、极小对理论（Pallaschke–Urbański 的专著；Scholtes 1992 “Minimal pairs of convex bodies in two dimensions”；Demyanov–Jeyakumar 1997 “Hunting for a smaller convex subdifferential”）中是否已有等价结论？若有，请给出定理位置，并说明我们的陈述（“对所有 DC 分解都临界，却非 Clarke 驻点”以及一维与二维的分界）是否仍属新的表述或新的推论。
- **Q1.6** 推广：高维中“对所有分解都 DC 临界”的点能否刻画？是否等价于 $F'(x;\cdot)$ 的所有极小拟微分对 $(A_0,B_0)$ 满足 $0\in A_0-B_0$？是否存在可检验的充分条件（例如由凹折痕的几何决定）？

### Q2. 确定性最优复杂度

- **Q2.1** 上界引理：固定 $x$、$v\in\partial g(x)$、$\eta>0$，$M(y)=\phi(y)-\langle v,y\rangle+\frac1{2\eta}\lVert y-x\rVert^2$，$z=\arg\min M$，$M(y)-M(z)\le\sigma$，$u=v-(z-x)/\eta$。声称 $M(y)-M(z)=\Psi_\phi(y,u)+\frac1{2\eta}\lVert y-z\rVert^2$，以及

$$
\Psi_g(y,v)+\tfrac{\eta}{2}\lVert u-v\rVert^2\le F(x)-F(y)+\sigma .
$$

  请给出完整证明。
- **Q2.2** 定理：选观察到的下降最小的一步输出；内层强凸次梯度法成本 $O(1+\eta B^2/\sigma)$（用 $\lVert z-x\rVert\le\eta B$）；取 $\eta=\delta/\varepsilon^2$、$\sigma=\delta/4$、$K=\lceil4\Delta/\delta\rceil$，得 $(\delta,\delta,\varepsilon)$-VAC，总成本 $O(\Delta B^2\delta^{-1}\varepsilon^{-2})$。核对每一步和适用的参数范围。
- **Q2.3** 容差不对称：在旧点 $x^k$ 输出，$v^k\in\partial g(x^k)$ 精确，$u$ 由近端点搬回，$\Psi_\phi(x^k,u)\le2G_\phi\eta\lVert u-v\rVert$，可得 $\delta_g=0$，代价 $O(\Delta B^2\delta_\phi^{-1}\varepsilon^{-3})$；而 $\delta_\phi=0$ 由 Q0.2 不可达。核对；并判断 $\varepsilon^{-3}$ 是否可改进。
- **Q2.4** 下界：Li–Pan 未缩放实例 $\bar F$ 加有界凸化项

$$
c_N(t)=\begin{cases}0,&t\le0,\\ \tfrac38t^2-\tfrac{N}{16}t^3,&0<t<2/N,\\ \tfrac{3}{4N}t-\tfrac{1}{2N^2},&t\ge2/N,\end{cases}
$$

  $\bar g=\sum c_N(z^m_j)$，$\bar\phi=\bar F+\bar g$。声称 $0\le c_N'\le\frac{3}{4N}$、$0\le c_N''\le\frac34$ 覆盖 $\bar F$ 所需负曲率；$\operatorname{Lip}(\bar g)\le\frac34\sqrt{M/N}$；$c_N'(0)=0$ 保证两个分量的完整次微分不跳过隐藏层；结合 Q1.2 的 Moreau 归约，得到 $(\varepsilon^2,\varepsilon^2,\varepsilon)$-VAC 的确定性 $\Omega(\varepsilon^{-4})$。请核对：$\bar F$ 的负曲率界是否确实不超过 $3/4$；凸性在 $t<0$ 区域与跨块处是否成立；成对抵抗 oracle 的不变量；Moreau 归约所需的光滑常数 $\rho$ 与 $c_N''$ 的关系。
- **Q2.5** 定位：在“确定性、紧界、非弱凸函数类”这一组合上，是否已有先例？Kong–Lewis 之后是否有人给出 DC 或更一般结构类的确定性匹配下界？据此判断“弱凸之外首个紧的确定性复杂度结果”能否成立，若不能，给出准确的定位句。

### Q3. 定位核对（不要求证明）

- **Q3.1** K7：Kornowski 的局部 oracle 能模拟 Kong–Lewis 的方向次梯度 oracle；若 Kornowski 的指数实例非凸模有界，就与 Kong–Lewis 的维数无关上界矛盾，所以这些实例不在常数适中的有界 DC 类中。请检查 Kong–Lewis 的全部假设在 Kornowski 构造上是否成立。
- **Q3.2** 阶梯 L0 ⟸ L1 ⟸ L2 的蕴含与容差是否正确；L1 是否确实仍被 $F_0$ 型伪临界满足。

## 4. 需要检验的“新见解”

请对每一条回答：(i) 数学上是否成立；(ii) 前人是否已得到（给出处）；(iii) 读者是否真会感到意外，针对哪类读者；(iv) 如何加强为更大的结果；(v) 能支撑它的材料。

- **W1：伪临界在一维是分解造成的假象，在二维是本质。** Tian–So（SPM 2026）指出坏分解能让任意点 DC 临界（存在性方向）。自然预期是选好分解就能消除。一维中 Jordan 分解一次消除全部非 Clarke 伪临界（Q1.3）；二维 $F_0$ 在原点对所有分解都临界却非 Clarke 驻点（Q1.4）。我们认为它给出“维数门槛”式的反直觉，且证明只需把量词从“存在分解”换成“对所有分解”。请特别判断：(a) 是否为极小对理论的已知推论；(b) 能否做成定量版本（例如分量有界时 Clarke 残差的下界）或高维刻画；(c) 能否推出算法层面的结论（任何分解、精确子问题的 DCA 都可能停在斜率为 1 的下降点）。
- **W2：判断临界的信息藏在负侧运输误差里。** 精确 DCA 的正侧间隙恒为零（V2），临界性只能由 $\Psi_g(x^{k+1},v^k)$ 判断。请判断这是否会改变 DC 研究者对停机准则的理解，以及与 DCA-PAGE 定义的关系。
- **W3：DCA 的确定性可能来自跨点配对。** DCA 用旧点的 $v$ 与新点的 $u$ 配对，失配由下降支付；若同点配对（L1）在普通分量 oracle 下需要指数次确定性查询，则 DCA 最朴素的结构特征恰好是绕开确定性障碍的出口。请评价这一表述作为研究假设是否合理，有无先例或反例迹象。
- **W4：确定性代价由负侧凹结构决定。** 结合 Kong–Lewis 与 Kornowski，指数价格只出现在凹质量无界的函数上。请判断这是否已是 Kong–Lewis 的既有观点（其标题即 “cost of nonconvexity”），我们的增量是什么。

另请检查以下我们认为“不令人意外”的结果，看是否有可以升级为新见解的角度：Q0 不可达性；Q1.2 校准；Q2 上界与下界；Q2.3 容差不对称。

## 5. 输出格式

1. **逐条核对表**：编号 | 判定 | 修正后的精确表述 | 依据（证明要点或文献定理号） | 新意判断。
2. **新见解评估**：W1–W4 各一段，按 (i)–(v) 作答，并给出一个从强到弱的排序。
3. **修正后的全文一句话与引言钩子**：基于核对结果重写，正面陈述，不加防御性措辞；钩子应以最强的新见解开头。
4. **需要补的证明与文献**：按优先级列出，并说明每项完成后能支撑哪一条主张。
5. **最大风险**：哪一条一旦被推翻，会让全文主线失效，以及替代方案。
