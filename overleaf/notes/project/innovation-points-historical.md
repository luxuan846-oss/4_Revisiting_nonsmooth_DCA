> 历史材料：按原文保存。证明状态、文献判断与行号属于当时版本；当前状态见 `notes/progress/PROJECT_STATUS.md`，本次整理未重新证明其结论。

# 文章创新点总结：非光滑 DC 驻点与 DCA 复杂度

> 本文档汇总论文的核心创新点与表述口径，依据 sample 原稿整理。

**核心创新位于“驻点目标的重新设计”和“复杂度分析框架”，算法更新本身不是最主要的贡献。**

文章的完整逻辑链是：

\[
\boxed{
\text{传统同点 DC 驻点存在有限查询障碍}
\;\Longrightarrow\;
\text{构造可计算的三参数证书}
\;\Longrightarrow\;
\text{统一分析 DCA 类方法}
\;\Longrightarrow\;
\text{恢复 }O(\varepsilon^{-2})\text{ 与 }O(\varepsilon^{-3})\text{ 基准}
}
\]

这正对应计算非光滑分析中的核心问题：**什么驻点概念既具有最优性含义，又能被算法在有限时间内计算和验证。** 现有文献也指出，DC criticality 虽然比 Clarke stationarity 更容易验证，但依赖具体 DC 分解；一般非光滑驻点还可能缺少可执行的有限时间终止准则。

---

## 一、研究的是什么问题

考虑

\[
\min_{x\in\mathbb R^n}F(x):=\phi(x)-g(x),
\]

其中：

* $\phi$ 和 $g$ 都是 proper closed convex functions；
* 两个分量都允许非光滑；
* 因此 $F$ 一般同时非凸、非光滑；
* 尤其关注 **$g$ 非光滑** 时的有限时间复杂度。

经典 DC criticality 是

\[
0\in \partial\phi(x)-\partial g(x).
\]

相应的近似形式是

\[
\operatorname{dist}\bigl(
0,\partial\phi(x)-\partial g(x)
\bigr)\le \varepsilon.
\]

问题在于，这个 residual 对有限时间算法不友好。例如在折点附近，迭代点已经无限接近最优解，次微分距离仍可能保持为常数量级。因此，“序列最终收敛到驻点”和“可以在有限时刻检测到一个小 residual 点”是两个不同结论。相关综述也明确把**寻找驻点、计算次微分和验证驻点**区分为三个计算问题。

---

## 二、具体做了什么

### 1. 证明传统 $\varepsilon$-criticality 存在有限查询障碍

考虑一个相当强的 component-wise DC oracle：

\[
\mathcal O_{\rm DC}(x)
:=
\bigl(\phi(x),g(x),u,v\bigr),
\qquad
u\in\partial\phi(x),\quad
v\in\partial g(x).
\]

这个 oracle 比只返回 $F(x)$ 和一个 Clarke subgradient 更强，因为算法可以分别看到两个凸分量。

结果表明：**即使 oracle 已经分别给出两侧函数值和次梯度，算法仍不能把经典 same-point $\varepsilon$-criticality 当作统一的有限时间目标。**

构造还有一个值得强调的点：在 $\phi$ 和 $g$ 两侧同时添加相同的隐藏 kink，目标函数

\[
F=\phi-g
\]

完全不变，但 DC criticality 会发生变化。由此可以构造一个点 $s$，满足

\[
0\in\partial\phi(s)-\partial g(s),
\qquad
0\notin\partial_C F(s).
\]

这同时揭示了：

* **DC criticality 的 decomposition dependence**；
* 传统同点 residual 的有限查询困难；
* DC oracle 更强也不能自动消除该困难。

不过，当前定理的准确表述是：固定 $(\Delta,L,G)$ 时，查询预算满足

\[
K\le cG/L.
\]

因此口头报告中更稳妥的说法是：

> **传统 DC residual 在所考虑的强 component-wise oracle 下存在有限预算障碍，不能直接作为统一的非渐近目标。**

暂时不要说成“在固定函数类上，对任意有限 $K$ 都绝对不可能”。

### 2. 提出三参数的统一 DC criticality

定义：

\[
\boxed{
\operatorname{dist}
\left(
\partial_{\delta_\phi}\phi(x),
\partial_{\delta_g}g(x)
\right)
\le\varepsilon
}
\]

并称 $x$ 为一个

\[
(\delta_\phi,\delta_g,\varepsilon)\text{-critical point}.
\]

