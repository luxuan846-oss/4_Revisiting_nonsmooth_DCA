> 来源：用户上传的 GPT Pro 报告完整版（较分享页提取版更完整），2026-10-16 入库。尚未独立审核；配套脚本 `Q3_sanity_checks.py` 未入库。

# Q3：普通分量 oracle 下的确定性边界

日期：2026-10-16。

**本报告的证明给出以下答案：L1 存在维数无关的确定性查询上界；L2 不存在维数无关上界，但存在依赖维数的多项式查询上界。固定其余参数时，本报告得到 L2 的 Ω(n) 下界与 O(n log n) 上界。**

这里的“已证明”表示下文给出了完整数学证明，不表示已经发表或经过独立同行复核。文献新颖性仍待验证。算法始终使用题设普通分量 oracle，采用精确实数查询模型；本报告不提供浮点稳定性、带噪声 oracle 或位复杂度保证。

## 1. 状态与精确结论

| 项目 | 状态 | 结论 |
|---|---|---|
| K7 | 部分结果 | 有限的 Kornowski 抵抗实例确实是全局 Lipschitz DC；已给出分量界随实例长度增长的分解。其整个困难族不能同时具有统一受控的非凸模。不能由此断言每个任意实例的最优分解常数都大。 |
| H1 | 已证明 | L1 可在普通分量 oracle 下确定性、维数无关地达到。 |
| H2(a) | 已证明 | 在固定类 \(\mathcal{D}(3,1,1)\) 中，固定 \(r=1/2,\varepsilon=1/4\)，L2 需要至少 \(n-2\) 次最坏情形查询。 |
| H2(b) | 否证 | “L2 不存在依赖维数的多项式确定性方法”被下文构造的上界否证。 |
| H3(a) | 否证 | 维数无关的确定性 L2 方法被 H2(a) 否证。 |
| H3(b) | 已证明 | 一个确定性的局部纯化过程，与稳健的线搜索结合，给出多项式查询上界。 |

**定理 1：L1 上界。** 对任意维数、任意题设函数对、任意合法对抗次梯度选择，存在确定性算法达到 L1，查询次数为
\[
O\!\left[
\left(1+\frac{\Delta}{r\varepsilon}\right)
\left(1+\frac{B^2}{\varepsilon^2}\right)
\left(1+\frac{G_g}{\varepsilon}\right)
\right].
\]
当所有主要比值均不小时，其主要项为 \(O(\Delta B^2G_g/(r\varepsilon^4))\)。完整表达式中的加一项不可删除，尤其在 \(G_g=0\) 时。

**定理 2：L2 上界。** 对同一函数类与同一 oracle，存在确定性算法达到 L2，查询次数为
\[
O\!\left[
\left(1+\frac{\Delta}{r\varepsilon}\right)
\left(1+\frac{B^2}{\varepsilon^2}\right)
\left(
1+\frac{B}{\varepsilon}
+n\log\!\left(2+\frac{B\sqrt{n}}{\varepsilon}\right)
\right)
\right].
\]
这是一条可达性上界，不主张其精度依赖最优。

**定理 3：L2 下界。** 固定 \(0<r<1\) 和 \(0<\varepsilon<1/\sqrt{2}\)。对任意维数 \(n\ge3\)、任意最多查询 \(T\le n-3\) 次的确定性算法，存在一个固定函数对
\[
(\phi,g)\in\mathcal{D}(3,1,1)
\]
及合法 oracle，使算法的输出点不满足 L2。输出点不必是已查询点。

## 2. 模型、输出含义与目标阶梯

采用题设全空间有限值凸函数类：
\[
\operatorname{Lip}(\phi)\le G_\phi,\qquad
\operatorname{Lip}(g)\le G_g,\qquad
F=\phi-g,\qquad
F(x^0)-\inf F\le\Delta.
\]
记 \(B=G_\phi+G_g\)。下文仅讨论 \(B>0\)、\(r>0\)、\(0<\varepsilon<B\)。若 \(B=0\) 或 \(\varepsilon\ge B\)，任意点已经满足 L2。

一次普通分量查询在 \(x\) 返回
\[
\bigl(\phi(x),g(x),u,v\bigr),\qquad
u\in\partial\phi(x),\quad v\in\partial g(x).
\]
算法不得指定次梯度选择。重复查询也不要求 oracle 返回同一个次梯度；证明只使用已经存储的合法响应。所有历史函数值和次梯度必须同时与同一个函数对相容。

确定性下界的量词为“先固定算法，再构造一个使全部历史回答成立的函数对”。由于算法确定，该函数对也可视为在其实际运行之前固定。随机对照结果另要求函数对在随机种子之前固定；不能把对抗函数选择放到随机轨迹实现之后。

所有复杂度均计普通分量查询次数。算法可进行精确实数算术、向量归一化及线段上的最小范数计算。不存在免费方向导数、完整次微分、Fenchel 共轭、凸子问题或精确近端算子查询。

用以下记号避免混淆：
\[
D_r(x)=\operatorname{conv}\!\bigcup_{y\in\overline{B}_r(x)}
\bigl(\partial\phi(y)-\partial g(y)\bigr),
\qquad
C_r(x)=\operatorname{conv}\!\bigcup_{y\in\overline{B}_r(x)}\partial_C F(y).
\]
L1 要求 \(\operatorname{dist}(0,D_r(x))\le\varepsilon\)，L2 要求 \(\operatorname{dist}(0,C_r(x))\le\varepsilon\)。采用闭球；下文 L2 的样本实际上位于球内部。

### 2.1 L2 蕴含 L1

凸函数的 Clarke 次微分等于凸次微分，Clarke 和法则给出
\[
\partial_C(\phi-g)(y)\subseteq\partial\phi(y)-\partial g(y).
\]
逐点取并集和凸包，得到 \(C_r(x)\subseteq D_r(x)\)。因此 L2 蕴含 L1。

### 2.2 L1 蕴含 L0

