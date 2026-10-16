# 非光滑 DCA：全文逻辑与新见解核查

日期：2026-10-16。

核查对象：用户上传的 gptpro-logic-and-insight-audit-prompt.md；GitHub 仓库当前 paper-structure-2026-10-16.md、irremovable-pseudo-criticality-2026-10-16.md、main.tex、appendix/lowerbound.tex；文末列出的原始文献。未获得当前编译 PDF，未作 PDF 排版审阅。本文没有向 GitHub 写入。

## 结论

数学主线可以保留。最值得加强的主结果是：在固定分量 Lipschitz 界下，仅松弛正侧支撑值误差，就能显式输出同点证书；达到 (ε²,0,ε)-VAC 的确定性基本查询复杂度为 Θε⁻⁴。本文给出上界的可计算见证和有界分量下界的成对抵抗 oracle 证明。

F₀ 的“任何分解都临界，却非 Clarke 驻点”成立。一维还可加强为整个次微分集合的精确还原，且不增加原分量界。不过，二维结论的几何机制可由已有平面极小对理论直接推出。DCA-PAGE 单侧 gap 的缺陷已被 MDCA v2 Remark 1 指出；非凸模决定确定性算法代价的观点也有明确先例。三者都应准确归属。

以下“本次推导”指本文给出的数学推导，不代表已经完成文献优先权认定，也不代表已进入当前论文。

## 1. 逐条核对

设 φ、g 为全空间有限凸函数，Lip(φ)≤Gφ、Lip(g)≤Gg，F=φ−g，F(x⁰)−inf F≤Δ，B=Gφ+Gg。球使用闭球。计数单位为一次成对分量函数值与次梯度查询。下界允许返回两个完整次微分。算法可做任意确定性内部运算，不能免费调用精确凸优化或近端算子。

| 编号 | 判定 | 精确表述或修正 | 依据 | 新意判断 |
|---|---|---|---|---|
| B1 | 成立，需列参数范围 | Li–Pan 的一般确定性下界是 Ω(G² min{ρΔ,G²} ε⁻⁴)，在 ε²≤c₀ min{G²,ρΔ} 下成立；目标是 Moreau 梯度，oracle 返回函数值与完整次微分。固定正参数时给出 ε 的四次下界。 | [1] Theorem 3；Theorem 2 先处理 zero-respecting 算法。 | 已有结果；不能直接当成成对分量下界。 |
| B2 | 无法判定完整原命题 | 官方页面确认 Tian–So 2021 论文存在；本次未取得可逐定理核对的原文，因此“certain DC programs”的精确函数类、oracle 和定理编号仍缺证。后续论文转述的无统一弱凸参数 NAS 障碍，不能替代成对 DC 临界下界。 | [11] 官方收录；[1] Remark 2 的转述。 | 不得写“此前无人研究”，也不得写“该文已覆盖 Q0”。 |
| B3 | 需修正 | Jordan 等与 Tian–So 给出 Ω(d) 类型、无维数无关保证的结果；Kornowski 2026 Theorem 3.1 才给出一般确定性局部 oracle 的指数维数下界。三个结果的强度不可合并归属。 | [3] Theorem 1；[4] Theorem 1；[5] Theorem 3.1。 | 背景事实。 |
| B4 | 需修正 | Ω(r⁻¹ε⁻³) 下界覆盖文中 zero-respecting 算法，包括随机算法；不能直接扩展到所有确定性算法。还应保留 Δ、L 及适用精度范围。 | [6] Theorem 3.1。 | 背景事实。 |
| B5 | 需修正 | Kong–Lewis 的完整上界含基线项：ceil(3Δ/(rε))·16L²/ε²·(1+floor(12Λ(r)/ε))。固定正 Λ 时主项为 r⁻¹ε⁻⁴；Λ=0 时不能把成本写成零。 | [2] Oracle 2.5、Proposition 6.3、Theorem 6.6。 | 有界 DC 与方向 oracle 的确定性正面结果已存在。 |
| B6 | 需修正 | “既有复杂度均依赖负侧光滑或仅按精确子问题计数”过强。Xu 等已在双侧非光滑情形计入内层次梯度成本，得到固定点映射目标的 ε⁻⁴ 阶；其成功准则和假设与本稿不同。 | [7] Assumption 2(ii)、Theorem 3；另见 [8]、[9]、[12]–[15]。 | 不能以双侧非光滑、计入内层或 ε⁻⁴ 上界本身宣称首创。 |
| Q0.1 | 成立 | 对固定分量常数、足够小的固定 ε 和任意有限预算，不存在统一成功保证。随机版本是最坏实例上的常数概率障碍；确定性版本是存在失败实例。输出点不必为查询点，计作额外一次查询即可。 | §2；[10] Theorem 5。 | 已有凸困难族的直接 DC 嵌入。 |
| Q0.2 | 成立，端点措辞需修正 | ∂δ0={0} 对每个有限 δ≥0 成立，因此 δφ=0 的目标继承同点小次梯度障碍。每个正 δφ 都可有限查询实现；“δφ→0 也不可达”不准确。 | §2、§6。 | 精确端点的不对称可以强调。 |
| Q0.3 | 无法认定优先权 | 严格 oracle 下界来自 [10]。Xu 等已经用绝对值例子指出同点近似 DC 临界的困难，并引入附近点目标。 | [7] §2；[10] Theorem 5。 | “这个问题此前没有人问过”应删除。 |
| V1 | 成立 | 下降恒等式不需要强凸；负侧见证取自旧点即可。F 下有界保证所涉共轭值有限。 | §3。 | Fenchel/Bregman 结构已有先例。 |
| V2 | 成立，已有先例 | DCA-PAGE Definition 12 是新点的正侧子问题 gap；精确 DCA 下每步为零。它不能单独判定当前原问题临界。 | [8] Definition 12；[9] Remark 1。 | 此批评与具体反例已公开。 |
| V3 | 需修正贡献表述 | ε-次微分、近似向量和跨点误差并非新工具。可辨增量在同点联合证书、可核查见证、明确基本查询模型及对应下界。 | [12]–[15]；本报告 §6–§7。 | 本次未找到完全相同的“证书＋固定分量紧界”；这不等于证明不存在先例。 |
| Q1.1 | 成立，补量词 | DC 临界等价于存在一次合法 DCA 选择使 x 为不动点；无下降方向等价于 ∂g(x)⊆∂φ(x)。g 在 x 可微时，精确 DC 临界、方向驻点和 Clarke 驻点一致。 | §3。 | 经典性质；“存在选择”不能写成“每种选择”。 |
| Q1.2 | 成立 | 给定 Moreau 转换常数正确。反向：在近端点得到精确两侧证书；在原点一般只能保证正侧值容差 O(ε)，不能保证 O(ε²)。 | §4。 | 校准有用；属于标准凸分析机制。 |
| Q1.3 | 成立，可加强 | 一维存在单个分解，使每一点 ∂Φ(x)−∂Γ(x)=∂CF(x)，并分别保持原 Gφ、Gg 界。 | §5.1。 | Jordan 分解经典；这里的全局集合等式值得陈述。 |
| Q1.4 | 成立，可加强 | F₀ 在原点对任何有限凸分解都 DC 临界。加径向凸项后属 D(4,1,1)，且任意 0<r<1 的 Goldstein 残差为 1/√2。 | §5.2–§5.3。 | 数学正确；几何机制已有极小对理论支撑。 |
| Q1.5 | 需修正 | 二维任意分解结论可由经典极小对存在性、平面唯一性和多边形最小性判据直接推出。未找到原文以本稿同样的 DC 临界/维数门槛语言陈述。 | [16] Theorems 7.1、7.2、7.4；[17]。 | 应称经典几何结果的优化推论，不能称新几何原理。 |
| Q1.6 | 需修正 | 对方向齐次模型的全部支撑函数表示，“所有表示相交”等价于“所有极小表示相交”。对一般 F，要获得全部实际 DC 分解的必要条件，还缺方向表示可实现性。 | §5.4。 | 高维几何刻画可继续研究；不能越过可实现性环节。 |
| Q2.1 | 成立，可加强 | 原子问题间隙恒等式与联合下降界正确；还存在同时控制旧点正侧 gap 的更强恒等式。 | §6.1。 | 更强恒等式消除了 Q2.3 的额外成本。 |
| Q2.2 | 成立，补参数与实现 | 完整上界为 O((1+Δ/δ)(1+B²/ε²))。在 δ≤Δ、ε≤B 下化为原式。§6.2 给出显式见证输出，全部成本为基本查询。 | §6。 | 与已有映射残差上界区别在成功准则及证书可计算性。 |
| Q2.3 | 需修正，可加强 | 旧点输出 (δ,0,ε)-VAC 仍只需 O(ΔB²/(δε²))；原先 ε⁻³ 的推导上界不紧。 | §6.1–§6.3。 | 本次实质加强：正侧松弛足够，负侧可精确。 |
| Q2.4 | 成立，需采用成对证明 | cN 的曲率覆盖正确。二阶导界按几乎处处理解；cN 为 C¹,¹。成对完整次微分的隐藏层不变量成立，并可扩展到任意确定性算法及任意输出点。 | §7；基础困难族来自 [1]。 | 有界凸化与成对扩展是所需的新连接。当前仓库旧附录尚未包含它。 |
| Q2.5 | 需修正 | 不使用宽泛的“弱凸之外首个紧确定性复杂度”。Tian–So 已给出非凸模依赖的紧界。准确主张是指定分量类、普通成对 oracle、VAC 成功准则和固定参数 ε⁻⁴ 紧界。 | [4] Proposition 4；§7。 | 所匹配的参数和目标必须写明。 |
| Q3.1 | 需修正 | 两文结合排除的是覆盖整个困难族的统一适中 Λ(r) 界；不能推出每个困难实例都非 DC 或 Λ(r)=∞。局部 germ oracle 能支持方向信息，不等于仅有完整 Clarke 集即可恢复方向导数。 | §8；[2]、[4]、[5]。 | W4 的一般观点已有先例。 |
| Q3.2 | 成立 | L2⇒L1⇒VAC(2Gφr,2Ggr,ε)。F₀ 在原点精确满足 L1，却在固定半径内不满足 L2 的小残差要求。 | §8。 | 阶梯正确；普通分量下 L1/L2 的复杂度未在本次任务中解决。 |

