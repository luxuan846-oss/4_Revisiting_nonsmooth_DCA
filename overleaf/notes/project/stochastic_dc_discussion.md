# 随机 DC 优化讨论稿

## 共同二次移位、统一临界性证书、Gap 函数、MVR 的 $\varepsilon^{-3}$ 与平滑化参数 $\gamma$

> 文档性质：研究讨论稿  
> 目的：完整整理当前关于 MDCA、DCA-PAGE、单循环随机 proximal-**subgradient** 方法、统一临界性证书和 Moreau 平滑化的讨论。  
> 状态说明：文中区分“已经由代数直接得到的结论”“可以从现有论文定理读出的结论”和“需要进一步正式证明的目标结果”。  
> 记号约定：所有函数默认定义在有限维欧氏空间；$\partial$ 表示凸次微分；$\operatorname{prox}$ 表示凸函数的邻近映射。

---

# 0. 核心结论

当前讨论可以概括为以下九个结论，但后文会完整展开每一步推导。

1. **共同二次移位后的精确 DCA，等价于原始 DC 分解上的精确 proximal DCA。**

   若
   $$
   F=A-B
   $$
   并同时加入
   $$
   \frac{\lambda}{2}\|x\|^2,
   $$
   则 shifted DCA 子问题等价于
   $$
   \min_x\left\{
   A(x)-\langle b^t,x\rangle
   +\frac{\lambda}{2}\|x-x^t\|^2
   \right\},
   \qquad b^t\in\partial B(x^t).
   $$

2. **精确 proximal DCA 与单步 proximal-gradient 不是同一个算法。**

   精确 proximal DCA 对整个凸侧 $A=f+h$ 求解邻近子问题；单步 proximal-gradient 还会把 $f$ 在当前点线性化。只有在二次移位等特殊分解下，两者才可能重合。

3. **统一证书的第三个残差槽是否为零，取决于用哪个 DC 分解报告证书。**

   对原始分解，显式 proximal 项通常产生
   $$
   \varepsilon=\frac{\|x^{t+1}-x^t\|}{\gamma}.
   $$
   对加入共同二次项后的 shifted 分解，同一个算法步可以写成
   $$
   \left(0,\delta_g+\frac{\|x^{t+1}-x^t\|^2}{2\gamma},0\right)
   $$
   的证书。误差从向量残差槽转移到了函数值松弛槽。

4. **MDCA/DCA-PAGE 的 lagged gap 在确定性精确 DCA 中每一步都为零。**

   随机情形下它不一定为零，因为算法用随机估计器构造子问题，而 gap 使用真实梯度构造参考子问题。因此，该 gap 主要测量随机子问题与真实子问题之间的不一致。

5. **该 lagged gap 不是完整的同点 DC 临界性度量。**

   它只控制正侧的 Fenchel–Young gap。负侧次梯度仍然位于前一迭代点，必须额外控制一个 transported Fenchel gap，才能得到完整的同点证书。

6. **对于直接模型**
   $$
   F(x)=f(x)+h(x)-g(x),
   $$
   **单步随机 proximal-gradient/subgradient 更新可以得到一个干净的统一证书：**
   $$
   \delta_\phi=0,
   \qquad
   \mathbb E\delta_g
   \le
   \frac{\Delta_0}{K}+\frac{\eta}{2}\bar V,
   $$
   $$
   \mathbb E\|u-v\|^2
   \lesssim
   \frac{\Delta_0}{\eta K}+\bar V.
   $$

7. **普通独立随机梯度在常数批量下只能给出 $\varepsilon^{-4}$；MVR/STORM 型递归估计器可以给出常数批量的 $\varepsilon^{-3}$。**

   关键参数平衡是
   $$
   \eta^2L_f^2\lesssim \alpha b,
   \qquad
   \frac{\alpha\sigma^2}{b}\lesssim\varepsilon^2,
   \qquad
   \frac{\Delta_0}{\eta K}\lesssim\varepsilon^2.
   $$

8. **MDCA Algorithm 1 的 critical-distance $\varepsilon^{-3}$ 是有意义的同点结果，但依赖光滑 $r_2$ 和精确凸子问题 oracle。**

   MDCA/DCA-PAGE 的 gap-based $\varepsilon^{-3}$ 不能直接解释为完整的非光滑同点临界性复杂度。

9. **S-MDCA 的固定-$\gamma$ $\varepsilon^{-4}$ 只是平滑代理目标 $F_\gamma$ 的复杂度。**

   若要得到原问题的精度，必须显式跟踪 $\gamma$。统一证书显示，固定 $\gamma$ 会留下 $O(\gamma)$ 量级的函数值松弛；因此 $\gamma$ 不能在端到端复杂度中被无条件视为常数。

---

# 1. 基本问题、记号与统一临界性证书

## 1.1 一般 DC 模型

考虑

$$
F(x)=A(x)-B(x),
$$

其中 $A,B$ 为 proper、closed、convex 函数。

在 MDCA 与 DCA-PAGE 的记号中，

$$
A=G+r_1,
\qquad
B=H+r_2.
$$

在我们更直接的复合模型中，

$$
A=\phi=f+h,
\qquad
B=g,
$$

其中：

- $f$ 是光滑凸函数，通常通过随机梯度访问；
- $h$ 是非光滑凸函数，但 $\operatorname{prox}_{\eta h}$ 可计算；
- $g$ 是凸函数，可以是非光滑函数；
- 目标函数 $F=f+h-g$ 一般非凸且非光滑。

## 1.2 $\varepsilon$-次微分与 Fenchel–Young gap

对凸函数 $q$，定义

$$
v\in\partial_\delta q(x)
$$

当且仅当

$$
q(y)\ge q(x)+\langle v,y-x\rangle-\delta,
\qquad
\forall y.
$$

当 $\delta=0$ 时，退化为标准凸次微分。

定义 Fenchel–Young gap

$$
\Phi_q(x,v)
:=
q(x)+q^*(v)-\langle v,x\rangle.
$$

由 Fenchel–Young 不等式，

$$
\Phi_q(x,v)\ge 0.
$$

并且

$$
v\in\partial_\delta q(x)
\quad\Longleftrightarrow\quad
\Phi_q(x,v)\le\delta.
$$

因此，$\Phi_q(x,v)$ 精确量化了向量 $v$ 偏离 $\partial q(x)$ 的函数值误差。

## 1.3 统一的同点临界性证书

对

$$
F=\phi-g,
$$

称 $x$ 为一个

$$
(\delta_\phi,\delta_g,\varepsilon)\text{-critical point},
$$

若存在向量 $u,v$ 满足

$$
u\in\partial_{\delta_\phi}\phi(x),
\qquad
v\in\partial_{\delta_g}g(x),
\qquad
\|u-v\|\le\varepsilon.
$$

三个槽分别表示：

1. $\delta_\phi$：正侧凸函数的函数值松弛；
2. $\delta_g$：负侧凸函数的函数值松弛；
3. $\varepsilon$：两个近似次梯度之间的向量不匹配。

当三者均为零时，

$$
u=v\in\partial\phi(x)\cap\partial g(x),
$$

所以 $x$ 是标准 DC 临界点。

这个定义的关键要求是：**两个近似次梯度必须被解释在同一个点 $x$ 上。**

---

# 2. 共同二次移位与 proximal DCA 的精确等价

## 2.1 共同二次移位

从

$$
F=A-B
$$

出发，对任意 $\lambda>0$，定义

$$
A_\lambda(x)
=
A(x)+\frac{\lambda}{2}\|x\|^2,
$$

$$
B_\lambda(x)
=
B(x)+\frac{\lambda}{2}\|x\|^2.
$$

显然

$$
A_\lambda(x)-B_\lambda(x)=A(x)-B(x)=F(x).
$$

因此，共同二次移位不改变目标函数，只改变 DC 分解。

## 2.2 shifted DCA 子问题

设

$$
b^t\in\partial B(x^t).
$$

则

$$
b^t+\lambda x^t
\in
\partial B_\lambda(x^t).
$$

在 shifted decomposition 上执行精确 DCA：

$$
x^{t+1}
\in
\arg\min_x
\left\{
A_\lambda(x)
-
\langle b^t+\lambda x^t,x\rangle
\right\}.
$$

展开：

$$
\begin{aligned}
x^{t+1}
&\in
\arg\min_x
\left\{
A(x)
+
\frac{\lambda}{2}\|x\|^2
-
\langle b^t,x\rangle
-
\lambda\langle x^t,x\rangle
\right\}\\
&=
\arg\min_x
\left\{
A(x)-\langle b^t,x\rangle
+
\frac{\lambda}{2}\|x-x^t\|^2
-
\frac{\lambda}{2}\|x^t\|^2
\right\}.
\end{aligned}
$$

最后一项与 $x$ 无关，因此

$$
\boxed{
x^{t+1}
\in
\arg\min_x
\left\{
A(x)-\langle b^t,x\rangle
+
\frac{\lambda}{2}\|x-x^t\|^2
\right\}.
}
$$

令

$$
\gamma=\frac1\lambda,
$$

则

$$
\boxed{
x^{t+1}
\in
\arg\min_x
\left\{
A(x)-\langle b^t,x\rangle
+
\frac1{2\gamma}\|x-x^t\|^2
\right\}.
}
$$

因此：

$$
\boxed{
\text{共同二次移位后的精确 DCA}
\equiv
\text{原分解上的精确 proximal DCA}.
}
$$

## 2.3 为什么不能简单写成 $\gamma=1/\rho$

MDCA 论文使用：

$$
\rho_1
=
A\text{ 的强凸常数},
$$

$$
\rho_2
=
B\text{ 的强凸常数},
$$

$$
\rho_{\mathrm{paper}}
=
\rho_1+\rho_2.
$$

如果原始 $A,B$ 只是凸函数，二者完全通过共同移位 $\lambda$ 获得强凸性，则

$$
\rho_1=\lambda,
\qquad
\rho_2=\lambda,
\qquad
\rho_{\mathrm{paper}}=2\lambda.
$$

此时

$$
\gamma=\frac1\lambda
=
\frac2{\rho_{\mathrm{paper}}}.
$$

所以：

- $1/\rho_1$ 在纯移位情形下可以解释为 proximal 参数；
- $1/(\rho_1+\rho_2)$ 一般不是该 proximal 参数；
- 若 $A,B$ 原本已经有强凸性，则 $\rho_1,\rho_2$ 还包含原始曲率，不能全部解释为显式 proximal regularization。

