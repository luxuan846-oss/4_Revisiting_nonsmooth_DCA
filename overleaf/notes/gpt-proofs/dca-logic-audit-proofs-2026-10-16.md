> 来源：GPT Pro 全文逻辑核查会话（用户分享链接 chatgpt.com/share/6ad280ae-f25c-83ea-a883-fd082e8c35f7）中生成的补充证明，2026-10-16 由助手原样提取入库，仅应用该会话自身的后续修订。逐条核查表见同目录 `DCA_logic_insight_audit_2026-10-16.md`（用户上传）。尚未独立审核。

# 非光滑 DCA 全文逻辑核查：补充证明

日期：2026-10-16。

核查依据：用户上传的全文逻辑与新见解核查任务；仓库 `luxuan846-oss/4_Revisiting_nonsmooth_DCA` 中的结构稿、不可消除伪临界证明笔记和本次读取的正文源码；末尾列出的文献原文。

这些证明是本次核查补出的推导，不表示它们已经写入仓库。本文未检视当前编译 PDF 的全部页面。文献新颖性与数学正确性分开判断。

## 1. 模型与成功判据

令 \(\phi,g:\mathbb{R}^n\to\mathbb{R}\) 凸、全空间有限，分别为 \(G_\phi,G_g\)-Lipschitz。记 \(F=\phi-g\)、\(B=G_\phi+G_g\)、\(F(x^0)-\inf F\le\Delta\)。每次基本查询返回两个分量的函数值以及各一个合法次梯度。算法不能免费要求指定的极端次梯度或精确近端。

定义 \(\Psi_h(x,w)=h(x)+h^*(w)-\langle w,x\rangle\)。点输出成功是存在 \(u,v\)，满足
\[
\Psi_\phi(x,u)\le\delta_\phi,\qquad
\Psi_g(x,v)\le\delta_g,\qquad
\|u-v\|\le\varepsilon.
\]
这里采用“输出具有证书的点”，不额外要求输出全部对偶见证或计算共轭值。

## 2. 同时控制新旧两个点的主恒等式

给定 \(x\)、\(v\in\partial g(x)\)、\(\eta>0\)，令
\[
M(w)=\phi(w)-\langle v,w\rangle+\frac{\|w-x\|^2}{2\eta},\qquad
z=\arg\min_w M(w),\qquad
u=v-\frac{z-x}{\eta}.
\]
强凸性保证 \(z\) 唯一，最优性给出 \(u\in\partial\phi(z)\)。实际内层输出 \(y\)，满足
\[
e=M(y)-M(z)\le\sigma.
\]
Fenchel 等式及平方展开给出
\[
e=\phi(y)-\phi(z)-\langle u,y-z\rangle+\frac{\|y-z\|^2}{2\eta}
=\Psi_\phi(y,u)+\frac{\|y-z\|^2}{2\eta}. \tag{2.1}
\]
另一方面，分别有
\[
M(x)-M(z)=\Psi_\phi(x,u)+\frac{\|z-x\|^2}{2\eta},
\]
\[
F(x)-F(y)=M(x)-M(y)+\frac{\|y-x\|^2}{2\eta}+\Psi_g(y,v).
\]
相加得到更强的精确恒等式
\[
\boxed{
F(x)-F(y)+e=
\Psi_\phi(x,u)+\Psi_g(y,v)
+\frac{\|z-x\|^2+\|y-x\|^2}{2\eta}.
}\tag{2.2}
\]
因此，在新点 \(y\) 有
\[
\Psi_\phi(y,u)\le\sigma,\qquad
\Psi_g(y,v)+\frac{\eta}{2}\|u-v\|^2\le F(x)-F(y)+\sigma. \tag{2.3}
\]
在旧点 \(x\) 则有
\[
\boxed{
\Psi_g(x,v)=0,\qquad
\Psi_\phi(x,u)+\frac{\eta}{2}\|u-v\|^2\le F(x)-F(y)+\sigma.
}\tag{2.4}
\]
这说明负侧零容差没有额外的精度指数成本。

### 2.1 确定性输出与总查询成本

