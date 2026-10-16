# 不可消除的伪临界点：二维例子

日期：2026-10-16。助手推导，尚未经合作者核对。文献新颖性未核实（需查 Demyanov–Rubinov 拟微分与 Pallaschke–Urbański、Scholtes 的极小对理论）。

## 命题

令

$$
F_0(x)=\max\{0,x_1,x_2\}-\max\{0,-x_1,-x_2\},\qquad x\in\mathbb R^2 .
$$

则对 $F_0$ 的**任意**凸分解 $F_0=\phi-g$（$\phi,g$ 有限凸），都有 $\partial\phi(0)\cap\partial g(0)\neq\emptyset$，但

$$
0\notin\partial_C F_0(0)=\operatorname{conv}\{(1,0),(0,1),(1,1)\},\qquad \operatorname{dist}\bigl(0,\partial_C F_0(0)\bigr)=1/\sqrt2 .
$$

全局版本：$F=F_0+3\max\{\lVert x\rVert-1,0\}$ 下有界，存在分量全局 Lipschitz 的分解，并且在原点附近 $F=F_0$，结论不变（证明只用 $0$ 处的方向导数）。

## 证明

记 $A=\partial\phi(0)$，$B=\partial g(0)$，$\gamma=\sigma_B=g'(0;\cdot)$。$F_0$ 正齐次，因此 $\sigma_A=F_0+\gamma$。

**第一步：交集条件。** 对紧凸集，$A\cap B\neq\emptyset$ 当且仅当对所有 $d$ 有 $\sigma_A(d)+\sigma_B(-d)\ge0$，即

$$
F_0(d)+w_B(d)\ge0,\qquad w_B(d):=\gamma(d)+\gamma(-d).
$$

**第二步：凹折痕迫使 $B$ 含有长度下界的面。** 在单位圆上把正齐次函数写成角度的函数。$\sigma_A=F_0+\gamma$ 为支撑函数，其 $h+h''$ 是非负测度；在角度 $\theta_0$ 处的原子等于 $A$ 在法向 $\theta_0$ 上暴露面的长度。$F_0$ 的负原子（凹折痕）为：

| 方向 | $F_0$ 的原子 |
|---|---|
| $(1,0)$ | $-1$ |
| $(0,1)$ | $-1$ |
| $(-1,-1)/\sqrt2$ | $-\sqrt2$ |

因此 $B$ 在法向 $(1,0)$ 上暴露一条长度不小于 $1$ 的竖直线段，在法向 $(0,1)$ 上暴露一条长度不小于 $1$ 的水平线段，在法向 $(-1,-1)$ 上暴露一条沿 $(1,-1)$、长度不小于 $\sqrt2$ 的线段。

**第三步：宽度下界。** 对 $d=(a,b)$，三条线段在 $d$ 上的投影长度分别为 $\lvert b\rvert$、$\lvert a\rvert$、$\lvert a-b\rvert$，故

$$
w_B(d)\ge\max\{\lvert a\rvert,\lvert b\rvert,\lvert a-b\rvert\}.
$$

**第四步：逐象限比较。** $F_0$ 在第一象限为 $\max(a,b)\ge0$，在第二、四象限为 $a+b$，在第三象限为 $\min(a,b)$。
- 第一象限：$F_0(d)\ge0$，条件自动成立。
- 第三象限：$-F_0(d)=\max(\lvert a\rvert,\lvert b\rvert)\le w_B(d)$。
- 第二象限（$a\le0\le b$）：$-F_0(d)=\lvert a\rvert-b\le\lvert a\rvert\le w_B(d)$；第四象限对称。

于是第一步的条件对所有 $d$ 成立，$0\in A-B$。

Clarke 次微分：$F_0$ 在原点附近各区域的梯度为 $e_1,e_2,(1,1)$，故 $\partial_C F_0(0)=\operatorname{conv}\{e_1,e_2,(1,1)\}$，最小范数元为 $(1/2,1/2)$。$\square$

## 对照：一维中存在一个分解，同时消除所有非 Clarke 伪临界点

（助手推导，待核。）设 $F:\mathbb R\to\mathbb R$ 为 DC，$F'$ 局部有界变差。取 $F'$ 的 Jordan 分解 $F'=c+V^+-V^-$，$V^\pm$ 单调不减且变差极小，令 $\phi'=c+V^+$，$g'=V^-$。在任意点 $x_0$：

- 凹折痕（$F'$ 向下跳）：$\phi'$ 在 $x_0$ 连续，$g'$ 跳跃。DC 临界 ⟺ $\phi'(x_0)\in[g'(x_0^-),g'(x_0^+)]$ ⟺ $F'(x_0^+)\le0\le F'(x_0^-)$ ⟺ $0\in\partial_C F(x_0)$。
- 凸折痕：$g'$ 连续，$\phi'$ 跳跃，同理 DC 临界 ⟺ $F'(x_0^-)\le0\le F'(x_0^+)$ ⟺ $0\in\partial_C F(x_0)$。
- 可微点：DC 临界 ⟺ $F'(x_0)=0$。

所以在 Jordan 分解下，每一点都有“DC 临界 ⟺ Clarke 驻点”。由于 Jordan 分解的变差极小，若 $F$ 有某个分量 Lipschitz 有界的分解，Jordan 分解的分量界不超过其常数倍。凹折痕处的局部极大（如 $-\lvert x\rvert$ 在 $0$）仍是 DC 临界，但它本身是 Clarke 驻点，不属于这里讨论的伪临界。

对照二维的 $F_0$：一维中一个规范分解可以同时消除全部非 Clarke 伪临界；从二维起，存在任何分解都消除不了的点。

## 含义与待做

- 伪临界性可以与分解无关：任何分解下的 DCA 型证书在 $0$ 处都已精确满足，但 $F_0$ 沿 $(-1,0)$ 以斜率 $1$ 下降。
- 由 Minkowski 和的单调性，若 $(A_0,B_0)\le(A,B)$ 为等价的更小对，则 $A-B\supseteq A_0-B_0$。因此“对所有分解临界”可能由 $F'(x;\cdot)$ 的极小拟微分对刻画。$\mathbb R^2$ 中极小对在平移意义下唯一（Scholtes 1992，待核），高维不唯一。高维刻画及其计算复杂度是待做问题。
