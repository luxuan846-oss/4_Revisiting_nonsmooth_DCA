> 历史材料：按原文保存。证明状态、文献判断与行号属于当时版本；当前状态见 `notes/progress/PROJECT_STATUS.md`，本次整理未重新证明其结论。

# Derivation Package: Proof Sketch of the Weakly Convex Reduction

## Target

逐行补全 `llx_nonsmooth.tex` 中 "Proof sketch" 帧（第 682--738 行）省略的推导，证明前一帧
"Reduction in Weakly Convex Optimization" 的完整命题：

设 $f$ 为 $\rho$-weakly convex（$\rho>0$），取典范 DC 分解
$$\phi(x)=f(x)+\tfrac{\rho}{2}\|x\|^2\ (\text{凸}),\qquad g(x)=\tfrac{\rho}{2}\|x\|^2\ (\text{凸、}\rho\text{-smooth}),$$
记 $r_{\delta_g}:=\sqrt{2\rho\delta_g}$，$\eta:=\widehat\varepsilon+r_{\delta_g}$。则：

- **(A)（等价转换）** $x$ 是 $(0,\delta_g,\widehat\varepsilon)$-critical
  $\iff \operatorname{dist}(0,\partial f(x))\le\eta$；
- **(B)（Moreau 推论）** 此时 $\|\nabla f_{1/(2\rho)}(x)\|\le 2\eta$，
  即 $x$ 是 nearly $2\eta$-stationary point。

## Status

COHERENT AS STATED。三步全部验证成立；slide 跳过了五个预备事实
（Fenchel gap 刻画、平移不变性、到球距离、hypomonotonicity、prox 一阶条件），
补上后每一行都是初等推导。(A) 双向成立；(B) 单向蕴含，与帧中 "Consequently" 措辞一致。

## Invariant Object

精度转换链：DC 值容差 $(\delta_g,\widehat\varepsilon)$ $\to$ 同点次梯度残差
$\operatorname{dist}(0,\partial f(x))$ $\to$ Moreau envelope 残差
$\|\nabla f_{1/(2\rho)}(x)\|$。
点 $x$ 全程不移动，容差按 $\eta=\widehat\varepsilon+\sqrt{2\rho\delta_g}$ 聚合、
再放大常数 $\frac{1}{1-\lambda\rho}\big|_{\lambda=1/(2\rho)}=2$。

## Assumptions

- $f:\mathbb R^n\to\mathbb R$ 有限值、$\rho$-weakly convex：$f+\tfrac{\rho}{2}\|\cdot\|^2$ 凸；
- $\delta_g>0$、$\widehat\varepsilon\ge0$、$\delta_\phi=0$；
- Moreau 步长 $\lambda=\tfrac{1}{2\rho}\in(0,\tfrac1\rho)$（Step 3 需要 $\lambda\rho<1$）；
- $\partial f$ 理解为 Clarke 次微分（有限值弱凸函数局部 Lipschitz，Clarke = limiting）。

## Notation

- $\partial_\delta h$：凸 $\delta$-次微分（tools 帧定义）；$\Phi_h(x,w)=h(x)+h^*(w)-\langle w,x\rangle$；
- $f_\lambda(x)=\min_y\{f(y)+\tfrac{1}{2\lambda}\|x-y\|^2\}$，$\operatorname{prox}_{\lambda f}$；
- $\mathbb B$：闭单位球；$[t]_+:=\max\{t,0\}$；
- $\operatorname{dist}(v,A)=\inf_{a\in A}\|v-a\|$，$\operatorname{dist}(A,B)=\inf_{a\in A,b\in B}\|a-b\|$。

## Derivation Strategy

先补五个 slide 隐含使用的预备事实（引理 A--E），再按 Step 1--3 逐行展开；
最后单列评注：假设去向、$\lambda$ 选择、方向性、光滑 $g$ 不可省的机制（$|x|$ 反例）。

## Derivation Map

1. 引理 A（gap 刻画）是 Step 1 中 "$v\in\partial_{\delta_g}g(x)\iff\|v-\rho x\|\le r_{\delta_g}$" 的依据；
2. Step 1 是纯恒等式：二次共轭 + 配方；
3. Step 2 用引理 B（平移不变）+ 引理 C（到球距离）+ 和法则，是恒等式；
4. Step 3 是命题：引理 D（弱凸 $\Rightarrow$ hypomonotone）+ 引理 E（prox 一阶条件）+ Cauchy--Schwarz；
5. 光滑性仅在 Step 1 出现——这是 nonsmooth $g$ 桥接失败的准确位置。

## Main Derivation

### 预备事实