重复 \(K\ge1\) 步，记 \(D_k=F(x^k)-F(x^{k+1})\)，选择可观察的
\[
k_*\in\arg\min_{0\le k<K}D_k.
\]
望远镜求和给出 \(D_{k_*}\le\Delta/K\)，无需每步单调。令 \(q_K=\Delta/K+\sigma\)。新点具有
\[
\left(\sigma,q_K,\sqrt{2q_K/\eta}\right)\text{-VAC},
\]
旧点具有
\[
\left(q_K,0,\sqrt{2q_K/\eta}\right)\text{-VAC}.
\]
选取
\[
\eta=\delta/\varepsilon^2,\qquad \sigma=\delta/4,\qquad
K=\max\{1,\lceil4\Delta/\delta\rceil\},
\]
则旧点为 \((\delta/2,0,\varepsilon)\)-VAC，故也是 \((\delta,0,\varepsilon)\)-VAC。

由 \(u\in\partial\phi(z)\) 及 \(v\in\partial g(x)\) 得到 \(\|z-x\|\le\eta B\)。在球 \(Q=\overline B_{\eta B}(x)\) 上求解 \(M\)，其每个次梯度范数不超过 \(2B\)，强凸参数为 \(\mu=1/\eta\)。

采用投影次梯度法：\(w_1=x\)，对 \(t=1,\ldots,T\)，取 \(s_t\in\partial M(w_t)\)，执行
\[
w_{t+1}=\Pi_Q\!\left(w_t-\frac{2}{\mu(t+1)}s_t\right),\qquad
\bar w_T=\frac{2}{T(T+1)}\sum_{t=1}^{T}t w_t.
\]
记 \(a_t=\|w_t-z\|^2\)、\(L_M=2B\)。投影不扩张性与强凸次梯度不等式给出
\[
M(w_t)-M(z)\le\frac{\mu}{4}\bigl((t-1)a_t-(t+1)a_{t+1}\bigr)+\frac{L_M^2}{\mu(t+1)}.
\]
乘以 \(t\) 后求和，平方项望远镜抵消；由凸性，
\[
M(\bar w_T)-M(z)\le\frac{2L_M^2}{\mu(T+1)}
=\frac{8\eta B^2}{T+1}.
\]
故每个内层需要 \(O(1+\eta B^2/\sigma)\) 次基本查询。总体为
\[
\boxed{O\!\left((1+\Delta/\delta)(1+B^2/\varepsilon^2)\right)}. \tag{2.5}
\]
在 \(\delta\le\Delta\)、\(\varepsilon\le B\) 的精度区间，简化为
\[
O\!\left(\Delta B^2/(\delta\varepsilon^2)\right).
\]
算法可实际计算输出点和 \(v^{k_*}\)。上面的 \(u\) 依赖分析中的精确近端点，因此不是已输出的显式向量。显式对偶见证输出是另一个需要注明的接口要求。

## 3. Moreau 校准及其反向限制

假设 \(g\) 凸且梯度全局 \(\rho\)-Lipschitz，其中 \(\rho>0\)。于是 \(F\) 为 \(\rho\)-弱凸函数。取
\[
p=\arg\min_y\{F(y)+\rho\|y-x\|^2\},\qquad d=x-p.
\]
设 \(x\) 为 \((\delta_\phi,\delta_g,\varepsilon)\)-VAC，见证为 \(u,v\)。光滑凸函数的 Fenchel 间隙满足
\[
\Psi_g(x,v)\ge\frac{\|v-\nabla g(x)\|^2}{2\rho},
\]
因此，令 \(b=\varepsilon+\sqrt{2\rho\delta_g}\)，则 \(\|u-\nabla g(x)\|\le b\)。

近端最优性给出
\[
t:=2\rho d+\nabla g(p)\in\partial\phi(p).
\]
将 \(u\in\partial_{\delta_\phi}\phi(x)\) 与 \(t\in\partial\phi(p)\) 的支撑不等式相加，得到
\[
\langle u-t,x-p\rangle\ge-\delta_\phi.
\]
由梯度 Lipschitz 性，
\[
2\rho\|d\|^2\le b\|d\|+\rho\|d\|^2+\delta_\phi.
\]
求解二次不等式，利用 \(\nabla F_{1/(2\rho)}(x)=2\rho d\)，得到
\[
\boxed{
\|\nabla F_{1/(2\rho)}(x)\|
\le b+\sqrt{b^2+4\rho\delta_\phi}.
}\tag{3.1}
\]

