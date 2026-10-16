> 历史材料：按原文保存。证明状态、文献判断与行号属于当时版本；当前状态见 `notes/progress/PROJECT_STATUS.md`，本次整理未重新证明其结论。

**z**# 研究简介 Note — 李露璇（Luxuan Li）

---

## Part I · 我的工作

### 1 · DC 正则化非凸约束问题的单循环随机方法 [ICML 2026】

| | |
|---|---|
| **问题** | $\min\ \varphi(x) - g(x)\ \ \text{s.t.}\ \ c(x) = 0$ —— $\varphi, g$ 非光滑，$c$ 非线性非凸，随机 first-oracle |
| **结果** | 单循环：随机 optimal $O(\varepsilon^{-3})$ oracle complexity |
| **核心洞察** | smoothing $\mu_k \downarrow 0$、罚参数 $\rho_k \uparrow \infty$、递归动量|

### 2 · DualHash：深度哈希的随机原始–对偶方法 [在审，SIAM J. Imaging Sciences]

| | |
|---|---|
| **问题** | 具体得到问题形式 |
| **结果** | 随机非凸多块原始–对偶优化的随机 optimal $O(\varepsilon^{-3})$ oracle complexity|
| **核心洞察** |W正则项的共轭函数及其邻近算子，非凸PDHG变式；|

### 3 · 双阻尼线性化 ADMM（DDLALM）[working paper]

| | |
|---|---|
| **问题** | $\min\ f(x) + g(x) + h(c(x))$ —— $g, h$ 非光滑、可非凸，c$ 非线性；|
| **结果** | Optimal $O(\varepsilon^{-3})$ 次迭代达到 $\varepsilon$-KKT 点 |
| **核心洞察** | a novel proximal-dual regularizaed ALM and adaptive regularization parameters adapative|

### 4 · 非光滑 DC 优化的统一分析 [working paper]

| | |
|---|---|
| **问题** | $\min\ \varphi(x) - g(x)$ —— 两个分量均为非光滑凸函数， $\varphi$可$\rho$-弱凸|
| **结果** | 传统 $\varepsilon$-criticality 在有限时间内**不可达**；需要一个统一的 criticality 概念恢复最优复杂度，并建立和一般的Goldstein-stationarity的关系 |
| **核心洞察** | 复杂度结果中，障碍出现在 oracle 层面，DCA算法在$g$非光滑下，无需光滑化，在此新的定义点下达到最优复杂度；|

**技术工具箱**：方差缩减（STORM 型递归动量）· subdifferential· primal-dual method; Lypunove function购药