## 2.4 gap 上界中的 $1/\rho_1$ 的真正来源

MDCA 的 gap–variance 上界具有形式

$$
\operatorname{gap}
\le
\frac{\|e^t\|^2}{2\rho_1}.
$$

在纯共同移位情形中，

$$
\rho_1=\frac1\gamma,
$$

所以右侧可以写成

$$
\frac{\gamma}{2}\|e^t\|^2.
$$

这个量纲确实与 proximal 参数一致。

但在一般强凸模型中，$1/\rho_1$ 更本质的来源是：若 $A$ 是 $\rho_1$-强凸函数，则共轭函数 $A^*$ 是 $1/\rho_1$-光滑函数。

因此，gap 对线性项扰动的二次稳定性由 $A^*$ 的光滑性控制。它不必对应算法中显式出现的某个步长。

---

# 3. 三类算法必须严格区分

当前讨论中容易混淆的算法有三类。

## 3.1 裸 DCA

给定

$$
b^t\in\partial B(x^t),
$$

计算

$$
x^{t+1}
\in
\arg\min_x
\left\{
A(x)-\langle b^t,x\rangle
\right\}.
$$

最优性条件为

$$
b^t\in\partial A(x^{t+1}).
$$

这里没有显式 proximal 项。

## 3.2 精确 proximal DCA

给定

$$
b^t\in\partial B(x^t),
$$

计算

$$
x^{t+1}
\in
\arg\min_x
\left\{
A(x)-\langle b^t,x\rangle
+
\frac1{2\gamma}\|x-x^t\|^2
\right\}.
$$

最优性条件为

$$
b^t-\frac1\gamma(x^{t+1}-x^t)
\in
\partial A(x^{t+1}).
$$

它要求能够精确求解整个 $A$ 的 proximal 子问题。

若

$$
A=f+h,
$$

则该更新等于

$$
x^{t+1}
=
\operatorname{prox}_{\gamma(f+h)}
\left(x^t+\gamma b^t\right).
$$

这通常不是一个简单的 $\operatorname{prox}_h$ 操作。

## 3.3 单步 proximal-gradient/subgradient

考虑

$$
F(x)=f(x)+h(x)-g(x),
$$

其中 $f$ 光滑、$h$ 可 prox、$g$ 可取次梯度。

选择

$$
v^t\in\partial g(x^t),
$$

并使用 $d^t$ 估计 $\nabla f(x^t)$，更新

$$
\boxed{
x^{t+1}
=
\operatorname{prox}_{\eta h}
\left(
x^t-\eta(d^t-v^t)
\right).
}
$$

该更新对应最小化局部模型

$$
h(x)
+
\langle d^t-v^t,x-x^t\rangle
+
\frac1{2\eta}\|x-x^t\|^2.
$$

它不仅线性化了负侧 $g$，还线性化了正侧光滑部分 $f$。

一般情况下，

$$
\operatorname{prox}_{\gamma(f+h)}
(x^t+\gamma v^t)
\neq
\operatorname{prox}_{\eta h}
(x^t-\eta(\nabla f(x^t)-v^t)).
$$

所以：

$$
\boxed{
\text{精确 proximal DCA}
\neq
\text{单步 proximal-gradient/subgradient}.
}
$$

## 3.4 两者何时重合

在 quadratic-shift 分解中，正侧可能退化成纯二次函数：

$$
A(x)
=
\frac L2\|x\|^2+r_1(x).
$$

此时精确 DCA 子问题为

$$
\min_x
\left\{
\frac L2\|x\|^2+r_1(x)
-
\langle q^t,x\rangle
\right\},
$$

其解为

$$
x^{t+1}
=
\operatorname{prox}_{r_1/L}
\left(
\frac{q^t}{L}
\right).
$$

若

$$
q^t
\approx
Lx^t-\nabla\ell(x^t),
$$

则

$$
x^{t+1}
\approx
\operatorname{prox}_{r_1/L}
\left(
x^t-\frac1L\nabla\ell(x^t)
\right).
$$

这正是 proximal-gradient 步。

因此，**MDCA 在 quadratic-shift 场景中可以坍缩为带动量的 proximal-gradient 方法；但 MDCA Algorithm 1 在一般 DC 分解下仍是精确凸子问题方法。**

---

# 4. 同一个 proximal DCA 步的两种统一证书

这一部分回答“第三个残差槽为什么有时是零、有时不是零”。

## 4.1 原始分解上的证书

设

$$
s^t:=x^{t+1}-x^t,
$$

并考虑精确 proximal DCA：

$$
x^{t+1}
=
\arg\min_x
\left\{
A(x)-\langle b^t,x\rangle
+
\frac1{2\gamma}\|x-x^t\|^2
\right\},
$$

其中

$$
b^t\in\partial B(x^t).
$$

由最优性条件，

$$
u^{t+1}
:=
b^t-\frac1\gamma s^t
\in\partial A(x^{t+1}).
$$

另一方面，定义负侧 transport gap

$$
\delta_B^{t+1}
:=
B(x^{t+1})-B(x^t)
-
\langle b^t,s^t\rangle.
$$

因为 $b^t\in\partial B(x^t)$，所以

$$
\delta_B^{t+1}\ge0
$$

且

$$
b^t
\in
\partial_{\delta_B^{t+1}}B(x^{t+1}).
$$

因此，在同一点 $x^{t+1}$ 上，

$$
u^{t+1}\in\partial A(x^{t+1}),
$$

$$
b^t\in\partial_{\delta_B^{t+1}}B(x^{t+1}),
$$

并且

$$
\|u^{t+1}-b^t\|
=
\frac1\gamma\|s^t\|.
$$

所以相对于原始分解 $A-B$，

$$
\boxed{
x^{t+1}
\text{ 是 }
\left(
0,
\delta_B^{t+1},
\frac1\gamma\|s^t\|
\right)\text{-critical}.
}
$$

## 4.2 shifted 分解上的证书

令

$$
\lambda=\frac1\gamma,
$$

$$
A_\lambda=A+\frac{\lambda}{2}\|\cdot\|^2,
$$

$$
B_\lambda=B+\frac{\lambda}{2}\|\cdot\|^2.
$$

同一个 proximal DCA 步等价于 shifted pair 上的裸 DCA。

定义

$$
q^t:=b^t+\lambda x^t.
$$

则

$$
q^t\in\partial B_\lambda(x^t).
$$

而 shifted DCA 子问题的最优性条件给出

$$
q^t\in\partial A_\lambda(x^{t+1}).
$$

将 $q^t$ 从 $x^t$ 运输到 $x^{t+1}$，新的负侧 gap 为

$$
\begin{aligned}
\delta_{B_\lambda}^{t+1}
&=
B_\lambda(x^{t+1})
-
B_\lambda(x^t)
-
\langle q^t,s^t\rangle\\
&=
B(x^{t+1})-B(x^t)-\langle b^t,s^t\rangle\\
&\quad+
\frac{\lambda}{2}
\left(
\|x^{t+1}\|^2-\|x^t\|^2
-
2\langle x^t,s^t\rangle
\right)\\
&=
\delta_B^{t+1}
+
\frac{\lambda}{2}\|s^t\|^2\\
&=
\delta_B^{t+1}
+
\frac1{2\gamma}\|s^t\|^2.
\end{aligned}
$$

因此，相对于 shifted pair，

$$
\boxed{
x^{t+1}
\text{ 是 }
\left(
0,
\delta_B^{t+1}
+
\frac1{2\gamma}\|s^t\|^2,
0
\right)\text{-critical}.
}
$$

## 4.3 结论：误差在证书坐标之间转移

同一个算法步具有两种表示：

$$
\boxed{
\text{原分解：}
\left(
0,\delta_B,\frac{\|s\|}{\gamma}
\right);
}
$$

$$
\boxed{
\text{shifted 分解：}
\left(
0,\delta_B+\frac{\|s\|^2}{2\gamma},0
\right).
}
$$

所以：

> **第三槽是否为零，不由“二次项是显式写出还是隐藏在强凸性假设中”决定，而由证书相对于哪个 DC 分解报告决定。**

这也是 decomposition dependence 的一个具体表现：共同移位会在函数值松弛和向量残差之间重新分配误差。

---

# 5. MDCA Algorithm 1 的准确算法结构

## 5.1 问题模型

MDCA 处理

$$
F(x)
=
G(x)-H(x)+r_1(x)-r_2(x).
$$

记

$$
A=G+r_1,
\qquad
B=H+r_2.
$$

其基本假设包括：

- $A$ 强凸；
- $B$ 强凸；
- $H$ 光滑并通过随机梯度访问；
- $r_2$ 在 critical-distance 结果中需要光滑；
- gap 结果试图去掉 $r_2$ 光滑性；
- MVR 结果需要 averaged smoothness。

## 5.2 每次迭代的三个步骤

MDCA 在迭代 $t$：

1. 选择
   $$
   w^t\in\partial r_2(x^t).
   $$

2. 使用随机估计器 $g^t$ 近似
   $$
   \nabla H(x^t).
   $$

3. 精确求解
   $$
   \widetilde x^{t+1}
   =
   \arg\min_x
   \left\{
   G(x)+r_1(x)
   -
   \langle g^t+w^t,x\rangle
   \right\}.
   $$

4. 做阻尼更新
   $$
   x^{t+1}
   =
   x^t
   +
   \eta_t
   \left(
   \widetilde x^{t+1}-x^t
   \right).
   $$

5. 用新的样本更新 $g^{t+1}$。

输出从

$$
\{\widetilde x^1,\ldots,\widetilde x^T\}
$$

中随机选择，而不是从

$$
\{x^1,\ldots,x^T\}
$$

中选择。

## 5.3 为什么输出 $\widetilde x^{t+1}$

精确子问题最优性给出

$$
g^t+w^t
\in
\partial A(\widetilde x^{t+1}).
$$

因此，正侧次梯度关系天然成立在 $\widetilde x^{t+1}$ 上。

但动量估计器的状态更新和下降分析围绕阻尼后的 $x^{t+1}$ 展开。MDCA 的技术结构因此包含两个点：

- $\widetilde x^{t+1}$：完整 DCA 子问题解和输出候选点；
- $x^{t+1}$：阻尼后的状态点，用于控制迭代漂移和递归估计器方差。