反向令 \(\kappa=\|\nabla F_{1/(2\rho)}(x)\|\)。在近端点 \(p\)，有精确分量见证及残差 \(\kappa\)。将正侧见证搬到旧点 \(x\)，令
\[
u=2\rho(x-p)+\nabla g(p),\qquad v=\nabla g(x),
\]
则
\[
\Psi_\phi(x,u)\le2G_\phi\|x-p\|=G_\phi\kappa/\rho,
\quad \Psi_g(x,v)=0,
\quad\|u-v\|\le3\kappa/2.
\]
故得到 \((G_\phi\kappa/\rho,0,3\kappa/2)\)-VAC。

不能无条件把旧点的正侧误差改善为 \(O(\kappa^2)\)。取 \(\phi(t)=|t|\)、\(g=0\)、\(\rho=1\)、\(x=\kappa/2\)，则 Moreau 梯度范数恰为 \(\kappa\)。对任何 \(|u|\le C\kappa\)，
\[
\Psi_\phi(x,u)=x(1-u)\ge\frac{\kappa}{2}(1-C\kappa).
\]
因此同点正侧误差至少为 \(\Omega(\kappa)\)。

## 4. 一维：Jordan 分解保留原有分量界

给定原分解 \(F=\phi_0-g_0\)，其中两个分量全局 Lipschitz。用分布二阶导数表示曲率测度：
\[
\mu=D^2F=D^2\phi_0-D^2g_0=\mu_+-\mu_-.
\]
\(\mu_+,\mu_-\) 是互相奇异的非负有限测度，且
\[
\mu_+\le D^2\phi_0,\qquad \mu_-\le D^2g_0.
\]
于是公共曲率测度
\[
\nu=D^2\phi_0-\mu_+=D^2g_0-\mu_-\ge0.
\]
选择凸函数 \(H\)，满足 \(D^2H=\nu\) 和 \(H'(-\infty)=0\)。令 \(\phi=\phi_0-H\)、\(g=g_0-H\)。它们仍凸，而且 \(\phi-g=F\)。

令 \(a_-\) 是 \(\phi_0\) 在负无穷的导数极限。新正侧的导数从 \(a_-\) 出发，只积累 \(\mu_+\)，因此其导数范围包含于原正侧导数范围。负侧相同。故
\[
\operatorname{Lip}(\phi)\le G_\phi,\qquad
\operatorname{Lip}(g)\le G_g.
\]
由于 \(\mu_+\) 与 \(\mu_-\) 互相奇异，在任何一点，两侧不能同时具有正的跳跃原子。故至多一侧在该点有非单点次微分，并且
\[
\boxed{
\partial\phi(x)-\partial g(x)
=[\min\{F'_-(x),F'_+(x)\},\max\{F'_-(x),F'_+(x)\}]
=\partial_C F(x),\qquad \forall x\in\mathbb{R}.
}\tag{4.1}
\]
连续变差与奇异连续变差不造成额外例外。这是存在性的规范分解结论，不提供普通分量 oracle 下的有限查询构造。

## 5. 二维及更高维：F0 的所有分解与既有几何判据

令
\[
T=\operatorname{conv}\{0,e_1,e_2\},\qquad
F_0=\sigma_T-\sigma_{-T}
=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\}.
\]
直接划分线性区域可得
\[
C:=\partial_C F_0(0)=\operatorname{conv}\{e_1,e_2,e_1+e_2\},
\qquad \operatorname{dist}(0,C)=1/\sqrt{2}.
\]

### 5.1 由 Bauer 判据得到更强结论

