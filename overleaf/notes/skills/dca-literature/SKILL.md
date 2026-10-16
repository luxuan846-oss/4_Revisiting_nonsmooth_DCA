---
name: dca-literature
description: 为 Revisiting Nonsmooth DCA 项目执行文献调研、新颖性比较与引用核对。用于比较双侧非光滑 DC 证书、DCA 类算法、驻点关系、oracle 复杂度与 MP/JMLR 贡献定位。
---

# DCA 文献调研

定位含 CLAUDE.md 与 overleaf/main.tex 的仓库根目录。下列路径以根目录为基准。

1. 读 overleaf/notes/progress/PROJECT_STATUS.md 与 overleaf/notes/prompts/gptpro-literature-research-prompt.md，沿正文引用读取当前初稿。两条 Codex 会话属于历史研究材料。
2. 提取函数类、证书和主要结果，区分稿件陈述与已核对证明。根据最接近工作的实质关系组织检索。
3. 逐篇比较函数类、oracle、驻点目标、误差参数、输出方式、复杂度单位与额外假设。精确凸子问题、prox 和一次分量查询分开计数。
4. 对 DCA-PAGE 的单侧 gap、Bregman DCA 的下降式、本文两侧 Fenchel 证书作定理级比较。不要因名称不同就判断创新。
5. 核对下界中的预算依赖、分量大小界和信息模型。一般目标函数 oracle 与分量 oracle 之间需要明确归约。
6. 对关键结论完成原文、出版/版本记录、独立书目或相关原文三项交叉核对。无法核对的明确保留为待验证；记录实际检索日期。
7. 将报告写到 literature/ 的日期目录，交付 Markdown、new-entries.bib 与 corrections.bib。只把实际完成结果写入 PROJECT_STATUS.md。

优先沿已有 2026-10-10 报告追踪近期版本，检索范围持续到执行日期。新文献改变判断时，说明改变了哪项结论。不要把历史助手的期刊建议作为前提。
