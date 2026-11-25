---
title: "Daily News #2026-11-27"
date: "2026-11-27 08:00:00"
description: >
  黄仁勋的“光”：详解 AI 算力背后的光通信产业链、英伟达赌注与技术博弈 京东基于 Apache Doris 构建统一湖仓分析引擎，支撑日均百万级查询与 PB 级数据扫描 一句话让 AI 创造 3D 世界：小红书开源 3DCodeFactory
tags:
- "查询优化"
- "开源数据集"
- "数据合成"
- "英伟达"
- "Qwen"
- "数据架构"
- "湖仓一体"
- "OLAP"
- "产业链"
- "多模态 AI"
- "CPO"
- "3D 代码生成"
- "AI 数据中心"
- "光通信"
- "Apache Doris"

---

> - 黄仁勋的“光”：详解 AI 算力背后的光通信产业链、英伟达赌注与技术博弈
> - 京东基于 Apache Doris 构建统一湖仓分析引擎，支撑日均百万级查询与 PB 级数据扫描
> - 一句话让 AI 创造 3D 世界：小红书开源 3DCodeFactory

## 📥 Tech News

### [黄仁勋的“光”：详解 AI 算力背后的光通信产业链、英伟达赌注与技术博弈](https://www.bestblogs.dev/article/876b75e45c?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-25 18:42:00
![](https://image.jido.dev/20251127045520_f3caed2e)
**英伟达正通过数百亿美元投资与收购整合光互连产业链，押注 CPO（共封装光学）等新技术突破 GPU 通信瓶颈，其深层动机在于垄断从高速互连芯片到激光器、光器件的全链条生态资源。**

* GPU 算力增长远超带宽：从 A100 到 B200 单卡算力提升约 7 倍，而 NVLink 带宽仅提升 3 倍，铜缆在距离、带宽、功耗三方面触及物理极限，形成“通信墙”，光通信成为 AI 数据中心跨 Scale Up / Scale Out / Scale Across 三层网络互连的关键支撑。
* 产业链格局分化：EML 激光器芯片由 Lumentum、Coherent 等控制，CW 光源依赖磷化铟材料，DSP 芯片由 Marvell、博通掌控；中国厂商在光模块量产上占据优势，但上游关键芯片与光器件仍被海外“卡脖子”。
* 英伟达向 Marvell、Lumentum 各投 20 亿美元并计划收购后者，推动 CPO 将光引擎直接共封装至交换芯片旁，把十几厘米的铜走线缩短到毫米级，预计 2028 年 Feynman 世代实现 NVLink CPO。
* CPO 虽降低功耗却带来维修不便的难题，行业衍生出 LPO、XPO、NPO 等多条竞争路线，分别围绕功耗、密度、可维护性寻求平衡。

### [京东基于 Apache Doris 构建统一湖仓分析引擎，支撑日均百万级查询与 PB 级数据扫描](https://www.infoq.cn/article/dcXaJcXchxExJfaxtveD)

来源：InfoQ 推荐

发布时间：2026-11-25 18:58:33
![](https://static001.infoq.cn/resource/image/0d/d7/0d9db382aa82b1e66542786b29640fd7.png)
**京东在 Doris Summit 2026 分享了将 Presto、StarRocks 等多引擎业务收敛至 Apache Doris、构建统一湖仓分析引擎的生产实践，目前支撑日均百万级查询与 PB 级数据扫描，AI Agent 查询占比约 20%。**

* 架构上依托 Doris 的 Multi-Catalog 访问 Hive、Hudi 等外部数据源，配合 Nereids 优化器与向量化 BE 引擎，承载呈“双峰潮汐”特征并走向 7×24 小时的 BI 报表、数据质量任务与 Agent 混合负载。
* 调度优化：将 FE 与 BE 扫描任务间的 Pull 模式重构为 Push 模式，BE 维持有界队列、无任务时挂起线程释放 CPU，并通过容量反馈控制积压、缓解消费速度差异导致的任务倾斜。
* 规划优化：将谓词前移至候选分区获取阶段实现精确分区裁剪，并让 File Listing 结果在 CBO 估算与 Split 生成间“一处准备、多处复用”，降低冷缓存下大规模分区的元数据访问开销。
* 执行层通过公共子表达式消除、谓词下推、按需读取列与 Shuffle 流控等提升吞吐；同时兼容 Presto/Spark SQL 方言，支持行列级权限与数据脱敏。未来规划 Agent 负载优化、预测加速、弹性湖仓与 Text-to-SQL 语义协同四大方向。

### [一句话让 AI 创造 3D 世界：小红书开源 3DCodeFactory](https://www.bestblogs.dev/article/0df8702ea1?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-25 17:59:00
![](https://image.jido.dev/20251127045428_1c4a68a7)
**小红书开源了大规模全自动 3D 数据合成框架 3DCodeFactory 及 5.52B token 的 3DCodeFactory-Data 数据集，基于其微调的 Qwen3.8-27B 模型在多个 3D 代码生成基准上超越同系列 2.4T 旗舰模型 Qwen3.8-Max。**

* 框架采用三阶段全自动管线：构建 10 大类 56 小类的 3D 分类体系并对齐语料分布；以合成参考图为视觉锚点生成结构化需求与多维评分准则；通过沙箱实机验证筛选高质量多轮交互轨迹。
* 数据集包含 5,045 条高质量轨迹，单条平均超 100 万 tokens，单场景代码量中位数达 4,270 行，在代码规模、交互深度与场景复杂度上显著超越现有开源数据集。
* 多维 Rubric 筛选机制效果显著：剔除任一维度未达准入阈值的样本、仅保留五项指标全部达标的轨迹，筛选后数据使模型训练全程稳步提升，明显优于未筛选组后期增速放缓的表现。
* 模型在 BlenderWorld、P3D-Bench、3DCodeBench 等基准上全面领先，且仅微调 1 个 Epoch 即实现，验证了数据质量优于数量的训练策略。