既有文献：Bauer 的约化多面体对判据，见 Grzybowski–Urbański [GU] 的 Theorem 5.5。这里“约化”意为：同一支撑函数差的任何凸集对，均可通过给该对的两个集合同时加入一个公共紧凸集得到。判据是：两个多面体不存在同一法向下同时暴露的平行边。

\(T\) 的边外法向为 \(-e_1,-e_2,(e_1+e_2)/\sqrt{2}\)，\(-T\) 的相应法向为其相反数，两个列表不相交。因此 \((T,-T)\) 为约化对。

对任意全空间有限凸分解 \(F_0=\phi-g\)，令 \(A=\partial\phi(0)\)、\(B=\partial g(0)\)。方向导数给出 \(\sigma_A-\sigma_B=\sigma_T-\sigma_{-T}\)，故存在紧凸集 \(K\)，使
\[
\boxed{A=T+K,\qquad B=-T+K.}\tag{5.1}
\]
因 \(0\in T\cap(-T)\)，有 \(K\subseteq A\cap B\)，于是每一种分解都在原点 DC 临界。同时
\[
A-B=2T+(K-K)\supseteq2T.
\]
因此不只是临界性失真，完整集合也存在定量失真：
\[
\inf_{F_0=\phi-g}d_H(\partial\phi(0)-\partial g(0),C)=1.
\]
下界来自 \(2e_1\in A-B\) 到 \(C\) 的距离；取规范多面体分解即可达到等号。

该证明是对既有几何定理的应用。不能据此宣称发现了新的极小对几何定理；“任何分解下的伪临界”这一优化表述的既有出处仍需要区分与核查。

将 \(T,-T\) 嵌入 \(\mathbb{R}^n\)，\(n\ge2\)，仍没有同一法向的平行暴露边。Bauer 判据继续适用。因此同样的所有分解结论适用于 \(F_0(x_1,x_2)\) 的高维嵌入。

### 5.2 原笔记的曲率与宽度证明

二维支撑函数 \(h(\theta)=\sigma_B((\cos\theta,\sin\theta))\) 满足 \(h+h''\ge0\) 的测度条件。若 \(d_0=(\cos\theta_0,\sin\theta_0)\)、\(t_0=(-\sin\theta_0,\cos\theta_0)\)，则
\[
h'_+(\theta_0)-h'_-(\theta_0)
=\max_{b\in B(d_0)}\langle b,t_0\rangle
-\min_{b\in B(d_0)}\langle b,t_0\rangle.
\]
由于 \(B(d_0)\) 是一条暴露线段或单点，右侧恰为该面的长度。连续函数项 \(h\,d\theta\) 不产生原子，所以它也等于测度 \(h+h''\) 的对应原子质量。

\(F_0\) 在三个法向 \(e_1,e_2,-(e_1+e_2)/\sqrt{2}\) 的负原子大小为 \(1,1,\sqrt{2}\)。因此 \(B\) 必须分别具有相应最小长度的面。对 \(d=(a,b)\)，各面在 \(d\) 方向上的投影长度给出
\[
w_B(d)\ge\max\{|a|,|b|,|a-b|\}\ge-F_0(d).
\]
于是 \(\sigma_{A-B}(d)=F_0(d)+w_B(d)\ge0\)，从支撑函数的分离刻画得到 \(0\in A-B\)。

### 5.3 全局版本和算法含义

令
\[
\widehat F(x)=F_0(x_1,x_2)+3\max\{\|x\|-1,0\}.
\]
由于 \(F_0\) 的 Lipschitz 常数为 \(\sqrt{2}\)，\(\widehat F\) 下有界且向无穷增长。自然分解分量的 Lipschitz 常数不超过 \(4,1\)。原点附近的方向导数与 Clarke 次微分不变。

对每一个 \(r\in(0,1)\)，
\[
\partial_r^G\widehat F(0)=C,
\qquad \operatorname{dist}(0,\partial_r^G\widehat F(0))=1/\sqrt{2}.
\]
然而，对所有凸分解，原点既满足零误差 VAC，也满足零残差的同点配对 Goldstein 条件。

