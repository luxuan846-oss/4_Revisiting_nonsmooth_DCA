> 历史材料：按原文保存。证明状态、文献判断与行号属于当时版本；当前状态见 `notes/progress/PROJECT_STATUS.md`，本次整理未重新证明其结论。

# Proof Skeleton: NAS / AC / NAC Slides

审校对象：`llx_nonsmooth.tex` 当前活动内容（源文件 SHA-256：
`9c0768193563155d890708e2304ca4a23c25cd3d012bedcce32387c70cc57abf`）。
默认编译结果为 9 页；附录源代码在 `\\ifshowappendix` 分支下另行核对。注释掉的旧草稿不属于当前 PDF 的证明范围。

## 1. 依赖图

```text
W1  F + (rho/2)||.||^2 convex, F proper/closed
 |\
 | \--> W2  lambda=1/(2 rho)<1/rho; Moreau prox unique; envelope C1
 |                 |
 |                 +--> M3  strong convexity of F(.)+rho||.-x||^2
 |
 +--> C1  canonical split phi=F+rho||.||^2, g=rho||.||^2
                   |
AC definition + convex epsilon-subdifferential (D1) ----+
                   |                                      |
                   +--> L1  AC <=> Moreau gap bound       |
NAC definition + witness attainment (D2) --> L2  NAC -> AC|
                   |                                      |
                   +--> L3  2G delta transport bound     |
NAS definition + local/global G-Lipschitz (W3) --> L4 NAS -> AC
                   |
L1 + M3 --> L5  gap -> Moreau-gradient bound
                   |
Q1 inner gap <= a --> L6  outer certificate bar-delta_t
                   |
L6 + telescoping + uniform random index --> T1 expected AC/NAS output
Q2 explicit projected strongly-convex subgradient method --> Q1
Q1 + T1 --> T2  O(rho Delta_0 G^2 / epsilon^4)
```

当前文字中 `D1`, `D2`, `W1`--`W3`, `Q1`, `Q2` 没有全部声明；因此从定义到主定理的图目前不是闭合证明。

## 2. 假设账本

| 编号 | 必要假设 | 当前 slides 中的位置 | 状态 |
|---|---|---|---|
| W1 | `F` proper, lower semicontinuous, and `F+(rho/2)||.||^2` convex | NAS frame 686--698 只写 rho-weakly convex | 未声明 |
| W2 | `rho>0`, `lambda=1/(2rho)<1/rho`; Moreau envelope/prox 的定义 | 686--698 使用但未定义 | 未声明 |
| W3 | 同一个 `G` 在包含 `x` 与 `prox(x)` 的邻域上 Lipschitz，或全局 `G`-Lipschitz | 637--732、886--963 写 “(locally) G-Lipschitz” | 作用域不清 |
| C1 | canonical split: `phi=F+rho||.||^2` convex, `g=rho||.||^2` | 700--708 | 在 W1 下成立 |
| D1 | `phi,g` proper closed convex；`x` 在两者定义域；`partial_delta` 的全局支撑不等式定义 | 570--598 已给定义；AC 页仍把 phi 写成 weakly convex | 部分缺失 |
| D2 | NAC 距离的 infimum 可由 `(y,u,v)` 达到，或 NAC 直接采用 witness 定义 | 637--657 与附录 886--925 | 缺失 |
| O1 | 每个内层点的 `s(y)` 满足 `s(y) in partial F(y)` 且范数 `<=G` | 附录 1064--1068 | 依赖 Lipschitz 与次微分类型，未声明 |
| O2 | 内层输出规则、步长、投影球、平均方式明确 | 算法 796--805 及附录 1070--1077 仍未给出 | 部分缺失 |
| O3 | 证书值/函数值查询口径明确 | 807--812 定义 `bar_delta_k`；oracle 定义仍被注释 | 缺失 |
| I1 | `K,J` 是正整数，ceilings/边界情形处理 | 823--846、1032--1044、1070--1077 | `K` 已处理，`J` 未处理 |
| P1 | 随机输出的概率模式与证书求和范围一致 | 算法 807--812、定理 823--846、附录 1032--1044 | 已满足 |

## 3. 类型化符号表