## 2. Q0 的量词和归约

令 q 为 [10] Theorem 5 的一维凸 1-Lipschitz 困难实例。定义

\[
\phi_q(s,t)=q(s)+|t|+|t-1|,\qquad g_q(s,t)=|t-1|.
\]

则 Fq(s,t)=q(s)+|t|。任意分量次梯度之差，其第一坐标属于 ∂q(s)。因此

\[
\operatorname{dist}(\partial\phi_q(s,t),\partial g_q(s,t))
\geq\operatorname{dist}(0,\partial q(s)).
\]

分量 Lipschitz 常数不超过 √5 和 1；起点取 (s⁰,0)，初始差距不增加。一次 q 的函数值与次梯度查询足以模拟一次成对查询。

[10] Theorem 5 对任意随机一阶算法给出一维凸困难族：以大于等于 1/3 的概率找到其空间松弛驻点，需 Ω(√log(1/r)) 次查询；特别地，同点 1/4-小次梯度无统一有限预算保证。对任意给定预算选择足够小 r，再做上述嵌入，得到 Q0。困难实例在算法固定之后、算法随机数实现之前确定。对确定性算法，失败概率只可能是零或一，故得到确定失败实例。

若算法输出此前未查询的点，将它作为额外一次查询，再使用预算 T+1 的下界。

当 g=0 时，若 v∈∂δg(0)(x)，则对所有 y 有 0≥〈v,y−x〉−δg。令 y 沿 v 无界增长，得到 v=0。所以 VAC(0,δg,ε) 要求 φ 在输出点具有范数不超过 ε 的精确次梯度。

这里的障碍只针对 δφ=0。对每个 δφ>0，§6 都给出有限查询上界。该归约的 Fq 仍是凸函数，因此不能把 Q0 解释成失去弱凸性之后才出现的现象。

## 3. DCA 恒等式与精确临界

定义 Fenchel 间隙

\[
\Psi_h(x,v)=h(x)+h^*(v)-\langle v,x\rangle.
\]

若 v∈∂g(x)，则 g*(v)=〈v,x〉−g(x)。直接代入得到

\[
F(x)-F(y)=\Psi_\phi(x,v)+\Psi_g(y,v)-\Psi_\phi(y,v).
\]

由于 F 下有界，φ(w)−〈v,w〉具有全局下界，所以 φ*(v)<∞。若 y 精确最小化 φ(w)−〈v,w〉，则 Ψφ(y,v)=0。

固定一个分解，存在 v∈∂g(x) 使 x 最小化 φ−〈v,·〉，当且仅当 ∂φ(x)∩∂g(x)≠∅。这是存在性不动点；一个指定的选择规则可能在同一临界点选择其他 v。

方向导数满足