这两个点的分离在分析 gap 和非光滑负侧时会产生实质影响。

## 5.4 精确子问题 oracle 的含义

MDCA 的主理论把

$$
\widetilde x^{t+1}
=
\arg\min_x
\left\{
A(x)-\langle g^t+w^t,x\rangle
\right\}
$$

视为可以精确计算。

因此，论文给出的“随机梯度复杂度”只计数 $H$-侧随机梯度，不计数求解 $A$-侧强凸子问题的内部代价。

只有在以下情形中，该复杂度接近端到端复杂度：

- $A$ 的 proximal mapping 有闭式；
- $A$ 是简单二次函数加简单正则项；
- quadratic-shift 分解使子问题退化为单次 prox；
- 或者存在一个被视为单位代价的精确 $A$-subproblem oracle。

在一般随机 $G$ 情形中，精确求解 $A$-侧子问题可能隐藏一个内层随机优化过程。

---

# 6. DCA-PAGE/MDCA 的 gap 函数到底测量什么

## 6.1 gap 的定义

记

$$
A=G+r_1.
$$

DCA-PAGE 的 lagged gap 具有形式

$$
\operatorname{gap}(x^t)
=
\max_x
\left\{
A(x^t)-A(x)
-
\langle q^{t-1},x^t-x\rangle
\right\},
$$

其中

$$
q^{t-1}
=
\nabla H(x^{t-1})+w^{t-1},
\qquad
w^{t-1}\in\partial r_2(x^{t-1}).
$$

在 MDCA 中，对输出候选点 $\widetilde x^{t+1}$ 的相应量是

$$
\operatorname{gap}_{t+1}
=
\max_x
\left\{
A(\widetilde x^{t+1})-A(x)
-
\langle q^t,\widetilde x^{t+1}-x\rangle
\right\},
$$

其中

$$
q^t
=
\nabla H(x^t)+w^t.
$$

## 6.2 它就是正侧 Fenchel–Young gap

利用凸共轭，

$$
\begin{aligned}
\operatorname{gap}_{t+1}
&=
A(\widetilde x^{t+1})
+
A^*(q^t)
-
\langle q^t,\widetilde x^{t+1}\rangle\\
&=
\Phi_A(\widetilde x^{t+1},q^t).
\end{aligned}
$$

所以

$$
\boxed{
\operatorname{gap}_{t+1}
=
\Phi_A(\widetilde x^{t+1},q^t).
}
$$

它等价于

$$
q^t
\in
\partial_{\operatorname{gap}_{t+1}}
A(\widetilde x^{t+1}).
$$

## 6.3 随机 MDCA 中为什么不一定为零

定义：

$$
\widehat q^t
:=
g^t+w^t,
$$

$$
q^t
:=
\nabla H(x^t)+w^t.
$$

算法精确求解的是随机子问题，因此只保证

$$
\widehat q^t
\in
\partial A(\widetilde x^{t+1}).
$$

而 gap 使用的是真实线性化向量 $q^t$。

所以：

$$
\operatorname{gap}_{t+1}=0
$$

当且仅当

$$
q^t\in\partial A(\widetilde x^{t+1}).
$$

算法一般只给出

$$
\widehat q^t\in\partial A(\widetilde x^{t+1}),
$$

因此随机情况下 gap 不一定为零。

## 6.4 确定性精确 DCA 中为什么每一步为零

若

$$
g^t=\nabla H(x^t),
$$

则

$$
\widehat q^t=q^t.
$$

于是

$$
q^t\in\partial A(\widetilde x^{t+1}),
$$

从而

$$
\boxed{
\operatorname{gap}_{t+1}=0.
}
$$

因此，在确定性精确 DCA 中，该 gap 对每一个完整 DCA 子问题解都自动为零。

这不是偶然现象，而是定义本身造成的：

$$
\operatorname{gap}_{t+1}
=
\left[
A(\widetilde x^{t+1})
-
\langle q^t,\widetilde x^{t+1}\rangle
\right]
-
\min_x
\left[
A(x)-\langle q^t,x\rangle
\right].
$$

它就是当前点对“真实线性化子问题”的函数次优性。

在确定性精确 DCA 中，$\widetilde x^{t+1}$ 正是该子问题的精确解，因此 gap 必然为零。

## 6.5 MDCA 的 gap–variance bound

若 $A$ 是 $\rho_1$-强凸函数，则

$$
A^*
$$

是 $1/\rho_1$-光滑函数。

利用

$$
\widehat q^t
\in
\partial A(\widetilde x^{t+1}),
$$

可以得到

$$
\Phi_A(\widetilde x^{t+1},q^t)
\le
\frac1{2\rho_1}
\|\widehat q^t-q^t\|^2.
$$

而

$$
\widehat q^t-q^t
=
g^t-\nabla H(x^t).
$$

因此

$$
\boxed{
\operatorname{gap}_{t+1}
\le
\frac1{2\rho_1}
\|g^t-\nabla H(x^t)\|^2.
}
$$

这说明 Theorem 4 的直接逻辑是：MVR 控制估计器均方误差，从而控制随机子问题解相对于真实子问题的函数次优性。

---

# 7. 为什么该 gap 不是完整的同点临界性度量

## 7.1 gap 为零只控制正侧

若

$$
\operatorname{gap}_{t+1}=0,
$$

则

$$
q^t\in\partial A(\widetilde x^{t+1}).
$$

但 $q^t$ 的负侧信息来自

$$
q^t
=
\nabla H(x^t)+w^t
\in
\partial B(x^t).
$$

因此得到的是

$$
q^t\in\partial A(\widetilde x^{t+1}),
$$

$$
q^t\in\partial B(x^t).
$$

两个次梯度关系位于不同点：

$$
\widetilde x^{t+1}
\quad\text{和}\quad
x^t.
$$

真正的同点 DC 临界性要求存在 $q$ 使得

$$
q\in\partial A(\widetilde x^{t+1})
\cap
\partial B(\widetilde x^{t+1}).
$$

所以，lagged gap 为零不能推出当前输出点临界。

## 7.2 一个满足强凸性的反例

取一维函数

$$
A(x)=\frac12x^2,
$$

$$
B(x)=\frac14x^2.
$$

则

$$
F(x)=A(x)-B(x)=\frac14x^2.
$$

从

$$
x^0=1
$$

开始，精确 DCA 使用

$$
q^0=B'(x^0)=\frac12.
$$

子问题为

$$
x^1
=
\arg\min_x
\left\{
\frac12x^2-\frac12x
\right\}
=
\frac12.
$$

由于

$$
A'(x^1)=\frac12=q^0,
$$

所以

$$
\operatorname{gap}(x^1)=0.
$$

但

$$
F'(x^1)
=
A'(x^1)-B'(x^1)
=
\frac12-\frac14
=
\frac14\neq0.
$$

因此：

$$
\boxed{
\operatorname{gap}(x^1)=0,
\qquad
x^1\text{ 不是临界点}.
}
$$

这个反例直接说明：按 lagged 定义，“gap 等于零当且仅当当前点临界”不成立。

## 7.3 缺失的负侧 transported gap

定义

$$
\delta_A^{t+1}
:=
\Phi_A(\widetilde x^{t+1},q^t)
=
\operatorname{gap}_{t+1}.
$$

再定义

$$
\delta_B^{t+1}
:=
\Phi_B(\widetilde x^{t+1},q^t).
$$

由于

$$
q^t\in\partial B(x^t),
$$

所以

$$
\delta_B^{t+1}
=
B(\widetilde x^{t+1})
-
B(x^t)
-
\langle q^t,\widetilde x^{t+1}-x^t\rangle.
$$

并且

$$
q^t
\in
\partial_{\delta_B^{t+1}}
B(\widetilde x^{t+1}).
$$

因此，完整同点证书是

$$
\boxed{
\left(
\delta_A^{t+1},
\delta_B^{t+1},
0
\right)\text{-critical}.
}
$$

MDCA/DCA-PAGE 的 gap theorem 只控制

$$
\delta_A^{t+1},
$$

没有控制

$$
\delta_B^{t+1}.
$$

## 7.4 随机误差也可以放进第三槽

算法精确子问题给出

$$
\widehat q^t
=
g^t+w^t
\in
\partial A(\widetilde x^{t+1}).
$$

而真实负侧向量

$$
q^t
=
\nabla H(x^t)+w^t
$$

满足

$$
q^t
\in
\partial_{\delta_B^{t+1}}
B(\widetilde x^{t+1}).
$$

因此同一个点也有证书

$$
\boxed{
\left(
0,
\delta_B^{t+1},
\|\widehat q^t-q^t\|
\right)\text{-critical}.
}
$$

又因为

$$
\widehat q^t-q^t
=
g^t-\nabla H(x^t),
$$

所以

$$
\boxed{
\left(
0,
\delta_B^{t+1},
\|g^t-\nabla H(x^t)\|
\right)\text{-critical}.
}
$$

这说明随机误差有两种表示：

- 放进正侧 Fenchel gap $\delta_A$；
- 放进向量残差 $\varepsilon$。

但无论哪种表示，都必须另外控制负侧 transport gap $\delta_B$。

## 7.5 对 Theorem 4 的准确评价

可以区分“数值不等式”和“临界性解释”。

### 数值不等式

$$
\operatorname{gap}_{t+1}
\le
\frac{\|g^t-\nabla H(x^t)\|^2}{2\rho_1}
$$

可以是正确的。

### 临界性解释

将该 lagged gap 直接解释为完整的非光滑同点 DC 临界性度量存在问题，因为它遗漏 $\delta_B$。

因此准确表述应当是：

> **Theorem 4 controls a one-sided Fenchel–Young gap that measures stochastic subproblem inconsistency. It does not by itself control same-point nonsmooth DC criticality.**

---

# 8. MDCA 的 critical-distance 结果为什么不同

## 8.1 critical-distance 定义

当 $r_2$ 光滑时，MDCA 使用

$$
d(x)
=
\operatorname{dist}
\left(
\nabla H(x)+\nabla r_2(x),
\partial A(x)
\right).
$$

该定义中的所有对象位于同一个点 $x$。

因此

$$
d(x)=0
$$

确实刻画标准 DC 临界性。

## 8.2 距离估计

MDCA 的精确子问题给出

$$
g^t+w^t
\in
\partial A(\widetilde x^{t+1}).
$$

当

