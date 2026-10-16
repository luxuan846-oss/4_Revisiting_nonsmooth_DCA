# 研究重叠核对与 JMLR 阅读建议

核对日期：2026-10-10。用户确认：2026 年 8 月形成主要结果，尚未公开。

## 当前判断

**本轮没有找到完整覆盖“同点三参数值松弛 DC 证书、驻点关系、指定分量信息模型下复杂度”这一组合的公开论文。但这只是定向检索结论，不能证明无人独立完成。**

**已确认存在直接相关的先行工作和 8 月以来的新结果。** 广义非光滑优化下界、DCA 的 gap 度量、Bregman 下降分析都已有实质结果。论文需要明确哪些定理超出了这些结果。

比较对象按当前项目的 DC/VAC 研究主线确定。读取了 `README.md`、`nonsmooth_discussion_su/llx_nonsmooth.tex`、`nonsmooth_discussion_su/INNOVATION_POINTS.md`，并参考约束 DC 稿件。当前讨论稿把固定函数类上的 DC 分量 oracle 下界列为未完成问题；本报告不把它计为已证明贡献。较早创新点总结中的更强陈述不能替代当前定理。

## 本轮核查范围

- 读取用户提供的两段 Codex 聊天及其原始文献记录。原始数据包含 1,035 条 `math.OC` 记录、2,766 条更新查询记录、9 条邮箱补充记录；它们存在交叉和无关项，不能相加当作独立论文数。
- 从以上记录的标题和摘要中定向筛出 28 条 DC、Goldstein、弱凸、Fenchel 相关候选，保存于 `thread_literature_candidates.json`。
- 补查 arXiv 2026-08-01 至 2026-08-31 的相关关键词，得到 27 条返回记录；补查 2026-10-04 至 2026-10-10 的更新时间窗口，得到 6 条。查询与返回值保存在对应 JSON。关键词会产生无关命中，也可能漏掉换用术语的工作。
- 对重点论文进行三类核对：元数据与首发日期、正文中的假设与结果、已有记录/正式发表页面或官方 BibTeX。来源间并非全部独立，不将“同站点三个入口”声称为三个独立证据。
- JMLR 阅读清单核对官方摘要、官方 BibTeX、PDF 首页及相关正文；检查了第 27 卷中与当前主题相近的标题。
- 本机未找到 `verify_papers.py`，采用直接官方来源核验。下表中的“已核验”表示身份和出处核验，且注明正文阅读范围；不表示完成整篇证明审计。

本轮无法覆盖未公开稿、非公开审稿材料，以及尚未被搜索/API 收录的页面。

## 8 月以来需要立即比较的公开工作

### 1. Li–Pan：弱凸问题的确定性最优复杂度

**已核验，arXiv 元数据和正文。** Jiajin Li, Siyu Pan, *Optimal Deterministic Oracle Complexity for Weakly Convex Optimization*，2026-08-04，arXiv:2608.03246。当前为预印本。