\[
F'(x;d)=\sigma_{\partial\phi(x)}(d)-\sigma_{\partial g(x)}(d).
\]

因此所有方向导数非负，当且仅当 ∂g(x)⊆∂φ(x)。g 在 x 可微时，其梯度在该点严格可微意义下可作 Clarke 微分的光滑减项，故

\[
\partial_C F(x)=\partial\phi(x)-\nabla g(x).
\]

“非 Clarke 的伪 DC 临界只能发生于 g 不可微处”适用于零误差临界点，不能不加容差地推广到一般 VAC。

## 4. Moreau 校准及反向限制

### 4.1 正向证明

假设 g 凸且全局 ρ-光滑，ρ>0。则 F 为 ρ-弱凸。设 x 的 VAC 见证为 u、v，令

\[
b=\varepsilon+\sqrt{2\rho\delta_g},\qquad
p=\operatorname{prox}_{\lambda F}(x),\quad
\lambda=\frac{1}{2\rho},\quad s=x-p.
\]

由 g* 的强凸性，或等价的光滑凸函数 Fenchel 间隙不等式，

\[
\|v-\nabla g(x)\|\leq\sqrt{2\rho\delta_g},\qquad
\|u-\nabla g(x)\|\leq b.
\]

近端最优性给出

\[
u_p:=2\rho s+\nabla g(p)\in\partial\phi(p).
\]

把 u∈∂δφφ(x) 与 up∈∂φ(p) 的支撑不等式相加，得到

\[
\langle u_p-u,s\rangle\leq\delta_\phi.
\]

代入 up，并使用 g 的梯度 Lipschitz 界，

\[
2\rho\|s\|^2
\leq\langle u-\nabla g(x),s\rangle
+\langle\nabla g(x)-\nabla g(p),s\rangle+\delta_\phi
\leq b\|s\|+\rho\|s\|^2+\delta_\phi.
\]

解此二次不等式，再乘 2ρ，得到

\[
\boxed{\|\nabla F_{1/(2\rho)}(x)\|
\leq b+\sqrt{b^2+4\rho\delta_\phi}.}
\]

因此 δφ、δg 为 O(ε²/ρ) 时，Moreau 梯度为 O(ε)。这是下界归约所需的方向。

### 4.2 反向证明与反例

假设 w=∇F1/(2ρ)(x)，且 ‖w‖≤τ。上面的 p 满足 ‖p−x‖≤τ/(2ρ)。在 p 处，

\[
u_p=w+\nabla g(p)\in\partial\phi(p),\qquad
v_p=\nabla g(p)\in\partial g(p),\qquad
\|u_p-v_p\|\leq\tau.
\]

所以附近点 p 精确满足 (0,0,τ)-VAC。

在原点 x，保持 up，并取 vx=∇g(x)。利用 φ 的 Lipschitz 界，

\[
\Psi_\phi(x,u_p)
=\phi(x)-\phi(p)-\langle u_p,x-p\rangle
\leq2G_\phi\|x-p\|\leq\frac{G_\phi\tau}{\rho}.
\]

同时 ‖up−vx‖≤τ+ρ‖x−p‖≤3τ/2。因此 x 满足

\[
\left(\frac{G_\phi\tau}{\rho},0,\frac{3\tau}{2}\right)\text{-VAC}.
\]

这个线性正侧容差不能统一提升为二次。取 φ(t)=|t|、g=0、x=τ/(2ρ)，其中 0<τ<1。近端点为零，Moreau 梯度等于 τ。若同点残差要求 ‖u‖≤Cτ，则

\[
\Psi_\phi(x,u)=x(1-u)\geq\frac{\tau}{2\rho}(1-C\tau).
\]

当 C 固定、τ→0 时，右侧是 τ/ρ 的量级。

## 5. 一维和二维的分解差距

### 5.1 一维保持原分量界的规范分解

设原分解 F=φ₀−g₀ 满足全局分量界。其分布二阶导数是有限有符号测度

\[
\mu=D^2F=\mu_{\phi_0}-\mu_{g_0}=\mu^+-\mu^-.
\]

Jordan 正负部分满足 μ⁺≤μφ₀、μ⁻≤μg₀，且互相奇异。令

\[
a=\phi'_{0,+}(-\infty),\qquad b=g'_{0,+}(-\infty),
\]

\[
p(t)=a+\mu^+(( -\infty,t]),\qquad
q(t)=b+\mu^-(( -\infty,t]).
\]

将单调函数 p、q 积分，得到有限凸函数 Φ、Γ，调整一个常数使 F=Φ−Γ。由于 p 始终位于原 φ₀ 左右无穷斜率之间，q 同理，

\[
\operatorname{Lip}(\Phi)\leq G_\phi,\qquad
\operatorname{Lip}(\Gamma)\leq G_g.
\]

在每一点，μ⁺ 和 μ⁻ 不会同时具有正原子。因此 p、q 至多一个跳跃。于是

\[
\partial\Phi(x)-\partial\Gamma(x)
=[\min\{F'_-(x),F'_+(x)\},\max\{F'_-(x),F'_+(x)\}]
=\partial_CF(x).
\]

连续变差和奇异连续变差没有原子，不影响这一逐点论证。这个结论同时处理所有点，且比临界点等价更强。

### 5.2 二维 F₀ 的直接证明

令

\[
F_0(x)=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}.
\]

对任意有限凸分解，记 A=∂φ(0)、B=∂g(0)。正齐次性给出 σA−σB=F₀。分离定理说明

\[
A\cap B\neq\varnothing
\iff F_0(d)+w_B(d)\geq0\quad\text{对所有 }d,
\quad w_B(d)=\sigma_B(d)+\sigma_B(-d).
\]

令单位法向 n(θ)=(cosθ,sinθ)，切向 t(θ)=(-sinθ,cosθ)，hB(θ)=σB(n(θ))。在 θ₀ 处，支撑函数的一侧角导数分别等于暴露面上 〈b,t(θ₀)〉 的最小值和最大值。因此角导数跳跃等于该暴露线段的长度。分布 hB+hB″ 的原子也就是此跳跃；hB 本身连续，故 hB 项没有原子。

F₀ 在法向 e₁、e₂、−(e₁+e₂)/√2 上的负跳跃分别为 −1、−1、−√2。为了让 σA=F₀+σB 保持支撑函数的非负曲率，B 的对应暴露面必须分别包含长度至少 1 的竖直段、长度至少 1 的水平段，以及长度至少 √2 的 (1,−1) 方向线段。因此对 d=(a,b)，

\[
w_B(d)\geq\max\{|a|,|b|,|a-b|\}\geq-F_0(d).
\]