| 符号 | 应有类型/定义 | 当前风险 |
|---|---|---|
| `F` | `R^d -> R union {+infty}`, proper closed, rho-weakly convex | domain/闭性未写 |
| `phi,g` | proper closed convex functions; `F=phi-g` | AC frame 将 phi 写成 weakly convex |
| `partial_delta h(x)` | `{v: h(z)>=h(x)+<v,z-x>-delta for all z}` for convex `h` | 已在 570--598 定义；AC 页的 `phi` 类别仍不一致 |
| `Phi_h(x,v)` | `h(x)+h^*(v)-<v,x>` | 已在 586--596 定义 |
| `B_delta(x)` | 明确为 closed Euclidean ball | 未定义 |
| `F_lambda(x)` | `inf_y {F(y)+(1/(2lambda))||y-x||^2}` | 未定义 |
| `prox_{F/(2rho)}(x)` | 明确为 `argmin_y {F(y)+rho||y-x||^2}` | notation 可被误读 |
| `partial F` | 指定 Frechet/limiting/convexified subdifferential | 当前混用风险 |
| `Delta_0` | `F(x_0)-inf F`, finite and nonnegative | 非负性依赖 `x_0` 与 `inf F` 定义 |
| `bar_delta_k` | computable upper certificate, `k=0,...,K-1` | value/oracle counting still unclear |
| `G,rho,epsilon,a,K,J` | positive scalars/integers with stated dependence | `K` ceiling present; `J` constant missing |

## 4. 规范化的量词版本

### NAC -> AC

在 `phi,g` proper closed convex、`B_delta(x)` 为闭球、NAC 采用 witness 形式且 `g` 在包含该球的开邻域上以同一常数 `G` Lipschitz 时：

```text
For every x, hat_epsilon, delta >= 0,
if there exist y,u,v with ||x-y|| <= delta,
u in partial phi(x), v in partial g(y), ||u-v|| <= hat_epsilon,
then x is (hat_epsilon, 0, 2G delta)-AC.
```

### NAS -> AC

在 `F` proper closed rho-weakly convex、`rho>0`、canonical split、且 `F` 在包含
`x` 和 `prox_{F/(2rho)}(x)` 的邻域上以 `G` Lipschitz 时：

```text
For every epsilon >= 0,
||grad F_{1/(2rho)}(x)|| <= epsilon
implies x is (0, G epsilon/(2rho), 0)-AC.
```

### AC -> NAS

在同一 canonical split、`delta_phi>=0`，并且 AC 使用 convex epsilon-subdifferential 时：

```text
x is (0,delta_phi,0)-AC
iff F(x)-F_{1/(2rho)}(x) <= delta_phi,
and therefore ||grad F_{1/(2rho)}(x)|| <= sqrt(8 rho delta_phi).
```

### 外层定理

若每个 `k=0,...,K-1` 的 `x^{k+1}` 满足 inner gap `<=a`，且 `K>=1`，并取
`R~Unif{0,...,K-1}`，则：

```text
E[bar_delta_R] <= Delta_0/K + a.
```

当前 slides 已采用随机输出 `R~Unif{0,...,K-1}`，可推出的是

```text
E[bar_delta_R] <= Delta_0/K + a,
E[||grad F_{1/(2rho)}(x_R)||^2] <= 8 rho (Delta_0/K+a),
```

而不是每个随机样本都满足同一个确定性阈值；当前定理的期望表述与此一致。

## 5. 微断言清单

| ID | 微断言 | 使用规则 | 侧条件 |
|---|---|---|---|
| MC-1 | `g` convex and `v in partial g(y)` implies `g(z)>=g(y)+<v,z-y>` | convex subgradient inequality | `g` proper convex; verified only if D1 added |
| MC-2 | `bar_delta_g>=0` and `v in partial_{bar_delta_g}g(x)` | algebra + MC-1 | D1 |
| MC-3 | `bar_delta_g<=2G||x-y||` | triangle inequality + Lipschitz + `||v||<=G` | uniform neighborhood Lipschitz |
| MC-4 | `partial_{d1}g(x) subset partial_{d2}g(x)` for `d1<=d2` | definition monotonicity | D1 |
| MC-5 | `phi=F+rho||.||^2` is convex | W1 and addition of `(rho/2)||.||^2` | standard weak-convex normalization |
| MC-6 | `H_x(y)=F(y)+rho||y-x||^2` is rho-strongly convex | W1 and square expansion | W1 |
| MC-7 | `delta_phi^*=F(x)-F_{1/(2rho)}(x)` | completion of square and infimum | Moreau definition, finite values |
| MC-8 | `delta_phi^*<=G||x-prox(x)||` | drop nonpositive quadratic term | uniform G-Lipschitz on pair |
| MC-9 | `gap >= (rho/2)||x-prox(x)||^2` | strong convexity at minimizer | minimizer existence/uniqueness |
| MC-10 | `||grad F_lambda(x)||=2rho||x-prox(x)||` | Moreau envelope gradient formula | W2 |
| MC-11 | `bar_delta_k>=gap_k` | inner gap inequality | exact `Q_k` definition |
| MC-12 | `sum_k bar_delta_k<=Delta_0+Ka` | telescoping and `F(x^K)>=inf F` | finite values; correct index range |
| MC-13 | uniform random index gives expected average bound | finite nonempty index set | `K>=1`; current theorem uses `K=ceil(...)` |
| MC-14 | projected strongly-convex subgradient average has `O(M^2/(rho J))` gap | explicit stepsize and weighted average theorem | projection set, `M=3G`, output rule |
| MC-15 | `K*J=O(rho Delta_0 G^2/epsilon^4)` | multiply ceilings in asymptotic regime | positive parameters and declared regime |