$$
w^t=\nabla r_2(x^t),
$$

可以写出

$$
\begin{aligned}
d(\widetilde x^{t+1})
&\le
\|
\nabla H(\widetilde x^{t+1})
+
\nabla r_2(\widetilde x^{t+1})
-
g^t
-
\nabla r_2(x^t)
\|\\
&\le
(L_H+L_{r_2})
\|\widetilde x^{t+1}-x^t\|
+
\|g^t-\nabla H(x^t)\|.
\end{aligned}
$$

所以 critical-distance 分析需要：

- 控制估计器误差；
- 控制 $\widetilde x^{t+1}-x^t$；
- 用 $H$ 与 $r_2$ 的光滑性把负侧信息运输到输出点。

这就是为什么 critical-distance theorem 需要 $r_2$ 光滑，而 gap theorem 试图绕开该假设。

## 8.3 对 MDCA Theorem 2 的评价

MDCA Theorem 2 的 MVR 结果是一个有意义的同点临界性 $\varepsilon^{-3}$ 结果，但应明确其 oracle 模型：

- 只计数 $H$-侧随机梯度；
- $A=G+r_1$ 子问题被精确求解；
- $r_2$ 光滑；
- 输出是完整子问题解 $\widetilde x^{t+1}$；
- 算法状态使用阻尼点 $x^{t+1}$。

因此它是：

$$
\boxed{
\text{exact-$A$-subproblem oracle 模型下的 same-point }\varepsilon^{-3}.
}
$$

---

# 9. 直接单循环模型 $f+h-g$

现在考虑我们真正希望分析的算法。

## 9.1 模型

设

$$
F(x)=f(x)+h(x)-g(x),
$$

其中：

- $f$ 是 $L_f$-光滑凸函数；
- $h$ 是 proper、closed、convex，且 prox 可计算；
- $g$ 是 proper、closed、convex，可以非光滑；
- $F$ 下有界。

定义

$$
\phi=f+h.
$$

## 9.2 随机单步更新

在迭代 $k$，选择

$$
v^k\in\partial g(x^k),
$$

并使用估计器 $d^k$ 估计

$$
\nabla f(x^k).
$$

更新：

$$
\boxed{
x^{k+1}
=
\operatorname{prox}_{\eta h}
\left(
x^k-\eta(d^k-v^k)
\right).
}
$$

记

$$
s^k:=x^{k+1}-x^k.
$$

## 9.3 邻近最优性条件

由 prox 最优性，

$$
0
\in
\partial h(x^{k+1})
+
d^k-v^k
+
\frac1\eta s^k.
$$

因此定义

$$
w^{k+1}
:=
v^k-d^k-\frac1\eta s^k,
$$

则

$$
w^{k+1}
\in
\partial h(x^{k+1}).
$$

再定义

$$
u^{k+1}
:=
\nabla f(x^{k+1})+w^{k+1}.
$$

由于 $f$ 可微凸，

$$
u^{k+1}
\in
\partial(f+h)(x^{k+1})
=
\partial\phi(x^{k+1}).
$$

因此：

$$
\boxed{
\delta_\phi=0
}
$$

逐路径精确成立。

这不是期望意义下的近似结论，而是每条随机轨迹上都成立的精确包含关系。

## 9.4 负侧 transport gap

因为

$$
v^k\in\partial g(x^k),
$$

定义

$$
\delta_g^{k+1}
:=
g(x^{k+1})
-
g(x^k)
-
\langle v^k,s^k\rangle.
$$

则

$$
\delta_g^{k+1}\ge0
$$

并且

$$
v^k
\in
\partial_{\delta_g^{k+1}}g(x^{k+1}).
$$

因此，在同一点 $x^{k+1}$ 上已经有：

$$
u^{k+1}\in\partial\phi(x^{k+1}),
$$

$$
v^k\in\partial_{\delta_g^{k+1}}g(x^{k+1}).
$$

剩余任务是控制

$$
\|u^{k+1}-v^k\|.
$$

---

# 10. 单步算法的残差与下降不等式

## 10.1 估计器误差

定义

$$
e^k
:=
\nabla f(x^k)-d^k.
$$

记

$$
V_k
:=
\mathbb E\|e^k\|^2.
$$

定义平均均方误差

$$
\bar V_K
:=
\frac1K
\sum_{k=0}^{K-1}
V_k.
$$

## 10.2 同点残差

由 $u^{k+1}$ 的定义，

$$
\begin{aligned}
u^{k+1}-v^k
&=
\nabla f(x^{k+1})
+
v^k-d^k-\frac1\eta s^k
-
v^k\\
&=
\nabla f(x^{k+1})-d^k-\frac1\eta s^k\\
&=
\nabla f(x^{k+1})-\nabla f(x^k)
+
e^k
-
\frac1\eta s^k.
\end{aligned}
$$

因此

$$
\|u^{k+1}-v^k\|
\le
\left(
L_f+\frac1\eta
\right)
\|s^k\|
+
\|e^k\|.
$$

记

$$
r_\eta
:=
L_f+\frac1\eta.
$$

则

$$
\|u^{k+1}-v^k\|^2
\le
2r_\eta^2\|s^k\|^2
+
2\|e^k\|^2.
$$

## 10.3 下降不等式的完整推导

由 $f$ 的光滑性，

$$
f(x^{k+1})
\le
f(x^k)
+
\langle\nabla f(x^k),s^k\rangle
+
\frac{L_f}{2}\|s^k\|^2.
$$

由

$$
w^{k+1}
=
v^k-d^k-\frac1\eta s^k
\in
\partial h(x^{k+1}),
$$

凸性给出

$$
h(x^k)
\ge
h(x^{k+1})
+
\langle w^{k+1},x^k-x^{k+1}\rangle.
$$

所以

$$
h(x^{k+1})-h(x^k)
\le
\langle w^{k+1},s^k\rangle.
$$

代入 $w^{k+1}$：

$$
h(x^{k+1})-h(x^k)
\le
\langle v^k-d^k,s^k\rangle
-
\frac1\eta\|s^k\|^2.
$$

负侧满足

$$
g(x^{k+1})-g(x^k)
=
\langle v^k,s^k\rangle
+
\delta_g^{k+1}.
$$

因此

$$
\begin{aligned}
F(x^{k+1})-F(x^k)
&=
f(x^{k+1})-f(x^k)\\
&\quad+
h(x^{k+1})-h(x^k)\\
&\quad-
g(x^{k+1})+g(x^k)\\
&\le
\langle\nabla f(x^k),s^k\rangle
+
\frac{L_f}{2}\|s^k\|^2\\
&\quad+
\langle v^k-d^k,s^k\rangle
-
\frac1\eta\|s^k\|^2\\
&\quad-
\langle v^k,s^k\rangle
-
\delta_g^{k+1}\\
&=
\langle e^k,s^k\rangle
-
\left(
\frac1\eta-\frac{L_f}{2}
\right)
\|s^k\|^2
-
\delta_g^{k+1}.
\end{aligned}
$$

对内积使用 Young 不等式：

$$
\langle e^k,s^k\rangle
\le
\frac{\eta}{2}\|e^k\|^2
+
\frac1{2\eta}\|s^k\|^2.
$$

得到

$$
F(x^{k+1})-F(x^k)
\le
-
\delta_g^{k+1}
-
\frac{1-\eta L_f}{2\eta}
\|s^k\|^2
+
\frac{\eta}{2}\|e^k\|^2.
$$

定义

$$
a_\eta
:=
\frac{1-\eta L_f}{2\eta}.
$$

只要

$$
0<\eta<\frac1{L_f},
$$

就有

$$
a_\eta>0.
$$

于是

$$
\boxed{
F(x^k)-F(x^{k+1})
\ge
\delta_g^{k+1}
+
a_\eta\|s^k\|^2
-
\frac{\eta}{2}\|e^k\|^2.
}
$$

---

# 11. 模块化统一证书

设

$$
\Delta_0
:=
F(x^0)-F_*,
\qquad
F_*:=\inf_xF(x)>-\infty.
$$

对下降不等式从 $k=0$ 到 $K-1$ 求和：

$$
\sum_{k=0}^{K-1}
\mathbb E\delta_g^{k+1}
+
a_\eta
\sum_{k=0}^{K-1}
\mathbb E\|s^k\|^2
\le
\Delta_0
+
\frac{\eta}{2}
\sum_{k=0}^{K-1}
V_k.
$$

## 11.1 负侧 value gap

直接得到

$$
\frac1K
\sum_{k=0}^{K-1}
\mathbb E\delta_g^{k+1}
\le
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K.
$$

若随机选择

$$
R\sim\operatorname{Unif}\{0,\ldots,K-1\}
$$

并输出

$$
\bar x=x^{R+1},
\qquad
v=v^R,
$$

则

$$
\boxed{
\mathbb E\Phi_g(\bar x,v)
\le
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K.
}
$$

## 11.2 平均步长

同样有

$$
a_\eta
\frac1K
\sum_{k=0}^{K-1}
\mathbb E\|s^k\|^2
\le
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K.
$$

因此

$$
\boxed{
\frac1K
\sum_{k=0}^{K-1}
\mathbb E\|s^k\|^2
\le
\frac1{a_\eta}
\left(
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K
\right).
}
$$

## 11.3 同点平方残差

由

$$
\|u^{k+1}-v^k\|^2
\le
2r_\eta^2\|s^k\|^2
+
2\|e^k\|^2,
$$

得到

$$
\boxed{
\mathbb E\|u-v\|^2
\le
\frac{2r_\eta^2}{a_\eta}
\left(
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K
\right)
+
2\bar V_K.
}
$$

同时

$$
\boxed{
\mathbb E\Phi_\phi(\bar x,u)=0.
}
$$

所以完整模块化结论是：

$$
\boxed{
\mathbb E\Phi_\phi(\bar x,u)=0,
}
$$

$$
\boxed{
\mathbb E\Phi_g(\bar x,v)
\le
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K,
}
$$

$$
\boxed{
\mathbb E\|u-v\|^2
\le
\frac{2r_\eta^2}{a_\eta}
\left(
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K
\right)
+
2\bar V_K.
}
$$

## 11.4 简化形式

若

$$
\eta L_f\le\frac12,
$$

则

$$
a_\eta
=
\frac{1-\eta L_f}{2\eta}
\ge
\frac1{4\eta},
$$

且