最后一个不等式逐象限直接成立：第一象限 F₀≥0；第三象限 −F₀=max{|a|,|b|}；另外两象限 F₀=a+b。于是 A∩B≠∅。

F₀ 可微区域的梯度只有 e₁、e₂、e₁+e₂。因此

\[
\partial_CF_0(0)=\operatorname{conv}\{e_1,e_2,e_1+e_2\},\qquad
\operatorname{dist}(0,\partial_CF_0(0))=\frac{1}{\sqrt{2}}.
\]

### 5.3 经典极小对解释及定量版本

令 T=conv{0,e₁,e₂}。则 F₀=σT−σ−T。T 与 −T 没有外法向相同的平行边对，故由 [16] Theorem 7.4，(T,−T) 是极小对。对任意等价对 (A,B)，Theorem 7.1 给出包含于其中的极小对，Theorem 7.2 说明该对为 (T+c,−T+c)。因 0∈T∩(−T)，有 c∈A∩B。

因此，本稿的任意分解结论是这套已有几何定理的直接推论。该判断有定理级依据；本次尚未找到前文以同样的“不可消除伪 DC 临界”语言陈述的结果。

考虑全局版本

\[
F(x)=F_0(x)+3\max\{\|x\|-1,0\}.
\]

自然分解的 Lipschitz 界为 4 和 1。因为 F₀(x)≥−‖x‖，可知 inf F=−1，且 F(0)=0。故它属于 D(4,1,1)。任意 0<r<1 时，

\[
\operatorname{conv}\bigcup_{\|y\|\leq r}\partial_CF(y)
=\operatorname{conv}\{e_1,e_2,e_1+e_2\}.
\]

所以原点在所有分解下精确满足 VAC 和 L1，但其 r-Goldstein 残差始终为 1/√2。

沿 −e₁ 的方向导数为 −1。对每个分解，选取共同次梯度 v∈A∩B，就存在保持原点不动的精确 DCA 轨迹。若该步加入正二次近端项，该选择下原点还是唯一子问题解。量词是“每个分解都有失败选择”，不包含“每一种次梯度选择都会失败”。

高维嵌入 F₀(x₁,x₂) 保持这一结论。给定任意测试方向 d，若其前两坐标非零，选一个包含 d 且投影到前两坐标可逆的二维子空间，在该子空间应用二维结论，即得 σA(d)+σB(−d)≥0。若前两坐标为零，此不等式由 F′(0;d)=0 直接成立。对所有 d 应用分离定理即可。

### 5.4 高维极小对刻画的边界

固定正齐次 DC 函数 p，令所有紧凸支撑表示组成集合

\[
\mathcal R(p)=\{(A,B):p=\sigma_A-\sigma_B\}.
\]

由极小对存在性，

\[
\bigl[\forall(A,B)\in\mathcal R(p),\ A\cap B\neq\varnothing\bigr]
\iff
\bigl[\forall\text{极小对 }(A_0,B_0)\in\mathcal R(p),\ A_0\cap B_0\neq\varnothing\bigr].
\]

对于一般非齐次 F，实际分解在 x 产生的次微分对只是 R(F′(x;·)) 的子集。上述右侧条件仍充分；若要声称它也必要，需要证明所用极小方向表示能够由 F 的实际分解实现。本文不把这项可实现性当成默认事实。

## 6. 加强后的上界：负侧精确与显式见证

### 6.1 精确近端点只作分析的恒等式

固定 x、v∈∂g(x)、η>0。设

\[
M(w)=\phi(w)-\langle v,w\rangle+\frac{\|w-x\|^2}{2\eta},\qquad
z=\operatorname*{argmin}_w M(w),\qquad
u_*=v-\frac{z-x}{\eta}\in\partial\phi(z).
\]

令 e=M(y)−M(z)≥0。展开二次项和 Fenchel 等式，得到

\[
e=\Psi_\phi(y,u_*)+\frac{\|y-z\|^2}{2\eta}.
\tag{6.1}
\]

同时

\[
M(x)-M(z)=\Psi_\phi(x,u_*)+\frac{\eta}{2}\|u_*-v\|^2,
\]

\[
M(x)-M(y)=F(x)-F(y)-\Psi_g(y,v)-\frac{\|y-x\|^2}{2\eta}.
\]

相加得到更强的恒等式

\[
\boxed{
\Psi_\phi(x,u_*)+\Psi_g(y,v)
+\frac{\eta}{2}\|u_*-v\|^2+\frac{\|y-x\|^2}{2\eta}
=F(x)-F(y)+e.}
\tag{6.2}
\]

原任务的 Q2.1 不等式由丢弃非负项获得。更重要的是，旧点 x 的正侧 gap 也直接由右侧控制，无须通过 2Gφ‖x−z‖ 作线性运输估计。Q2.3 的额外 ε⁻¹ 正是该较松估计产生的。

### 6.2 全部见证可计算的内层算法

以下算法不需要精确 z，也不需要计算 φ*。

令 w₁=x，迭代 j=1,…,J：查询 aⱼ∈∂φ(wⱼ)，计算

\[
c_j=a_j-v+\frac{w_j-x}{\eta},\qquad
w_{j+1}=w_j-\frac{2\eta}{j+1}c_j.
\tag{6.3}
\]

由

\[
w_{j+1}-x=\frac{j-1}{j+1}(w_j-x)-\frac{2\eta}{j+1}(a_j-v)
\]

归纳得 ‖wⱼ−x‖≤ηB，故 ‖cⱼ‖≤2B。无需投影。

取权重 λⱼ=2j/[J(J+1)]，计算

\[
y=\sum_{j=1}^J\lambda_jw_j,\qquad
u=\sum_{j=1}^J\lambda_ja_j,\qquad
S=\sum_{j=1}^J\lambda_j\bigl(\langle a_j,w_j\rangle-\phi(w_j)\bigr).
\tag{6.4}
\]

因为 φ*(aⱼ)=〈aⱼ,wⱼ〉−φ(wⱼ)，共轭凸性给出 φ*(u)≤S。因而

\[
\ell(w)=-S+\langle u-v,w\rangle+\frac{\|w-x\|^2}{2\eta}\leq M(w).
\]

该显式二次函数的最小值和最小点分别为

\[
D=-S+\langle u-v,x\rangle-\frac{\eta}{2}\|u-v\|^2,
\qquad z_{\mathrm d}=x-\eta(u-v)=w_{J+1}.
\tag{6.5}
\]

末个等式由 (6.3) 乘 j(j+1) 后求和得到。再查询 y 的分量值，计算 E=M(y)−D。由于 D≤min M，有 E≥0。

