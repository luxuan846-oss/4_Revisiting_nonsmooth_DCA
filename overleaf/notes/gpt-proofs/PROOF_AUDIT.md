> 历史材料：按原文保存。证明状态、文献判断与行号属于当时版本；当前状态见 `notes/progress/PROJECT_STATUS.md`，本次整理未重新证明其结论。

# Proof Audit: Nearly Approximate Stationarity Slides

审校时间：2026-08-19（Asia/Shanghai）  
审校输入：`llx_nonsmooth.tex` 当前活动 frames 570--1089（默认 PDF 9 页；附录源代码另行核对）  
输入 SHA-256：`9c0768193563155d890708e2304ca4a23c25cd3d012bedcce32387c70cc57abf`

## Verdict

**FAIL / critical_gap**：NAS/AC/NAC 的主要系数经复算没有算术错误；当前版本仍不能作为完整严谨证明。此前的随机输出/确定性 `argmin` 冲突和附录 I 方向标题已修复；剩余的全局阻断点是内层复杂度证明，另有一组可在设置页补齐的定义与 oracle 假设。

1. 内层 “projected deterministic subgradient method therefore attains `O(1/J)`” 没有给出步长、输出平均、初始点和常数，复杂度定理没有从当前文字推出。
2. AC/NAS/NAC 所需的凸 `delta`-次微分、弱凸归一化、闭性/域和 oracle 条件仍未在活动 slides 中完整声明；这些属于设置补充，不是新的系数错误。

## 分级问题

### P0-1 — 随机输出、索引和结论模式冲突【已修复】

- **状态**：INVALID / GLOBAL（历史问题，当前不计入开放问题）
- **类别**：STOCHASTIC_MODE_CONFUSION, QUANTIFIER_ERROR, IMPLICATION_REVERSAL
- **严重性**：CRITICAL_RESOLVED
- **位置**：当前算法 `llx_nonsmooth.tex:807--812`；定理 `:823--846`；附录 IV `:1032--1044`
- **原说法**：算法返回 `x^{k_star}`，其中 `k_star ~ Unif{1,...,K}`；附录却取 `t_star in argmin_{0<=t<T} bar_delta_t` 并给出确定性上界。
- **原问题**：均匀随机抽样只能推出
  
  \[
  \mathbb E[\bar\delta_R]\le \Delta_0/T+a,
  \qquad
  \mathbb E\|\nabla F_{1/(2\rho)}(x_R)\|^2
  \le 8\rho(\Delta_0/T+a),
  \]
  
  不能推出每个随机返回点满足 `bar_delta <= epsilon^2/(8rho)`。此外，附录控制的是 `x_t`, `t=0,...,T-1`，算法抽样 `x_1,...,x_K` 可能包含未被控制的 `x_T`，并遗漏 `x_0`。
- **可验证反例**：令证书序列为 `(0,1)`，从两项中均匀抽样；平均值为 `1/2`，但抽到第二项时确定性阈值 `0` 失败。该逻辑与函数来源无关。
- **当前修复**：算法、附录和定理统一使用 `k_star~Unif{0,...,K-1}`，并改为 `E[bar_delta]` 与 `E[||grad||^2]` 结论。逐点 AC 证书写成随机索引对应的随机容差 `bar_delta_{k_star}`，这是成立的。
- **状态**：已关闭；不再阻断当前期望型主定理。

### P0-2 — 内层 `O(G^2/(rho J))` 没有被当前证明建立

- **状态**：UNJUSTIFIED / GLOBAL
- **类别**：UNPROVEN_SUBCLAIM, MISSING_DERIVATION, HIDDEN_ASSUMPTION
- **严重性**：CRITICAL
- **位置**：附录 V，`:1050--1088`；算法 `:784--812`
- **当前说法**：在球上使用 “a projected deterministic subgradient method”，因此有
  \[
  H_t(x_{t+1})-\min H_t=O(G^2/(\rho J)).
  \]
- **问题**：算法现在给出了投影球和 `J` 步，但仍没有给出步长 `eta_j`、起点、最后迭代/最佳迭代/加权平均的输出方式，也没有常数。对一般 projected subgradient method，最后迭代的 `O(1/J)` 函数值 gap 不能由这句话自动推出。
- **可用修复**：明确令 `C_t=B(x_t,G/rho)`，取 `eta_j=2/(rho(j+1))`，并输出加权平均
  \[
  \bar y_J=\frac{2}{J(J+1)}\sum_{j=1}^J j y_j.
  \]
  对 `||q_t(y)||<=3G` 的投影次梯度迭代，可写出
  \[
  H_t(\bar y_J)-H_t(y_t^*)\le \frac{18G^2}{\rho(J+1)}.
  \]
  于是 `J+1 >= 288G^2/epsilon^2` 足以实现 `a=epsilon^2/(16rho)`。若采用别的输出规则，必须给出对应定理和常数。
