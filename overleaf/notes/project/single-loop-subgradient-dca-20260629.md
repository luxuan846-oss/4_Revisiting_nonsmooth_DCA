# 单循环次梯度 DCA 收敛性研究讨论
**日期：** 2026-06-29  
**背景：** 结合周报（20260607）第一部分与 MoSSP 非光滑 DC 目标延伸工作

---

## 0. 核心问题出发点

周报第一部分提出了两个研究问题：

> **Q1.** 当 $g$ 非光滑但确定（deterministic）时，单循环 DCA 能否获得与无约束光滑情形相当的近最优复杂度？随机情形单循环能否到 $\epsilon^{-3}$？
>
> **Q2.** 当 $g$ 非光滑且随机（stochastic）时，复杂度结果是多少？双循环至多到多少？单循环有没有到 $\epsilon^{-4}$ 或 $\epsilon^{-3}$？

以及杨磊老师提出的问题：

> **基于次梯度类的 DCA 算法，能否收敛到一个可解释的稳定点，并给出相应的复杂度分析？**

---

## 1. 必须先澄清的混淆：$-2/-3/-4$ 指的不是同一个量

**这是整个讨论最重要的一个澄清。**

文献中 $\epsilon^{-3}$、$\epsilon^{-4}$ 等指数，指的是不同的 oracle 下、不同的稳定性度量下的复杂度。你的困惑根源在于把三个不同来源的 "$-3$" 混在一起：

| 来源 | $-3$ 的真实含义 | 度量 | $g$-side 假设 |
|------|--------------|------|-------------|
| MDCA (Chayti & Jaggi 2025) | MVR + averaged smoothness 买来的 $\phi$-side rate | critical-distance / gap | $g$ **确定、非光滑**，排除在随机外 |
| DCA-PAGE (Nguyen et al. 2025) | finite-sum $O(N+N^{1/2}\epsilon^{-2})$，online $O(b+b^{1/2}\epsilon^{-2})$ | one-sided gap | $g$ 确定 |
| Cutkosky et al. ICML 2023 | $O(\epsilon^{-3}\delta^{-1})$，$\delta$ 是**空间球半径** | **Goldstein 邻域**度量，$\delta\neq\delta_g$ | 一般非光滑非凸，与 DC 无关 |

**关键结论：**
- MDCA/DCA-PAGE 的 $-3$ 是**光滑侧**用 MVR/VR 买来的，$g$ 在这些工作里是确定的，根本不在随机估计里。
- Cutkosky 的 $\epsilon^{-3}\delta^{-1}$ 的 $\delta$ 是 Goldstein 邻域的球半径，**和你的 $\delta_g$（Fenchel 缺陷）完全不同**，不能直接类比。
- 因此"单循环纯次梯度 DCA 能不能到 $-3$"这个问题，对于**随机非光滑 $g$** 的情形，**答案在当前框架下是否定的**——这不是你做不到，是结构问题。

---

## 2. 两个分析轴——必须解耦

复杂度指数背后有**两个完全正交的轴**，你的问题混淆了它们：

| 轴 | 控制的对象 | 在算法中对应 |
|----|-----------|------------|
| **循环结构**（单循环 vs 双循环） | $\phi$-side / smooth-side 的优化残差如何压下去 | $R_{k+1} = \frac{1}{\gamma_k}\|x^{k+1}-x^k\| + \alpha_{k+1}$ |
| **$g$-side oracle 质量**（光滑/VR/原始次梯度） | transported $g$-side Fenchel 缺陷如何控制 | $\delta_g^{k+1} = \epsilon_g^k + g(x^{k+1})-g(x^k)-\langle b^k, x^{k+1}-x^k\rangle$ |

文献里 $-3$/$-4$ 的差别，**几乎全部来自第二个轴**（$g$-side oracle 质量），而不是第一个轴（循环结构）。

---

## 3. 关键参考文献定位