下面证明 E 的明确上界。定义

\[
\ell_j(w)=\phi(w_j)+\langle a_j,w-w_j\rangle-\langle v,w\rangle
+\frac{\|w-x\|^2}{2\eta}.
\]

用更新式展开距离平方，有精确等式

\[
\begin{aligned}
j\bigl(M(w_j)-\ell_j(w)\bigr)
={}&\frac{j(j-1)}{4\eta}\|w_j-w\|^2
-\frac{j(j+1)}{4\eta}\|w_{j+1}-w\|^2\\
&+\frac{\eta j}{j+1}\|c_j\|^2.
\end{aligned}
\]

求和，乘 2/[J(J+1)]，并使用 M 的凸性以及 ℓ=Σλⱼℓⱼ，得

\[
M(y)-\ell(w)
\leq-\frac{\|w_{J+1}-w\|^2}{2\eta}
+\frac{2\eta}{J(J+1)}\sum_{j=1}^J\frac{j}{j+1}\|c_j\|^2.
\]

取 w=z_d=wJ+1，得到

\[
\boxed{0\leq E\leq\frac{8\eta B^2}{J+1}.}
\tag{6.6}
\]

可计算的正侧间隙上界为

\[
\widehat\Psi_\phi(q,u)=\phi(q)+S-\langle u,q\rangle\geq\Psi_\phi(q,u)\geq0.
\]

它满足两条完全可计算的等式：

\[
E=\widehat\Psi_\phi(y,u)+\frac{\|y-z_{\mathrm d}\|^2}{2\eta},
\]

\[
\boxed{
\widehat\Psi_\phi(x,u)+\Psi_g(y,v)
+\frac{\eta}{2}\|u-v\|^2+\frac{\|y-x\|^2}{2\eta}
=F(x)-F(y)+E.}
\tag{6.7}
\]

其中 Ψg(y,v)=g(y)−g(x)−〈v,y−x〉，也由已查询信息得到。这样，算法显式输出 u、v 和正侧 gap 的可核查上界。加权和只需在线累计，不需要保留全部切平面。

### 6.3 外层定理

给定 δ>0、ε>0，设置

\[
\eta=\frac{\delta}{\varepsilon^2},\qquad
\sigma=\frac{\delta}{4},\qquad
K=\max\left\{1,\left\lceil\frac{4\Delta}{\delta}\right\rceil\right\},
\qquad
J=\max\left\{1,\left\lceil\frac{8\eta B^2}{\sigma}\right\rceil\right\}.
\]

外层 k=0,…,K−1，在 xᵏ 查询 vᵏ∈∂g(xᵏ)，执行 §6.2 内层，令 xᵏ⁺¹=yᵏ。记录 dₖ=F(xᵏ)−F(xᵏ⁺¹)，选取 dₖ 最小的 k*，输出旧点 xᵏ* 及其 uᵏ*、vᵏ*、Sᵏ*。

由于 Σdₖ=F(x⁰)−F(xᴷ)≤Δ，所以 dₖ*≤Δ/K。由 (6.6)–(6.7)，

\[
\widehat\Psi_\phi(x^{k_*},u^{k_*})
+\frac{\eta}{2}\|u^{k_*}-v^{k_*}\|^2
\leq\frac{\Delta}{K}+\sigma\leq\frac{\delta}{2}.
\]

因此输出点满足

\[
\boxed{
\Psi_\phi(x^{k_*},u^{k_*})\leq\delta/2,\qquad
v^{k_*}\in\partial g(x^{k_*}),\qquad
\|u^{k_*}-v^{k_*}\|\leq\varepsilon.}
\tag{6.8}
\]

每次内层仅用 J 次普通分量查询，外层和平均点值查询增加 O(K)，故总成本

\[
\boxed{O\left(\left(1+\frac{\Delta}{\delta}\right)
\left(1+\frac{B^2}{\varepsilon^2}\right)\right).}
\]

当 δ≤Δ 且 ε≤B，化为 O(ΔB²/(δε²))。取 δ=ε²，得到显式 (ε²,0,ε)-VAC 的 ε⁻⁴ 上界。这里的初始函数值差距假设足够，不需要所有外层点预先满足一个统一差距界。

新点输出同样成立：由 E≤σ 与 (6.7)，得到 (σ,Δ/K+σ,√(2(Δ/K+σ)/η))-VAC。旧点输出的负侧可以精确，故不再需要为了消除 δg 而增加 ε⁻¹。

## 7. 固定分量界下的匹配下界

### 7.1 从 Li–Pan 引用的输入

[1] 的未缩放困难函数记为 f̄，维数 d=MN，其中 N≥60、2≤M≤N/12。Propositions 2–5 给出：f̄ 全局 1-Lipschitz、下有界、初始差距≤3M/N；存在坐标子空间序列 V₋₁={0}⊆V₀⊆…，满足

\[
z\in\mathcal V_t\Longrightarrow\partial\bar f(z)\subseteq\mathcal V_{t+1},
\]

以及 H≥MN/120，使

\[
z\in\mathcal V_{H-1}\Longrightarrow
\|\nabla\bar f_{1/2}(z)\|>\frac{1}{8\sqrt{N}}.
\tag{7.1}
\]

这里只引用这些性质及其 Lemma 3 的最大值表示，不重新声称基础困难族是本稿构造。

### 7.2 有界凸化的全局凸性

按 [1] Lemma 3、Proposition 2 的表示，对每个非负单位球权重 w，相关分支可写为

\[
F_w(z)=C(w)+\frac{2}{N}\sum_{m=1}^Mw_mP(z^m)
-\frac{2}{N}\sum_{m=1}^Ma_m(w)\psi(z^m),\qquad
\bar f=\max_wF_w,
\]

其中 P 凸，aₘ(w)=1−wₘ₊₁∈[0,1]，wM+1=0，

\[
\psi(z^m)=\frac{1}{N}\sum_{j=1}^Nq\left(\frac{N}{4}z_j^m\right),\qquad
q(s)=\begin{cases}0&s\leq0,\\3s^2-2s^3&0<s<1,\\1&s\geq1.\end{cases}
\]

在每个坐标上，负曲率为 −aₘq″(Nt/4)/8。采用任务中的

\[
c_N(t)=\begin{cases}
0,&t\leq0,\\
\frac{3}{8}t^2-\frac{N}{16}t^3,&0<t<2/N,\\
\frac{3}{4N}t-\frac{1}{2N^2},&t\geq2/N.
\end{cases}
\]