MC-1--MC-13 are algebraically valid after the listed assumptions are added. MC-14 is not established by the current sentence “therefore”. MC-15 is therefore currently conditional.

## 6. 系数复算

采用 Davis--Drusvyatskiy 约定 `F+(rho/2)||.||^2` convex：

```text
g(x)=rho||x||^2 has smoothness 2rho.
H_x(y)=F(y)+rho||y-x||^2 is rho-strongly convex.
lambda=1/(2rho)<1/rho.

NAC -> AC: delta_g <= 2G delta.
NAS -> AC: delta_phi <= G epsilon/(2rho).
AC -> NAS: gap <= delta_phi,
             ||grad F_{1/(2rho)}(x)|| <= sqrt(8rho delta_phi).

Outer: K >= 16rho Delta_0/epsilon^2,
       a = epsilon^2/(16rho),
       gap <= epsilon^2/(8rho).

Inner: radius <= G/rho, ||q_t|| <= 3G,
       explicit weighted projected method gives gap <= 18G^2/(rho(J+1)),
       so J+1 >= 288G^2/epsilon^2 is sufficient.
```

因此**没有发现这些系数本身的算术错误**。阻断点是系数所依赖的定义、输出方式和内层算法没有完整写出。

## 7. 反例记录

1. **AC threshold 不是 NAS 的等价表述。** 取 `rho=G=1`, `F(y)=|y|`,
   `x=0.05`, `epsilon=0.1`。此时 `lambda=1/2`, `prox(x)=0`,
   `||grad F_lambda(x)||=0.1`, 但
   `F(x)-F_lambda(x)=0.05-0.0025=0.0475 > epsilon^2/8=0.00125`。
   因而 theorem 页的 “i.e.” 不能理解为双向等价，应改为 “and hence”。

2. **NAC 距离未必给出精确 witness（若 `B_delta` 未声明为闭球）。**
   取 `x=0`, `delta=1`, `g(y)=y^2`, `phi(z)=2z`，并把 `B_delta(x)`
   解释为开球。则 `union_{|y|<1} partial g(y)=(-2,2)`，
   `partial phi(0)-union=(0,4)`，其到 0 的距离为 0，但没有 `u=v` 的 witness。
   这正是附录 I 从 distance 直接写成 “there exist” 所缺的闭性/达到性条件。

3. **`2G delta` 系数的 sharpness candidate。** `g(t)=|t|`, `y=0`,
   `v=-1`, `x=d>0` gives `g(x)-g(y)-v(x-y)=2d=2G||x-y||`.
   因此在仅有 Lipschitz 假设下不能把该系数无条件降到 `G delta`。

## 8. 限制与审校状态

- 当前 PDF 为 9 页，`pdflatex -interaction=nonstopmode -halt-on-error` 连续两次成功。
- 上一版的随机输出/确定性 argmin 冲突已由当前源文件修复：当前活动算法与附录都使用 `{0,...,K-1}`，定理改为期望结论。
- 编译仍有 hyperref/font warning；本次未发现 fatal error。
- 本报告覆盖当前 PDF 中未注释的 frames 570--1089，并单独检查了 `\\ifshowappendix` 下的附录源代码；注释掉的旧 lower-bound 草稿不计入结论。
- 按用户要求，本轮没有启动额外审稿 agent；因此没有独立盲审线程可作为通过证据。