利用 Fenchel–Young gap

\[
\Phi_h(x,w)
:=
h(x)+h^*(w)-\langle w,x\rangle,
\]

它等价于存在 $u,v$，使得

\[
\Phi_\phi(x,u)\le\delta_\phi,
\qquad
\Phi_g(x,v)\le\delta_g,
\qquad
|u-v|\le\varepsilon.
\]

三个参数分别具有明确含义：

| 参数 | 数学含义 | 算法含义 |
| ------------- | -------------------------------------- | --------------------------- |
| $\delta_\phi$ | $u$ 距离成为 $\phi$ 的精确次梯度还有多少 Fenchel gap | DCA 子问题的求解误差 |
| $\delta_g$ | 旧点的 $g$-次梯度迁移到新点产生的值误差 | 非光滑 $g$ 的结构性 transport cost |
| $\varepsilon$ | 两个近似 dual certificates 的距离 | 一阶驻点 mismatch |

这里最重要的设计是：**两个次梯度仍然放在同一个原始点 $x$，只沿函数值方向进行松弛。**

Goldstein stationarity 使用空间邻域：

\[
y\in B_\delta(x),
\]

而本定义使用同点上的 Fenchel-gap 松弛。两者对应不同的 relaxation axis：

\[
\text{Goldstein：空间松弛},
\qquad
\text{本文定义：值松弛}.
\]

### 3. 证明新定义不是任意放松

做了三类理论验证。

**精确一致性。** 当

\[
\delta_\phi,\delta_g,\varepsilon\to0,
\]

证书恢复

\[
0\in\partial\phi(x)-\partial g(x).
\]

因此这个定义在误差消失时回到 exact DC criticality。

**统一已有近似概念。** 框架可以容纳已有的：

* $\varepsilon$-criticality；
* nearby/nearly criticality；
* value-inexact DCA certificates；
* Frank–Wolfe-type DC gap；
* Goldstein stationarity。

例如，在 Lipschitz 条件下，一个 $(\delta,\varepsilon)$-Goldstein stationary point 可以转化为

\[
(2G_\phi\delta,\,2G_g\delta,\,\varepsilon)\text{-critical point}.
\]

反方向一般不成立，因为 DC criticality 依赖分解。若一个分量可微，即本文定义的 **faithful decomposition** 情形，则 DC criticality 与 Clarke stationarity 可以重新一致。

**解释传统 residual 的失败。** 例子

\[
\Psi(x)=\bigl||x|-1\bigr|
\]

说明：靠近非光滑最优点时，经典 critical-distance residual 仍可能保持 $O(1)$，但 Fenchel gap 连续趋于零。

因此新证书不仅用于证明复杂度，也可以作为更合理的算法诊断量。

### 4. 建立一个统一 DCA 分析恒等式

文章最核心的技术等式是：

\[
\boxed{
F(x^{k+1})-F(x^k)
=
\Phi_\phi(x^{k+1},v^k)
-\Phi_\phi(x^k,v^k)
-\Phi_g(x^{k+1},v^k)
}
\]

其中

\[
v^k\in\partial g(x^k).
\]

等价地，

\[
F(x^k)-F(x^{k+1})
=
\Phi_\phi(x^k,v^k)
+
\Phi_g(x^{k+1},v^k)
-
\Phi_\phi(x^{k+1},v^k).
\]

这个等式把每一步目标下降精确分配到三个量：

* 当前点的 $\phi$-side gap；
* 新点的 $g$-side transport gap；
* 子问题求解所注入的 $\phi$-side inexactness。

因此它比普通的 descent inequality 更强。它是一套 **certificate accounting identity**，也就是证书的精确记账公式。

Exact DCA、inexact DCA、proximal DCA、prox-subgradient DCA 和 stochastic DCA 都可以放进这一套账本中。

---

## 三、恢复了哪些复杂度结果

记

\[
\Delta_0:=F(x^0)-F^\star.
\]

### 复杂度汇总