对每一种分解，选择任一 \(v\in\partial\phi(0)\cap\partial g(0)\)，原点就是精确 DCA 子问题的一个极小点。若采用近端 DCA，原点还是相应强凸子问题的唯一极小点。故存在合法次梯度选择，使算法持续输出原点；与此同时 \(\widehat F'(0;-e_1)=-1\)。这不是“每一种次梯度选择都会产生恒定轨迹”。

### 5.4 高维可检验充分条件及一般性限制

对任意多面体 \(P,Q\)，若它们没有同一法向下的平行暴露边，则它们为约化对。对方向模型 \(p=\sigma_P-\sigma_Q\)，任意表示均形如 \((P+K,Q+K)\)。因此
\[
\text{每个支撑函数表示都临界}\quad\Longleftrightarrow\quad P\cap Q\ne\varnothing.
\]
若再有 \(0\notin\partial_C p(0)\)，即得不可消除伪临界。这是来自既有几何判据的可检验推论。

对一般 DC 目标，“所有实际分解”与“方向导数的所有形式拟微分对”并非定义上相同。任意实际分解产生一个形式对；反方向需要把形式对实现为该目标的局部或全局分解。在正齐次目标上，支撑函数直接提供实现，因此可利用 [GU] Theorem 7.1 的极小子对存在性，证明“所有形式对临界”等价于“所有极小形式对临界”。没有实现论证时，不应把这一等价直接移用于一般目标。

## 6. 固定分量界下的确定性下界

以下使用 Li–Pan [LP] 的未缩放困难目标 \(\bar F\) 和其坐标层级。它们满足 \(N\ge60\)、\(2\le M\le N/12\)、\(\operatorname{Lip}(\bar F)\le1\)、初始间隙不超过 \(3M/N\)，以及深度至少 \(MN/120\) 的完整次微分隐藏性质。

### 6.1 全局凸化

令 \(q(s)=0\) 对 \(s\le0\)，\(q(s)=3s^2-2s^3\) 对 \(0<s<1\)，\(q(s)=1\) 对 \(s\ge1\)。使用任务中的
\[
c_N(t)=\begin{cases}
0,&t\le0,\\
\frac{3}{8}t^2-\frac{N}{16}t^3,&0<t<2/N,\\
\frac{3}{4N}t-\frac{1}{2N^2},&t\ge2/N.
\end{cases}
\]
它为凸的 \(C^1\) 函数，并有
\[
0\le c_N'(t)\le3/(4N),\qquad
c_N''(t)=\begin{cases}3/4-3Nt/8,&0<t<2/N,\\0,&\text{其他区间},\end{cases}
\]
后二阶导数公式按几乎处处解释，梯度的全局 Lipschitz 常数为 \(3/4\)。

设 \(C_N(z)=\sum_{m,j}c_N(z_j^m)\)、\(\bar g=C_N\)、\(\bar\phi=\bar F+C_N\)。

利用
\[
\|[\sigma]_+\|=\max_{\alpha\ge0,\|\alpha\|\le1}\langle\alpha,\sigma\rangle,
\]
可把 \(\bar F+C_N\) 表示为凸分段线性项与以下可分离项之和的逐点上确界：
\[
h_\theta(t)=c_N(t)-\frac{2\theta}{N^2}q(Nt/4),\qquad 0\le\theta\le1.
\]
这里 \(\theta=1-\alpha_{m+1}\)，末块取 \(\alpha_{M+1}=0\)。因此只需检查 \(h_\theta\) 凸。

在 \(0<t<2/N\)，
\[
h_\theta''(t)=(1-\theta)c_N''(t)\ge0.
\]
在 \(2/N<t<4/N\)，\(q''(Nt/4)\le0\)，所以 \(h_\theta''\ge0\)。在其余区间二阶导数为零。拼接点处函数与一阶导数连续。故每个 \(h_\theta\) 在整条实线上凸，进而 \(\bar\phi\) 全局凸。这也处理了负坐标、拼接点和相邻块的耦合。

分量界为
\[
\operatorname{Lip}(\bar g)\le\frac{3}{4}\sqrt{M/N},\qquad
\operatorname{Lip}(\bar\phi)\le1+\frac{3}{4}\sqrt{M/N}.
\]
因此所有实例都属于固定类 \(\mathcal{D}(2,1,1)\)。

### 6.2 两个完整次微分的抵抗 oracle

有
\[
\partial\bar g(z)=\{\nabla C_N(z)\},\qquad
\partial\bar\phi(z)=\partial\bar F(z)+\nabla C_N(z).
\]
因为 \(c_N(0)=c_N'(0)=0\)，\(\nabla C_N(z)\) 的支持包含于 \(z\) 的支持，且未显露坐标不贡献函数值。

给定任意有限预算的确定性算法，在增大的环境维数中构造正交列向量。每轮只为已显露坐标固定列向量；对当前查询 \(x^t\)，令已固定坐标 \(z_i^t=\langle u_i,x^t\rangle\)，其他坐标设为零。返回两个函数值及两个完整次微分的已固定旋转。凡本轮首次显露的列，选为与历史及当前查询、既有列均正交的方向。

这样保持三个不变量：

1. 每个历史查询在尚未固定列上的坐标均为零。
2. 两个历史分量值在后续补全旋转时均不改变。
3. 两个历史完整次微分在后续补全旋转时均不改变。

最后补全一个固定正交嵌入，得到与全部历史响应一致的固定函数对。新增 \(\nabla C_N\) 不推进层级，故 [LP] 的层级下界继续有效。任意非查询输出可追加为一次查询，得到相同渐近下界。这里必须同时保存两个函数值和两个完整次微分；仅证明差值 oracle 一致不够。

### 6.3 Moreau 归约及参数选择

\(\nabla\bar g\) 实际为 \(3/4\)-Lipschitz，因而也为 \(1\)-Lipschitz。校准时取 \(\rho=1\)，即可直接对齐 [LP] 的 Moreau 参数 \(1/2\)。

若 \(x\) 是 \((\varepsilon^2,\varepsilon^2,\varepsilon)\)-VAC，则第 3 节给出
\[
\|\nabla\bar F_{1/2}(x)\|\le C_*\varepsilon,
\quad C_*=(1+\sqrt{2})+\sqrt{(1+\sqrt{2})^2+4}.
\]
而 [LP] 困难层级中的所有可达点都满足 \(\|\nabla\bar F_{1/2}(x)\|>1/(8\sqrt N)\)。选定足够小的绝对常数 \(c>0\)，令
\[
N=\lfloor c\varepsilon^{-2}\rfloor,\qquad M=\lfloor N/12\rfloor,
\]
使 \(C_*\varepsilon<1/(8\sqrt N)\)。当精度足够小时，\(N\ge60\)、\(M\ge2\)，并且
\[
H\ge MN/120=\Omega(\varepsilon^{-4}).
\]
所以，在固定类 \(\mathcal{D}(2,1,1)\) 上，任意确定性算法的平衡 VAC 查询复杂度为 \(\Omega(\varepsilon^{-4})\)，即使每次返回两个完整次微分。更强的成功目标 \((\varepsilon^2,0,\varepsilon)\)-VAC 继承该下界。结合第 2 节，两种目标的确定性复杂度均为 \(\Theta(\varepsilon^{-4})\)。

这是固定正常数、随精度增长维数的结论。它没有证明随机化下界，也没有证明所有独立参数的最优依赖。下界实例位于弱凸子类；上界允许非弱凸 DC 目标。两者仍然构成同一 DC 类上的有效 minimax 匹配。

## 7. 不可达性与必要量词

Kornowski–Shamir [KS] Theorem 5 给出一维凸 1-Lipschitz 困难族。对任意有限预算与随机一阶算法，都不能在整个族上保证以固定成功概率产生同点小次梯度点。

取
\[
\phi_q(x,y)=q(x)+|y|+|y-1|,\qquad
 g_q(x,y)=|y-1|.
\]
任意正侧次梯度的第一坐标属于 \(\partial q(x)\)，任意负侧次梯度第一坐标为零，故
\[
\operatorname{dist}(\partial\phi_q(x,y),\partial g_q(x,y))
\ge\operatorname{dist}(0,\partial q(x)).
\]
分量界不超过 \(\sqrt5,1\)，每次成对查询仅需一次 \(q\) 查询。归约保持原有确定性及随机成功概率量词。困难实例可以依赖算法和预算；不能交换为一个实例同时击败所有算法或所有预算。

对 \(g=0\)，\(\partial_\delta g(x)=\{0\}\) 对任意有限 \(\delta\ge0\) 成立，因此 \(\delta_\phi=0\) 的 VAC 目标继承上述障碍。每个固定 \(\delta_\phi>0\) 都可用第 2 节算法达到，所以“\(\delta_\phi\to0\) 也不可达”应替换为“零容差端点无统一有限查询保证”。

## 8. Q3 的蕴含与限定

定义
\[
S_r^{\mathrm{pair}}(x)=\operatorname{conv}\bigcup_{y\in\overline B_r(x)}(\partial\phi(y)-\partial g(y)).
\]
Clarke 次微分和差法则给出 \(\partial_C F(y)\subseteq\partial\phi(y)-\partial g(y)\)，所以 L2 推出 L1。

若 L1 由 \(\sum_i\lambda_i(u_i-v_i)\) 见证，\(u_i\in\partial\phi(y_i)\)、\(v_i\in\partial g(y_i)\)、\(\|y_i-x\|\le r\)，则
\[
\Psi_\phi(x,u_i)\le2G_\phi r,\qquad
\Psi_g(x,v_i)\le2G_g r.
\]
由共轭函数的凸性，\(u=\sum_i\lambda_i u_i\)、\(v=\sum_i\lambda_i v_i\) 见证
\[
\mathrm{L1}(r,\varepsilon)\Longrightarrow
\mathrm{VAC}(2G_\phi r,2G_g r,\varepsilon).
\]
第 5 节给出了 L1 与 L2 的定量分离。

Kong–Lewis [KL] Theorem 6.6 的方向 oracle 上界为
\[
\left\lceil\frac{3\Delta}{r\varepsilon}\right\rceil
\frac{16L^2}{\varepsilon^2}
\left(1+\left\lfloor\frac{12\Lambda(r)}{\varepsilon}\right\rfloor\right),
\]
其中 [KL] Proposition 6.3 在 DC 情形给出 \(\Lambda(r)\le G_g\)。方向 oracle 要返回方向导数及与该方向相容的 Clarke 次梯度，普通任意分量次梯度不直接提供这种能力。

Kornowski [KE] 的最强局部信息下界覆盖该方向信息接口。因此，对满足方向可微等假设的困难族，不能同时拥有足以使上述上界为多项式的统一非凸模控制。该论证不排除每个具体困难实例属于某个大常数 DC 类，也不证明其非凸模为无穷。它没有解决普通分量 oracle 下的 L1/L2 可达性。

## 9. 需要修正的两项全局背景

第一，固定全局分量 Lipschitz 界的 DC 类并不包含全部全局 Lipschitz 弱凸函数。例如 \(F(t)=\sin t\) 为 1-Lipschitz、1-弱凸且下有界；若它可写为两个全局 Lipschitz 凸函数之差，其导数 \(\cos t\) 就应在整条实线上具有有限总变差，与事实矛盾。因此应说“允许非弱凸目标的结构类”，不应画成包含所有弱凸函数的嵌套关系。

第二，当前读取的 `overleaf/sections/deterministic_dca.tex` 仍同时要求全空间强凸与全局有界次梯度。在全空间有限值设定下不相容。若 \(g\) 为 \(\gamma\)-强凸，\(v_0\in\partial g(0)\)，则 \(\|v_x\|\ge\gamma\|x\|-\|v_0\|\)。应把二次项仅放入近端子问题，保持原分量不变。

## 10. 文献定位与核查边界

- [LP] Li–Pan, *Optimal Deterministic Oracle Complexity for Weakly Convex Optimization*, arXiv:2608.03246v1. 正式 PDF Theorem 3.2 为一般确定性下界；Remark 3.1 处理任意输出；Remark 3.2 转述 Tian–So 2021 的预算依赖弱凸模；Section 6 为抵抗 oracle。
- [KS] Kornowski–Shamir, *On the Complexity of Finding Small Subgradients in Nonsmooth Optimization*, arXiv:2209.10346. Theorem 5 为一维凸不可达性；其空间容差下界为根号对数级。
- [KL] Kong–Lewis, *The cost of nonconvexity in deterministic nonsmooth optimization*, arXiv:2210.00652v2 / Mathematics of Operations Research. Proposition 2.4、Oracle 2.5、Proposition 6.3、Theorem 6.6。
- [KE] Kornowski, *The Exponential Price of Determinism in Nonsmooth Nonconvex Optimization*, arXiv:2609.23837v1. Theorem 3.1：一般 Lipschitz 类、确定性局部算法、Goldstein 目标，指数维数下界。
- [KZ] Kornowski, arXiv:2609.17780. Theorem 3.1：zero-respecting 算法的 Goldstein 下界，包含随机算法。不得未经额外归约升级为所有确定性算法。
- [GU] Grzybowski–Urbański, *Minimal Pairs of Convex Sets Which Share a Recession Cone*, SIAM Journal on Optimization 32(2), 1049–1068, 2022; arXiv:2012.06536. 本报告定理编号按所读取 arXiv PDF：Theorem 5.5 为 Bauer 判据，Theorem 7.1 为极小子对存在性，Theorem 7.2 为平面极小对平移唯一性。Theorem 6.1 关联 Hartman 最小函数表示与凸集表示。
- Ch. Bauer, *Minimal and reduced pairs of convex bodies*, Geometriae Dedicata 62, 179–192, 1996. 本次判据依据 [GU] 正文完整转述，不冒充已读 Bauer 原始付费全文。
- Scholtes, *Minimal pairs of convex bodies in two dimensions*, Mathematika 39(2), 267–273, 1992. 本次查阅出版页与 [GU] 的对应定理转述；未获得原全文。
- Faust–Fawzi–Saunderson, *A Bregman Divergence View on the Difference-of-Convex Algorithm*, AISTATS 2023, PMLR 206, 3427–3439. Theorem 5 及其证明已有双 Bregman 下降分解；运行假设要求负侧可微，计数为精确 DCA 更新。
- DCA-PAGE: Nguyen et al., *Improved Rates for Stochastic Variance-Reduced Difference-of-Convex Algorithms*, arXiv:2509.11657v1. Definition 12 正是旧点负侧见证在新点的正侧间隙，精确 DCA 下恒零。
- MDCA: *Stochastic Difference-of-Convex Optimization with Momentum*, arXiv:2510.17503v2. Remark 1 已公开给出上述 gap 批评和二次例子；Lemma 3 区分固定点残差与同点临界距离。该批评不应列作本项目首次发现。
- Zhang–Yamada, *An Inexact Proximal Linearized DC Algorithm with Provably Terminating Inner Loop*, arXiv:2305.06520; Optimization, online 2024, volume publication 2025. Algorithm 2 式 (10) 与 (12) 已同时使用两侧 epsilon 次微分和向量距离，但分属新旧点。Theorem 4.5 为内层有限终止，Theorem 4.7 为聚点临界性。本次未找到该文给出本项目固定类上的完整 minimax 查询界。
- Tian–So, *Testing Approximate Stationarity Concepts for Piecewise Affine Functions*, arXiv:2501.03224v1 / SODA 2025. Theorem 4.11 为指定多面体分解的 Clarke 和差规则精确性；Corollary 3.6 为判断给定 DC 临界点是否 Clarke 驻点的计算困难性。它们与“所有分解”量词不同。

未完成原文定理级核查的项目：Tian–So 2021 BFOM 工作坊论文的公开 Drive PDF 未成功读取；Tian–So 2024 的原定理与接口逐项核对；任务中未具体指定的 Moudafi、Yao 文献；Sun、Xu、de Oliveira–Tcheou 的全部原定理，以及 InmBDCA 的三参数证书比较。tPLDCA 对部分旧工作的讨论仅用作线索。对这些项目，报告不作“已有覆盖”或“首次”判断。未检索到同一表述不等于已证明新颖性。