取 \(y\in\overline{B}_r(x)\) 和 \(u\in\partial\phi(y)\)。全局 Lipschitz 界给出 \(\|u\|\le G_\phi\)。对任意 \(z\)，
\[
\begin{aligned}
\phi(z)
&\ge\phi(y)+\langle u,z-y\rangle\\
&=\phi(x)+\langle u,z-x\rangle
  +\phi(y)-\phi(x)+\langle u,x-y\rangle\\
&\ge\phi(x)+\langle u,z-x\rangle-2G_\phi r.
\end{aligned}
\]
故 \(u\in\partial_{2G_\phi r}\phi(x)\)。对 \(g\) 同理。

若 \(w=\sum_j\lambda_j(u_j-v_j)\in D_r(x)\)，其中两个见证使用同一个 \(y_j\)，令
\[
\bar{u}=\sum_j\lambda_j u_j,\qquad
\bar{v}=\sum_j\lambda_j v_j.
\]
近似次微分是凸集，所以
\[
\bar{u}\in\partial_{2G_\phi r}\phi(x),\qquad
\bar{v}\in\partial_{2G_g r}g(x),\qquad
\bar{u}-\bar{v}=w.
\]
这证明题设两步蕴含。有限维、全空间 Lipschitz 凸函数的次微分图闭且有界，因此这里相应的并集与凸包在闭球上紧，距离下确界能够达到。

## 附录 A：L1 的完整证明

### A.1 一维线搜索引理

设 \(p,q\) 在区间 \([a,b]\) 上为有限凸函数，\(q\) 为 \(G_g\)-Lipschitz。记 \(h=p-q\)，并假设
\[
A:=\frac{h(b)-h(a)}{b-a}=-\sigma<0.
\]
查询点 \(t\) 时只取得任意合法
\[
\alpha_t\in\partial p(t),\qquad\beta_t\in\partial q(t).
\]
端点次梯度均理解为全空间凸函数限制后的合法支撑斜率，满足 \(|\beta_t|\le G_g\)。目标是找到 \(\alpha_t-\beta_t<0\)。

算法先查询两个端点并检验左端点。若尚未成功，则查询当前区间中点并检验。每次中点检验失败，保留平均斜率更小的一半。相等时固定保留左半。旧响应直接复用。

若 \(s<t\) 且左端点检验失败，即 \(\alpha_s-\beta_s\ge0\)，凸性分别给出
\[
p(t)-p(s)\ge\alpha_s(t-s),\qquad
q(t)-q(s)\le\beta_t(t-s).
\]
所以
\[
\frac{h(t)-h(s)}{t-s}\ge\beta_s-\beta_t. \tag{A1}
\]

**主张。** 如果从 \([a,b]\) 开始的前 \(k\) 次检验均失败，则
\[
\beta_a-\beta_b\le kA. \tag{A2}
\]

当 \(k=1\) 时，这就是 (A1)。设结论对 \(k-1\) 成立。第一次中点检验也失败。设保留半区间与舍弃半区间的平均斜率为 \(A_K,A_D\)。由于二分等长，
\[
A_K\le A,\qquad A_K+A_D=2A.
\]
保留区间具有 \(k-1\) 次失败检验：保留区间的左端点加后续中点。舍弃区间的左端点也已经检验失败。分别使用归纳假设与 (A1)，相加得到
\[
\beta_a-\beta_b
\le(k-1)A_K+A_D
=(k-2)A_K+2A
\le kA.
\]
这证明主张。

再由 \(\beta_b-\beta_a\le2G_g\)，得到
\[
k\sigma\le2G_g.
\]
因此至多
\[
1+\left\lfloor\frac{2G_g}{\sigma}\right\rfloor
\]
次检验后必定成功，另计最初读取右端点的一次查询。这一证明从未使用 \(h\) 的方向导数，也未把 \(\alpha_t-\beta_t\) 当作 \(\partial_C h(t)\) 的元素。

### A.2 最小范数线段更新

设 \(\|w\|,\|p\|\le B\)、\(w\ne0\)，且
\[
\langle p,w\rangle\le\tfrac{1}{2}\|w\|^2.
\]
令 \(w^+\) 为线段 \([w,p]\) 中的最小范数向量。它可通过一维二次函数的截断极小点精确计算。

取 \(t=\|w\|^2/(8B^2)\in[0,1]\)，并使用 \(\|p-w\|\le2B\)，得到
\[
\begin{aligned}
\|w^+\|^2
&\le\|w+t(p-w)\|^2\\
&\le\|w\|^2-t\|w\|^2+4B^2t^2\\
&=\|w\|^2\left(1-\frac{\|w\|^2}{16B^2}\right).
\end{aligned}\tag{A3}
\]
若 \(w^+\ne0\)，则
\[
\frac{1}{\|w^+\|^2}\ge\frac{1}{\|w\|^2}+\frac{1}{16B^2}.
\]
所以不超过 \(\lceil16B^2/a^2\rceil\) 次这类更新后，向量范数必定不大于 \(a\)。

### A.3 外层算法与查询次数

每个阶段固定一个中心 \(x\)，查询一次并初始化 \(w=u-v\)。