| 方法 | 得到的证书 | 复杂度 |
| ------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Exact DCA | $\left(0,\frac{\Delta_0}{K},0\right)$ | $K=O(\Delta_0/\delta_g)$ |
| Inexact DCA | $\left(\sigma,\frac{\Delta_0}{K}+\sigma,0\right)$ | 外层 $O\!\left(\frac{\Delta_0}{\delta_g-\sigma}\right)$ |
| PS-DCA | $\left(0,\frac{\Delta_0}{K},O(K^{-1/2})\right)$ | $O\!\left(\max\{\Delta_0/\delta_g,\,L_f\Delta_0/\varepsilon^2\}\right)$ |
| Exact proximal DCA | $\left(0,\frac{\Delta_0}{K},\sqrt{\frac{\Delta_0}{\gamma K}}\right)$ | $O\!\left(\max\{\Delta_0/\delta_g,\,\Delta_0/(\gamma\varepsilon^2)\}\right)$ |
| 随机 minibatch | $(O(\varepsilon^2),O(\varepsilon^2),\varepsilon)$ | $O(\sigma^2L_f\Delta_0\,\varepsilon^{-4})$ SFO |
| MVR / recursive momentum | $(O(\varepsilon^2),O(\varepsilon^2),\varepsilon)$ | $O(\sigma L_f\Delta_0\,\varepsilon^{-3})$ SFO |

### 1. Exact DCA：$O(\delta_g^{-1})$

Exact DCA 每次精确求解

\[
x^{k+1}\in
\arg\min_x\{\phi(x)-\langle v^k,x\rangle\},
\qquad
v^k\in\partial g(x^k).
\]

由于 $v^k\in\partial\phi(x^{k+1})$，有

\[
\delta_\phi=0,\qquad \varepsilon=0.
\]

唯一剩余的误差来自 $v^k$ 从 $x^k$ 被迁移到 $x^{k+1}$ 后产生的 $g$-side Fenchel gap：

\[
\delta_g\le \frac{\Delta_0}{K}.
\]

因此

\[
K=O\left(\frac{\Delta_0}{\delta_g}\right).
\]

### 2. Proximal DCA：恢复确定性 $O(\varepsilon^{-2})$

Exact proximal DCA 得到

\[
\left(
0,\frac{\Delta_0}{K},
\sqrt{\frac{\Delta_0}{\gamma K}}
\right)\text{-critical}.
\]

因此取

\[
K=O(\varepsilon^{-2})
\]

时，可以同时得到

\[
\delta_g=O(\varepsilon^2),
\qquad
\text{mismatch}=O(\varepsilon).
\]

也就是：

\[
\boxed{
(0,O(\varepsilon^2),\varepsilon)
\quad\text{within}\quad
O(\varepsilon^{-2})\text{ iterations}.
}
\]

这就是**恢复确定性最优复杂度阶**的含义。

当 $g$ 进一步 $L_g$-smooth 时，

\[
\delta_g=O(\varepsilon^2/L_g)
\]

可以转换成经典同点 $\varepsilon$-stationarity。因此在 smooth $g$ 情形，确实恢复了通常的

\[
O(\varepsilon^{-2})
\]

一阶复杂度。

当 $g$ 非光滑时，恢复的是新定义下的

\[
(0,O(\varepsilon^2),\varepsilon)\text{-criticality},
\]

不能说算法在 $O(\varepsilon^{-2})$ 内找到了经典

\[
\operatorname{dist}
\bigl(0,\partial\phi(x)-\partial g(x)\bigr)\le\varepsilon
\]

的点。

### 3. 随机情形：恢复 $O(\varepsilon^{-4})$ 和 $O(\varepsilon^{-3})$

对于

\[
F(x)=f(x)+h(x)-g(x),
\qquad
f(x)=\mathbb E_\xi[f(x;\xi)],
\]

将所有随机误差压缩到平均均方估计误差

\[
\bar V
:=
\frac1K\sum_{k=0}^{K-1}
\mathbb E|d^k-\nabla f(x^k)|^2.
\]

最终证书满足

\[
\delta_\phi
=
\frac{\eta}{2}\bar V,
\]

\[
\delta_g
=
\frac{\Delta_0}{K}
+
\frac{\eta}{2}\bar V,
\]

以及