- **下游影响**：没有 Q1，就没有 `T J` 复杂度和主定理的 oracle bound。

### P1-1 — AC 定义把 `phi` 写成 weakly convex，但使用的是凸 `delta`-次微分

- **状态**：UNDERSTATED / GLOBAL
- **类别**：REGULARITY_GAP, NORMALIZATION_MISMATCH
- **严重性**：MAJOR
- **位置**：AC frame `:601--608`（依赖前一页 `:570--598` 的定义）
- **问题**：上一页已经给出 `partial_delta h` 的凸函数定义；但 AC 页仍把 `phi` 写成 `weakly convex`，随后把该凸 `delta`-次微分、Fenchel gap 和 `partial_0 phi=partial phi` 应用于 `phi`。若 `phi` 真只弱凸，当前定义与后续等价式不匹配。
- **最小修复**：把 AC 前提改成 `phi,g` 均为 proper closed convex，并声明 `x in dom phi cap dom g`、`delta_phi,delta_g,hat epsilon>=0`；上一页的 `partial_delta` 定义可直接沿用。原定义为
  \[
  \partial_\delta h(x)=\{v:h(z)\ge h(x)+\langle v,z-x\rangle-\delta,\ \forall z\}.
  \]

### P1-2 — 弱凸参数约定、Moreau 定义和次微分类型缺失

- **状态**：UNDERSTATED / GLOBAL
- **类别**：NORMALIZATION_MISMATCH, MISSING_DERIVATION, REFERENCE_MISMATCH
- **严重性**：MAJOR
- **位置**：NAS frame `:686--734`，附录 II--III `:927--997`
- **问题**：系数 `rho`, `2rho`, `1/(2rho)`, `sqrt(8rho delta_phi)` 只在 Davis--Drusvyatskiy 约定
  \[
  F+(\rho/2)\|\cdot\|^2\text{ convex}
  \]
  下成立。当前未写该约定，也未定义
  \[
  F_\lambda(x)=\inf_y\{F(y)+(2\lambda)^{-1}\|y-x\|^2\},
  \quad
  \operatorname{prox}_{F/(2\rho)}(x)=\arg\min_y\{F(y)+\rho\|y-x\|^2\}.
  \]
  `partial F` 的 Frechet/limiting/Clarke 类型也未固定。
- **最小修复**：在 NAS 定义前写 proper closed `F`、标准弱凸约定、`rho>0`、`lambda=1/(2rho)<1/rho`，并指定次微分。对有限值 locally Lipschitz `F`，可说明 prox 最优性给出一个 limiting/Clarke-compatible witness。
- **核验**：Davis--Drusvyatskiy 原文明确采用 `F+(rho/2)||.||^2` convex 且 `lambda<1/rho`；因此 slides 的系数在该约定下是对的。

### P1-3 — NAC 的 distance 没有推出附录所需的精确 witness

- **状态**：UNJUSTIFIED / LOCAL
- **类别**：QUANTIFIER_ERROR, CASE_INCOMPLETE
- **严重性**：MAJOR
- **位置**：NAC 定义 `:637--657`；附录 I `:886--925`
- **问题**：从
  \[
  \operatorname{dist}(0,A)\le\widehat\varepsilon
  \]
  直接写成存在一个 `y,u,v` 满足 `||u-v||<=hat epsilon`，需要 `A` 闭且距离达到。当前没有说明 `B_delta` 是闭球，也没有给出次微分图闭性/局部有界性。
- **反例**：若 `B_1(0)` 为开球，取 `g(y)=y^2`, `phi(z)=2z`, `x=0`。则差集为 `(0,4)`，距离为 0，但不存在 `u=v` witness。
- **最小修复**：直接把 NAC 定义改为存在 witness；或声明闭球、proper closed convex 函数、在包含球的开邻域上 Lipschitz，从而证明相关集合紧/闭并且 infimum 达到。

### P1-4 — “locally G-Lipschitz” 的统一作用域不明确

- **状态**：UNDERSTATED / GLOBAL（对 NAS-to-AC），LOCAL（对 NAC-to-AC）
- **类别**：HIDDEN_ASSUMPTION, CONSTANT_DEPENDENCE_HIDDEN
- **严重性**：MAJOR
- **位置**：`:637--673`、`:686--732`、附录 I `:886--924`、附录 II `:927--963`
- **问题**：证明同时需要 `|g(x)-g(y)|<=G||x-y||` 和 `||v||<=G`，以及 `|F(x)-F(hat x)|<=G||x-hat x||`。点态 “locally” 不保证同一个 `G` 覆盖整个球或 prox 点。
- **最小修复**：改为全局 `G`-Lipschitz；或明确在包含 `{x} union B_delta(x)` / `{x,hat x}` 的开邻域上以同一 `G` Lipschitz，并说明 convex subgradient norm bound。