**引理 A（Fenchel gap 刻画 $\delta$-次微分）.**
对闭正常凸 $h$、$\delta\ge0$：
$$v\in\partial_\delta h(\bar x)\iff\Phi_h(\bar x,v)\le\delta.$$
证：$v\in\partial_\delta h(\bar x)$ 定义为 $h(z)\ge h(\bar x)+\langle v,z-\bar x\rangle-\delta\ (\forall z)$
$\iff h(z)-\langle v,z\rangle\ge h(\bar x)-\langle v,\bar x\rangle-\delta\ (\forall z)$
$\iff \inf_z\{h(z)-\langle v,z\rangle\}\ge h(\bar x)-\langle v,\bar x\rangle-\delta$
$\iff -h^*(v)\ge h(\bar x)-\langle v,\bar x\rangle-\delta$
$\iff h(\bar x)+h^*(v)-\langle v,\bar x\rangle\le\delta$。$\square$

**引理 B（平移不变）.** $\operatorname{dist}(A+t,B+t)=\operatorname{dist}(A,B)$，
因 $(a+t)-(b+t)=a-b$。$\square$

**引理 C（到球的距离）.** 对任意非空 $A\subseteq\mathbb R^n$、$r\ge0$：
$$\operatorname{dist}(A,r\mathbb B)=\bigl[\operatorname{dist}(0,A)-r\bigr]_+.$$
证：单点情形，若 $\|a\|\le r$ 取 $b=a$ 得 $0$；若 $\|a\|>r$，则
$\|a-b\|\ge\|a\|-\|b\|\ge\|a\|-r$，且 $b=\tfrac{r}{\|a\|}a$ 达到，故
$\operatorname{dist}(a,r\mathbb B)=[\|a\|-r]_+$。再对 $a\in A$ 取下确界，
$[\cdot-r]_+$ 单调连续，与下确界可交换。$\square$

**引理 D（弱凸 $\iff$ $\rho$-hypomonotone）.**
$$\langle q-w,x-y\rangle\ge-\rho\|x-y\|^2,\qquad\forall q\in\partial f(x),\ w\in\partial f(y).$$
证：$\phi=f+\tfrac{\rho}{2}\|\cdot\|^2$ 凸且 $\partial\phi(x)=\partial f(x)+\rho x$
（光滑项和法则）。凸次微分单调，对 $q+\rho x\in\partial\phi(x)$、$w+\rho y\in\partial\phi(y)$：
$$\langle(q+\rho x)-(w+\rho y),x-y\rangle\ge0
\iff\langle q-w,x-y\rangle\ge-\rho\|x-y\|^2.\ \square$$

**引理 E（prox 一阶条件与 envelope 梯度）.**
$\lambda\in(0,\tfrac1\rho)$ 时 $f+\tfrac{1}{2\lambda}\|\cdot-x\|^2$ 为
$(\tfrac1\lambda-\rho)$-强凸，$y=\operatorname{prox}_{\lambda f}(x)$ 唯一存在，且
$$0\in\partial f(y)+\tfrac{1}{\lambda}(y-x)
\ \Longrightarrow\
w:=\lambda^{-1}(x-y)\in\partial f(y),
\qquad \nabla f_\lambda(x)=w.$$
（第二式为 Danskin 定理。）$\square$

### Step 1：二次 Fenchel gap（恒等式）

$$g^*(v)=\sup_z\{\langle v,z\rangle-\tfrac{\rho}{2}\|z\|^2\}
=\tfrac{1}{\rho}\|v\|^2-\tfrac{1}{2\rho}\|v\|^2
=\tfrac{1}{2\rho}\|v\|^2,$$
驻点 $z^\star=v/\rho$。于是
$$\Phi_g(x,v)=\tfrac{\rho}{2}\|x\|^2+\tfrac{1}{2\rho}\|v\|^2-\langle v,x\rangle
=\tfrac{1}{2\rho}\|v-\rho x\|^2,$$
最后一步配方直接验证。由引理 A：
$$v\in\partial_{\delta_g}g(x)\iff\tfrac{1}{2\rho}\|v-\rho x\|^2\le\delta_g
\iff\|v-\rho x\|\le\sqrt{2\rho\delta_g}=:r_{\delta_g},$$
即 $\partial_{\delta_g}g(x)=\rho x+r_{\delta_g}\mathbb B$：以唯一精确次梯度 $\rho x$
为球心的闭球，值容差按 $\sqrt{\cdot}$ 速率变成对偶半径。$\delta_g=0$ 应回
$\partial g(x)=\{\rho x\}$，自洽。

### Step 2：平移两集合（恒等式）