$$
r_\eta
=
L_f+\frac1\eta
\le
\frac{3}{2\eta}.
$$

因此

$$
\frac{2r_\eta^2}{a_\eta}
=
O\left(\frac1\eta\right).
$$

从而

$$
\boxed{
\mathbb E\|u-v\|^2
\lesssim
\frac{\Delta_0}{\eta K}
+
\bar V_K.
}
$$

统一证书的核心预算变成：

$$
\boxed{
\frac{\Delta_0}{\eta K}
\lesssim
\varepsilon^2,
}
$$

$$
\boxed{
\bar V_K
\lesssim
\varepsilon^2.
}
$$

这个形式将优化算法的确定性下降部分与随机估计器部分完全分开。

---

# 12. 普通随机梯度为什么是 $\varepsilon^{-4}$

若每一步使用批量 $b$ 的独立无偏随机梯度：

$$
d^k
=
\frac1b
\sum_{i=1}^b
\nabla f_{\xi_i^k}(x^k),
$$

且

$$
\mathbb E
\|
\nabla f_\xi(x)-\nabla f(x)
\|^2
\le
\sigma^2,
$$

则

$$
V_k
\le
\frac{\sigma^2}{b}.
$$

所以

$$
\bar V_K
\le
\frac{\sigma^2}{b}.
$$

为了使

$$
\bar V_K\lesssim\varepsilon^2,
$$

必须取

$$
b
=
\Theta\left(
\frac{\sigma^2}{\varepsilon^2}
\right).
$$

若使用固定步长

$$
\eta=\Theta(1/L_f),
$$

则确定性预算要求

$$
K
=
\Theta\left(
\frac{L_f\Delta_0}{\varepsilon^2}
\right).
$$

总随机梯度复杂度为

$$
Kb
=
\Theta\left(
\frac{\sigma^2L_f\Delta_0}{\varepsilon^4}
\right).
$$

因此：

$$
\boxed{
\text{单循环结构本身不产生 }\varepsilon^{-3}.
}
$$

必须依赖递归方差缩减，才能在常数批量下将 $\bar V_K$ 压到 $O(\varepsilon^2)$。

---

# 13. MVR/STORM 估计器与常数批量 $\varepsilon^{-3}$

## 13.1 估计器形式

一个典型 MVR/STORM 更新为

$$
d^{k+1}
=
(1-\alpha)
\left[
d^k
+
\widehat\nabla f_{I_{k+1}}(x^{k+1})
-
\widehat\nabla f_{I_{k+1}}(x^k)
\right]
+
\alpha
\widehat\nabla f_{I_{k+1}}(x^{k+1}).
$$

同一批样本 $I_{k+1}$ 用于两个点的梯度差。

## 13.2 MVR 估计器通常不是条件无偏的

一般有

$$
\mathbb E_k[d^{k+1}]
=
\nabla f(x^{k+1})
+
(1-\alpha)
\left[
d^k-\nabla f(x^k)
\right].
$$

因此

$$
\mathbb E_k[d^{k+1}]
\neq
\nabla f(x^{k+1})
$$

除非前一时刻估计误差恰好为零。

所以理论假设应表述为：

- 基础随机梯度 oracle 无偏；
- 递归估计器满足一个均方误差递推。

不应要求递归估计器 $d^k$ 本身在每一步条件无偏。

## 13.3 MSE 递推

在 averaged smoothness 假设下，

$$
\mathbb E_\xi
\|
\nabla f_\xi(x)-\nabla f_\xi(y)
\|^2
\le
L_f^2\|x-y\|^2,
$$

可以得到

$$
\boxed{
V_{k+1}
\le
(1-\alpha)V_k
+
\frac{2L_f^2}{b}
\mathbb E\|s^k\|^2
+
\frac{2\alpha^2\sigma^2}{b}.
}
$$

该递推包含三项：

1. $(1-\alpha)V_k$：历史误差衰减；
2. $(2L_f^2/b)\|s^k\|^2$：迭代漂移引入的偏差；
3. $2\alpha^2\sigma^2/b$：新样本噪声。

## 13.4 与下降不等式耦合

将递推求和：

$$
\alpha
\sum_{k=0}^{K-1}V_k
\le
V_0
+
\frac{2L_f^2}{b}
\sum_{k=0}^{K-1}
\mathbb E\|s^k\|^2
+
\frac{2K\alpha^2\sigma^2}{b}.
$$

由下降分析，

$$
\sum_{k=0}^{K-1}
\mathbb E\|s^k\|^2
\le
\frac{\Delta_0}{a_\eta}
+
\frac{\eta}{2a_\eta}
\sum_{k=0}^{K-1}V_k.
$$

代入：

$$
\begin{aligned}
\alpha\sum V_k
&\le
V_0
+
\frac{2L_f^2\Delta_0}{b a_\eta}\\
&\quad+
\frac{L_f^2\eta}{b a_\eta}
\sum V_k
+
\frac{2K\alpha^2\sigma^2}{b}.
\end{aligned}
$$

为了将 $\sum V_k$ 的耦合项吸收到左侧，需要

$$
\frac{L_f^2\eta}{b a_\eta}
\le
c\alpha
$$

对某个 $c<1$ 成立。

由于

$$
a_\eta
=
\frac{1-\eta L_f}{2\eta},
$$

所以

$$
\frac{L_f^2\eta}{b a_\eta}
=
\frac{2L_f^2\eta^2}{b(1-\eta L_f)}.
$$

当 $\eta L_f\le1/2$ 时，条件简化为

$$
\boxed{
\eta^2L_f^2
\lesssim
\alpha b.
}
$$

## 13.5 平均估计误差的模块化上界

吸收耦合项后，可以得到

$$
\bar V_K
\lesssim
\frac{V_0}{\alpha K}
+
\frac{L_f^2\Delta_0}{\alpha b a_\eta K}
+
\frac{\alpha\sigma^2}{b}.
$$

在

$$
\eta^2L_f^2
\asymp
\alpha b
$$

的平衡下，

$$
\frac{L_f^2}{\alpha b a_\eta}
\asymp
\frac1\eta.
$$

因此

$$
\boxed{
\bar V_K
\lesssim
\frac{V_0}{\alpha K}
+
\frac{\Delta_0}{\eta K}
+
\frac{\alpha\sigma^2}{b}.
}
$$

结合统一证书：

$$
\boxed{
\mathbb E\|u-v\|^2
\lesssim
\frac{\Delta_0}{\eta K}
+
\frac{V_0}{\alpha K}
+
\frac{\alpha\sigma^2}{b}.
}
$$

---

# 14. 三种参数平衡及其复杂度

## 14.1 方案一：普通随机梯度

$$
\bar V_K\le\sigma^2/b.
$$

需要

$$
b=\Theta(\sigma^2/\varepsilon^2),
$$

$$
K=\Theta(L_f\Delta_0/\varepsilon^2).
$$

总复杂度：

$$
\boxed{
O(\sigma^2L_f\Delta_0\varepsilon^{-4}).
}
$$

## 14.2 方案二：固定步长、增大批量的 MVR

若固定

$$
\eta=\Theta(1/L_f),
$$

则吸收条件

$$
\eta^2L_f^2\lesssim\alpha b
$$

变成

$$
1\lesssim\alpha b.
$$

若选择

$$
\alpha=\Theta(\varepsilon/\sigma),
$$

则需要

$$
b=\Theta(\sigma/\varepsilon).
$$

噪声底为

$$
\frac{\alpha\sigma^2}{b}
=
O(\varepsilon^2).
$$

同时

$$
K=\Theta(L_f\Delta_0/\varepsilon^2).
$$

总随机梯度数：

$$
Kb
=
O(\sigma L_f\Delta_0\varepsilon^{-3}).
$$

这个结果在总样本复杂度上是 $\varepsilon^{-3}$，但每步批量随精度增长：

$$
b=\Theta(\varepsilon^{-1}).
$$

## 14.3 方案三：常数批量、缩小步长的 MVR

固定

$$
b=O(1).
$$

为了使噪声底满足

$$
\frac{\alpha\sigma^2}{b}
\lesssim
\varepsilon^2,
$$

取

$$
\boxed{
\alpha
=
\Theta\left(
\frac{b\varepsilon^2}{\sigma^2}
\right).
}
$$

再取最大可行步长

$$
\boxed{
\eta
=
\Theta\left(
\frac{\sqrt{\alpha b}}{L_f}
\right)
=
\Theta\left(
\frac{b\varepsilon}{L_f\sigma}
\right).
}
$$

确定性预算要求

$$
\frac{\Delta_0}{\eta K}
\lesssim
\varepsilon^2.
$$

所以

$$
\boxed{
K
=
\Theta\left(
\frac{L_f\sigma\Delta_0}
{b\varepsilon^3}
\right).
}
$$

每次 MVR 更新通常需要在相同批量上计算两个点的梯度，因此总梯度数为

$$
2bK+b_0.
$$

若初始化批量选择使

$$
V_0=O(\varepsilon^2),
$$

例如

$$
b_0=O(\sigma^2/\varepsilon^2),
$$

则

$$
\boxed{
2bK+b_0
=
O\left(
\frac{L_f\sigma\Delta_0}{\varepsilon^3}
+
\frac{\sigma^2}{\varepsilon^2}
\right).
}
$$

小 $\varepsilon$ 下主项是

$$
\boxed{
O(\sigma\varepsilon^{-3}).
}
$$

## 14.4 输出统一证书

在上述常数批量参数下：

$$
\boxed{
\mathbb E\Phi_\phi(\bar x,u)=0,
}
$$

$$
\boxed{
\mathbb E\Phi_g(\bar x,v)
\le
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K
=
O(\eta\varepsilon^2),
}
$$

$$
\boxed{
\mathbb E\|u-v\|^2
\le
O(\varepsilon^2).
}
$$

因为

$$
\eta
=
\Theta\left(
\frac{\varepsilon}{L_f\sigma}
\right)
$$

在常数批量下，所以

$$
\mathbb E\Phi_g(\bar x,v)
=
O\left(
\frac{\varepsilon^3}{L_f\sigma}
\right).
$$

这比通常要求的 $O(\varepsilon^2/L_f)$ 更小，但该更强尺度来自步长随 $\varepsilon$ 缩小。

## 14.5 参数需要加上截断

正式定理中不能直接假设

$$
\alpha<1,
\qquad
\eta<1/L_f
$$