### P1-5 — oracle 模型没有在活动 slides 中定义，且计数口径不一致

- **状态**：UNJUSTIFIED / GLOBAL
- **类别**：REFERENCE_MISMATCH, MISSING_DERIVATION, DIMENSION_TRACKING
- **严重性**：MAJOR
- **位置**：算法标题 `:781`；注释 oracle 定义 `:366--381`；附录 V `:1080--1088`
- **问题**：算法写 `O_DC`，但其定义被注释；附录 V 又改用一次 `F` 的函数值/次梯度查询。计算 `argmin bar_delta_t` 需要 `F(x_t),F(x_{t+1})`，加权平均输出可能还需要额外值查询。故 “exactly TJ ... up to constants” 同时用了 exact 和 up to constants 两种口径。
- **最小修复**：明确 oracle 返回 `(F(y),s(y))` 或 `(phi(y),g(y),u(y),v(y))`；说明函数值是否计入一次 FO query；把总数写成 `T J+O(T)` 或统一成 `O(TJ)`，并说明最后输出点是否额外查询。

### P1-6 — 主定理中的 “i.e.” 把单向蕴含写成了等价表述【已修复】

- **状态**：INVALID / LOCAL（历史问题，当前不计入开放问题）
- **类别**：IMPLICATION_REVERSAL, SCOPE_OVERCLAIM
- **严重性**：CRITICAL_RESOLVED
- **位置**：上一版定理；当前定理 `:823--846`
- **原问题**：
  \[
  (0,\varepsilon^2/(8\rho),0)\text{-AC}
  \Longrightarrow \|\nabla F_{1/(2\rho)}(x)\|\le\varepsilon
  \]
  成立，但反向蕴含一般不成立。当前 “i.e.” 容易读成等价。
- **已验证反例**：`rho=G=1`, `F(y)=|y|`, `x=0.05`, `epsilon=0.1`。有 `prox_{F/(2rho)}(x)=0`、Moreau gradient norm `0.1`，但 Moreau gap `0.0475`，大于 `epsilon^2/8=0.00125`。故该点是 epsilon-NAS，却不是指定阈值的 AC。
- **当前状态**：当前定理已删除该 “i.e.”，改为随机 AC 证书与期望 NAS 梯度平方结论；反例保留作为回归检查。

### P1-7 — `J` 的整数常数与 Big-O 适用范围仍未声明

- **状态**：OVERSTATED / GLOBAL（边界参数）
- **类别**：CASE_INCOMPLETE, CONSTANT_DEPENDENCE_HIDDEN
- **严重性**：MAJOR
- **位置**：定理 `:819--856`；附录 IV `:1000--1046`；附录 V `:1070--1078`
- **问题**：`K` 已使用 ceiling 且 `Delta_0 in (0,infty)`，边界问题已显著收窄；但 `J=O(G^2/epsilon^2)` 仍不是一个可执行的正整数参数，且纯乘积 Big-O 需要声明渐近 regime。
- **最小修复**：写
  \[
  T=\max\{1,\lceil16\rho\Delta_0/\varepsilon^2\rceil\},
  \quad
  J=\max\{1,\lceil288G^2/\varepsilon^2\rceil\},
  \]
  或声明结论仅针对固定正参数、`epsilon` 足够小时的渐近阶，并说明 `J` 的常数。

### P2-1 — NAS 文本中的 “Equivalently” 需要改成精确的等式加蕴含

- **状态**：UNCLEAR / LOCAL
- **类别**：UNJUSTIFIED_ASSERTION
- **严重性**：MINOR
- **位置**：NAS frame `:686--698`
- **问题**：Moreau gradient bound 与 `||x-hat x||` 是等价的；`dist(0,partial F(hat x))<=epsilon` 是 prox 最优性给出的后果，不是独立的等价定义。
- **修复**：写 `||x-hat x||=(2rho)^{-1}||grad F_{1/(2rho)}(x)||`，且 `2rho(x-hat x) in partial F(hat x)`, hence the distance bound.

### P2-2 — 隐藏附录中的未定义交叉引用

- **状态**：UNJUSTIFIED / LOCAL
- **类别**：REFERENCE_MISMATCH
- **严重性**：MINOR
- **位置**：附录 II `:946`
- **问题**：`\eqref{eq:ac-common-witness}` 没有对应的 `\label`；启用附录时会产生 undefined reference。
- **修复**：删除该引用或在共同 witness 的显示式上补 `\label`。

### P2-3 — 记号和版面细节