来源：[摘要与版本历史](https://arxiv.org/abs/2608.03246)；[正文](https://arxiv.org/html/2608.03246v1)。

事实：研究全局 Lipschitz 弱凸函数，以 Moreau 包络梯度衡量驻点；oracle 返回函数值和整个次微分。在文中规定的初始差距和精度范围内，给出四次精度依赖的确定性下界，并与已知上界匹配。

推断：若贡献写成“确定性弱凸优化的四次精度复杂度是否必要”，该问题已有直接答案。DC/VAC 的目标不自动被这篇覆盖，但也不能只说“oracle 不同”就排除它：对规范二次 DC 分解，要核对信息模拟、精度转换和分量全局 Lipschitz 限制。二次分量在全空间不具有统一有界次梯度，不能直接忽略函数类差异。

### 2. Kornowski：Goldstein 驻点的精度下界

**已核验，arXiv 元数据和正文第 2–3、5 节。** Guy Kornowski, *The Complexity of Finding Stationary Points in Nonsmooth Nonconvex Optimization*，2026-09-15，arXiv:2609.17780。当前为预印本。

来源：[摘要与版本历史](https://arxiv.org/abs/2609.17780)；[正文](https://arxiv.org/html/2609.17780v1)。

事实：证明 Goldstein 驻点的紧精度下界，并研究另一种允许组合更远梯度的松弛驻点。当前版本的正式定理针对 **zero-respecting 算法**，即不主动进入 oracle 尚未揭示的坐标方向的算法。第 5 节把扩展到任意随机局部算法列为未来版本内容。

推断：它更新了你对一般非光滑驻点复杂度的背景陈述。不能把其当前结果不加算法类限制地转述为“所有随机算法的下界”。它没有直接建立同点、依赖 DC 分解的三参数证书下界。

### 3. Kornowski：确定性算法的指数维数代价

**已核验，arXiv 元数据和正文 Theorem 3.1。** Guy Kornowski, *The Exponential Price of Determinism in Nonsmooth Nonconvex Optimization*，2026-09-20，arXiv:2609.23837。当前为预印本。

来源：[摘要与版本历史](https://arxiv.org/abs/2609.23837)；[正文](https://arxiv.org/html/2609.23837v1)。

事实：在一般 Lipschitz 非凸函数类和局部 oracle 模型下，确定性算法寻找 Goldstein 驻点的查询复杂度具有指数级维数依赖。定理有明确的精度和维数适用范围。

推断：若论文把“确定性一般非光滑优化能否拥有多项式维数依赖”作为待解决问题，需要更新。给定 DC 分解后，oracle 会提供目标函数局部信息以外的结构，且 VAC 的成功判据不同；不能未经归约直接移植这个下界。

### 4. Ding–Yuan：指数下界、上界与 DC 困难实例

**已核验，arXiv 元数据和正文 Theorems 2.2–2.3、第 6.2 节、Appendix C。** Yixi Ding, Ya-xiang Yuan, *Exponential Deterministic Query Complexity of Goldstein Stationarity*，2026-09-29 首发，2026-10-07 更新至 v2，arXiv:2609.38082。当前为预印本。作者注明 v2 仅修正排版错误。

来源：[摘要与版本历史](https://arxiv.org/abs/2609.38082)；[正文](https://arxiv.org/html/2609.38082v2)。

版本差异已直接核对 arXiv v1/v2 的完整 TeX 源文件：仅两处将作者名 `Ya-Xiang Yuan` 更正为 `Ya-xiang Yuan`，分别位于 PDF 作者元数据与标题页作者字段。正文、定理、证明、DC 附录以及同期工作说明均未变化。差异保存于 `ding_yuan_versions/source_diff.txt`。

事实：研究确定性局部 oracle，给出指数级下界和函数值 oracle 上界。**Proposition C.1 明确证明其每个有限困难实例都是 DC。** 给出的凸分量 Lipschitz 上界随构造中分支数线性增长。Remark C.2 明确区分某个分解的代价与所有分解中的最优内在量。正文也披露了 Kornowski 的相近同期工作。

推断：不能以“他们研究一般函数，我们研究 DC”排除重叠。真正要比较的是：

1. 两个凸分量的大小限制是否固定，是否独立于查询预算。
2. 是否分别向算法提供两个分量的信息。
3. 下界目标是目标函数的 Goldstein 驻点，还是分解相关的 DC/VAC 证书。

待验证：你的拟议下界是否在这三点上给出实质新增内容。目前本地讨论稿没有完成该下界，不能仅凭研究方向认定已有可发表的区分。

### 5. Li–Tsuchiya–Yamanishi：复合 online-to-nonconvex 转换

**已核验，arXiv 元数据，正文 Assumption 3.1、Definition 3.3 和第 4 节。** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi, *Composite Online-to-Nonconvex Conversion with Optimal Oracle Complexity*，2026-10-08，arXiv:2610.12328。当前为预印本。

来源：[摘要与版本历史](https://arxiv.org/abs/2610.12328)；[正文](https://arxiv.org/html/2610.12328v1)。

事实：研究非凸 Lipschitz 项加凸正则项，并采用 proximal Goldstein 驻点。给出随机一阶和零阶复杂度；一阶部分的 Assumption 3.1 要求该非凸项可微，并规定无偏性及二阶矩条件。不能只依据标题，将其一阶结论转述为任意非光滑分量的一阶结论。

推断：它与随机复合扩展相关，必须进入最新 related work；目前没有直接覆盖双侧非光滑 DC 的同点值松弛证书。凸正则项可以表达凸约束，不能据此视为已处理当前稿件的一般非凸约束。

## 更直接的先行工作

### Nguyen–Yurtsever–Sra–Toh，DCA-PAGE，2025

**已核验，arXiv 元数据和正文第 V 节。** *Improved Rates for Stochastic Variance-Reduced Difference-of-Convex Algorithms*，2025-09-15，arXiv:2509.11657。arXiv 作者备注为 IEEE CDC 2025 accepted；本轮没有另查 IEEE 会议最终出版记录。

来源：[摘要](https://arxiv.org/abs/2509.11657)；[Definition 12 与第 V 节](https://arxiv.org/html/2509.11657v1)。

事实：论文已讨论“点接近最优解，critical distance 仍为常数”的例子，并使用 gap 指标给出随机 DCA 分析。Definition 12 的 gap 是固定旧点次梯度后，凸分量的线性化子问题值差。

推断：通过凸共轭定义，该 gap 可以写成相应凸分量的 Fenchel–Young gap。因此，“首次用函数值 gap 替代 DC 残差”“首次解释残差在折点附近失效”不适合作为当前工作的独立新颖性陈述。该文没有在已检查位置同时给出你所写的两侧值误差与次梯度失配三参数定义；是否构成实质推进，应逐条比较证书性质和复杂度。

### Faust–Fawzi–Saunderson，AISTATS 2023

**已核验，PMLR 发表页、机构页面、PDF §2.2 和 Theorem 5。** *A Bregman Divergence View on the Difference-of-Convex Algorithm*，PMLR 206:3427–3439，2023。

来源：[正式发表页](https://proceedings.mlr.press/v206/faust23a.html)；[PDF](https://proceedings.mlr.press/v206/faust23a/faust23a.pdf)；[Monash 记录](https://research.monash.edu/en/publications/a-bregman-divergence-view-on-the-difference-of-convex-algorithm/)。

事实：Theorem 5 已用两项 Bregman 散度表达单步下降，并通过求和统一若干非渐近结果。§2.2 的运行假设要求第二凸分量在定义域内部可微；这不等于要求目标函数光滑，也不等于覆盖任意双侧非光滑情形。

推断：你的一步 Fenchel-gap 恒等式需要明确解释与该下降恒等式的关系。可能的新增内容位于双侧非光滑、两侧独立误差、非精确子问题、统一驻点转换和实际一阶信息成本；恒等式的重新记号化本身不足以证明新增贡献。

### 其他背景

- Rotaru, Patrinos, Glineur, *Tight Analysis of Difference-of-Convex Algorithm (DCA) Improves Convergence Rates for Proximal Gradient Descent*，2025-03-06，arXiv:2503.04486；arXiv 标注 PMLR 258:4114–4122, 2025。已核验摘要与元数据；其亚线性临界点结果假设至少一个分量光滑。[来源](https://arxiv.org/abs/2503.04486)
- *An Inexact Proximal Linearized DC Algorithm with Provably Terminating Inner Loop*，arXiv:2305.06520。已核验身份及摘要，涉及 epsilon-subdifferential 和内循环有限终止。尚未在本轮逐定理比较。[来源](https://arxiv.org/abs/2305.06520)
- *Fenchel-Young Duality Gaps: Certified Early Stopping for Regularized Inverse Problems*，2026-09-15，arXiv:2609.17629。已核验元数据和摘要。逆问题中的对偶间隙证书与当前 DC 驻点目标不同，不能仅按 Fenchel 关键词判定重复。[来源](https://arxiv.org/abs/2609.17629)
- Xu 等，*Riemannian Difference-of-Convex Optimization for K-Means Clustering*，2026-09-28，arXiv:2609.34310。已核验元数据和摘要；属于流形 DC 应用与算法复杂度背景，尚未完成与约束扩展的定理级比较。[来源](https://arxiv.org/abs/2609.34310)

## JMLR 优先阅读清单

以下前六篇已核对官方摘要、BibTeX 和 PDF；PDF 与文本位于 `sources/`。优先级属于基于当前研究主线的判断。

| 优先顺序 | 论文与正式出处 | 重点借鉴 | 比较边界 |
|---|---|---|---|
| 1 | Guy Kornowski, Ohad Shamir. **Oracle Complexity in Nonsmooth Nonconvex Optimization**. JMLR 23(314):1–44, 2022. [官方页](https://jmlr.org/papers/v23/21-1507.html) | 困难性如何引出驻点松弛；oracle、函数类和量词的写法 | 目标函数局部 oracle 的困难性不能自动成为 DC 分量 oracle 的困难性 |
| 2 | Koulik Khamaru, Martin J. Wainwright. **Convergence Guarantees for a Class of Non-convex and Non-smooth Optimization Problems**. JMLR 20(154):1–52, 2019. [官方页](https://jmlr.org/papers/v20/18-762.html) | 将梯度、近端和 Frank–Wolfe 更新放进统一理论叙述；CCCP 简化 | 需要逐一核对各模型假设；本地 BibTeX 尚以 2018 arXiv 记录这篇，正式引用宜用 2019 JMLR 版本 |
| 3 | Hoai An Le Thi, Hoang Phuc Hau Luu, Hoai Minh Le, Tao Pham Dinh. **Stochastic DCA with Variance Reduction and Applications in Machine Learning**. JMLR 23(206):1–44, 2022. [官方页](https://jmlr.org/papers/v23/21-1146.html) | 随机 DC 方法最直接的基线；定理与机器学习例子的组织 | 有限和结构、光滑采样分量、额外假设下的残差速率，不能当作任意双侧非光滑一阶复杂度 |
| 4 | Guy Kornowski, Ohad Shamir. **An Algorithm with Optimal Dimension-Dependence for Zero-Order Nonsmooth Nonconvex Stochastic Optimization**. JMLR 25(122):1–14, 2024. [官方页](https://jmlr.org/papers/v25/23-1159.html) | 一篇围绕单一明确复杂度贡献的紧凑写作范例；维数、精度和概率保证的表达 | 零阶 oracle 与 Goldstein 目标，非 DC 分量信息模型 |
| 5 | Zhize Li, Jian Li. **Simple and Optimal Stochastic Gradient Methods for Nonsmooth Nonconvex Optimization**. JMLR 23(239):1–61, 2022. [官方页](https://jmlr.org/papers/v23/21-0028.html) | 梯度复杂度与近端调用分别计数；有限和/在线变体组织 | 光滑非凸项加非光滑正则的复合设置，不能由标题推成一般非光滑 DC |
| 6 | Junwen Qiu, Xiao Li, Andre Milzarek. **A New Random Reshuffling Method for Nonsmooth Nonconvex Finite-sum Optimization**. JMLR 26(191):1–46, 2025. [官方页](https://jmlr.org/papers/v26/24-0891.html) | 在同一稿件中区分非渐近复杂度、整序列收敛与最后迭代点速率 | 正则项弱凸、近端可用；与任意 DC 凹侧非光滑不同 |
| 扩展参考 | Yuchen Li, Laura Balzano, Deanna Needell, Hanbaek Lyu. **Convergence and complexity of block majorization-minimization for constrained block-Riemannian optimization**. JMLR 27(42):1–77, 2026. [官方页](https://jmlr.org/papers/v27/24-0020.html) | 如果保留约束/MM 扩展，可参考统一框架与分块子问题的叙述 | 主题为分块流形约束；本轮主要核验身份和摘要，不作为证明已排除重叠的依据 |

这里的 PMLR/AISTATS/CDC 条目属于新颖性比较，**不计入 JMLR 正刊清单**。

## JMLR 编委名单与主题初选

来源：[官方编委页面](https://www.jmlr.org/editorial-board.html)，抓取日期 2026-10-10。

- 主编：Pradeep Ravikumar；Tong Zhang。
- 页面包含 95 条 Action Editors、4 条 MLOSS Editors、478 条审稿委员会条目、21 条顾问委员会条目，另有管理与制作人员。
- 这些是官网条目数。保留原页面中疑似重复姓名和缺失字段，没有自行补齐或声称均为独立人数。
- 完整姓名、机构、研究方向和个人链接见 `jmlr_editorial_board.md`、`jmlr_editorial_board.csv`、`jmlr_editorial_board.json`；原始 HTML 同目录保留。

**按研究方向的初选，尚未核对作者与编委的合作关系：**

| Action Editor | 官网机构 | 与当前工作的连接 |
|---|---|---|
| Shiqian Ma | Rice University | 一阶方法、随机算法 |
| Peter Richtarik | KAUST | 凸/非凸优化、随机一阶方法、算子分裂 |
| Silvia Villa | Genova University | 优化、一阶方法、正则化 |
| Lam Nguyen | IBM Research | 随机梯度、非凸优化、随机优化 |
| Lin Xiao | Meta FAIR | 凸优化、随机优化、机器学习优化 |
| Sebastian Stich | CISPA | 凸/非凸优化、随机优化 |

以上是主题匹配推断，不代表编辑可用性、录用倾向或最终推荐顺序。旧论文首页的 Editor 是当时处理编辑，不能替代当前 Action Editors 名单。

[JMLR 投稿说明](https://www.jmlr.org/author-info.html)明确要求建议 3–5 位 Action Editors，并与审稿委员会区分；提交前需要核对利益冲突。该页面也明确允许已放在 arXiv 或个人网站的预印本投稿。

## 当前应采取的动作

1. 把 8 月版本中真正已证明的贡献固定为明确的定理陈述，包含函数类、信息模型、成功判据和成本单位。当前材料中仍标为 open 的下界继续保留该状态。
2. 优先比较 DCA-PAGE §V、Faust 等 Theorem 5、Ding–Yuan Appendix C。分别回答：三参数证书增加了什么；双侧非光滑和非精确分析增加了什么；固定分量界与分量 oracle 下界增加了什么。
3. 在上述区分清楚、证明可审阅且合作者同意后，尽快准备公开预印本。JMLR 允许预印本先公开。该建议不构成代为上传授权，本轮未公开任何稿件。

**关键结论：** 已有实质相邻结果，但本轮尚未找到完整覆盖当前 DC/VAC 组合的论文。

**常见误解：** 题目接近、复杂度指数相同、困难实例属于 DC，都不足以单独证明两项工作完全重复；检索未命中也不足以证明创新性。

**下一步：** 完成上述三项最接近先行工作的逐定理差异表，并据此确定预印本的核心贡献表述。
