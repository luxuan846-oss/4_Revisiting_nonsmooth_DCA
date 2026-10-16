> 历史材料：按原文保存。证明状态、文献判断与行号属于当时版本；当前状态见 `notes/progress/PROJECT_STATUS.md`，本次整理未重新证明其结论。

# 两块非光滑问题的问题澄清稿

## Target

澄清以下四件彼此不同的事：

1. 单块 DC 问题中何种近似 criticality 可有限时间计算；
2. 两块交替算法的 cluster point 能否成为联合临界点；
3. Aubin 性在两块分析中究竟承担何种职责；
4. direct nonsmooth 算法与 smoothing 算法应当在何种相同目标下比较。

## Status

COHERENT AFTER REFRAMING

原先“是否需要 Aubin 性”混合了 subsequential stationarity、whole-sequence convergence 和 finite-time residual 三个不同结论。

## Invariant Object

对两块目标 `J(x,y)`，首先固定联合临界性目标：

$$
0 \in \partial J(\bar x,\bar y).
$$

对于 DC 单块目标 `F(x)=\phi(x)-g(x)`，固定可计算的值松弛证书：

$$
\operatorname{dist}\bigl(\partial_{\delta_\phi}\phi(x),\partial_{\delta_g}g(x)\bigr)\le\epsilon.
$$

二者不能直接等同；前者是 joint limiting-subdifferential stationarity，后者是 decomposition-dependent but finite-time computable DC certificate。

## Assumptions

- `J` 为 proper closed 且下有界。
- 交替 proximal / ASAP 更新产生充分下降，因而 `\|z^{k+1}-z^k\|\to0`。
- 为将 partial residual 传至极限点，需要相应 partial subdifferential 的 parametric closedness；师姐论文以 blockwise restricted prox-regularity 给出该性质。
- 为从所有块的 partial criticality 推至 joint criticality，需要额外的 assembly condition：

$$
\Big(\mathop{\times}_i \partial_{x_i}J(z)\Big)\times
\Big(\mathop{\times}_j \partial_{y_j}J(z)\Big)
\subseteq \partial J(z).
$$

- Aubin 性只在需要将中间 Gauss--Seidel 点的 partial residual 移到当前完整迭代点，并取得 relative-error bound 时使用。

## Derivation Strategy

将问题分为“极限点结论”与“有限时间可计算性”。先证明每一个，再讨论它们之间是否可桥接。

## Derivation Map

1. 充分下降给出 `\|z^{k+1}-z^k\|\to0`。
2. 每个块的最优性给出中间点上的 `\xi_i^{k+1}\in\partial_{x_i}J(\tilde z_i^{k+1})`，且 `\xi_i^{k+1}\to0`。
3. partial parametric closedness 给出极限点的 coordinate criticality：`0\in\partial_{x_i}J(\bar z)`。
4. assembly condition 才能将 coordinate criticality 提升为 `0\in\partial J(\bar z)`。
5. 若需要 `\operatorname{dist}(0,\partial J(z^k))\le C\|z^k-z^{k-1}\|`，需要 Aubin 性将 `\partial_{x_i}J(\tilde z_i^k)` 定量迁移至 `\partial_{x_i}J(z^k)`。

## Main Derivation

### 单块问题

单块 PPA 的 optimality condition 已直接落在同一点：

$$
0\in\partial F(x^{k+1})+\mu^{-1}(x^{k+1}-x^k).
$$

因此步长消失与 `\partial F` 的图闭性足以给出 cluster-point stationarity。

### 两块问题

Gauss--Seidel 更新只给出不同中间点上的 partial inclusions。即使 closedness 导致

$$
0\in\partial_xJ(\bar x,\bar y),\qquad 0\in\partial_yJ(\bar x,\bar y),
$$

也仍需 assembly condition 才能得到 `0\in\partial J(\bar x,\bar y)`。

反例为 `J(x,y)=\max\{x,y\}`：原点满足两个 partial inclusion，却不满足 `0\in\partial J(0,0)`。

### Aubin 性

Aubin 性的输出是 relative-error estimate，而不是 coordinate-to-joint implication 本身：

$$
\operatorname{dist}(0,\partial J(z^k))
\le C\|z^k-z^{k-1}\|.
$$

它用于 KL analysis 中的 finite length 和 whole-sequence convergence。若只主张每个 cluster point 为联合临界点，Aubin 性未必需要；但 assembly condition 与 partial closedness 仍不可省略。

### 与单块 DC 可计算性主线的关系

`sample (2).tex` 的贡献是说明 exact same-point DC criticality 在有限时间内可能不可达，并以 `(\delta_\phi,\delta_g,\epsilon)` Fenchel-gap certificate 给出可计算替代。

两块问题中的自然开放问题不是直接复制该定义，而是：能否构造一个 joint two-block certificate，使其既能由 block updates 有限时间输出，又在所有 tolerance 趋零时退化到联合临界性？

## Boundaries and Non-Claims

- “算法数值上一定收敛到该点”不能由 cluster-point stationarity 推出；还需要 KL 或其他 whole-sequence mechanism。
- Aubin 性不是一般非光滑函数自动满足的性质；在 max、`\ell_1` 等折点附近需逐点验证或避免依赖它。
- direct raw subgradient 的数值优势不能预设；应比较 direct proximal / prox-linear 与 smoothing 的总 oracle cost 和原问题证书。

## Open Risks

- 师姐论文的 assembly condition 对非可分 nonsmooth coupling 很强。对 `H(x,y)=\|x-Py\|_1`，在 `x=Py` 处两个 partial subgradient 的任意组合一般无法组成 full subgradient，因此该条件不自动成立。
- 需要明确你的张量耦合项属于哪一类：block-separable、jointly smooth、还是共享 outer nonsmooth function。不同结构决定可否避免 Aubin 性。