| 优先级 | 文献 | 在你论文里的角色 |
|--------|------|----------------|
| 1 | Nguyen et al. 2025 ([arXiv:2509.11657](https://arxiv.org/abs/2509.11657)) | 直接对标：DCA-PAGE，finite-sum/online rate，one-sided gap |
| 2 | Chayti & Jaggi 2025 (MDCA, [OpenReview](https://openreview.net/pdf?id=7aIxLa5L9E)) | 对标：momentum 处理 smooth concave side 噪声，$-3$ 是 smooth-side 意义 |
| 3 | Hu et al. 2024 ([arXiv:2405.18577](https://arxiv.org/abs/2405.18577)) | 对标：single-loop + inexact prox / Moreau envelope，max-structured weakly convex |
| 4 | Cutkosky et al. ICML 2023 ([PMLR](https://proceedings.mlr.press/v202/cutkosky23a.html)) | 对标：generic stochastic nonsmooth nonconvex，$O(\epsilon^{-3}\delta^{-1})$ Goldstein stationarity，注意 $\delta$ 含义不同 |
| 5 | Zhang et al. 2020 ([arXiv:2002.04130](https://arxiv.org/abs/2002.04130)) | 支撑有限时间不可达性：exact Clarke / exact same-point nonsmooth stationarity 不可作有限步目标 |

---

## 4. 你草稿（`sample.tex`）的现状

草稿已有以下完整内容：

1. **有限时间不可达性**（Theorem 1）：基于 Zhang hidden-kink 构造，迁移到 DC 设定。
2. **两侧 Fenchel certificate 定义**（Definition 1）：$(\delta_\phi, \delta_g, \epsilon)$-critical point，即 $\operatorname{dist}(\partial_{\delta_\phi}\phi(\bar x), \partial_{\delta_g}g(\bar x)) \le \epsilon$。
3. **certificate 迁移引理**（Lemma 1）：$b^k\in\partial_{\epsilon_g^k}g(x^k) \Rightarrow b^k\in\partial_{\delta_g^{k+1}}g(x^{k+1})$，其中 $\delta_g^{k+1} = \epsilon_g^k + g(x^{k+1})-g(x^k)-\langle b^k, x^{k+1}-x^k\rangle$。
4. **$\min||x|-1|$ 例子**：Fenchel gap $\to 0$ as $x\to\pm1$，而 critical distance $\equiv 1$。
5. **算法框架**（Algorithm 1）和**决定论实例化表格**（Table 1）。
6. **Complexity Analysis 章节**：Section IV-B（确定性 $O(\epsilon^{-2})$），Section IV-C（finite-sum），Section IV-D（online $O(\epsilon^{-4})$）。

**草稿完成度约 80%，框架正确，复杂度部分仍是草稿性陈述，尚需完整证明。**

---

## 5. 三个可能的论文故事（Story A/B/C）

### Story A：统一框架
**题眼：** two-sided Fenchel certificate 统一了 critical-distance、one-sided DCA gap、concave-side linearization。复杂度是支撑证据，贡献是概念澄清。
- 风险低，审稿人可能说"只是重新打包"。

### Story B：非光滑 $g$ 的单循环复杂度
**题眼：** 单循环 DCA 在 $g$ 非光滑时获得有限时间复杂度，无需对 $g$ 光滑化，$O(\epsilon^{-2})$（确定性）、$O(\epsilon^{-4})$（随机）。度量本身是交付物。
- 中等风险；必须预先解释"为什么 $\epsilon^{-4}$ 而非 $-3$"，并说清和 Cutkosky $\delta$ 的区别。

### Story C：$-3$ 壁垒（难）
**题眼：** 对原始 bounded-variance 随机非光滑 $g$-oracle，单循环 DCA 卡在 $\epsilon^{-4}$；到 $\epsilon^{-3}$ 需要 Moreau 光滑化或 VR-compatible Fenchel oracle 的 $g$-side 结构。一个真正的**相变（phase transition）**。
- 最高品位，风险最高；需要上界 + 下界两半都到位。

**你的选择：Story C。**

---

## 6. Story C 可行性分析

### 6.1 Story C 必须交付的两半

| 半边 | 内容 | 可行性 |
|------|------|--------|
| **上界（构造性）** | 一个算法 + $g$-side oracle，达到 $\tilde O(\epsilon^{-3})$ | 中高（路线 1 较可行） |
| **下界（障碍）** | 证明纯 bounded-variance 次梯度 oracle 下单循环无法突破 $\epsilon^{-4}$ | 中低（有坍塌风险） |

只有上界 → 退化为 Story B（好但不是 C）。只有下界 → 纯负面结果（单薄）。**C 的品位来自两半都有。**

### 6.2 上界一半：能否造出 $\epsilon^{-3}$ 的 $g$-side oracle？

**路线 1：Moreau 光滑化（可行性高）**

- 用 Moreau envelope $g_\mu$ 替换 $g$，其梯度 $L_g = 1/\mu$-Lipschitz。
- 偏差 $|g-g_\mu| = O(\mu\kappa_g^2)$，要求 $\le \epsilon$，逼出 $\mu = O(\epsilon)$，于是 $L_g = \Omega(\epsilon^{-1})$。
- 光滑化后 MVR/PAGE/STORM 可用，$g$-side 到 $\epsilon^{-3}$。
- **⚠️ 必须验证：** $L_g = 1/\mu = \Omega(\epsilon^{-1})$ 是否把率常数里省下来的 $\epsilon^{-1}$ 又吃回去。**这是决定路线 1 是否成立的唯一计算。**

**路线 2：直接对次梯度做 VR（可行性低）**

- 需要 averaged smoothness：$\mathbb{E}\|\nabla h_\xi(x)-\nabla h_\xi(y)\|^2 \le L^2\|x-y\|^2$。
- 非光滑 $g_\xi$ 的原始次梯度**不满足此条件**（就是 $\min||x|-1|$ 那个跳变）。
- 没有现成引擎。**不建议押注。**

### 6.3 下界一半：能否证明 $\epsilon^{-4}$ 壁垒？

三个诚实的隐患：

1. **Theorem 1 不能直接用。** 现有不可达定理（Zhang hidden-kink）针对 $\delta_g=0$（精确临界性），而 $\epsilon^{-4}$ 壁垒是 $\delta_g=O(\epsilon)$ 处的**统计/方差下界**——完全不同的机制（信息论式，类似 SGD 的 $\sigma^2\epsilon^{-2}$ 下限）。等于要从零写新下界。

2. **"单循环"必须形式化。** 针对特定算法模板的下界弱（审稿人会说"换算法"）；针对一整类 oracle 的下界强但难得多。

3. **可能根本是假的。** 若 Moreau 路线只用 bounded-variance oracle 就能到 $-3$，那"原始 oracle 卡在 $-4$"这个 claim 就**错了**，分离直接坍塌，退回 Story B。

### 6.4 唯一的承重问题（先于写作必须判定）

> **Moreau 光滑化路线，只用 bounded-variance oracle 能否到 $\epsilon^{-3}$？还是需要原始 $g$ 上的 averaged smoothness？**

| 判定结果 | 含义 |
|----------|------|
| bounded-variance **足够** | 上界容易，但下界大概率假。Story C **坍塌为 B**。转 B。 |
| 需要 **averaged smoothness** （而原始非光滑 $g$ 没有） | 真实结构鸿沟存在。Story C 分离是**真的**，值得证。 |

**这个岔路一页计算就能判定，是下一步最紧迫的事，优先于写任何内容。**

---

## 7. 直接回答杨磊老师的问题

**"基于次梯度类的 DCA，能否收敛到一个可解释的稳定点，并给出复杂度分析？"**

**分三层回答：**

### 层次 1：确定性次梯度 DCA（$g$ 非光滑、确定）
- **结论：可以。已经做出来了。**
- 次梯度 $b^k\in\partial g(x^k)$ 是 exact，迁移误差靠 $\|d^k\|^2$ telescoping 压下去。
- **单循环 $O(\epsilon^{-2})$**，收敛到 $(\delta_\phi, \delta_g, \epsilon)$-critical point。
- 稳定点可解释性来自两侧 Fenchel certificate，不是某个替代点。

### 层次 2：随机次梯度 DCA（$g$ 非光滑、随机）
- **结论：可以，单循环，$O(\epsilon^{-4})$。**
- $R_{k+1}$ 里多一个 $\|e^k\|$ 噪声项；$K=O(\epsilon^{-2})$ 外循环 × $m=O(\epsilon^{-2})$ 样本。
- **这是真结果，单循环可证。但不是 $-3$。**
- 原因：纯次梯度噪声无 averaged smoothness，PAGE/MVR 引擎用不上。

### 层次 3：单循环纯次梯度 DCA 到 $O(\epsilon^{-3})$（周报里"最优？"）
- **结论：在当前框架下基本不可能，而"不可能"本身是高质量 insight。**
- 文献里所有 $-3$ 都是光滑侧或 VR 侧买来的，与纯次梯度非光滑 $g$ 无关。
- Cutkosky $\epsilon^{-3}\delta^{-1}$ 的 $\delta$ 是 Goldstein 空间球，**不是你的 $\delta_g$**，不能类比。
- 这构成 Story C 的下界方向（尚需严格证明）。

**给老师汇报的一句话：**

> 次梯度类 DCA 的收敛性可以分析，单循环就行；它收敛到我们定义的两侧 Fenchel 稳定点（可解释、统一了已有几种 DC criticality）；确定性 $\epsilon^{-2}$、随机 $\epsilon^{-4}$；$\epsilon^{-3}$ 是纯次梯度 oracle 的天花板，突破它需要 Moreau 光滑化或方差缩减的 $g$-side Fenchel oracle——这正是论文的核心 insight 和 future work 方向。

---

## 8. 复杂度全景图

| 设定 | $g$-side oracle | 算法结构 | Rate | 度量 | 是否已有 |
|------|---------------|---------|------|------|---------|
| det. 非光滑 $g$ | exact subgradient | 单循环 | $O(\epsilon^{-2})$ | 两侧 Fenchel cert | **你的草稿（已做）** |
| stoch. **光滑** $\phi$（MDCA 领域） | MVR，averaged smooth | 单循环 | $O(\epsilon^{-3})$ | critical-dist / gap | MDCA/DCA-PAGE |
| stoch. 非光滑 $g$，raw bounded-var | 原始次梯度 | 单循环 | $O(\epsilon^{-4})$ | 两侧 Fenchel cert | **你的草稿（可做）** |
| stoch. 非光滑 $g$ → $\epsilon^{-3}$？ | Moreau/VR-compatible Fenchel | 单循环 | **TBD** | 两侧 Fenchel cert | **Story C 上界，待验证** |
| 一般 stoch. 非光滑非凸，Goldstein | directional oracle | online-to-nonconvex | $O(\epsilon^{-3}\delta^{-1})$ | Goldstein 邻域 | Cutkosky 2023（**$\delta$ 含义不同！**） |

---

## 9. 下一步行动（优先级排序）

1. **（最优先）做 Moreau 承重计算。**  
   $\mu=O(\epsilon)$ 时，$L_g=1/\mu$ 是否使 rate 常数从 $\epsilon^{-3}$ 退回 $\epsilon^{-4}$？还是保持 $-3$ 且只多个 $\kappa_g$ 相关常数？**这一页计算决定 Story C 是否存在。**

2. **（次优先）把层次 2 的随机 $O(\epsilon^{-4})$ 证明链条走通。**  
   $R_{k+1}$ 的期望控制 → descent inequality → telescope → 输出选择。这是 Story B 的闭合，也是 Story C 下界的对照组。

3. **（再次）确定 Story C 下界的形式化范围。**  
   针对特定估计量（弱版）还是整类 oracle（强版）？弱版可做，强版需新机制。

4. **（最后）按最终 Story 选择补全草稿的 Contributions 节和 Future Works 节。**

---

## 10. 关于 Theorem 1（"这个定理是否必要"）的确认

周报第 3 节的三点论证是正确的，逻辑链没有问题：

- **下界不从超类自动传子类**：Zhang 的 hardness 在大类（L-Lipschitz）成立，需要显式验证反例落在 DC 子类 $\mathcal{D}(\Delta,L)$ 里才能搬运。✓
- **DC oracle 更强，下界依然成立**：在反例上，查询点落在线性段，$\partial\phi(x_i)$ 和 $\partial g(x_i)$ 都是单点，与单 oracle 同信息；DC oracle 的额外能力在这个实例上没有帮助。✓  
- **度量更弱，结论更强**：$\partial_C(\phi-g)\subseteq \partial\phi - \partial g$，故 DC criticality 比 Clarke stationarity 弱（更容易满足）；证明"连更弱目标都不可达"比 Zhang 更强，而非其推论。✓

---

## 11. $(\delta_\phi,\delta_g,\varepsilon)$-critical 与 Goldstein 稳定性的关系，以及到精确临界点的距离

**讨论时间：2026-06-30**

### 11.1 问题背景

我们在 Definition `def:delta-eps-critical` 中定义了 **两侧 Fenchel 证书**：

$$
\operatorname{dist}\!\bigl(\partial_{\delta_\phi}\phi(\bar\bx),\ \partial_{\delta_g}g(\bar\bx)\bigr)\le\varepsilon,
$$

其中 $\bv\in\partial_\delta q(\bx)\iff \Phi_q(\bx,\bv):=q(\bx)+q^*(\bv)-\langle\bv,\bx\rangle\le\delta$（Fenchel–Young gap）。

需要厘清它与**标准 $(\delta,\varepsilon)$-Goldstein 稳定性**的关系，以及当误差 $\delta_\phi,\delta_g,\varepsilon\to0$ 时能否还原精确临界点。这套分析对标 Zhang et al. (ICML 2020) §3.1 的三段式逻辑。

---

### 11.2 Zhang §3.1 三段式逻辑（对标骨架）

| 步骤 | Zhang 的内容 | 我们要做的对标 |
|---|---|---|
| ① **硬度** | Thm 5：精确 $\varepsilon$-Clarke 稳定性有限时间不可达 | Thm 1（DC 版不可达，已有） |
| ② **光滑等价/折返** | Prop 6：光滑下 $(\tfrac\varepsilon{3L},\tfrac\varepsilon3)$-Goldstein $\Rightarrow \|\nabla f\|\le\varepsilon$ | **命题（待写）：光滑折返，误差 $\sqrt{2L\delta}$** |
| ③ **极限坍缩** | Lemma 7：$\delta\to0$ 时 Goldstein subdiff $\to$ Clarke subdiff | **直接：$\delta_\phi,\delta_g\to0$ 时 $\partial_{\delta}\phi\to\partial\phi$（同点，更干净）** |

---

### 11.3 两种松弛的本质区别

|  | **$(\delta,\varepsilon)$-Goldstein** | **$(\delta_\phi,\delta_g,\varepsilon)$-critical（本文）** |
|---|---|---|
| 扩张轴 | **空间**：在 $\mathcal B_\delta(\bar\bx)$ 内收集 Clarke 次梯度再取凸包 | **值**：允许 Fenchel–Young gap $\le\delta$（同点） |
| 两侧耦合 | 同一见证点 $y\in\mathcal B_\delta(\bar\bx)$，$\phi,g$ 的次梯度来自**同一** $y$ | 两侧**独立**：$\bu\in\partial_{\delta_\phi}\phi(\bar\bx)$，$\bv\in\partial_{\delta_g}g(\bar\bx)$ |
| 评估点 | 邻近 $y$ | **同点** $\bar\bx$ |

**方向性（包含关系）：** 设 $\phi,g$ 均 $G$-Lipschitz 凸，则空间扩张 $\subseteq$ 值扩张：

$$
\bigcup_{y\in\mathcal B_\delta(\bar\bx)}\partial q(y)\ \subseteq\ \partial_{2G\delta}q(\bar\bx).
$$

*证明一行：* 取 $\bu\in\partial q(y)$，$\|y-\bar\bx\|\le\delta$，则 $\Phi_q(\bar\bx,\bu)=q(\bar\bx)-q(y)-\langle\bu,\bar\bx-y\rangle\le G\delta+G\delta=2G\delta$。

**推论（Goldstein $\Rightarrow$ 本文定义）：** $(\delta,\varepsilon)$-Goldstein 稳定性 $\Rightarrow$ $(2G\delta,2G\delta,\varepsilon)$-critical。

**逆方向不成立。** 原因有二：
1. 值扩张比空间扩张严格更大（同点上 Fenchel gap 允许"值方向"偏差，空间扩张只允许邻近点）；
2. 我们的两侧证书**解耦**：$\bu,\bv$ 无需来自同一见证点，而 Goldstein 需要公共 $y$。

因此：**Goldstein 是我们新定义的真子集（对应更强的稳定性），我们的定义更弱，更容易被算法满足，故复杂度更低**（表格中 $\widetilde O(\delta^{-1}\varepsilon^{-2})$ vs Goldstein 的 $\widetilde O(\delta^{-1}\varepsilon^{-3})$）。

---

### 11.4 对标 Lemma 7（$\delta\to0$ 坍缩还原）

**命题（坍缩还原）：** 凸函数的 $\delta$-次微分关于 $\delta$ 单调递减，且

$$
\bigcap_{\delta>0}\partial_\delta q(\bar\bx)=\partial q(\bar\bx).
$$

故 $\delta_\phi,\delta_g,\varepsilon\to0$ 时

$$
\operatorname{dist}\!\bigl(\partial_{\delta_\phi}\phi(\bar\bx),\,\partial_{\delta_g}g(\bar\bx)\bigr)\le\varepsilon
\ \longrightarrow\ 
\operatorname{dist}\!\bigl(\partial\phi(\bar\bx),\,\partial g(\bar\bx)\bigr)=0,
$$

即 $\partial\phi(\bar\bx)\cap\partial g(\bar\bx)\neq\emptyset$，精确 DC 临界 $0\in\partial\phi(\bar\bx)-\partial g(\bar\bx)$ 成立。

**与 Zhang Lemma 7 的关键差异：**
- Zhang 的坍缩是**空间邻域** $\delta\to0$ 的 Painlevé–Kuratowski 集合收敛（Goldstein subdiff → Clarke subdiff），需要将评估点从 $y$ 拉回 $\bar\bx$；
- 我们的坍缩是**同点**的单调集合极限，直接还原 $\partial\phi(\bar\bx)$ 和 $\partial g(\bar\bx)$，不涉及点的移动，逻辑更简洁。

---

### 11.5 对标 Prop 6（光滑情形折返，回答"距精确临界点多近"）

**核心不等式（光滑凸函数的共轭强凸性）：** 若 $q$ 是 $L_q$-光滑凸函数，则 $q^*$ 是 $\tfrac{1}{L_q}$-强凸，于是

$$
\Phi_q(\bar\bx,\bv)\ge\frac{1}{2L_q}\|\bv-\nabla q(\bar\bx)\|^2.
$$

因此 $\bv\in\partial_{\delta_q}q(\bar\bx)$ 蕴含

$$
\boxed{\|\bv-\nabla q(\bar\bx)\|\le\sqrt{2L_q\delta_q}.}
$$

这就是我们语境下的"折返误差"。注意：Zhang 的误差是线性的 $L\delta$（因为 $\delta$ 是空间半径），我们的是 $\sqrt{2L\delta}$（因为 $\delta_\phi,\delta_g$ 是**函数值 gap**，经共轭强凸换成梯度偏差，必然带平方根）。**量纲不同，不可直接类比，写命题时需要注明。**

**（B1）仅 $g$ 光滑（最常见的 DC 情形：$\phi$ 非光滑，$g$ 光滑）：**

$g$-侧证书 $\bv\in\partial_{\delta_g}g(\bar\bx)$ 在**同点** $\bar\bx$ 折返到 $\nabla g(\bar\bx)$，误差 $\sqrt{2L_g\delta_g}$：

$$
\operatorname{dist}\!\bigl(\nabla g(\bar\bx),\ \partial_{\delta_\phi}\phi(\bar\bx)\bigr)
\le \|\bu-\bv\|+\|\bv-\nabla g(\bar\bx)\|
\le \varepsilon+\sqrt{2L_g\delta_g}.
$$

即 $\bar\bx$ 到精确临界条件（$g$ 侧锚定在 $\nabla g(\bar\bx)$）的残差为 $\varepsilon+\sqrt{2L_g\delta_g}$，**同点，无位移**。

**（B2）两边都光滑：**

$$
\boxed{\|\nabla\Psi(\bar\bx)\|=\|\nabla\phi(\bar\bx)-\nabla g(\bar\bx)\|\le\varepsilon+\sqrt{2L_\phi\delta_\phi}+\sqrt{2L_g\delta_g}.}
$$

$\delta_\phi,\delta_g,\varepsilon\to0$ 时 $\|\nabla\Psi(\bar\bx)\|\to0$，两种稳定性等价，与 Zhang Prop 6 完全同构，但**全程在同点 $\bar\bx$ 完成，无空间位移**。

---

### 11.6 非光滑情形：Brøndsted–Rockafellar 折返到邻近点

$\phi$（或 $g$）非光滑时，无法在同点锚定到精确次梯度，需要用 BR 定理折返到邻近点。

**BR 定理（对凸函数）：** $\bu\in\partial_{\delta_\phi}\phi(\bar\bx)$ $\Rightarrow$ 取 $\eta=\sqrt{\delta_\phi}$，存在 $\bx_\phi,\bu'$ 使得

$$
\bu'\in\partial\phi(\bx_\phi),\quad \|\bx_\phi-\bar\bx\|\le\sqrt{\delta_\phi},\quad \|\bu'-\bu\|\le\sqrt{\delta_\phi}.
$$

**（C1）两边都非光滑：** 对 $\phi,g$ 各用一次 BR，得两个锚点 $\bx_\phi,\bx_g$：

$$
\bu'\in\partial\phi(\bx_\phi),\quad \bv'\in\partial g(\bx_g),\quad 
\|\bx_\phi-\bar\bx\|\le\sqrt{\delta_\phi},\quad \|\bx_g-\bar\bx\|\le\sqrt{\delta_g},
$$

$$
\|\bu'-\bv'\|\le\varepsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g}.
$$

这恰好是文献里的 **nearly $\varepsilon'$-critical point**（两锚点版，$\varepsilon'=\varepsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g}$），见草稿 `Def: epsilon-critical point 3`（Yao 2022）。

**（C2）$g$ 光滑、$\phi$ 非光滑（最常用 DC 情形的一般版）：** 只对 $\phi$ 用 BR，$g$-侧用光滑性在折返点处补 Lipschitz 误差 $\|\nabla g(\bx_\phi)-\nabla g(\bar\bx)\|\le L_g\sqrt{\delta_\phi}$，得**单锚点、同点 DC 残差**：

$$
\boxed{\operatorname{dist}\!\bigl(0,\ \partial\phi(\bx_\phi)-\nabla g(\bx_\phi)\bigr)\le\varepsilon+(1+L_g)\sqrt{\delta_\phi}+\sqrt{2L_g\delta_g},\quad \|\bx_\phi-\bar\bx\|\le\sqrt{\delta_\phi}.}
$$

即：有限时间输出点 $\bar\bx$ 落在一个**真临界残差为 $O(\varepsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g})$ 的近似临界点 $\bx_\phi$** 的 $\sqrt{\delta_\phi}$ 邻域内。

---

### 11.7 汇总："距精确临界点多近"

| 结构假设 | 折返到哪 | DC 残差（到 $0\in\partial\phi-\partial g$） | 空间位移 $\|\bx_\phi-\bar\bx\|$ |
|---|---|---|---|
| 两边**光滑** | **同点** $\bar\bx$ | $\varepsilon+\sqrt{2L_\phi\delta_\phi}+\sqrt{2L_g\delta_g}$ | $0$ |
| 仅 $g$ **光滑** | 邻近点 $\bx_\phi$ | $\varepsilon+(1+L_g)\sqrt{\delta_\phi}+\sqrt{2L_g\delta_g}$ | $\le\sqrt{\delta_\phi}$ |
| 两边**非光滑** | 两锚点 $\bx_\phi,\bx_g$ | $\varepsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g}$ | $\le\sqrt{\delta_\phi},\sqrt{\delta_g}$ |

**结论：** 我们的 $(\delta_\phi,\delta_g,\varepsilon)$-critical point 在误差参数的量级上与精确临界点的距离是 $O(\varepsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g})$（DC 残差），空间位移为 $O(\sqrt{\delta_\phi})$（$\phi$ 非光滑时）或 $0$（$\phi,g$ 均光滑时）。

---

### 11.8 必须在论文中诚实标注的两个技术点

**（1）量纲差异不可掩盖。** Zhang 的折返误差线性 $L\delta$（空间半径），我们是 $\sqrt{2L\delta}$（函数值 gap 经共轭强凸换算）。在命题中须写清 $\delta_\phi,\delta_g$ 的单位是"函数值"而非"空间半径"。

**（2）"DC 残差小" $\neq$ "到真精确临界点的空间距离小"。** 上表第 3 列是 DC 残差，BR 给的 $\sqrt\delta$ 是到**一个残差小的点**的位移，不是到**最近的精确临界点 $\bx^*$** 的距离。后者需要额外的 error bound / KL 条件 / sharpness 才能由残差反推空间距离。命题里只声明残差刻画，空间距离留作 Remark。

---

### 11.9 对标小结

| Zhang §3.1 | 我们的对应结果 | 主要差异 |
|---|---|---|
| Thm 5（精确不可达） | Thm 1（DC 精确不可达，已有） | DC oracle 更强，结论更强 |
| Lemma 7（空间坍缩 $\to$ Clarke） | 命题（值坍缩 $\to$ $\partial\phi,\partial g$，**同点**） | 同点单调极限，更干净 |
| Prop 6（光滑折返，误差 $L\delta$） | 命题（光滑折返，误差 $\sqrt{2L\delta}$，**同点**） | 量纲差异：$\delta$ 是值 gap |
| 无对应（空间扩张机制不需要） | BR 折返（非光滑，邻近点，误差 $\sqrt{\delta}$） | 新增，统一 DCA 旧点线性化解释 |

1. outline

- 可以刻画，而且应该按 **2020 ICML 的三步逻辑**来写。
- 你的新稳定点距离 exact DC criticality 有两种刻画：**图距离 \(O(\sqrt{\delta})\)** 和 **光滑情形下的同点残差 \(O(\sqrt{L\delta})\)**。
- 当 \(\delta_\phi,\delta_g,\epsilon\to0\) 时，在自然有界性和收敛假设下，可以还原回
  $$
  \partial\phi(x)\cap\partial g(x)\neq\emptyset.
  $$

2. conclusion

大哥，你这个思路是对的。对标 Zhang et al. ICML 2020 的 3.1 节，新的有限时间稳定性可以这样解释：

$$
\operatorname{dist}
\left(
\partial_{\delta_\phi}\phi(x),
\partial_{\delta_g}g(x)
\right)
\le \epsilon
$$

是 exact DC criticality

$$
0\in \partial\phi(x)-\partial g(x)
$$

的一个 **finite-time reachable relaxation**。当误差趋于零时，它会回到原来的 DC criticality；如果某一侧光滑，还能给出更强的定量误差界。

## 1. 对标 2020 ICML 的逻辑

Zhang et al. ICML 2020 的逻辑是：

1. ordinary \(\epsilon\)-stationarity 在一般 nonsmooth nonconvex 下有限时间不可达。
2. 引入 \((\delta,\epsilon)\)-Goldstein stationarity，用邻域内 generalized gradients 的 convex combination 代替同点 Clarke subgradient。
3. 证明这个定义合理：
   $$
   \delta\downarrow0
   \quad\Longrightarrow\quad
   \partial_\delta^G F(x)\to \partial_C F(x).
   $$

对应到你的 DC 版本，可以写成：

1. exact same-point DC criticality
   $$
   0\in\partial\phi(x)-\partial g(x)
   $$
   在一般 nonsmooth DC 下不是有限时间可达目标。
2. 引入 two-sided Fenchel certificate：
   $$
   \operatorname{dist}
   \left(
   \partial_{\delta_\phi}\phi(x),
   \partial_{\delta_g}g(x)
   \right)
   \le \epsilon.
   $$
3. 证明合理性：
   $$
   \delta_\phi,\delta_g,\epsilon\to0
   \quad\Longrightarrow\quad
   \partial\phi(x)\cap\partial g(x)\neq\emptyset.
   $$

Zhang et al. 的原文逻辑可以看 PMLR 版本，他们明确说 exact \(\epsilon\)-stationary 有有限时间障碍，因此引入 \((\delta,\epsilon)\)-stationarity，并说明 \(\delta\to0\) 时回到 Clarke stationarity。[Zhang et al. 2020](https://proceedings.mlr.press/v119/zhang20p/zhang20p.pdf)

## 2. 你的定义和 exact criticality 的距离

你的定义是：

$$
\operatorname{dist}
\left(
\partial_{\delta_\phi}\phi(x),
\partial_{\delta_g}g(x)
\right)
\le \epsilon.
$$

这等价于存在

$$
u\in\partial_{\delta_\phi}\phi(x),
\qquad
v\in\partial_{\delta_g}g(x),
$$

使得

$$
\|u-v\|\le \epsilon.
$$

这里的 \(\partial_\delta q(x)\) 是 convex analysis 的 \(\delta\)-subdifferential：

$$
u\in\partial_\delta q(x)
\Longleftrightarrow
q(z)\ge q(x)+\langle u,z-x\rangle-\delta,
\qquad \forall z.
$$

它和 exact subdifferential 的关系是：

$$
\partial q(x)\subseteq \partial_\delta q(x),
$$

并且

$$
\boxed{
\bigcap_{\delta>0}\partial_\delta q(x)
=
\partial q(x).
}
$$

所以在固定点 \(x\) 上：

$$
\delta\downarrow0
\quad\Longrightarrow\quad
\partial_\delta q(x)\downarrow \partial q(x).
$$

这就是你定义能还原回 \(\partial g\) 和 \(\partial\phi\) 的核心。

## 3. 更精确的图距离刻画

对一般 nonsmooth convex \(q\)，不能指望直接得到

$$
\operatorname{dist}(u,\partial q(x))\le C\delta.
$$

原因是 \(\partial q\) 可能在 \(x\) 处跳变。

但可以用 Brøndsted–Rockafellar 定理得到 **graph distance** 形式：

若

$$
u\in\partial_\delta q(x),
$$

则对任意 \(\lambda>0\)，存在

$$
y,\quad \hat u\in\partial q(y),
$$

使得

$$
\|y-x\|\le \lambda,
$$

以及

$$
\|\hat u-u\|\le \frac{\delta}{\lambda}.
$$

取

$$
\lambda=\sqrt{\delta},
$$

得到

$$
\boxed{
\operatorname{dist}
\left(
(x,u),
\operatorname{gph}\partial q
\right)
\lesssim
\sqrt{\delta}.
}
$$

因此你的 two-sided certificate 可以推出：

存在

$$
x_\phi,x_g,
\qquad
\hat u\in\partial\phi(x_\phi),
\qquad
\hat v\in\partial g(x_g),
$$

满足

$$
\|x_\phi-x\|\lesssim \sqrt{\delta_\phi},
\qquad
\|x_g-x\|\lesssim \sqrt{\delta_g},
$$

并且

$$
\|\hat u-\hat v\|
\lesssim
\epsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g}.
$$

这给出一个非常清楚的解释：

$$
\boxed{
\text{你的 finite-time point 是一个 nearby split exact-subgradient certificate。}
}
$$

注意这里 \(x_\phi\) 和 \(x_g\) 可以不同，所以它还不是 same-point exact DC criticality。

## 4. 如果凹的部分光滑

如果 DC 目标是

$$
\Psi(x)=\phi(x)-g(x),
$$

且凹部分 \(-g\) 对应的 \(g\) 是 convex \(L_g\)-smooth，则

$$
\partial g(x)=\{\nabla g(x)\}.
$$

这时有更强的同点误差界：

若

$$
v\in\partial_{\delta_g}g(x),
$$

则 Fenchel gap 控制梯度误差：

$$
\boxed{
\|v-\nabla g(x)\|
\le
\sqrt{2L_g\delta_g}.
}
$$

因此，如果你的 certificate 满足

$$
\operatorname{dist}
\left(
\partial_{\delta_\phi}\phi(x),
\partial_{\delta_g}g(x)
\right)
\le \epsilon,
$$

那么可以推出

$$
\boxed{
\operatorname{dist}
\left(
\nabla g(x),
\partial_{\delta_\phi}\phi(x)
\right)
\le
\epsilon+\sqrt{2L_g\delta_g}.
}
$$

这已经很接近原来的 DC criticality：

$$
\nabla g(x)\in\partial\phi(x).
$$

如果进一步 \(\phi\) 也 \(L_\phi\)-smooth，则

$$
\partial\phi(x)=\{\nabla\phi(x)\},
$$

并且

$$
\boxed{
\|\nabla\phi(x)-\nabla g(x)\|
\le
\epsilon
+\sqrt{2L_\phi\delta_\phi}
+\sqrt{2L_g\delta_g}.
}
$$

这就是最强、最干净的定量刻画。

## 5. 如果只有一侧非光滑

若 \(g\) 光滑、\(\phi\) 非光滑，则你能得到：

$$
\operatorname{dist}
\left(
\nabla g(x),
\partial_{\delta_\phi}\phi(x)
\right)
\le
\epsilon+\sqrt{2L_g\delta_g}.
$$

但不能自动得到

$$
\operatorname{dist}
\left(
\nabla g(x),
\partial\phi(x)
\right)
$$

的小量，除非对 \(\phi\) 加额外条件，例如 polyhedral、metric regularity、subdifferential calmness 等。

所以严谨说法是：

$$
\partial_{\delta_\phi}\phi(x)
\to
\partial\phi(x)
$$

成立，但有限 \(\delta_\phi>0\) 时，不能无条件给出同点距离界。

## 6. 极限还原结论

假设存在序列

$$
x_k\to x^\star,
$$

并且

$$
\operatorname{dist}
\left(
\partial_{\delta_{\phi,k}}\phi(x_k),
\partial_{\delta_{g,k}}g(x_k)
\right)
\le \epsilon_k,
$$

其中

$$
\delta_{\phi,k}\to0,
\qquad
\delta_{g,k}\to0,
\qquad
\epsilon_k\to0.
$$

再假设 \(\phi,g\) 在相关邻域内 locally Lipschitz，使得 certificate 有界。则可以取子列，使得

$$
u_k\in\partial_{\delta_{\phi,k}}\phi(x_k),
\qquad
v_k\in\partial_{\delta_{g,k}}g(x_k),
$$

并且

$$
\|u_k-v_k\|\le\epsilon_k.
$$

由有界性取极限：

$$
u_k\to u^\star,
\qquad
v_k\to v^\star.
$$

因为

$$
\epsilon_k\to0,
$$

所以

$$
u^\star=v^\star.
$$

又因为 \(\delta\)-subdifferential 的闭图性质，

$$
u^\star\in\partial\phi(x^\star),
\qquad
v^\star\in\partial g(x^\star).
$$

于是

$$
u^\star\in\partial\phi(x^\star)\cap\partial g(x^\star).
$$

因此

$$
\boxed{
0\in\partial\phi(x^\star)-\partial g(x^\star).
}
$$

这就是你要的“误差趋于 0 后还原回原 criticality”。

## 7. 我建议你写成一个 proposition

可以设计成三段：

**Proposition A：Exact Consistency**

$$
\delta_\phi=\delta_g=\epsilon=0
\quad\Longleftrightarrow\quad
0\in\partial\phi(x)-\partial g(x).
$$

**Proposition B：Graph-distance Approximation**

若

$$
\operatorname{dist}
\left(
\partial_{\delta_\phi}\phi(x),
\partial_{\delta_g}g(x)
\right)
\le\epsilon,
$$

则存在 nearby exact subgradient certificates：

$$
\hat u\in\partial\phi(x_\phi),
\qquad
\hat v\in\partial g(x_g),
$$

满足

$$
\|x_\phi-x\|\lesssim \sqrt{\delta_\phi},
\qquad
\|x_g-x\|\lesssim \sqrt{\delta_g},
$$

以及

$$
\|\hat u-\hat v\|
\lesssim
\epsilon+\sqrt{\delta_\phi}+\sqrt{\delta_g}.
$$

**Proposition C：Smooth-side Conversion**

如果 \(g\) 是 \(L_g\)-smooth，则

$$
\operatorname{dist}
\left(
\nabla g(x),
\partial_{\delta_\phi}\phi(x)
\right)
\le
\epsilon+\sqrt{2L_g\delta_g}.
$$

如果 \(\phi,g\) 都 smooth，则

$$
\|\nabla\phi(x)-\nabla g(x)\|
\le
\epsilon+\sqrt{2L_\phi\delta_\phi}+\sqrt{2L_g\delta_g}.
$$

## 8. 最终判断

你的方向是对的，但建议不要声称：

$$
(\delta_\phi,\delta_g,\epsilon)\text{-critical}
\Rightarrow
\text{near exact DC critical at the same point}
$$

在一般 nonsmooth 情形下这句话不成立。

更严谨的说法是：

$$
\boxed{
\text{一般 nonsmooth：得到 graph-distance 近似和极限一致性。}
}
$$

$$
\boxed{
\text{光滑侧存在时：可得到同点残差的定量误差界。}
}
$$

本地草稿中你已经有对应基础：Goldstein 定义和 \(\delta\to0\) 的逻辑在 [preliminaries.tex](/Users/liluxuan/Documents/My_Papers/6_Stochastic_DCAM/cdc2026_template/extension/sections/preliminaries.tex:122)，你的 DCA certificate 定义在 [algorithm_DCA.tex](/Users/liluxuan/Documents/My_Papers/6_Stochastic_DCAM/cdc2026_template/extension/sections/algorithm_DCA.tex:223)，transport lemma 在 [algorithm_DCA.tex](/Users/liluxuan/Documents/My_Papers/6_Stochastic_DCAM/cdc2026_template/extension/sections/algorithm_DCA.tex:387)。


I've now mapped both definitions precisely. Here is the clean analysis of how the two notions relate.

Setup
Both certify approximate stationarity of the same DC function $\Psi=\phi-g$ ($\phi,g$ proper closed convex, $G$-Lipschitz / bounded subgradients $|\cdot|\le G$), but they relax exact criticality $0\in\partial\phi(\bar x)-\partial g(\bar x)$ along different axes:

enlargement axis	coupling of $\phi,g$	evaluation point
$(\delta,\varepsilon)$-Goldstein $\operatorname{dist}(0,\partial^G_\delta\Psi(x))\le\varepsilon$	spatial ball $\mathcal B_\delta(x)$ + Clarke + conv	coupled: subgradients of $\phi,g$ taken at a common witness $y$	nearby $y\in\mathcal B_\delta(x)$
Your $(\delta_\phi,\delta_g,\varepsilon)$-critical $\operatorname{dist}(\partial_{\delta_\phi}\phi(x),\partial_{\delta_g}g(x))\le\varepsilon$	value tolerance (Fenchel–Young gap)	decoupled: $\phi$-side and $g$-side certificates independent	the same point $x$
So the question "包含还是什么" has a clean answer: one-directional containment, with your notion the strictly weaker (larger) set.

The bridge lemma (spatial $\subseteq$ value)
For $G$-Lipschitz convex $q$ and $|y-x|\le\delta$, take $u\in\partial q(y)$. Its Fenchel–Young gap at $x$ is
$$\Phi_q(x,u)=q(x)+q^*(u)-\langle u,x\rangle=q(x)-q(y)-\langle u,x-y\rangle\in[0,,2G\delta],$$
(lower bound by convexity; upper bound since $|q(x)-q(y)|\le G\delta$ and $|\langle u,x-y\rangle|\le G\delta$). Hence
$$\boxed{\ \bigcup_{y\in\mathcal B_\delta(x)}\partial q(y)\ \subseteq\ \partial_{2G\delta}q(x).\ }\tag{$\star$}$$
The spatial enlargement is contained in the value enlargement. (If $q$ is $L$-smooth the constant sharpens to $\tfrac{L}{2}\delta^2$.)

Proposition — Goldstein $\Rightarrow$ your notion
$(\delta,\varepsilon)$-Goldstein stationary $\implies$ $(2G\delta,,2G\delta,,\varepsilon)$-critical.

Proof. Let $\omega\in\partial^G_\delta\Psi(x)$ with $|\omega|\le\varepsilon$. By Carathéodory $\omega=\sum_i\lambda_i\omega_i$, $\omega_i\in\partial_C\Psi(y_i)\subseteq\partial\phi(y_i)-\partial g(y_i)$, $y_i\in\mathcal B_\delta(x)$. Write $\omega_i=u_i-v_i$ and set $\bar u=\sum_i\lambda_i u_i,\ \bar v=\sum_i\lambda_i v_i$. By $(\star)$, each $u_i\in\partial_{2G\delta}\phi(x)$; since $\partial_{2G\delta}\phi(x)$ is convex, $\bar u\in\partial_{2G\delta}\phi(x)$, and likewise $\bar v\in\partial_{2G\delta}g(x)$. Then
$$\operatorname{dist}\big(\partial_{2G\delta}\phi(x),\partial_{2G\delta}g(x)\big)\le|\bar u-\bar v|=|\omega|\le\varepsilon. \qquad\square$$

So Goldstein $\subseteq$ your set (up to the harmless $2G$ scaling of the radii). Your certificate is implied by, hence weaker than, Goldstein — exactly the "easier target ⇒ lower complexity" story your Table tells ($\widetilde O(\delta^{-1}\varepsilon^{-2})$ vs Goldstein's $\widetilde O(\delta^{-1}\varepsilon^{-3})$).

The converse fails — and why (two independent reasons)
(1) Value $\supsetneq$ spatial, even at the same point. $(\star)$ is strict. Take $\phi(x)=|x|$ at a smooth point $x>\delta$: spatially $\bigcup_{|y-x|\le\delta}\partial\phi(y)={1}$, but $\partial_\delta\phi(x)=[,1-\delta/x,,1,]$. The value-subdifferential is a fat interval where the spatial one is a singleton.

(2) Decoupling — the structural gap. This is the essential one. A Goldstein subgradient of $\Psi$ requires $u\in\partial\phi(y)$ and $v\in\partial g(y)$ at a common $y$. Your certificate only asks for $u\in\partial_{\delta_\phi}\phi(x)$, $v\in\partial_{\delta_g}g(x)$ with $|u-v|\le\varepsilon$ — no common witness.

Brøndsted–Rockafellar gives a partial reconstruction (a $\delta$-subgradient at $x$ is $\sqrt\delta$-close to an exact subgradient at a $\sqrt\delta$-nearby point), but applied to $\phi$ and $g$ it lands them at different nearby points $x_\phi\ne x_g$. You cannot reassemble these into an element of $\partial\phi(y)-\partial g(y)$ at a single $y$, so no Goldstein subgradient is produced. There is no reverse inclusion with comparable parameters.

Limit consistency
Drive all radii to $0$: Goldstein $\to$ Clarke ($\partial^G_\delta\Psi\to\partial_C\Psi\subseteq\partial\phi-\partial g$), and your notion with $\delta_\phi=\delta_g=0$ becomes $\operatorname{dist}(\partial\phi(x),\partial g(x))\le\varepsilon$. Both collapse to the same exact DC criticality $0\in\partial\phi-\partial g$. They agree only in the limit; for any fixed positive radius your set is strictly larger.

One-line takeaway
$(\delta,\varepsilon)$-Goldstein $\subsetneq$ $(2G\delta,2G\delta,\varepsilon)$-critical. Containment is strict and one-way: Goldstein implies your notion (so your certificate is genuinely weaker/cheaper), but your decoupled, value-tolerance, same-point certificate does not imply any Goldstein-type guarantee, because (i) value-enlargement dominates spatial-enlargement and (ii) the two convex sides are no longer tied to a common witness point.

Want me to formalize this as a proposition + remark (with the $|x|$ smooth-point counterexample) and drop it into preliminaries.tex or the appendix? I'd add it right after Definition def:delta-eps-critical to position your notion against the Goldstein baseline.