它满足 cN(0)=cN′(0)=0，0≤cN′≤3/(4N)，并且几乎处处

\[
c_N''(t)=\frac{1}{8}\left[q''\left(\frac{N}{4}t\right)\right]_+\in[0,3/4].
\]

所以 cN 是 C¹,¹ 凸函数。注意 0 处二阶导数不必存在，不能写成处处 C²。

令 CN(z)=Σm,j cN(zⱼᵐ)。对于每个 w，所有坐标曲率

\[
c_N''(t)-\frac{a_m(w)}{8}q''\left(\frac{N}{4}t\right)\geq0.
\]

这在 t<0、0<t<2/N、2/N<t<4/N 和 t>4/N 均成立。各连接点的一阶导数连续；正权重凸函数 P 不破坏凸性。因此 Fw+CN 全局凸，其最大值 f̄+CN 也全局凸。跨块没有未控制的交叉负曲率：固定 w 后所有非线性光滑项按块、按坐标分离；最后的最大值保持凸性。

又有

\[
\operatorname{Lip}(C_N)\leq\frac{3}{4}\sqrt{M/N},\qquad
\operatorname{Lip}(\nabla C_N)\leq\frac{3}{4}.
\]

### 7.3 归一化及成功准则转换

定义

\[
\phi=\frac{1}{2}(\bar f+C_N),\qquad g=\frac{1}{2}C_N,\qquad F=\frac{1}{2}\bar f.
\]

由 M/N≤1/12，两个分量均为全局 1-Lipschitz，初始差距≤1/8。因此该函数对属于 D(1,1,1)。g 的梯度 Lipschitz 常数≤3/8。选 ρ=1/2 作为有效上界，§4 推出

\[
(\varepsilon^2,\varepsilon^2,\varepsilon)\text{-VAC}
\Longrightarrow\|\nabla F_1(x)\|\leq(2+\sqrt{6})\varepsilon.
\tag{7.2}
\]

缩放给出 F₁=(1/2)f̄₁/₂，所以 (7.1) 变为

\[
\|\nabla F_1(z)\|>\frac{1}{16\sqrt{N}}\quad(z\in\mathcal V_{H-1}).
\]

令 A=2+√6，并选

\[
N=\left\lfloor\frac{1}{1024A^2\varepsilon^2}\right\rfloor,\qquad
M=\lfloor N/12\rfloor.
\]

对充分小 ε，参数满足所需范围，且 1/(16√N)≥2Aε。故 V_{H−1} 中没有平衡 VAC 成功点，H=Ω(ε⁻⁴)。负侧精确的 (ε²,0,ε)-VAC 是更强目标，同样受此下界约束。

### 7.4 两套完整次微分保持隐藏层

Clarke 光滑加法公式与凸性给出

\[
\partial\phi(z)=\frac{1}{2}\bigl(\partial\bar f(z)+\nabla C_N(z)\bigr),\qquad
\partial g(z)=\left\{\frac{1}{2}\nabla C_N(z)\right\}.
\]

由于 cN′(0)=0，z∈Vt 蕴含 ∇CN(z)∈Vt。因此

\[
z\in\mathcal V_t\Longrightarrow
\partial\phi(z)\cup\partial g(z)\subseteq\mathcal V_{t+1}.
\tag{7.3}
\]

这是完整集合的包含，故不依赖 oracle 从集合中挑哪个次梯度。cN(0)=0 同时保证未显露坐标不增加分量函数值。

### 7.5 任意确定性算法的成对抵抗 oracle

固定一个确定性算法及有限预算 T。为覆盖任意未查询输出，把输出追加为一次查询，令 T₀=T+1。工作空间选 R^{d+T₀}。

维护已指定的正交列 {uᵢ:i∈Iₜ}。Iₜ 是此前两个完整分量次微分出现的坐标支持的并集。算法给出第 t 个查询 xᵗ 后，定义未旋转坐标

\[
z_i^t=\begin{cases}\langle u_i,x^t\rangle&i\in I_t,\\0&i\notin I_t.\end{cases}
\]

在 zᵗ 计算两个分量值及完整次微分。对当前响应新出现的坐标 i，为 uᵢ 选择与 x⁰,…,xᵗ 以及此前所有已指定列正交的单位方向。需要的列数不超过 d−|Iₜ|，而可用正交补维数至少

\[
d+T_0-(t+1)-|I_t|\geq d-|I_t|.
\]

所以选择总能完成。随后返回

\[
\bigl(\phi(z^t),g(z^t),\ U\partial\phi(z^t),\ U\partial g(z^t)\bigr),
\]

其中响应只使用已指定列。

新列与全部历史查询正交，因此不会改变此前 z 的任何坐标。历史上新列对应的坐标全为零；所有历史函数值和集合响应继续一致。由 (7.3) 归纳可知 zᵗ∈Vt−1。

预算结束后，把剩余列补成正交矩阵 U，仍要求它们与所有历史查询正交。此时 Uᵀxᵗ=zᵗ 对全部历史点及追加输出点成立。最终固定函数对

\[
\phi_U(x)=\phi(U^\top x),\qquad g_U(x)=g(U^\top x)
\]

精确产生全部历史四元组。凸性、分量 Lipschitz 界、初始差距均保持；完整次微分满足 ∂φU=U∂φ、∂gU=U∂g。Moreau 梯度满足

\[
\nabla(F_U)_1(x)=U\nabla F_1(U^\top x),
\]

范数不变。所以当 T₀≤H 时，任意确定性算法的查询点与输出点都不能满足 (7.2)。这证明一般确定性成对完整次微分查询下的 Ω(ε⁻⁴) 下界。

### 7.6 定理范围

综合 §6 和 §7，在 D(1,1,1) 上，达到显式 (ε²,0,ε)-VAC 的确定性查询复杂度为 Θ(ε⁻⁴)。上界只需要普通成对分量 oracle；下界即使返回两套完整次微分仍成立。

这不是三个独立容差、全部 Gφ/Gg/Δ 参数的最优依赖定理，也不是随机算法下界。

下界位于含光滑负侧的子类，不妨碍它为更大的双侧非光滑 DC 类提供最坏情形下界。若要求两个分量都实际不可微，可加独立绝对值分量，代价只改变常数。若要求 F 本身不弱凸，可加独立目标 −|t|+2(|t|−1)₊，分到负侧 |t| 与正侧 2(|t|−1)₊；其 Fenchel 间隙分离且非负，成功证书投影回原坐标仍满足原下界。

当前仓库 appendix/lowerbound.tex 仍是光滑困难函数加公共二次项的旧归约。该旧文本不证明本节的固定分量界 ε⁻⁴ 结论，应由本节成对构造替换，而非直接更换定理标题。