1. 若 \(\|w\|\le\varepsilon\)，输出中心 \(x\)。
2. 否则令 \(e=w/\|w\|\)，查询 \(x'=x-re\)。若
   \[
   F(x)-F(x')\ge r\varepsilon/3,
   \]
   将中心更新为 \(x'\)，删除旧阶段的向量，重新初始化。
3. 若下降检验失败，在 \([0,r]\) 上令
   \[
   p(t)=\phi(x'+te)-\varepsilon t/2,\qquad
   q(t)=g(x'+te),\qquad h=p-q.
   \]
   此时
   \[
   \frac{h(r)-h(0)}{r}<\varepsilon/3-\varepsilon/2=-\varepsilon/6.
   \]
   使用 A.1，只需检验 oracle 实际返回的
   \[
   \langle u-v,e\rangle-\varepsilon/2<0.
   \]
   最多 \(K_1=1+\lfloor12G_g/\varepsilon\rfloor\) 次检验即可找到一个向量 \(p_*\)，满足
   \[
   \langle p_*,w\rangle<\frac{\varepsilon\|w\|}{2}<\frac{\|w\|^2}{2}.
   \]
4. 将 \(w\) 更新为 \([w,p_*]\) 中的最小范数元，回到步骤 1。

每个向量均来自同一中心半径 \(r\) 内的同点分量差。线段更新保留凸组合性质。因此输出时 \(w\in D_r(x)\)，证明的是 L1。

每个阶段最多发生
\[
I_1=\left\lceil\frac{16B^2}{\varepsilon^2}\right\rceil
\]
次向量更新。成功的中心更新次数不超过 \(\lfloor3\Delta/(r\varepsilon)\rfloor\)。设
\[
D_1=1+\left\lfloor\frac{3\Delta}{r\varepsilon}\right\rfloor.
\]
一个计入所有端点且允许重复计算的安全上界为
\[
N_{L1}\le D_1\bigl[1+(I_1+1)(K_1+3)\bigr]. \tag{A4}
\]
这证明定理 1。无需额外加入正侧跳跃次数项；负侧凸次梯度的总变化已经控制全部失败检验。

## 附录 B：确定性局部纯化

“纯化”在本文中仅表示：找到一个邻近点，使该点任何普通分量差都接近一个真实 Clarke 次梯度。不要求找到精确可微点。

### B.1 引理的精确陈述

给定中心 \(z\)、半径 \(\tau>0\)、误差 \(0<s\le B\)。只使用普通分量 oracle，可以确定性地找到 \(y\in B_\tau(z)\) 与该点实际返回的 \(u,v\)，使
\[
\operatorname{diam}\bigl(\partial\phi(y)-\partial g(y)\bigr)\le s,
\qquad
\operatorname{dist}\bigl(u-v,\partial_C F(y)\bigr)\le s. \tag{B1}
\]
查询次数至多
\[
Q(n,B,s)=n\left(\left\lceil\log_2\frac{4B\lceil\sqrt{n}\rceil}{s}\right\rceil+2\right)+1. \tag{B2}
\]
全部查询点均在 \(\overline{B}_\tau(z)\) 内。

### B.2 算法

令
\[
H=\phi+g,\qquad k=\lceil\sqrt{n}\rceil,\qquad
J=\left\lceil\log_2\frac{4Bk}{s}\right\rceil.
\]
普通查询给出的 \(u+v\) 属于 \(\partial H\)，且范数不超过 \(B\)。初始化 \(c=z,R=\tau\)。逐个处理坐标 \(i=1,\ldots,n\)。

1. 查询端点
   \[
   a=c-\frac{R}{2} e_i,\qquad b=c+\frac{R}{2} e_i.
   \]
   记实际返回的 \(H\) 次梯度为 \(A,C\)，并存储 \(\alpha=A_i,\beta=C_i\)。
2. 做 \(J\) 次二分。查询当前中点 \(m\)，得到 \(M\in\partial H(m)\)。若
   \[
   M_i-\alpha\le\beta-M_i,
   \]
   保留左半及其已存储端点响应；否则保留右半。
3. 记最终区间长度为 \(\ell=R2^{-J}\)，其中点为 \(c^+\)。令
   \[
   R^+=\frac{\ell s}{16Bk}.
   \]
   用 \((c^+,R^+)\) 替换 \((c,R)\)，继续下一个坐标。

最后查询中心 \(y=c\)，返回实际 \(u,v\)。

### B.3 二分为何有效

凸次微分单调性给出
\[
0\le\langle C-A,b-a\rangle=R(\beta-\alpha).
\]
中点同理满足 \(\alpha\le M_i\le\beta\)。因此每次选择的端点标量间距至少减半。最初间距不超过 \(2B\)，故最终
\[
\beta-\alpha\le2B2^{-J}\le\frac{s}{2k}. \tag{B3}
\]
算法没有要求端点返回极端次梯度。

### B.4 从线段端点控制整个小球

设最终区间端点为 \(a=c^+-\ell e_i/2\)、\(b=c^++\ell e_i/2\)。取任意 \(x\in\overline{B}_{R^+}(c^+)\)、任意 \(W\in\partial H(x)\)。与左端点的单调性给出
\[
0\le\langle W-A,x-a\rangle
=\frac{\ell}{2}(W_i-\alpha)+\langle W-A,x-c^+\rangle.
\]
由于 \(\|W-A\|\le2B\)，得到
\[
W_i\ge\alpha-\frac{4BR^+}{\ell}.
\]
与右端点同理，得到
\[
W_i\le\beta+\frac{4BR^+}{\ell}.
\]
因此整个新球内所有 \(H\) 次梯度的第 \(i\) 个坐标，落在宽度不超过
\[
\beta-\alpha+\frac{8BR^+}{\ell}
\le\frac{s}{2k}+\frac{s}{2k}
=\frac{s}{k} \tag{B4}
\]
的区间中。

又因为
\[
\|c^+-c\|\le R/2,\qquad R^+\le R/16,
\]
新球包含在旧球内部。已经处理的坐标宽度保证不会在后续步骤丢失。端点、中点也一直留在初始球内。

### B.5 从 \(\partial H\) 到真实 Clarke 次梯度

最终点 \(y\) 处，记 \(A=\partial\phi(y)\)、\(C=\partial g(y)\)。全空间有限凸函数的和法则给出
\[
\partial H(y)=A+C.
\]
对任何非空紧集定义其第 \(i\) 个坐标宽度为该坐标最大值减最小值。直接展开最大值与最小值可得
\[
\operatorname{width}_i(A-C)
=\operatorname{width}_i(A)+\operatorname{width}_i(C)
=\operatorname{width}_i(A+C).
\]
由 (B4)，\(A-C\) 各坐标宽度均不超过 \(s/k\)。故任意两点 \(p,q\in A-C\) 满足
\[
\|p-q\|^2\le n(s/k)^2\le s^2.
\]
同时 \(\varnothing\ne\partial_C F(y)\subseteq A-C\)。所以实际返回的任意 \(u-v\in A-C\) 到 \(\partial_C F(y)\) 的距离不超过 \(s\)。这证明 (B1)。

每个坐标使用两次端点查询和 \(J\) 次中点查询，最后一次输出查询给出 (B2)。查询次数不依赖 \(\tau\)，但查询点间距会随坐标处理而变小。这是精确查询结论，不能直接作为浮点算法的稳定性结论。

## 附录 C：从局部纯化到 L2

不能在 A.3 中找到一个原始分量差以后，任意扰动其位置并沿用原来的内积保证。原始差可能是伪向量。这里先用函数值建立对整个小邻域都有效的方向上界，再在该邻域纯化。

### C.1 稳健方向搜索引理

给定 \(0<a\le B\)、单位向量 \(e\)、步长 \(R_0>0\)，令
\[
x'=x-R_0e,
\qquad F(x)-F(x')<R_0a/3.
\]
取
\[
m=\left\lceil\frac{16B}{a}\right\rceil+1,
\qquad h=R_0/m,
\qquad z_j=x'+jhe\quad(0\le j\le m).
\]
查询全部网格点，并对 \(1\le j\le m-1\) 计算
\[
S_j=
\frac{\phi(z_{j+1})-\phi(z_j)}{h}
-\frac{g(z_j)-g(z_{j-1})}{h}.
\]
精确求和得到
\[
\sum_{j=1}^{m-1}hS_j
=F(x)-F(x')-[\phi(z_1)-\phi(z_0)]
+[g(z_m)-g(z_{m-1})]
<\frac{mha}{3}+hB.
\]
因此某个最小值索引 \(j\) 满足
\[
S_j<\frac{a}{3}+\frac{B+a/3}{m-1}\le\frac{5a}{12}. \tag{C1}
\]
最后一步使用 \(a\le B\) 和 \(m-1\ge16B/a\)。

令 \(\tau=ha/(48B)\)。任取 \(y\in\overline{B}_\tau(z_j)\) 及 \(u\in\partial\phi(y),v\in\partial g(y)\)。正侧支撑不等式给出
\[
\phi(z_{j+1})\ge\phi(y)+\langle u,z_{j+1}-y\rangle,
\]
结合 \(|\phi(y)-\phi(z_j)|\le G_\phi\tau\)、\(\|u\|\le G_\phi\)，可得
\[
\langle u,e\rangle\le
\frac{\phi(z_{j+1})-\phi(z_j)}{h}+\frac{2G_\phi\tau}{h}.
\]
负侧使用 \(g(z_{j-1})\ge g(y)+\langle v,z_{j-1}-y\rangle\)，得到
\[
\langle v,e\rangle\ge
\frac{g(z_j)-g(z_{j-1})}{h}-\frac{2G_g\tau}{h}.
\]
相减即
\[
\langle u-v,e\rangle
\le S_j+\frac{2B\tau}{h}
\le\frac{5a}{12}+\frac{a}{24}
=\frac{11a}{24}<\frac{a}{2}. \tag{C2}
\]
这是对整个小球和任意合法 oracle 选择都成立的保证。

### C.2 L2 算法

设
\[
a=s=\varepsilon/2,\qquad R_0=r/2.
\]
每个阶段固定中心 \(x\)。调用 B.2，以 \(x\) 为纯化中心、半径 \(r/4\)、误差 \(s\)，取得向量 \(p=u-v\)，令 \(w=p\)。同时保存其纯化位置和凸组合权重。

1. 若 \(\|w\|\le a\)，输出当前中心 \(x\)。
2. 否则令 \(e=w/\|w\|\)，查询 \(x'=x-R_0e\)。若
   \[
   F(x)-F(x')\ge R_0a/3=r\varepsilon/12,
   \]
   将中心更新为 \(x'\)，丢弃旧阶段向量，重新初始化。
3. 下降失败时使用 C.1 的网格，选择最小 \(S_j\)。在 \(B_\tau(z_j)\) 内调用纯化过程，仍取误差 \(s\)，得到 \(p=u-v\)。
4. 将 \(w\) 更新为线段 \([w,p]\) 中的最小范数元，保存相应凸组合权重，回到步骤 1。

C.2 保证 \(\langle p,w\rangle<a\|w\|/2<\|w\|^2/2\)，因此 A.2 的几何更新界适用。全部保存的纯化位置都在 \(B_r(x)\) 内：初始化偏移小于 \(r/4\)，后续偏移不超过 \(R_0+\tau<r\)。

### C.3 为什么输出满足 L2

当前 \(w\) 是实际返回向量的凸组合：
\[
w=\sum_j\lambda_jp_j,
\qquad \lambda_j\ge0,
\qquad\sum_j\lambda_j=1.
\]
每个 \(p_j\) 的纯化保证提供一个存在性见证
\[
q_j\in\partial_C F(y_j),\qquad \|p_j-q_j\|\le s,
\qquad y_j\in B_r(x).
\]
令 \(q=\sum_j\lambda_jq_j\in C_r(x)\)。那么
\[
\|q-w\|
\le\sum_j\lambda_j\|q_j-p_j\|
\le s.
\]
输出时
\[
\operatorname{dist}(0,C_r(x))\le\|q\|\le\|w\|+s\le a+s=\varepsilon.
\]
纯化误差通过凸组合保持为 \(s\)，不会随样本数量累加。算法不需要显式取得不可查询的 \(q_j\)；它输出有 L2 保证的点，并可保存有限查询记录及所用宽度界。

### C.4 查询次数与显式常数

令
\[
\begin{aligned}
D_2&=1+\left\lfloor\frac{12\Delta}{r\varepsilon}\right\rfloor,\\
I_2&=\left\lceil\frac{64B^2}{\varepsilon^2}\right\rceil,\\
m&=\left\lceil\frac{32B}{\varepsilon}\right\rceil+1,\\
Q&=n\left(\left\lceil\log_2\frac{8B\lceil\sqrt{n}\rceil}{\varepsilon}\right\rceil+2\right)+1.
\end{aligned}
\]
中心阶段数不超过 \(D_2\)，每阶段向量更新数不超过 \(I_2\)。初始化纯化及中心值读取至多 \(Q+1\) 次；每次方向搜索计入试探点、全部网格与纯化，不超过 \(Q+m+3\) 次。一个安全上界是
\[
N_{L2}\le
D_2\bigl[Q+1+(I_2+1)(Q+m+3)\bigr]. \tag{C3}
\]
这证明定理 2。

## 附录 D：固定分量常数的维数下界

固定一个最多查询 \(T\) 次、随后输出 \(\widehat{x}\) 的确定性算法。令起点为原点，并对所有查询返回
\[
\phi(x_t)=g(x_t)=0,\qquad u_t=v_t=0.
\]
记录它在这个确定响应下的查询点与输出点。由于 \(n\ge T+3\)，存在两个正交单位向量 \(a,b\)，同时垂直于
\[
\operatorname{span}\{x_1,\ldots,x_T,\widehat{x}\}.
\]
若算法提前输出，只需使用实际查询点。定义正交投影坐标
\[
Px=(\langle a,x\rangle,\langle b,x\rangle).
\]
取
\[
\begin{aligned}
P_0(z)&=\max\{0,z_1,z_2\},\\
Q_0(z)&=\max\{0,-z_1,-z_2\},\\
F_0(z)&=P_0(z)-Q_0(z),\\
\phi(x)&=P_0(Px)+2(\|Px\|-1)_+,\\
g(x)&=Q_0(Px).
\end{aligned}\tag{D1}
\]

### D.1 函数类与历史一致性

\(P_0,Q_0\) 都是 1-Lipschitz 凸函数。函数 \((\|z\|-1)_+\) 凸且 1-Lipschitz。因此
\[
\operatorname{Lip}(\phi)\le3,
\qquad \operatorname{Lip}(g)\le1.
\]
所有查询点和输出点满足 \(Px=0\)。此处两个分量值均为零，且原点分别属于它们的次微分。因此全部零响应都是 (D1) 这个固定函数对的真实合法响应。

这解决了量词与自适应一致性问题。没有在不同时间改变旧函数值，也没有免费指定真实 Clarke 次梯度。

### D.2 目标函数下有界且初始间隙为 1

对任意 \(z\in\mathbb{R}^2\)，有 \(|F_0(z)|\le\|z\|\)。两个坐标同号时，\(F_0\) 是其中一个坐标；异号时 \(F_0=z_1+z_2\)，其平方不超过 \(z_1^2+z_2^2\)。于是记 \(t=\|Px\|\)，
\[
F(x)\ge-t+2(t-1)_+\ge-1.
\]
取 \(Px=(-1,0)\) 可达到 \(-1\)，所以
\[
F(0)=0,\qquad\inf F=-1,
\qquad F(0)-\inf F=1.
\]

### D.3 输出点不满足 L2

\(F_0\) 在可微区域的梯度恰为
\[
(1,0),\qquad(0,1),\qquad(1,1).
\]
在 \(\widehat{x}\) 的半径 \(r<1\) 邻域内，\(\|Px\|<1\)，径向凸项恒为零。该邻域内全部 Clarke 次梯度都属于
\[
\operatorname{conv}\{a,b,a+b\}.
\]
令 \(d=(a+b)/\sqrt{2}\)，则这些向量都满足
\[
\langle q,d\rangle\ge\frac{1}{\sqrt{2}}.
\]
取空间并集与凸包后仍然成立，因此
\[
\operatorname{dist}(0,C_r(\widehat{x}))\ge\frac{1}{\sqrt{2}}>\varepsilon.
\]
定理 3 得证。

这里使用了题设二维例子的显式分解，不需要“任意分解都产生伪临界”的更强 K8 命题。径向项仅用于保证全空间下有界，且其分量 Lipschitz 代价是固定常数。

## 附录 E：K1 的完整核对

固定 \(x\)、\(v\in\partial g(x)\)、\(\eta>0\)，令
\[
M(y)=\phi(y)-\langle v,y\rangle+\frac{\|y-x\|^2}{2\eta},
\qquad z=\arg\min M.
\]
二次项与全局 Lipschitz 线性增长保证极小点存在；强凸性保证其唯一。最优性给出
\[
u=v-\frac{z-x}{\eta}\in\partial\phi(z).
\]
使用 Fenchel 间隙 \(\Psi_h(y,a)=h(y)+h^*(a)-\langle a,y\rangle\)，直接展开得
\[
M(y)-M(z)=\Psi_\phi(y,u)+\frac{\|y-z\|^2}{2\eta}. \tag{E1}
\]
若内层误差不超过 \(\sigma\)，则 \(u\in\partial_\sigma\phi(y)\)。

另一方面，
\[
F(x)-F(y)
=M(x)-M(y)+\frac{\|y-x\|^2}{2\eta}+\Psi_g(y,v).
\]
由强凸性 \(M(x)-M(z)\ge\|z-x\|^2/(2\eta)\)，得到更强的不等式
\[
\Psi_g(y,v)+\frac{\|y-x\|^2+\|z-x\|^2}{2\eta}
\le F(x)-F(y)+\sigma.
\]
舍去非负的 \(\|y-x\|^2\) 项，即题设 K1：
\[
\Psi_g(y,v)+\frac{\eta}{2}\|u-v\|^2
\le F(x)-F(y)+\sigma. \tag{E2}
\]

重复 \(K\) 步并选择实际目标下降最小的一步。目标差望远镜求和不超过 \(\Delta\)，所以输出点满足
\[
\left(
\sigma,
\frac{\Delta}{K}+\sigma,
\sqrt{\frac{2}{\eta}\left(\frac{\Delta}{K}+\sigma\right)}
\right)
\]
的 L0 证书。

### E.1 基本分量查询的内层实现

由于 \(\|u\|\le G_\phi\)、\(\|v\|\le G_g\)，有 \(\|z-x\|\le\eta B\)。在球 \(\overline{B}_{\eta B}(x)\) 上，\(M\) 的可取得次梯度范数不超过 \(2B\)，强凸参数为 \(\mu=1/\eta\)。

在该球上使用投影次梯度步骤，步长 \(\alpha_t=2/[\mu(t+1)]\)，输出按权重 \(t\) 的平均点。为完整计数，设 \(D_t=\|y_t-z\|^2\)、\(H=2B\)。投影非扩张性及强凸次梯度不等式给出
\[
M(y_t)-M(z)
\le\frac{\mu(t-1)}{4}D_t-\frac{\mu(t+1)}{4}D_{t+1}
+\frac{H^2}{\mu(t+1)}.
\]
乘以 \(t\) 并求和，距离项望远镜相消，得到
\[
\sum_{t=1}^{T}t[M(y_t)-M(z)]\le\frac{TH^2}{\mu}.
\]
由凸性，平均点 \(\bar{y}_T\) 满足
\[
M(\bar{y}_T)-M(z)\le\frac{2H^2}{\mu(T+1)}
=\frac{8\eta B^2}{T+1}. \tag{E3}
\]
每次迭代仅需一次普通分量查询，以获得 \(\phi\) 的一个次梯度；当前负侧 \(v\) 维持固定。

取
\[
\eta=\frac{\delta}{\varepsilon^2},\qquad
\sigma=\frac{\delta}{4},\qquad
K=\max\!\left\{1,\left\lceil\frac{4\Delta}{\delta}\right\rceil\right\},
\qquad
T=\left\lceil\frac{32B^2}{\varepsilon^2}\right\rceil,
\]
即可达到 \((\delta,\delta,\varepsilon)\)-L0。计入各外层端点函数值查询，总成本为
\[
O\!\left[\left(1+\frac{\Delta}{\delta}\right)
\left(1+\frac{B^2}{\varepsilon^2}\right)\right].
\]
题设主要项 \(O(\Delta B^2/(\delta\varepsilon^2))\) 在非平凡参数范围成立。这里的 \(u\) 依赖分析中的精确 \(z\)，是存在性见证；此算法没有声称显式输出该 \(u\)。

## 3. K2–K7 的文献核查

下文 [R1]–[R10] 均为论文原文或出版方页面。自行推导与文献已有结论分别标明。

### K2：Kong–Lewis

[R1] Theorem 6.6 的原文查询界是
\[
\left\lceil\frac{3(F(x^0)-\min F)}{r\varepsilon}\right\rceil
\frac{16L^2}{\varepsilon^2}
\left(1+\left\lfloor\frac{12\Lambda(r)}{\varepsilon}\right\rfloor\right).
\]
其主要项包含 \(\varepsilon^{-4}\)，不是 \(\varepsilon^{-3}\)。原文公式不宜用于解释零间隙等退化边界；本报告自己的上界保留了加一项。

Oracle 2.5 返回函数值、方向导数及方向相容向量。其抽象方向次梯度映射要求
\[
\langle G(x,e),e\rangle=F'(x;e),\qquad\|G(x,e)\|\le L,
\]
但抽象定义本身没有普遍要求 \(G(x,e)\in\partial_C F(x)\)。Proposition 2.4 说明，对于方向可微的有限维 Lipschitz 函数，可以选择属于 Clarke 次微分的这种映射。使用这一选择才能直接读成题设 L2 保证。

Proposition 6.3 给出 \(\Lambda(r)\le\operatorname{Lip}(g)\)。题设有限凸分量保证 Hadamard 方向可微。沿直线的凸函数右导数右连续，两者相减满足该文方向半光滑条件。全空间也满足 Theorem 6.6 的可行邻域条件。因此适用性上的缺口是 oracle 信息，不是题设 DC 类缺少这些正则性。

### K3：Kornowski 的指数下界

[R2] Theorem 3.1 假设
\[
r<\Delta/L,\qquad\varepsilon<L/32,\qquad
n\ge\left\lceil2\log_2\frac{L}{8\varepsilon}\right\rceil.
\]
它对一般 \(L\)-Lipschitz、初始间隙不超过 \(\Delta\) 的目标，证明确定性局部算法若要保证某个迭代点满足 L2，必须有
\[
T>\left(\frac{L}{32\varepsilon}\right)^{n/2}.
\]
“局部”在该文表示：两个目标在查询点邻域内相同，则 oracle 响应相同。它允许比一阶信息更强的响应，但不自动返回题设指定分解的两个分量。该下界不能直接移植到固定分量界的普通分量模型。

### K4：Kornowski 的最优精度下界

[R3] Theorem 3.1 针对 zero-respecting 一阶算法，包括此约束下的随机算法。其参数范围包含
\[
\varepsilon\le c\min\!\left\{L,\frac{rL^2}{\Delta},\frac{\Delta}{r}\right\},
\]
维数为 \(\Theta(\Delta L^2/(r\varepsilon^3))\)，下界为
\[
\Omega\!\left(\frac{\Delta L^2}{r\varepsilon^3}\right).
\]
该结果没有自动证明任意确定性普通分量算法的相同下界。应用前还必须建立受控 DC 分解，并证明两个分量的额外响应不破坏隐藏坐标结构。本报告没有声称完成该精度下界归约。

### K5：Jordan 等与 Tian–So

[R4] COLT 2023 Theorem 1 给出一般目标一阶模型的 \(\Omega(n)\) 下界，Theorem 2 给出仅用次梯度、无函数值时的确定性障碍。[R5] Theorem 1 加强到局部 oracle 的维数障碍，Theorem 2 排除 general zero-respecting 的统一有限时间保证。它们均不能直接忽略题设提供的额外分量信息。

[R5] Remark 3 指出其有限困难构造可以是分段线性 DC。Proposition 4 已经证明其模型中对非凸模 \(\Lambda(r)\) 的线性依赖是最优的。因此，“非凸模必须进入复杂度”不能作为本报告的新颖性主张。附录 D 的增量是固定分量常数且全部分量响应相容的直接构造；其文献新颖性仍待验证。

### K6：随机对照

对随机种子之前固定的 \((\phi,g)\)，全维绝对连续扰动几乎必然落在两个分量共同可微的位置。因此在这些查询点，任意合法 oracle 都必须返回真实梯度，且
\[
u-v=\nabla F.
\]
只在线段上随机采样不自动满足该论证；整条线可能位于不可微集合中，须使用合适的全维扰动机制。

这给出从分量 oracle 到目标梯度信息的单向模拟，不给出两个 oracle 的双向等价。普通 \(F\) 梯度信息无法重建指定的 \(\phi,g\)。

[R6] Theorems 2.4、2.6 使用这种随机扰动思想。在其停止时间/期望查询解释下，主要成本为 \(O(\Delta B^2/(r\varepsilon^3))\)；高概率固定预算版本还包含失败概率和外层次数的对数项。因此题设的 \(O(r^{-1}\varepsilon^{-3})\) 应注明固定其他参数和成功概率口径。“差距完全来自确定性”不能替代这些模型限定，也不能据此声称本报告函数类的随机精度下界已经匹配。

### K7：哪些内容能够证明

**自行推导：有限困难实例存在显式 DC 分解。** [R2] Section 4 的未缩放构造可写为
\[
\widetilde{F}(x)=\min_{1\le t\le T}h_t(x),
\]
其中
\[
h_t(x)=\min_{z\in\overline{B}_\rho(x_t)}
\left\{\langle e_1,z-x_t\rangle+\sigma_K(x-z)\right\}.
\]
这里 \(\sigma_K\) 是该文单位球面球冠的支撑函数。由于支撑函数凸且 1-Lipschitz，上式被最小化的函数关于 \((x,z)\) 联合凸；约束球是凸紧集。因此每个 \(h_t\) 都是有限凸、1-Lipschitz 函数。其凸性也可直接用两个极小点的凸组合验证。

令
\[
S=\sum_{t=1}^{T}h_t,
\qquad
Q=\max_{1\le t\le T}\sum_{j\ne t}h_j.
\]
则 \(S,Q\) 凸，\(\widetilde{F}=S-Q\)，且
\[
\operatorname{Lip}(S)\le T,
\qquad\operatorname{Lip}(Q)\le T-1.
\]
该文最终截断目标
\[
F=\max\{L\widetilde{F},-\Delta\}
\]
因而具有分解
\[
\phi=\max\{LS,LQ-\Delta\},\qquad g=LQ,
\]
满足
\[
\operatorname{Lip}(\phi)\le LT,
\qquad \operatorname{Lip}(g)\le L(T-1).
\]
这证明这些有限困难实例属于 DC 类，并说明固定分量常数不可被忽略。对该文进一步平滑的版本，分别卷积两个凸分量仍保持凸性及相同 Lipschitz 上界；正则性不会形成额外障碍。

**局部信息到方向信息。** 目标在一点的局部函数芽决定其方向导数与 Clarke 次微分。可在
\[
\{q\in\partial_C F(x):\langle q,e\rangle=F'(x;e)\}
\]
中选择唯一的最小范数元；[R1] Proposition 2.4 保证该集合非空。这个选择只依赖局部函数芽，且范数不超过 \(L\)。所以可把全部方向的这种信息视为一个合法的强局部 oracle 响应，或由理想函数芽 oracle 读取。这里没有声称用有限次普通函数值查询求出方向导数。

**量词上的结论。** 上述 DC 分解也保证 [R1] 所需正则性。因此，若整个抵抗困难族都具有统一小的 \(\Lambda(r)\)，[R1] 的方向算法就会与 [R2] 对所有局部算法的下界冲突。不存在覆盖该困难族的维数无关统一界。对专门抵抗 Kong–Lewis 算法的实例，可以进一步用其实际查询下界反推非凸模必须增长。

但此论证没有证明：任意选择的一组中心生成的每个实例，其最优 DC 分量常数都必须达到某个给定增长率。对整个困难族的统一界判断和逐实例最小分解常数，是不同量词。K7 因此标为部分结果。

## 4. 2024–2026 文献覆盖检查

| 已检查原文 | 已有内容 | 与本报告接口的差别 |
|---|---|---|
| Kong–Lewis，MOR 2024，Oracle 2.5、Proposition 2.4、Theorem 6.6 | 有非凸模控制的确定性方向算法 | 使用方向相容信息；没有给出本文普通分量纯化过程。 |
| Tian–So，MP 2024，Theorems 1–2、Proposition 4 | 局部 oracle 下界；非凸模依赖的最优性 | 没有直接提供固定分量界且可读取两分量的下界归约。 |
| Tian–So，SODA 2025，Theorem 5.8、Definition 5.1、Corollary 5.10 | 分段仿射函数的稳健驻点测试 | 明确假设额外的精确驻点测试 oracle；还使用有限表示信息。不是题设普通分量模型。 |
| Gebken，COAP 2024，Theorem 1 | 弱下半光滑情形下确定性次梯度采样二分的有限终止 | 取得的是目标的真实 Clarke 次梯度；终止论证未给本文参数的统一分量查询界。 |
| Gebken，JOTA 2025，Theorem 5.1 | 通过 Goldstein 次微分分析局部速度和增长条件 | 所检查的结果没有构造普通分量到 Clarke 信息的有限查询模拟。 |
| Diakonikolas–Guzmán，arXiv 2403.16317 v2，Theorem 4.9 | 用局部次梯度变化量细化优化复杂度 | 所检查的结果没有覆盖本文这个无附加变化模假设的确定性分量纯化定理。 |
| Kornowski，arXiv 2609.23837、2609.17780，均为 Theorem 3.1 | 一般目标局部指数下界；zero-respecting 精度下界 | 均需要检查函数类和分量信息，不能直接替代本报告的模型证明。 |

这次检查没有找到直接覆盖 B.1、C.4 与 D.1 这一组合结果的定理。此结论仅描述已检查文献；不能当作排他性的新颖性证明。有关定量近似可微性、凸次微分直径与确定性 oracle 模拟的更早文献仍应独立补查。

## 5. 自审与小规模反例检验

附带脚本 `Q3_sanity_checks.py` 使用标准库有理数算术，不使用浮点近似，也不使用随机算法。每项检验针对一个具体可能失败点。

| 检验对象 | 要检测的失败 | 实际结果 |
|---|---|---|
| H1 的共享折点例子 | 把原始分量差误当方向导数，或二分失败次数递推错误 | 线性目标上安排 7 个共享折点，对抗选择产生 7 次失败；理论上界 14 次。随后找到合法负差。 |
| 局部纯化 | 依赖极端次梯度、后处理坐标破坏先处理坐标、球不嵌套 | 二维分段仿射 DC 对分别使用平均次梯度及两个相反选择规则；均为 21 次查询，最终差集合直径为零，全部中间不等式成立。 |
| 网格与纯化衔接 | 离开线段后内积保证失效 | 321 段的例子中，最小 secant 为 -1，纯化后的方向内积仍为 -1。 |
| 隐藏二维下界 | 任意输出泄露未计入的方向、间隙或分量常数失控 | 五维、两次查询、额外独立输出的例子满足全部零响应与分离余量平方 1/2。 |
| 最小范数更新 | 分母或常数错误 | 三个有理数例子，包括内积阈值边界，均满足 (A3)。 |

这些检验不能替代证明，也没有穷尽所有实例。

量词审阅：下界先固定算法，最终一次性定义函数对；上界对任何合法次梯度选择成立。空间审阅：每次中心更新删除旧样本，避免把旧位置错误地放入新中心的 Goldstein 球。目标审阅：A 仅证明 L1；B–C 通过真实 Clarke 存在性见证证明 L2。常数审阅：下界分量界、间隙均与查询预算无关。维数审阅：纯化成本显式含 \(n\)，没有把它隐藏在常数中。

独立人工审核应首先检查三个环节：B.4 的整个小球宽度界及嵌套不变量；C.1 的两侧差商和扰动误差符号；D.1 将任意输出计入正交空间后，全部历史四元组是否仍由同一函数对实现。

## 6. 与仓库的对齐及范围

本次读取的仓库版本是 `main` 的 `3f086eab46057d885c2e36168222fa05dc4d7924`，包括 README、PROJECT_STATUS 与 `criticality.tex` 的相关范围。仓库状态仍是初稿整理后的版本。附件提到的 `overleaf/notes/project/paper-structure-2026-10-16.md` 在该版本读取返回 404；不能把附件提及但未读到的后续笔记当作已审核内容。本报告以本次上传的 Q3 prompt 为任务定义，没有修改远端仓库。

源码中的 `lem:spatial-to-value` 与第 2.2 节使用相同运输机制。但源码把假设写成“在包含 x,y 的某个凸集上 Lipschitz”，其证明直接使用全部次梯度范数有界，这个局部表述不足。反例为
\[
q(t)=\max\{t,0\},\qquad C=[-1,0],\qquad x=-1,y=0,v=1\in\partial q(0).
\]
函数在 \(C\) 上为 0-Lipschitz，却有
\[
q(x)-q(y)-v(x-y)=1>0.
\]
本报告只在 Q3 的全空间 Lipschitz 条件下使用该引理，故不存在该缺口。源码可把该版本的假设写为全局 Lipschitz；若保留局部版本，需要对所用次梯度另加适当界。

## 7. 对论文问题的判断

**可以保留的科学问题：给定一个全局分量常数受控的 DC 分解，确定性方法越过伪临界缺口，需要付出什么信息成本？**

本报告的答案是：普通分量查询足以越过这一缺口，但必须允许维数代价。L1 的维数无关性与 L2 的至少线性维数代价形成分离；局部纯化又把 L2 的确定性代价限制为多项式。固定其余参数后，上下界对维数相差一个对数因子。

这没有证明“指定某个 DCA 迭代一定能够做到”，也没有证明所有精度参数的最优阶。正面算法需要主动查询坐标邻域，并使用精确函数值维护方向保证。随机对照与普通 DCA 路径都应单独陈述，不能与此存在性算法定理混同。

真正值得独立核查的新意候选是：**普通分量 oracle 的有限查询纯化，以及它与固定分量界的维数下界共同给出的可达性边界。**

## 原始文献

[R1] Kong, W.; Lewis, A. S. *The cost of nonconvexity in deterministic nonsmooth optimization*. Mathematics of Operations Research 49(4), 2024. Oracle 2.5; Proposition 2.4; Proposition 6.3; Theorem 6.6. 原文：https://arxiv.org/html/2210.00652v2 。出版方：https://pubsonline.informs.org/doi/10.1287/moor.2022.0289 。

[R2] Kornowski, G. *The Exponential Price of Determinism in Nonsmooth Nonconvex Optimization*. arXiv:2609.23837v1, 2026. Theorem 3.1; Section 4. 原文：https://arxiv.org/html/2609.23837v1 。

[R3] Kornowski, G. *The Complexity of Finding Stationary Points in Nonsmooth Nonconvex Optimization*. arXiv:2609.17780v1, 2026. Theorem 3.1. 原文：https://arxiv.org/html/2609.17780v1 。

[R4] Jordan, M.; Kornowski, G.; Lin, T.; Shamir, O.; Zampetakis, M. *Deterministic Nonsmooth Nonconvex Optimization*. COLT 2023, PMLR 195:4570–4597. Theorems 1–2. 出版方：https://proceedings.mlr.press/v195/jordan23a.html 。

[R5] Tian, L.; So, A. M.-C. *No Dimension-Free Deterministic Algorithm Computes Approximate Stationarities of Lipschitzians*. Mathematical Programming, 2024. Theorems 1–2; Remark 3; Proposition 4. 作者原文：https://laitian.net/papers/lip_det_hard-MPA.pdf 。

[R6] Davis, D.; Drusvyatskiy, D.; Lee, Y. T.; Padmanabhan, S.; Ye, G. *A gradient sampling method with complexity guarantees for Lipschitz functions in high and low dimensions*. NeurIPS 2022. Theorems 2.4、2.6. 原文：https://arxiv.org/html/2112.06969v2 。

[R7] Tian, L.; So, A. M.-C. *Testing Approximate Stationarity Concepts for Piecewise Affine Functions*. SODA 2025. Definition 5.1; Theorem 5.8; Corollary 5.10. 原文：https://arxiv.org/html/2501.03224v1 。

[R8] Gebken, B. *A note on the convergence of deterministic gradient sampling in nonsmooth optimization*. Computational Optimization and Applications 88:151–165, 2024. Theorem 1. 出版方：https://link.springer.com/article/10.1007/s10589-024-00552-0 。

[R9] Gebken, B. *Analyzing the Speed of Convergence in Nonsmooth Optimization via the Goldstein subdifferential*. Journal of Optimization Theory and Applications, 2025. 出版方：https://link.springer.com/article/10.1007/s10957-025-02748-8 。

[R10] Diakonikolas, J.; Guzmán, C. *Optimization on a Finer Scale: Bounded Local Subgradient Variation Perspective*. arXiv:2403.16317v2. 原文：https://arxiv.org/html/2403.16317v2 。