和法则 $\partial\phi(x)=\partial f(x)+\rho x$（$\phi$ 凸，二次项 $C^1$）。
由引理 B（同时平移 $-\rho x$）与引理 C：
$$\operatorname{dist}\bigl(\partial\phi(x),\partial_{\delta_g}g(x)\bigr)
=\operatorname{dist}\bigl(\partial f(x)+\rho x,\ \rho x+r_{\delta_g}\mathbb B\bigr)
=\operatorname{dist}\bigl(\partial f(x),\ r_{\delta_g}\mathbb B\bigr)
=\bigl[\operatorname{dist}(0,\partial f(x))-r_{\delta_g}\bigr]_+.$$

展开 certificate（记 $d:=\operatorname{dist}(0,\partial f(x))$）：
$(0,\delta_g,\widehat\varepsilon)$-critical
$\iff[d-r_{\delta_g}]_+\le\widehat\varepsilon$。
若 $d\le r_{\delta_g}$ 左端为 $0$，条件自动成立；若 $d>r_{\delta_g}$ 条件为
$d\le r_{\delta_g}+\widehat\varepsilon$。合并两情形即 (A)：
$$d\le\eta:=\widehat\varepsilon+r_{\delta_g}.$$

显式向量版本（同一事实的几何）：写 $u=q+\rho x$（$q\in\partial f(x)$）、
$v=\rho x+\xi$（$\|\xi\|\le r_{\delta_g}$），则 $\|u-v\|=\|q-\xi\|$。
最优 $\xi$ 是 $q$ 在球 $r_{\delta_g}\mathbb B$ 上的投影：
$\|q\|\le r_{\delta_g}$ 时取 $\xi=q$（距离 $0$），
否则取 $\xi=\tfrac{r_{\delta_g}}{\|q\|}q$（距离 $\|q\|-r_{\delta_g}$）。

### Step 3：Moreau envelope 残差（命题，单向）

由 (A) 存在 $q\in\partial f(x)$、$\|q\|\le\eta$
（$\partial f(x)=\partial\phi(x)-\rho x$ 非空紧，inf 可达）。
取 $\lambda>0$，记 $y=\operatorname{prox}_{\lambda f}(x)$、
$w=\nabla f_\lambda(x)=\lambda^{-1}(x-y)\in\partial f(y)$（引理 E）。

$q$ 在 $x$ 处、$w$ 在 $y$ 处，是**两个点上的次梯度**。引理 D 连接它们：
$$\langle q-w,x-y\rangle\ge-\rho\|x-y\|^2.$$
代入 $x-y=\lambda w$：
$$\lambda\langle q-w,w\rangle\ge-\rho\lambda^2\|w\|^2
\ \Longrightarrow\
\lambda\langle q,w\rangle\ge(1-\lambda\rho)\lambda\|w\|^2
\ \Longrightarrow\
\langle q,w\rangle\ge(1-\lambda\rho)\|w\|^2.$$
Cauchy--Schwarz：$(1-\lambda\rho)\|w\|^2\le\langle q,w\rangle\le\|q\|\|w\|$。
$w=0$ 平凡；$w\ne0$ 且 $\lambda\rho<1$ 时
$$\|w\|\le\frac{\|q\|}{1-\lambda\rho}.$$
取 $\lambda=\tfrac{1}{2\rho}$（$1-\lambda\rho=\tfrac12$）：
$$\|\nabla f_{1/(2\rho)}(x)\|=\|w\|\le2\|q\|\le2\eta
=2\bigl(\widehat\varepsilon+\sqrt{2\rho\delta_g}\bigr).\ \blacksquare$$

### Step 3 的最简形式（凸伴随函数 + 单调性，四行）

hypomonotonicity 引理可以整个省去。令 $\phi=f+\tfrac{\rho}{2}\|\cdot\|^2$（凸），
则 $q+\rho x\in\partial\phi(x)$、$w+\rho y\in\partial\phi(y)$，
凸次微分单调给出
$$0\le\bigl\langle(q+\rho x)-(w+\rho y),\,x-y\bigr\rangle
=\lambda\langle q,w\rangle-\lambda(1-\lambda\rho)\|w\|^2,$$
（末步代入 $x-y=\lambda w$ 展开），即 $(1-\lambda\rho)\|w\|^2\le\langle q,w\rangle$，
Cauchy--Schwarz 收尾：$\|w\|\le\|q\|/(1-\lambda\rho)$。