## 8. Q3 定位与 K7

### 8.1 目标阶梯

Clarke 差法则给出 ∂CF(y)⊆∂φ(y)−∂g(y)，因此 L2⇒L1。

若 a∈∂h(y)、‖y−x‖≤r，h 凸且 Gh-Lipschitz，则

\[
\Psi_h(x,a)=h(x)-h(y)-\langle a,x-y\rangle\leq2G_hr.
\]

对 L1 见证的凸组合逐项运输，再用 h* 的凸性，得到

\[
L1(r,\varepsilon)\Longrightarrow
\operatorname{VAC}(2G_\phi r,2G_gr,\varepsilon).
\]

闭球、次微分图闭性、局部有界性和有限维凸包紧性保证所用距离达到。F₀ 则给出 L1 与 L2 的严格差距。

### 8.2 Kong–Lewis 的完整成本

[2] Theorem 6.6 的查询界为

\[
\left\lceil\frac{3\Delta}{r\varepsilon}\right\rceil
\frac{16L^2}{\varepsilon^2}
\left(1+\left\lfloor\frac{12\Lambda(r)}{\varepsilon}\right\rfloor\right).
\]

Oracle 2.5 需要给出目标值、方向导数及与该方向相容的 Clarke 次梯度。全空间有界 DC 函数满足方向可微和所需方向正则性质；Proposition 6.3 给出 Λ(r)≤Lip(g)。普通分量 oracle 的两个任意次梯度之差不自动成为所需相容向量。

### 8.3 K7 应如何陈述

局部 germ oracle 给出查询点足够小邻域内完整函数信息，可恢复方向导数及局部广义梯度结构；其信息强于单个次梯度或完整 Clarke 集合。对满足 Kong–Lewis 假设的实例，用它模拟方向 oracle 没有信息障碍。

因此，若 Kornowski 指数困难族在同一目标参数下还享有统一的适中 Λ(r) 上界，就可将 Kong–Lewis 算法作为一个确定性局部算法，得到矛盾。正确结论是：该最坏情形困难族不能同时具有这样的统一结构界。

不能进一步断言每个个别困难函数都非 DC、Λ(r)=∞，或所有大 Λ 问题都必然困难。下界量词为“每个算法存在困难实例”，上界中的 Λ 是结构参数，不是逐实例难度的充要刻画。

这类认识还有直接先例：[4] §3.2 讨论 Kong–Lewis，并用其分段线性困难实例建立 Proposition 4：在相应确定性算法类中，对非凸模 Λ 的线性依赖是紧的。因此 W4 不适合独立作为新认识。

本报告未证明普通分量 oracle 下 L1 或 L2 的确定性最优复杂度。现有结果没有自动回答该精确模型。本任务也未要求完成 Q3 的独立证明。

## 9. W1–W4 的新见解评估

**W1：一维可消除，二维存在不可消除的伪临界。** 数学成立；一维可升级为全次微分集合相等且保持原分量界，二维可升级为固定半径 Goldstein 残差分离。对 DCA 与机器学习优化读者，量词从某个分解变为所有分解具有解释价值。对极小对理论读者，二维核心几何是现有定理的直接推论。加强方向应放在定量驻点分离、算法选择量词，以及哪些结构能排除此现象。支撑材料为 §5 和 [16]–[17]；不要把经典 Jordan/极小对理论当作新构造。

**W2：负侧运输误差携带精确 DCA 更新后的临界信息。** 对新点的正侧 gap，这个判断正确；单侧 gap 恒为零的批评已明确出现在 [9] Remark 1。双 Bregman 下降结构也见 [15] Theorem 5。其用途是解释为什么证书需要同步两侧信息。不能把它写成所有有效证书都必须松弛负侧：§6 的旧点输出已经给出 δg=0。新的可用认识是，同一条下降恒等式支持新点与旧点两种认证，其中旧点实现负侧精确而不增加查询阶数。

**W3：跨点配对可能解释确定性可达性。** 目前是条件性研究假设，没有普通分量 oracle 下 L1 指数下界支撑。仓库 Q3 任务同时提出了 L1 可达的正面路线，因此论文不能提前认定困难位于 L0/L1 之间。跨点计算与同点值证书的转换已经严格成立；它是否解释 L1/L2 的算法分离仍待证明。强化需要同一 oracle、同一函数类下真正的可达性分离定理，而非比喻或目标名称差异。

**W4：负侧凹结构控制确定性代价。** Kong–Lewis 已用非凸模量化线搜索成本，Tian–So Proposition 4 又给出该参数依赖的紧性。作为背景认识成立，作为本文新发现不成立。可继续研究的增量在普通分量信息与方向一致信息之间的转换代价。当前证据只支持结构性上界与最坏族限制，不能支持“非凸模大当且仅当确定性困难”的结论。

按概念研究潜力排序：W1 > W3 > W2 > W4。W3 仍是猜想，不能计入已完成成果。按当前可形成论文定理的支撑度：加强后的 Q2 最优证书复杂度优先，其次是准确归属经典几何的一维/二维分离。

## 10. 修正后的主线与引言钩子

### 全文一句话

在分量全局 Lipschitz 的 DC 类上，同点精确次微分残差没有统一有限查询保证；仅松弛正侧支撑值误差，即可用最优 Θ(ε⁻⁴) 次确定性基本查询显式产生 (ε²,0,ε)-VAC，而一维可还原、二维起可能不可还原的临界结构，刻画了这种可计算证书与原目标 Goldstein 驻点之间的差距。

### 引言钩子

即使允许重新选择任意凸分解，DC 临界性仍可能接受一个沿某方向严格下降、并与 Goldstein 驻点保持固定距离的点。一维中，Jordan 分解能同时消除全部这类失真；二维中，经典极小对理论已经允许不可消除的例子。因此，研究 DC 算法需要同时回答两个问题：有限一阶信息能够认证什么，以及该证书对原目标究竟保证什么。

本文针对这两个问题建立可计算性与解释性的对应：精确正侧次微分的同点目标无统一有限查询保证；允许正侧支撑值误差后，负侧仍可保持精确，并以最优 ε⁻⁴ 确定性查询复杂度输出完整证书。负侧光滑时，该证书推出 Moreau 驻点；双侧非光滑时，定量几何分离说明其局限。普通分量信息能否进一步达到分解无关的 Goldstein 目标，作为后续边界问题提出。

## 11. 入稿优先级与最大风险