自动成立。

应写成类似

$$
\alpha
=
\min\left\{
\alpha_{\max},
c_\alpha\frac{b\varepsilon^2}{\sigma^2}
\right\},
$$

$$
\eta
=
\min\left\{
\frac{c_\eta}{L_f},
c_\eta\frac{\sqrt{\alpha b}}{L_f}
\right\}.
$$

当 $\varepsilon$ 足够小时，进入主要的 $\varepsilon^{-3}$ 渐近区间。

---

# 15. “他们的 $\varepsilon^{-3}$ 是否有意义”需要分结果回答

## 15.1 MDCA Theorem 2：有意义

目标：

$$
\mathbb E d(\widehat x)^2
\le
\varepsilon^2.
$$

特点：

- 同点 critical distance；
- $r_2$ 必须光滑；
- 精确 $A$-subproblem oracle；
- MVR；
- 常数每步批量；
- 随机梯度复杂度 $O(\sigma\varepsilon^{-3})$。

结论：

$$
\boxed{
\text{这是有意义的同点临界性 }\varepsilon^{-3}.
}
$$

但它的 oracle 模型强于普通单步 proximal-gradient 方法。

## 15.2 DCA-PAGE critical-distance 结果：有意义

DCA-PAGE 使用 PAGE 型估计器，在线版本通过周期性大 anchor batch 获得类似

$$
O\left(
b+\sqrt b\,\varepsilon^{-2}
\right)
$$

的复杂度。

当

$$
b=\Theta(\sigma^2/\varepsilon^2)
$$

时，得到

$$
O\left(
\sigma^2\varepsilon^{-2}
+
\sigma\varepsilon^{-3}
\right).
$$

在相同 smooth-$r_2$ critical-distance 口径下，这也是有效结果。

## 15.3 MDCA Theorem 4：不能作为完整非光滑临界性的 $\varepsilon^{-3}$

目标：

$$
\mathbb E\operatorname{gap}(\widehat x)
\le
\tau.
$$

其 gap 是

$$
\delta_A
=
\Phi_A(\widetilde x^{t+1},q^t),
$$

但没有控制

$$
\delta_B
=
\Phi_B(\widetilde x^{t+1},q^t).
$$

因此其 $\varepsilon^{-3}$ 只是将 gap tolerance 设为 $\varepsilon^2$ 后得到的平方尺度换算。

结论：

$$
\boxed{
\text{它不是完整的非光滑 same-point criticality }\varepsilon^{-3}.
}
$$

## 15.4 DCA-PAGE gap theorem：存在相同问题

DCA-PAGE 的 Definition 12 使用前一迭代点的真实梯度和次梯度。

在确定性精确 DCA 中，该 gap 每步为零，但迭代点一般不临界。

所以该 gap theorem 不能直接被引用为完整非光滑 DC 临界性复杂度。

## 15.5 直接 PS-DCA + MVR 的潜在优势

直接算法

$$
x^{k+1}
=
\operatorname{prox}_{\eta h}
\left(
x^k-\eta(d^k-v^k)
\right)
$$

不需要：

- 精确求解 $f+h$ 的子问题；
- $g$ 光滑；
- 对负侧次梯度做点间 Lipschitz 运输；
- Moreau 平滑 $g$。

它可以直接给出：

$$
\delta_\phi=0,
$$

$$
\delta_g
=
\Phi_g(x^{k+1},v^k),
$$

$$
\varepsilon
=
\|u^{k+1}-v^k\|.
$$

因此它更适合讨论真正的非光滑负侧。

---

# 16. 能否宣称统一度量下的 $\varepsilon^{-3}$ 最优性

当前不能仅因为指数匹配就直接宣称“最优”。

## 16.1 必须先固定目标精度口径

例如，可以定义目标为：

$$
\mathbb E\|u-v\|^2
\le
\varepsilon^2,
$$

$$
\mathbb E\delta_\phi
\le
c\frac{\varepsilon^2}{L},
$$

$$
\mathbb E\delta_g
\le
c\frac{\varepsilon^2}{L}.
$$

若只要求

$$
\mathbb E\delta_g\le\varepsilon,
$$

而其他论文要求

$$
\mathbb E d(x)^2\le\varepsilon^2,
$$

二者的指数不能直接比较。

## 16.2 平滑子类中的梯度残差转换

若 $\phi,g$ 都光滑凸，则 Fenchel gap 可以控制次梯度误差。

对 $L_\phi$-光滑凸 $\phi$：

$$
\Phi_\phi(x,u)
\ge
\frac1{2L_\phi}
\|u-\nabla\phi(x)\|^2.
$$

对 $L_g$-光滑凸 $g$：

$$
\Phi_g(x,v)
\ge
\frac1{2L_g}
\|v-\nabla g(x)\|^2.
$$

因此

$$
\begin{aligned}
\|\nabla(\phi-g)(x)\|
&\le
\|\nabla\phi(x)-u\|\\
&\quad+
\|u-v\|\\
&\quad+
\|v-\nabla g(x)\|\\
&\le
\sqrt{2L_\phi\delta_\phi}
+
\varepsilon
+
\sqrt{2L_g\delta_g}.
\end{aligned}
$$

若

$$
\delta_\phi=O(\varepsilon^2/L_\phi),
$$

$$
\delta_g=O(\varepsilon^2/L_g),
$$

则

$$
\|\nabla(\phi-g)(x)\|
=
O(\varepsilon).
$$

## 16.3 下界 reduction 的路线

要证明统一证书下的 $\Omega(\varepsilon^{-3})$，需要：

1. 将标准随机光滑非凸问题嵌入
   $$
   f+h-g
   $$
   的子类；

2. 确保该嵌入满足相同 oracle 假设：
   - bounded variance；
   - mean-squared smoothness；
   - 每步批量计数方式；
   - 初始化方式；

3. 证明统一证书达到指定尺度时，标准梯度范数也是 $O(\varepsilon)$；

4. 调用相同 oracle 模型下的随机非凸优化下界。

一个自然嵌入是：对 $L$-光滑非凸样本函数 $\psi_\xi$，令

$$
f_\xi(x)
=
\psi_\xi(x)
+
\frac L2\|x\|^2,
$$

$$
g(x)
=
\frac L2\|x\|^2,
$$

$$
h=0.
$$

若每个 $\psi_\xi$ 的 Hessian 下界为 $-L I$，则 $f_\xi$ 为凸函数。

此时

$$
f-g=\psi.
$$

对二次 $g$，

$$
\Phi_g(x,v)
=
\frac1{2L}
\|v-Lx\|^2.
$$

所以

$$
\delta_g=O(\varepsilon^2/L)
$$

和

$$
\|u-v\|\le\varepsilon
$$

可以推出

$$
\|\nabla\psi(x)\|=O(\varepsilon).
$$

## 16.4 当前最稳妥的 claim

在正式完成下界 reduction 前，建议写：

> **The proposed method matches the optimal $\varepsilon^{-3}$ dependence known for smooth stochastic nonconvex optimization under the corresponding mean-squared smoothness oracle assumptions.**

完成 reduction 后，才可以写：

> **The $O(\varepsilon^{-3})$ complexity is optimal for the specified unified certificate.**

---

# 17. S-MDCA 与 Moreau 平滑化

## 17.1 平滑代理目标

S-MDCA 定义

$$
F_\gamma(x)
=
A_\gamma(x)
-
H(x)
-
(r_2)_\gamma(x),
$$

其中

$$
A=G+r_1.
$$

Moreau envelope 为

$$
q_\gamma(x)
=
\min_y
\left\{
q(y)+\frac1{2\gamma}\|y-x\|^2
\right\}.
$$

定义

$$
u^*(x)
=
\operatorname{prox}_{\gamma A}(x),
$$

$$
z^*(x)
=
\operatorname{prox}_{\gamma r_2}(x).
$$

则

$$
\nabla A_\gamma(x)
=
\frac{x-u^*(x)}{\gamma},
$$

$$
\nabla(r_2)_\gamma(x)
=
\frac{x-z^*(x)}{\gamma}.
$$

因此

$$
\boxed{
\nabla F_\gamma(x)
=
\frac{z^*(x)-u^*(x)}{\gamma}
-
\nabla H(x).
}
$$

## 17.2 Lemma 8 的三个点

定义

$$
p_1
:=
\frac{x-u^*(x)}{\gamma}
\in
\partial A(u^*(x)),
$$

$$
p_2
:=
\frac{x-z^*(x)}{\gamma}
\in
\partial r_2(z^*(x)).
$$

则

$$
\nabla F_\gamma(x)
=
p_1-\nabla H(x)-p_2.
$$

最初三个对象位于不同点：

- $p_1$ 位于 $u^*(x)$；
- $\nabla H(x)$ 位于 $x$；
- $p_2$ 位于 $z^*(x)$。

Lemma 8 选择

$$
\widehat x=u^*(x)
$$

作为最终点，并利用光滑性运输：

$$
\nabla H(x)
\longrightarrow
\nabla H(\widehat x),
$$

$$
p_2=\nabla r_2(z^*(x))
\longrightarrow
\nabla r_2(\widehat x).
$$

因此

$$
\begin{aligned}
&\operatorname{dist}
\left(
0,
\partial A(\widehat x)
-
\nabla H(\widehat x)
-
\partial r_2(\widehat x)
\right)\\
&\qquad
\le
\|\nabla F_\gamma(x)\|
+
L_H\|x-u^*(x)\|
+
L_{r_2}\|u^*(x)-z^*(x)\|.
\end{aligned}
$$

## 17.3 最终确实是同一点，但有附加条件

Lemma 8 最终给出的 critical-distance 位于

$$
\widehat x=u^*(x)
$$

同一个点上。

因此它不是“不同点残差”。

但它要求：

1. $r_2$ 光滑；
2. $\|p_1\|$ 有界；
3. $\|\nabla H(x)\|$ 有界；
4. 迭代点不能逃向无界区域。

因为

$$
\|x-u^*(x)\|
=
\gamma\|p_1\|,
$$

且

$$
\|u^*(x)-z^*(x)\|
\le
\gamma
\left(
\|\nabla F_\gamma(x)\|
+
\|\nabla H(x)\|
\right).
$$

所以

$$
\widehat\varepsilon
\le
\varepsilon(1+\gamma L_{r_2})
+
\gamma
\left(
L_H\|p_1\|
+
L_{r_2}\|\nabla H(x)\|
\right).
$$