**点关系（本步唯一的几何内容）：** $\nabla f_\lambda(x)=\lambda^{-1}(x-y)=w$，
Moreau 梯度就是 prox 位移的缩放，故证 $\|\nabla f_\lambda(x)\|$ 小与证
prox 位移 $\|x-y\|$ 小是同一句话。结论
$$\|x-y\|=\lambda\|w\|\le\frac{\lambda\|q\|}{1-\lambda\rho}
\ \xrightarrow{\ \lambda=\frac{1}{2\rho}\ }\ \|x-y\|\le\frac{\eta}{\rho},\qquad \|w\|\le2\eta.$$
凸情形（$\rho=0$）整步退化为单行 $\|w\|\le\|q\|$（因子 $1$，$f(z)=\|z\|$ 取等）；
弱凸性恰好只付出因子 $\frac{1}{1-\lambda\rho}=2$。
slide 中的「$\rho$-hypomonotonicity」即上面第一行移项后的等价写法，
可直接删去。

## Remarks and Interpretation

- **假设去向：** Step 1 只用 $g$ 二次（光滑）凸；Step 2 用和法则 + 平移不变；Step 3 用
  弱凸性（hypomonotonicity）与 $\lambda\rho<1$。
- **$\lambda=\tfrac{1}{2\rho}$：** 常数 $\tfrac{1}{1-\lambda\rho}$ 在
  $\lambda\uparrow\tfrac1\rho$ 时爆破；取中点给因子 $2$。几何含义：
  $\|w\|\le\varepsilon$ 蕴含存在 $y$ 使
  $\|x-y\|=\lambda\|w\|\le\tfrac{\varepsilon}{2\rho}$ 且
  $\operatorname{dist}(0,\partial f(y))\le\varepsilon$——$x$ 附近有近似驻点，
  即 nearly stationarity 的本义（Davis--Drusvyatskiy 的标准取法）。
- **方向性：** Step 1--2 是等价；Step 3 单向。帧中 "Consequently ... is also" 与此一致。
- **光滑 $g$ 不可省（alertblock 的机制）：** Step 1 的同点球结构依赖 $g^*$ 强凸。
  一般 $L_g$-光滑凸 $g$ 同样有
  $\partial_{\delta_g}g(x)\subseteq\partial g(x)+\sqrt{2L_g\delta_g}\,\mathbb B$
  （由 $g^*$ 的 $\tfrac{1}{L_g}$-强凸性：
  $g^*(v)\ge g^*(w_g)+\langle x,v-w_g\rangle+\tfrac{1}{2L_g}\|v-w_g\|^2$，$w_g\in\partial g(x)$，
  代入得 $\Phi_g(x,v)\ge\tfrac{1}{2L_g}\|v-w_g\|^2$）。
  而 merely Lipschitz 凸 $g$ 失败：$g(x)=|x|$、$x=\tfrac{\delta}{2}>0$、$v=-1$ 时
  $\Phi_g(x,v)=x(1-v)=\delta$，故 $v\in\partial_\delta g(x)$，但
  $\operatorname{dist}(v,\partial g(x))=2\gg\sqrt{2\delta}$。
  值容差无法按 $\sqrt{\delta}$ 速率换算成同点范数容差；保住的只是空间型结论
  （$v=-1\in\partial g(0)$，$\|x-0\|=\tfrac{\delta}{2}\le\sqrt{2\delta}$：
  接近邻近点处的精确次微分，Goldstein 型）。
- **标度：** $\eta$ 中 $\widehat\varepsilon$（对偶范数）线性进入、$\delta_g$（值）以
  $\sqrt{2\rho\,\cdot}$ 换算。要 $\eta=O(\varepsilon_{\rm stat})$ 需
  $\widehat\varepsilon=O(\varepsilon_{\rm stat})$、$\delta_g=O(\varepsilon_{\rm stat}^2/\rho)$，
  即 $\delta_g=O(\varepsilon^2)$ 自然标度，与 complexity 帧的 scaling 一致。

## Boundaries and Non-Claims

- (B) 无逆命题：小 Moreau 残差不给出 $\operatorname{dist}(0,\partial f(x))$ 小。
- 本推导是逐点 certificate conversion，不是 oracle reduction
  （prox 需额外子问题；DC component-wise oracle 与整体 subdifferential oracle 互不支配，
  不能据此继承 Li--Pan 下界）。
- 等价 (A) 依赖 $\delta_\phi=0$；$\delta_\phi>0$ 时二次 slack
  $\tfrac{\rho}{2}\|z-x\|^2$ 介入，只有 $\partial_{\delta_\phi}f(x)+\rho x\subseteq\partial_{\delta_\phi}\phi(x)$
  的单侧包含。
- 二次 $g$ 非全局 Lipschitz，本帧是解释性桥接（连接 certificate 与经典弱凸驻性），
  并非 $\mathcal D(\Delta,L,G)$ 类的成员。

## Open Risks

- 推导本身无风险；slide 层面仅两处笔误级省略：Step 2 第一个等号未注明平移不变与和法则，
  Step 3 未注明 $w\in\partial f(y)$ 的出处（prox 一阶条件）。