1. 用 §6 的完整可计算证书定理替换只有存在性见证的上界；明确旧点输出、查询计数和参数范围。它同时支撑 δg=0、同阶成本及可核查证书三个主张。
2. 用 §7 替换当前公共二次项下界。独立核对两套完整次微分、全部历史函数值、最终固定函数对及任意输出点。该步骤支撑 Optimal Complexity。
3. 将 §5 写成规范分解与不可消除分离的定理/推论，明确引用极小对文献，保留定量 Goldstein 缺口和 DCA 选择量词。
4. 修正文献定位：加入 Xu 等计入内层的非光滑上界、MDCA 对旧 gap 的直接批评，以及 Tian–So Proposition 4。对 Tian–So 2021 原始 DC 定理、旧不精确 DCA 的完全同证书优先权保留待核状态。

最大的数学风险仍是把较弱 oracle 的下界直接搬到较强成对 oracle。本文已给出相应延拓；它必须作为正式证明入稿，而不能只引用 Li–Pan 定理。若该环节经独立审阅发现不可修复的问题，应保留显式上界和几何分离，撤下最优性主张。

最大的定位风险是把经典几何、已有 gap 批评和已有非凸模观点同时列作新见解。把主贡献集中到指定信息模型下的必要松弛、可核查证书与匹配复杂度，即使这些文献归属全部保留，主线仍成立。

## 12. 文献定位

以下条目用于原文定位；正文已经注明哪些结论完整核过、哪些只核到题录或摘要。

[1] Li–Pan, Optimal Deterministic Oracle Complexity for Weakly Convex Optimization, arXiv:2608.03246v1. Theorems 2–3; Lemmas 3–4、10–11; Propositions 2–5. https://arxiv.org/html/2608.03246v1

[2] Kong–Lewis, The Cost of Nonconvexity in Deterministic Nonsmooth Optimization, Mathematics of Operations Research, 2024; arXiv:2210.00652v2. Oracle 2.5; Proposition 6.3; Theorem 6.6. https://arxiv.org/pdf/2210.00652v2

[3] Jordan et al., Deterministic Nonsmooth Nonconvex Optimization, COLT 2023, PMLR 195. Theorems 1–2. https://proceedings.mlr.press/v195/jordan23a/jordan23a.pdf

[4] Tian–So, No dimension-free deterministic algorithm computes approximate stationarities of Lipschitzians, Mathematical Programming 208, 51–74, 2024. Theorem 1; §3.2; Proposition 4. https://www.se.cuhk.edu.hk/~manchoso/papers/lip_det_hard-MPA.pdf

[5] Kornowski, arXiv:2609.23837v1. Theorem 3.1; §5.1. https://arxiv.org/html/2609.23837v1

[6] Kornowski, arXiv:2609.17780v1. Theorem 3.1，算法类限制为 zero-respecting。 https://arxiv.org/html/2609.17780v1

[7] Xu, Qi, Lin, Jin, Yang, Stochastic Optimization for DC Functions and Non-smooth Non-convex Regularizers with Non-asymptotic Convergence, ICML 2019, PMLR 97. §2；Assumption 2(ii)；Theorems 2–3。 https://proceedings.mlr.press/v97/xu19c/xu19c.pdf

[8] Nguyen, Yurtsever, Sra, Toh, Improved rates for stochastic variance-reduced difference-of-convex algorithms, arXiv:2509.11657v1. Definition 12。 https://arxiv.org/html/2509.11657v1

[9] Stochastic Difference-of-Convex Optimization with Momentum, arXiv:2510.17503v2，2026-10-09 更新。Lemmas 2–3；Remark 1。 https://arxiv.org/html/2510.17503v2

[10] Kornowski–Shamir, On the Complexity of Finding Small Subgradients in Nonsmooth Optimization, arXiv:2209.10346v2. Theorem 5。 https://arxiv.org/html/2209.10346v2

[11] Tian–So, On the Hardness of Computing Near-Approximate-Stationary Points of Clarke Regular Nonsmooth Nonconvex Problems and Certain DC Programs, ICML 2021 Workshop on Beyond First-Order Methods in ML。官方列表确认题录；原始定理未取得完整核查。 https://sites.google.com/view/optml-icml2021/accepted-papers

[12] Sun–Sampaio–Candido, Proximal point algorithm for minimization of DC function, Journal of Computational Mathematics 21(4), 451–462, 2003；Moudafi–Maingé, On the convergence of an approximate proximal method for DC functions, Journal of Computational Mathematics 24(4), 475–480, 2006。本次核至出版社题录、摘要及 [13] 引文，未据此填写未经核对的定理号。 https://global-sci.com/index.php/JCM/article/view/11570 ; https://www.global-sci.com/JCM/article/view/11779

[13] Zhang–Yamada, tPLDCA, arXiv:2305.06520v2, Optimization 2024。Algorithm 2，条件 (10)–(12)，Theorems 4.5、4.7。 https://arxiv.org/html/2305.06520v2

[14] InmBDCA, arXiv:2412.05697v1；JOTA 2025。Theorems 21–22 计外层更新步长指标；其强凸分量假设与全局有界分量类不同。 https://arxiv.org/html/2412.05697v1

[15] Faust–Fawzi–Saunderson, AISTATS 2023, PMLR 206。§2.2；Theorem 5 的双 Bregman 下降分解，负侧分量可微。 https://proceedings.mlr.press/v206/faust23a/faust23a.pdf

[16] Grzybowski–Urbański, Minimal Pairs of Convex Sets Which Share a Recession Cone, SIAM Journal on Optimization 2022；arXiv:2012.06536。Theorems 7.1、7.2、7.4。Theorem 7.4 回引 Grzybowski–Pallaschke–Urbański 2009 的 Theorem 3.5。 https://arxiv.org/pdf/2012.06536

[17] Scholtes, Minimal pairs of convex bodies in two dimensions, Mathematika 39(2), 267–273, 1992。平面极小对在共同平移意义下唯一；可由 [16] Theorem 7.2 核对引用关系。

[18] Yao, Lin, Yang, A Note on Complexity for Two Classes of Structured Non-Smooth Non-Convex Compositional Optimization, arXiv:2411.14342v1。Algorithm 2、Theorem 5.8：随机附近临界目标与精确子模型操作，并非本稿普通成对查询模型。 https://arxiv.org/html/2411.14342v1

Demyanov–Jeyakumar 1997 的 Hunting for a smaller convex subdifferential，以及 de Oliveira–Tcheou 2019 的惯性不精确 DCA，本次没有取得足以逐条否定完全同证书优先权的全文定位。不得将这项检索缺口写成“已排除全部先例”。