若要写成

$$
\widehat\varepsilon
=
O(\varepsilon+\gamma),
$$

必须对 $\|p_1\|$ 与 $\|\nabla H(x)\|$ 建立统一上界。

“目标函数下有界”本身不能自动推出这些上界。

---

# 18. 不要求 $r_2$ 光滑的统一平滑化证书

统一证书允许不把三个对象强行运输到 $u^*(x)$。

## 18.1 将 prox 次梯度运输回 $x$

仍定义

$$
u=u^*(x),
\qquad
z=z^*(x),
$$

$$
p_A
=
\frac{x-u}{\gamma}
\in
\partial A(u),
$$

$$
p_2
=
\frac{x-z}{\gamma}
\in
\partial r_2(z).
$$

定义

$$
\delta_A(x,\gamma)
:=
A(x)-A(u)-\langle p_A,x-u\rangle.
$$

由于

$$
p_A\in\partial A(u),
$$

所以

$$
p_A
\in
\partial_{\delta_A(x,\gamma)}A(x).
$$

同理定义

$$
\delta_2(x,\gamma)
:=
r_2(x)-r_2(z)-\langle p_2,x-z\rangle.
$$

则

$$
p_2
\in
\partial_{\delta_2(x,\gamma)}r_2(x).
$$

因为 $H$ 在 $x$ 可微，

$$
\nabla H(x)+p_2
\in
\partial_{\delta_2(x,\gamma)}
(H+r_2)(x).
$$

## 18.2 向量残差正好是平滑梯度

有

$$
p_A
-
\left[
\nabla H(x)+p_2
\right]
=
\nabla F_\gamma(x).
$$

因此：

$$
\boxed{
x
\text{ 是 }
\left(
\delta_A(x,\gamma),
\delta_2(x,\gamma),
\|\nabla F_\gamma(x)\|
\right)\text{-critical}.
}
$$

这个结论：

- 所有对象位于同一个点 $x$；
- 不要求 $r_2$ 光滑；
- 不要求将次梯度从 $z$ 运输到 $u$；
- 直接揭示 $\gamma$ 进入两个 value-gap 槽。

## 18.3 $\delta_A,\delta_2$ 的尺度

若 $A$ 在相关区域是 $M_A$-Lipschitz，且 $r_2$ 是 $M_2$-Lipschitz，则其相关次梯度有界：

$$
\|p_A\|\le M_A,
\qquad
\|p_2\|\le M_2.
$$

又因为

$$
x-u=\gamma p_A,
$$

$$
x-z=\gamma p_2,
$$

可以得到粗略上界

$$
\delta_A(x,\gamma)
=
O(\gamma M_A^2),
$$

$$
\delta_2(x,\gamma)
=
O(\gamma M_2^2).
$$

所以：

$$
\boxed{
\delta_\phi=O(\gamma),
\qquad
\delta_g=O(\gamma),
\qquad
\varepsilon=\|\nabla F_\gamma(x)\|.
}
$$

若相关函数额外光滑，还可能得到 $O(\gamma^2)$ 型 Bregman gap 上界，但非光滑一般情形中自然尺度是 $O(\gamma)$。

---

# 19. $\gamma$ 不能无条件视为常数

## 19.1 固定 $\gamma$ 的含义

若算法只保证

$$
\|\nabla F_\gamma(x)\|\to0
$$

而 $\gamma$ 固定，则统一证书变为

$$
\delta_\phi=O(\gamma),
$$

$$
\delta_g=O(\gamma),
$$

$$
\varepsilon\to0.
$$

两个 value-gap 不会随迭代次数趋于零。

所以固定 $\gamma$ 得到的是：

$$
\boxed{
\text{固定平滑代理问题的临界点，或原问题的固定精度近似临界点。}
}
$$

## 19.2 不同精度口径对应不同 $\gamma$

### 若要求标准残差 $O(\varepsilon)$

使用 Lemma 8 的 smooth transport，并假设相关范数有界，通常需要

$$
\gamma=O(\varepsilon).
$$

### 若要求统一 value-gap 为 $O(\varepsilon^2)$

若

$$
\delta_\phi,\delta_g=O(\gamma),
$$

则需要

$$
\boxed{
\gamma=O(\varepsilon^2).
}
$$

因此，“取 $\gamma$ 为常数”只适合讨论固定平滑目标的 stationarity，不适合直接宣称原始非光滑目标的任意精度复杂度。

---

# 20. S-MDCA 的 $\varepsilon^{-4}$ 从哪里来

## 20.1 S-MDCA 的两类随机误差

S-MDCA：

- 对 $H$-侧使用 Polyak 或 MVR；
- 用一个随机 proximal-gradient 步近似
  $$
  u^*(x^t)=\operatorname{prox}_{\gamma(G+r_1)}(x^t).
  $$

因此存在两类误差：

1. $H$-侧估计器误差；
2. $G$-侧 proximal tracking error。

## 20.2 关键噪声项

其定理包含类似

$$
\frac{\eta_1M^2}{\gamma}
$$

的项，其中：

- $M^2$ 是 $G$-侧随机梯度方差；
- $\eta_1$ 是内层单步 proximal-gradient 步长；
- $1/\gamma$ 来自强凸 prox 子问题的尺度。

为了使该项小于 $\varepsilon^2$，必须取

$$
\eta_1
=
O\left(
\frac{\gamma\varepsilon^2}{M^2}
\right).
$$

外层步长又受到 $\eta_1$ 限制，因此

$$
\eta_0
=
O\left(
\frac{\gamma\varepsilon^2}{M^2}
\right).
$$

下降项

$$
\frac{\Phi_0}{\eta_0T}
\le
\varepsilon^2
$$

要求

$$
\boxed{
T
=
O\left(
\frac{\Phi_0M^2}
{\gamma\varepsilon^4}
\right).
}
$$

## 20.3 为什么 MVR 没有把它变成 $\varepsilon^{-3}$

MVR 只减少 $H$-侧噪声。

但限制 $\eta_1$ 的是 $G$-侧单步随机 prox-gradient 噪声：

$$
\frac{\eta_1M^2}{\gamma}.
$$

因此，即使 $H$-侧项达到

$$
O(\varepsilon^{-3}),
$$

整体仍被

$$
O\left(
\frac1{\gamma\varepsilon^4}
\right)
$$

限制。

所以：

$$
\boxed{
\varepsilon^{-4}
\text{ 来自单侧方差缩减和 $G$-侧 tracking noise。}
}
$$

它不是 Moreau 平滑化本身的不可避免下界。

若对 $G$-侧也使用 MVR/PAGE/SPIDER 型估计器，固定 $\gamma$ 下有可能恢复 $\varepsilon^{-3}$。

## 20.4 转回原问题后的复杂度

论文报告的 $\varepsilon^{-4}$ 通常固定 $\gamma$。

若按 smooth transport 要求

$$
\gamma=\Theta(\varepsilon),
$$

则直接代入显示至少出现

$$
O(\varepsilon^{-5})
$$

量级。

若按统一 value-gap 要求

$$
\gamma=\Theta(\varepsilon^2),
$$

则直接代入显示至少出现

$$
O(\varepsilon^{-6})
$$

量级。

这里“至少”是因为 $\Phi_0$、$L_\gamma=L+2/\gamma$ 和其他常数也可能继续依赖 $\gamma$。正式端到端结论必须完整追踪这些依赖。

---

# 21. 结果对比表

| 方法 | 每步核心操作 | 随机侧 | 非光滑负侧 | 目标度量 | 典型复杂度 | 关键限制 |
|---|---|---|---|---|---|---|
| DCA-PAGE critical-distance | 精确解 $A$-子问题 | $H$ | 要求 $r_2$ 光滑 | same-point distance | 在线可到 $\varepsilon^{-3}$ 主项 | 大 anchor batch；精确子问题 |
| DCA-PAGE lagged gap | 精确解 $A$-子问题 | $H$ | 可非光滑 | one-sided FY gap | gap 平方尺度下 $\varepsilon^{-3}$ | 缺失负侧 transport gap |
| MDCA Algorithm 1 critical-distance | 精确解 $A$-子问题 + 阻尼 | $H$ | 要求 $r_2$ 光滑 | same-point distance | 常数批量 $\varepsilon^{-3}$ | 精确 $A$-subproblem oracle |
| MDCA Algorithm 1 gap | 精确解 $A$-子问题 + 阻尼 | $H$ | 可非光滑 | one-sided FY gap | gap 平方尺度下 $\varepsilon^{-3}$ | 不是完整同点证书 |
| S-MDCA | 单步随机 tracking + Moreau 平滑 | $G,H$ | 通过 prox/平滑处理 | $\|\nabla F_\gamma\|$ | 固定 $\gamma$ 下 $\varepsilon^{-4}$ | $G$-侧噪声；$\gamma$ 转换成本 |
| 直接 PS-DCA + 普通 SGD | 单次 $\operatorname{prox}_h$ | $f$ | $g$ 可非光滑 | $(0,\delta_g,\varepsilon)$ | $\varepsilon^{-4}$ | 独立噪声底 |
| 直接 PS-DCA + MVR | 单次 $\operatorname{prox}_h$ | $f$ | $g$ 可非光滑 | $(0,\delta_g,\varepsilon)$ | 目标：常数批量 $\varepsilon^{-3}$ | 需完成严格 Lyapunov 与参数证明 |

---

# 22. 建议的论文主线

当前讨论可以组织成四个核心理论模块。

## 22.1 模块一：分解变换与证书坐标变换

### 定理 A：共同移位等价性

证明：

$$
\text{shifted exact DCA}
\equiv
\text{original exact proximal DCA}.
$$

### 定理 B：统一证书变换

证明同一个点满足

$$
\left(
0,\delta_g,\frac{\|s\|}{\gamma}
\right)
$$

相对于原始分解，以及

$$
\left(
0,\delta_g+\frac{\|s\|^2}{2\gamma},0
\right)
$$

相对于 shifted 分解。

### 理论意义

说明 DC 分解会改变：

- 算法子问题；
- oracle 放置；
- 临界性证书中误差的分配方式；
- 复杂度常数。

## 22.2 模块二：现有 gap 的完整解释

### Proposition A

证明 MDCA/DCA-PAGE gap 等于

$$
\Phi_A(x^{t+1},q^t).
$$