- **状态**：COSMETIC
- **类别**：UNJUSTIFIED_ASSERTION / NORMALIZATION_MISMATCH
- **严重性**：MINOR
- **位置**：附录 V `:1054`、`:1080--1088`
- **问题**：当前附录写成 `y_k^\star=\operatorname{argmin}H_k`，没有显式变量；虽然强凸性保证唯一解，但记号仍可被理解为集合。复杂度页的 `KJ` 还没有把 `O(K)` 的函数值/输出查询单独列出。
- **修复**：写 `y_k^*:=\arg\min_y H_k(y)`，并把总查询数写成 `KJ+O(K)` 或统一为带 ceilings 的 `O((1+K)(1+J))`。

### P2-4 — 文献比较语句需要限定为同阶比较

- **状态**：OVERSTATED / LOCAL
- **类别**：SCOPE_OVERCLAIM
- **严重性**：MINOR
- **位置**：定理页 `:849--854`
- **问题**：当前证明与 Davis--Drusvyatskiy、Davis--Grimmer 的 oracle 模型和随机性设定并未完全相同；“matching the guarantees”容易被理解为完整定理逐项相同。
- **修复**：改为“在相应假设和 oracle 口径下具有相同的 `\varepsilon^{-4}` 指数”，或明确列出可比条件。

## 系数审计表

| 结论 | 复算结果 | 备注 |
|---|---|---|
| `g=rho||x||^2` smoothness | `2rho`，正确 | 标准 Euclidean norm |
| `H_x` strong convexity | `rho`，正确 | 依赖 `F+(rho/2)||.||^2` convex |
| NAC -> AC | `2G delta`，正确 | 仅在统一 Lipschitz/witness 条件下 |
| NAS -> AC | `G epsilon/(2rho)`，正确 | 依赖 prox 点在 Lipschitz 区域 |
| AC -> NAS | `sqrt(8rho delta_phi)`，正确 | strong-convexity factor `rho/2` 正确 |
| Outer `K,a` | `16,16,8`，正确 | 当前随机期望版本，`K=ceil(16rho Delta_0/epsilon^2)` |
| Inner radius | `G/rho`，正确 | `y*` 存在且 F global G-Lipschitz |
| Inner subgradient norm | `3G`，正确 | 在投影球内 |
| Total exponent | `epsilon^-4`，正确 | 需补齐 Q1/Q2 与 ceilings |

## 证明链修复后的可接受版本

当前期望型主定理的可接受证明链为：

1. 先声明 proper closed `rho`-weakly convex `F` 的标准约定和 canonical split。
2. 激活 convex `partial_delta`/Fenchel gap 定义，并将 AC 的 `phi,g` 都设为 proper closed convex。
3. 运行 `k=0,...,K-1`；每个 inner solve 用明确的 projected weighted subgradient method，保证 gap `<=a`。
4. 由均匀随机索引得到 `E[bar_delta_R]<=Delta_0/K+a`。
5. 附录 IV 给出期望 gap；AC-to-NAS 给出期望平方梯度 bound。
6. 取正整数 ceilings，得到 `O((1+rho Delta_0/epsilon^2)(1+G^2/epsilon^2))`，在固定正 `rho,Delta_0,G` 且 `epsilon->0` 时为 `O(rho Delta_0 G^2 epsilon^-4)`。

## 外部核验记录

- Davis--Drusvyatskiy, *Stochastic Model-Based Minimization of Weakly Convex Functions*: 本地 PDF 明确写 `F+(rho/2)||.||^2` convex、`lambda<1/rho`、`grad F_lambda=lambda^{-1}(x-prox)` 和 prox 点的近似驻点解释。
- Crossref DOI `10.1137/18M1178244`: 标题、作者、年份与 slides 引用一致。
- Crossref DOI `10.1287/ijoo.2022.0087` 与 Semantic Scholar: Sun--Sun 标题、作者、期刊卷期页码一致；原 publisher PDF 受 Cloudflare 阻断，因此 NAC 逐式原始定义标记为待补核验，不把引用本身判为错误。
- Crossref DOI `10.1137/17M1151031`: Davis--Grimmer 题名、作者、卷期、页码与 slides 一致。

## 编译证据

命令：`pdflatex -interaction=nonstopmode -halt-on-error llx_nonsmooth.tex`  
结果：默认分支成功，9 页，页面尺寸 `362.835 x 272.126 pt`；连续两次编译后仅剩非致命 warning。隐藏附录分支临时编译成功，14 页；除附录 II 的未定义 `eq:ac-common-witness` 外没有发现新的引用或公式构建错误。  
非致命 warning：hyperref `pdfauthor` 重复设置、字体替代、PDF string 中的 token；本次没有 fatal error。

## 审校边界

本报告覆盖当前 PDF 中未注释的 frames 570--1089，并单独检查了 `\ifshowappendix` 下的附录源代码；注释掉的 lower-bound、multiblock、Fenchel identity、Goldstein 等草稿没有进入当前 PDF，因此没有被计入本 verdict。若这些 frame 重新取消注释，需要单独复核其假设和引用。