\[
\varepsilon_{\rm slot}
\le
r_\eta
\sqrt{
\frac1{a'_\eta}
\left(
\frac{\Delta_0}{K}
+\frac{\eta}{2}\bar V
\right)
}
+
\sqrt{\bar V}.
\]

这个结果揭示了一个重要机制：

\[
\boxed{
\bar V
\text{ 在线性尺度进入 Fenchel slots，}
\quad
\sqrt{\bar V}
\text{ 进入 mismatch slot。}
}
\]

因此，若要求 mismatch 为 $O(\varepsilon)$，必须控制

\[
\bar V=O(\varepsilon^2).
\]

**普通 minibatch。** 需要

\[
b=O(\sigma^2/\varepsilon^2),
\qquad
K=O(\varepsilon^{-2}),
\]

总 SFO 数是

\[
\boxed{
O(\sigma^2L_f\Delta_0\,\varepsilon^{-4}).
}
\]

**MVR / STORM 型递归动量。** 通过精度相关的参数：

\[
\alpha=\Theta(\varepsilon/\sigma),
\qquad
b=\Theta(\sigma/\varepsilon),
\]

并使用初始 batch

\[
\Theta(\sigma^2/\varepsilon^2),
\]

得到

\[
\boxed{
O(\sigma L_f\Delta_0\,\varepsilon^{-3})
}
\]

的总 SFO complexity。

这与随机非凸优化中常见的 benchmark 相符：普通 stochastic method 为 $O(\varepsilon^{-4})$，variance reduction 为 $O(\varepsilon^{-3})$。

注意：**constant-batch MVR 存在非零 variance floor，不能令 $\bar V\to0$**。$O(\varepsilon^{-3})$ 依赖上述 accuracy-tied batch 和 momentum 参数。

---

## 四、“恢复复杂度”应该怎样准确表述

恢复了两个基准。

### 确定性基准

在自然精度标度

\[
\delta_\phi,\delta_g=O(\varepsilon^2)
\]

下，直接处理非光滑 $g$ 的 proximal DCA 达到

\[
\boxed{O(\varepsilon^{-2})}.
\]

因此，**不需要先 smoothing $g$**，也能得到与 smooth nonconvex first-order methods 相同的复杂度指数。

### 随机基准

同样在

\[
\delta_\phi,\delta_g=O(\varepsilon^2),
\qquad
\text{mismatch}\le\varepsilon
\]

的标度下：

\[
\boxed{
O(\varepsilon^{-4})
\quad\text{普通 minibatch},
}
\]

\[
\boxed{
O(\varepsilon^{-3})
\quad\text{MVR/recursive momentum}.
}
\]

所以可以说：

> **新 criticality 使直接非光滑 DCA 恢复了 smooth/proximal optimization 的标准确定性和随机复杂度指数。**

这里“恢复”的对象是**复杂度指数和自然误差标度**。在 $g$ 非光滑时，它并不等于恢复经典 same-point residual。

---

## 五、创新点应该怎样讲

### 创新一：从算法设计提升到“目标—oracle”共同设计

文章首先说明传统目标存在问题，然后重新设计一个能够有限时间计算的目标。

这个逻辑比“提出一个新 DCA 变体”更完整：

\[
\text{不可计算性诊断}
\to
\text{新证书}
\to
\text{算法复杂度}.
\]

### 创新二：提出同点、双侧、三参数 Fenchel 证书

已有近似驻点常通过移动原始点来放松。本证书固定原始点，只放松两个凸分量的 Fenchel–Young equality。

并且它能够区分：

* 算法求解误差；
* 非光滑 transport error；
* dual mismatch。

这三个误差在很多已有 residual 中被混在一起。

### 创新三：用一个恒等式统一整个 DCA 家族

one-step identity 同时解释了：

* exact DCA 为什么只有 $\delta_g$；
* inexact DCA 的 $\delta_\phi$ 从哪里来；
* proximal DCA 的 $\varepsilon$ 从哪里来；
* smoothing bias 应该进入哪个 slot；
* stochastic variance 为什么同时产生一阶和二阶影响。

这是一种统一分析机制，不只是某个定理的技术引理。

### 创新四：解释 variance reduction 为什么必要

文章没有只给出 $O(\varepsilon^{-3})$ 数字，而是解释了：

\[
\bar V
\longmapsto
\begin{cases}
O(\bar V), & \delta_\phi,\delta_g,\\
O(\sqrt{\bar V}), & \varepsilon.
\end{cases}
\]

因此 mismatch slot 决定随机复杂度，variance reduction 才能把

\[
O(\varepsilon^{-4})
\]

改善到

\[
O(\varepsilon^{-3}).
\]

这是一个明确的机制性结论。

---

## 六、可以直接对老师这样介绍

> 我研究的是两个凸分量都可能非光滑的 DC 问题
> \[
> \min_x\phi(x)-g(x).
> \]
> 我首先考察传统的 same-point $\varepsilon$-criticality 是否适合作为有限时间目标。即使算法可以分别查询 $\phi$ 和 $g$ 的函数值与次梯度，稿件中的构造仍然给出了有限查询障碍。因此，经典 residual 无法直接支撑一般的非渐近复杂度分析。
>
> 为此，我定义了一个
> \[
> (\delta_\phi,\delta_g,\varepsilon)
> \]
> 三参数 criticality。它用两个 Fenchel–Young gap 表示两个分量的值误差，用 $\varepsilon$ 表示两侧 dual certificates 的 mismatch。该定义在三个误差趋零时恢复 exact DC criticality，并且可以统一已有的 near-criticality、Goldstein stationarity 和 Frank–Wolfe DC gap。
>
> 在算法分析上，我得到一个 DCA 的 one-step Fenchel-gap identity。这个恒等式可以统一分析 exact、inexact、proximal 和 stochastic DCA。由此，proximal DCA 在
> \[
> \delta_g=O(\varepsilon^2)
> \]
> 的自然标度下达到
> \[
> O(\varepsilon^{-2})
> \]
> 的确定性复杂度；随机 minibatch 达到
> \[
> O(\varepsilon^{-4}),
> \]
> 使用 MVR 递归动量后达到
> \[
> O(\varepsilon^{-3}).
> \]
> 核心结论是，在新的可计算证书下，即使 $g$ 非光滑，也不需要 smoothing 就可以恢复标准的一阶复杂度指数。

---

## 七、当前稿件必须收紧的地方

### 1. 约束问题目前还没有完成

Abstract 和 contributions 写了：

* general nonlinear/nonconvex constraints；
* constrained $O(\varepsilon^{-2})$；
* single-loop constrained method。

但正文中的原始约束已经被注释，constrained section 目前只有 assumption 和 certificate 草稿，算法、定理及证明尚未完成。

因此，当前可以稳定主张的是：

\[
\boxed{
\text{无约束 DC criticality}
+
\text{确定性/随机 DCA 复杂度}.
}
\]

约束 $O(\varepsilon^{-2})$ 目前不能作为已完成贡献。

### 2. Lower bound 的语言需要与定理一致

正文贡献写成“no finite-time algorithm”，但当前定理带有

\[
K\le cG/L
\]

的 horizon restriction。

建议改成：

> We establish a finite-query barrier for classical same-point DC criticality under a strong component-wise oracle.

若要保留完全的“finite-time unattainability”，还需要固定 $G$ 后覆盖任意 $K$ 的更强构造。

### 3. 强凸性与全局有界次梯度需要重新处理

稿件中同时假设：

\[
g\text{ 是 }\gamma\text{-strongly convex},
\]

以及

\[
\sup_x\sup_{v\in\partial g(x)}|v|\le G.
\]

在无界空间 $\mathbb R^n$ 上，这两个条件通常不相容。强凸函数的次梯度会随 $|x|$ 增长。给 $\phi$ 和 $g$ 同时加二次项也会破坏 bounded-subgradient assumption。

可选修正包括：

* 只在有界迭代区域内假设局部次梯度有界；
* 假设有效域或 level set 紧；
* 将 strong convexity 与 bounded-subgradient 分别用于不同定理；
* 移除“WLOG 同时成立”的表述。

这是当前最需要优先检查的技术点。

### 4. Stochastic smoothing 的 $O(\varepsilon^{-3})$ 仍是 conjecture

稿件已明确写出：

\[
L_\mu=L_f+\frac1\mu
\]

在

\[
\mu=\Theta(\varepsilon)
\]

时是否重新进入 drift condition 尚未完整处理。

因此可以讲：

* direct stochastic DCA 的 MVR $O(\varepsilon^{-3})$ 已有推导；
* smoothed stochastic method 的 $O(\varepsilon^{-3})$ 仍待完整 Lyapunov analysis。

### 5. “Optimal”建议暂时改成“matches the benchmark exponent”

确定性部分已经有 smooth hard-instance embedding，能够讨论 tightness up to condition number。

随机 $O(\varepsilon^{-3})$ 当前主要是与已有 online MVR rate 对齐。除非进一步给出针对**同一个 oracle model 和同一个三参数证书**的 lower bound，否则更稳妥的表述是：

> **matches the standard optimal stochastic exponent**

而不是：

> **we establish the optimal oracle complexity**。

---

## 本质总结

**这篇文章的主要理论贡献，是把“不可有限时间验证的经典 DC 驻点”替换为一个同点、双侧、可计算且渐近精确的 Fenchel-gap 证书，并据此统一恢复确定性 $O(\varepsilon^{-2})$ 和随机 MVR $O(\varepsilon^{-3})$ 的复杂度指数。**