### Proposition B

证明 deterministic exact DCA 中该 gap 每步为零。

### Proposition C

给出反例，说明 lagged gap 为零不推出当前点临界。

### Proposition D

补全为

$$
(\delta_A,\delta_B,0)
$$

或

$$
(0,\delta_B,\|e^t\|)
$$

的同点统一证书。

## 22.3 模块三：直接 stochastic PS-DCA 的模块化定理

算法：

$$
x^{k+1}
=
\operatorname{prox}_{\eta h}
\left(
x^k-\eta(d^k-v^k)
\right).
$$

主定理应首先保持估计器无关：

$$
\mathbb E\Phi_\phi=0,
$$

$$
\mathbb E\Phi_g
\le
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V_K,
$$

$$
\mathbb E\|u-v\|^2
\lesssim
\frac{\Delta_0}{\eta K}
+
\bar V_K.
$$

随后分别代入：

- 独立 mini-batch SGD；
- PAGE；
- SARAH；
- STORM/MVR；
- 可能的 adaptive momentum。

## 22.4 模块四：常数批量 MVR 的 $\varepsilon^{-3}$

需要正式证明：

$$
\bar V_K
\lesssim
\frac{V_0}{\alpha K}
+
\frac{\Delta_0}{\eta K}
+
\frac{\alpha\sigma^2}{b}
$$

在

$$
\eta^2L_f^2
\lesssim
\alpha b
$$

下成立。

然后选择：

$$
b=O(1),
$$

$$
\alpha=\Theta(\varepsilon^2/\sigma^2),
$$

$$
\eta=\Theta(\varepsilon/(L_f\sigma)),
$$

$$
K=\Theta(L_f\sigma\Delta_0/\varepsilon^3).
$$

最终得到：

$$
\mathbb E\Phi_\phi=0,
$$

$$
\mathbb E\Phi_g=O(\eta\varepsilon^2),
$$

$$
\mathbb E\|u-v\|^2\le O(\varepsilon^2).
$$

---

# 23. 需要正式检查的技术点

以下内容不能仅凭讨论直接写成最终 theorem，必须在论文证明中逐项核对。

## 23.1 过滤族与条件期望

必须明确：

- $x^{k+1}$ 是否在采样 $I_{k+1}$ 前确定；
- MVR 的两个梯度是否使用同一批独立样本；
- $v^k$ 是否对当前过滤族可测；
- 输出随机索引是否独立于算法随机性。

## 23.2 MVR 递推的常数

需要确认：

$$
V_{k+1}
\le
(1-\alpha)V_k
+
\frac{2L_f^2}{b}\|s^k\|^2
+
\frac{2\alpha^2\sigma^2}{b}
$$

中的常数是否需要：

- $(1-\alpha)^2$；
- $2(1-\alpha)^2L_f^2/b$；
- 额外 covariance 项；
- 不同的 averaged smoothness 常数。

这些不会改变主指数，但会影响可行参数区域。

## 23.3 下降不等式中的估计器偏差

当前下降证明只使用路径上的误差向量

$$
e^k=\nabla f(x^k)-d^k,
$$

不要求

$$
\mathbb E_k[e^k]=0.
$$

这是 MVR 适用的关键。

正式证明中应避免在不必要处使用无偏性。

## 23.4 初始批量

项

$$
\frac{V_0}{\alpha K}
$$

需要明确处理。

可选方案：

1. 取
   $$
   b_0=\Theta(\sigma^2/\varepsilon^2),
   $$
   使 $V_0=O(\varepsilon^2)$；

2. 直接把 $V_0$ 保留在复杂度中；

3. 使用一次递归 warm-up；

4. 使用 normalized initialization。

## 23.5 $\delta_g$ 的目标尺度

应先决定论文最终采用：

- $\mathbb E\delta_g\le\varepsilon$；
- $\mathbb E\delta_g\le\varepsilon^2/L$；
- $\mathbb E\delta_g\le c\eta\varepsilon^2$；
- 或者直接报告完整参数依赖，不强行统一成单一 $\varepsilon$。

最严谨的做法是首先报告参数化结果：

$$
\left(
0,
\frac{\Delta_0}{K}+\frac{\eta}{2}\bar V_K,
\sqrt{
C\left(
\frac{\Delta_0}{\eta K}+\bar V_K
\right)
}
\right).
$$

然后再给 corollary 选择目标精度。

## 23.6 “最优性”下界

必须保证下界和上界使用相同：

- oracle 模型；
- 单样本 smoothness 假设；
- mean-squared smoothness 假设；
- bounded variance 假设；
- 批量计数方式；
- 目标残差定义；
- 期望形式。

否则只能说“匹配已知最优指数”，不能说“在本文度量下最优”。

---

# 24. 当前最准确的研究判断

## 24.1 关于共同二次移位

正确判断是：

> **MDCA 的 WLOG 强凸化可以解释为原始分解上的 proximal DCA，但只有共同移位贡献的强凸参数才对应显式 proximal 参数。**

## 24.2 关于 Algorithm 1 是否就是随机 proximal-gradient

准确判断是：

> **一般不是。Algorithm 1 是精确凸子问题 oracle 方法。只有 quadratic-shift 等特殊分解使正侧子问题具有闭式 prox 时，它才退化为 proximal-gradient 类更新。**

## 24.3 关于 gap 在确定性情况下是否为零

准确判断是：

> **对确定性精确 DCA 子问题解，该 lagged one-sided gap 每一步为零。对一般单步 proximal-gradient 更新，该 gap 不一定为零，除非该单步更新恰好等于完整 DCA 子问题解。**

## 24.4 关于 gap theorem 的价值

准确判断是：

> **gap theorem 的数值上界可以有意义，因为它量化随机估计器造成的子问题不一致；但它不能单独证明完整的非光滑同点临界性。**

## 24.5 关于我们的统一解释

准确判断是：

> **统一证书不是简单地“换一种解释现有 gap”，而是补上了现有 one-sided gap 缺失的负侧 transported slack，并允许把随机误差、proximal 移动和平滑化误差统一放入三个槽。**

## 24.6 关于直接单循环算法

准确判断是：

> **直接分析 $f+h-g$ 的 stochastic proximal-gradient/subgradient 算法是独立于 MDCA exact-subproblem 路线的算法贡献。它在 $g$ 非光滑时仍能构造同点证书，并且 MVR 有希望给出常数批量 $\varepsilon^{-3}$。**

## 24.7 关于 $\varepsilon^{-3}$

准确判断是：

> **应先给出统一证书对 $(K,\eta,\alpha,b,V_0)$ 的完整依赖，再做参数平衡。只有在统一目标尺度和 oracle 成本后，才能比较不同论文中的 $\varepsilon^{-3}$。**

## 24.8 关于 S-MDCA 的 $\varepsilon^{-4}$

准确判断是：

> **该 $\varepsilon^{-4}$ 是固定 $\gamma$ 的平滑目标复杂度，并受 $G$-侧单步 stochastic prox-gradient 噪声限制。它不是原始非光滑 DC 问题的无条件 $\varepsilon^{-4}$ 下界。**

---

# 25. 最终研究路线

建议按以下顺序推进。

1. **先固定统一临界性定义。**

   明确三槽的尺度和期望形式。

2. **证明 decomposition/shift 的证书转换定理。**

   这是概念层贡献。

3. **严格重写 DCA-PAGE/MDCA gap。**

   给出 Fenchel–Young 表示、确定性退化、反例和补全证书。

4. **证明直接 PS-DCA 的 estimator-agnostic 模块化定理。**

   先不引入 STORM 细节。

5. **单独证明 MVR 的 Lyapunov 递推。**

   明确吸收条件
   $$
   \eta^2L_f^2\lesssim\alpha b.
   $$

6. **给出两种 $\varepsilon^{-3}$ 调参。**

   - 固定步长、大批量；
   - 缩小步长、常数批量。

7. **与 MDCA/DCA-PAGE 分 oracle 模型比较。**

   不把 exact-subproblem 方法和单步 prox-gradient 方法混为一类。

8. **重写 Moreau smoothing 的端到端解释。**

   明确
   $$
   \gamma
   $$
   对原问题证书的依赖。

9. **最后做下界 reduction。**

   在此之前不直接宣称统一度量最优。

---

# 26. 一句话总结

> **MDCA 的主算法是带阻尼和 MVR 的精确 DCA 子问题方法；其 critical-distance $\varepsilon^{-3}$ 是有效的同点结果，但其 lagged gap 只测量正侧随机子问题不一致。共同二次移位揭示了 exact DCA 与 proximal DCA 的等价性，也揭示了统一证书中 value-slack 与 vector-residual 的分解依赖。对直接模型 $f+h-g$，单步 stochastic proximal-gradient/subgradient 方法可以逐路径得到 $\delta_\phi=0$，并将复杂度问题归结为控制平均估计误差 $\bar V_K$。普通随机梯度给出 $\varepsilon^{-4}$，MVR 在联合调节动量系数与步长后有望给出常数批量的 unified-certificate $\varepsilon^{-3}$。Moreau 平滑化中的 $\gamma$ 必须进入端到端复杂度，固定 $\gamma$ 的 $\varepsilon^{-4}$ 不能直接解释为原始非光滑 DC 问题的复杂度。**

---

# 参考文献与核对对象

1. *Stochastic Difference-of-Convex Optimization with Momentum*，重点核对：
   - Algorithm 1；
   - Assumptions 1–4；
   - Lemmas 2、4、5、6；
   - Theorems 2、4、5；
   - Appendix G, Lemma 8。

2. *Improved Rates for Stochastic Variance-Reduced Difference-of-Convex Algorithms*，重点核对：
   - quadratic-shift 分解 (S)；
   - Algorithm 1；
   - Definition 6；
   - Definition 12；
   - gap analysis；
   - online PAGE complexity。

3. Xu et al., *Stochastic Optimization for DC Functions and Non-smooth Non-convex Regularizers with Non-asymptotic Convergence*，重点核对：
   - stagewise proximal DC；
   - proximal mapping residual；
   - nearly critical point；
   - smoothing parameter 与原问题精度的转换。

4. Maskan et al., *Revisiting Frank-Wolfe for Structured Nonconvex Optimization*，重点核对：
   - decomposition dependence；
   - quadratic-shift 导致 projected-gradient/proximal-point 两类算法；
   - gap 对分解的依赖。
