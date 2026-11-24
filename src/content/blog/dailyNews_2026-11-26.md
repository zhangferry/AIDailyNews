---
title: "Daily News #2026-11-26"
date: "2026-11-26 08:00:00"
description: >
  谷歌用 Gemini 设计量子算法并经 Lean 形式化证明验证，最高提速 290 倍 GPT-6 models demonstrate intrinsic protein-design capabilities OceanBase 发布 AI 数据平台 OceanLake 并开源 OceanSeek，AI 营收突破 1 亿元 iPhone 相机掌门人麦考马克退休：「果味」影像的缔造者与争议 How iFood scales coding agents across 15,000 repositories
tags:
- "量子计算"
- "GPT-6"
- "影像"
- "DevOps"
- "生物科学"
- "Apple"
- "湖仓一体"
- "AI"
- "OceanBase"
- "数据库"
- "数据基础设施"
- "计算摄影"
- "LLM"
- "架构设计"
- "Gemini"
- "Google"
- "形式化验证"
- "蛋白质设计"
- "代码安全"
- "科技新闻"
- "大语言模型"
- "AI Agent"

---

> - 谷歌用 Gemini 设计量子算法并经 Lean 形式化证明验证，最高提速 290 倍
> - GPT-6 models demonstrate intrinsic protein-design capabilities
> - OceanBase 发布 AI 数据平台 OceanLake 并开源 OceanSeek，AI 营收突破 1 亿元
> - iPhone 相机掌门人麦考马克退休：「果味」影像的缔造者与争议
> - How iFood scales coding agents across 15,000 repositories

## 📥 Tech News

### [谷歌用 Gemini 设计量子算法并经 Lean 形式化证明验证，最高提速 290 倍](https://www.bestblogs.dev/article/bf3a198973?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-24 19:30:00
![](https://media.bestblogs.dev/20261102062447_47af1ad.jpeg)
**Google DeepMind 与 Google Quantum AI 首次将 AI 智能体团队与形式化验证工具 Lean 结合，实现量子算法的自动发现与数学证明，特定量子算术运算的理论资源效率最高提升 290 倍。**

* 研究团队通过定义计算问题、正确性要求与资源约束，启动多个 Gemini 4 智能体团队并行探索算法方案，再由 Lean 系统对数学正确性和资源开销进行机器核验。
* 除算术运算的 290 倍提升外，核聚变模拟的逻辑量子比特从 5650 个降至 4338 个（时空成本降约 11.8 倍），光化学模拟降低约 8.22 倍，药物代谢模拟降低约 2.49 倍。
* 该方法绕开了复杂量子电路无法在经典计算机完整模拟、当前硬件又无法实际执行的困境，为量子算法研发提供了可验证的路径。
* 人类专家的角色随之转变：从大量手工电路优化，转向选择研究问题、定义正确性标准与解释科学意义，预示着科研范式的深层变化。

### [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)

来源：OpenAI News

发布时间：2026-11-24 21:00:00
![](https://images.ctfassets.net/kftzwdyauwt9/4u7ogWwVXuqX5GRdnZxsLM/23d72378f6fea65debd91c914f32fb54/protein-workflows-intrinsic-desktop-light.png?w=3840&q=90&fm=webp)
**OpenAI 研究表明 GPT-6 系列模型无需调用专门的生物模型，仅凭推理和通用代码工具即可设计全新蛋白质结构与氨基酸序列。**

* 在 14 项蛋白质设计任务上，内部研究模型的表现与专门模型（如 RFdiffusion）相当或更优，但预测完整蛋白质结构仍是明显短板。
* 与 Onava 的实验室验证中，基于 GPT-6.2 三维设计的 322 个 minibinder 针对 5 个靶点测试，35 个（10.9%）显示结合活性；对 MDM2 的序列重设计中，88 个设计有 75 个（85%）初筛结合阳性。
* 新序列与原始序列差异显著（中位数最高达 50%），且对未公开结构也能给出多个有效序列，证明其能力超越简单记忆复现。
* 研究者可通过自然语言在从原子键到整体形状的尺度上引导设计，仅需修改提示即可切换任务而无需重训练，相关成果已以预印本形式发布。

### [OceanBase 发布 AI 数据平台 OceanLake 并开源 OceanSeek，AI 营收突破 1 亿元](https://www.infoq.cn/article/qEXNRNufkiFkiUEU9aae)

来源：InfoQ 推荐

发布时间：2026-11-24 20:21:09
![](https://static001.infoq.cn/resource/image/c0/3b/c09260eddb6be79ed6cd7c91924cb93b.png)
**OceanBase 发布湖库一体 AI 数据平台 OceanLake，并以 Apache 2.0 协议开源核心引擎 OceanSeek，其 AI 业务营收已突破 1 亿元。**

* Agent 正在打破数据库与数据仓库的分工：蚂蚁内部 MCP 访问量半年增长 13.36 倍，Agent 脉冲式负载要求数据基础设施具备高并发、低延迟与弹性扩缩容能力
* CTO 杨传辉给出三个判断：湖库一体（支持 Iceberg、Paimon 开放表格式）；Agent 友好（逻辑表与数据分支可秒级创建独立读写环境）；多模混合搜索（一次查询组合标量过滤、JSON、全文检索与向量搜索）
* 本体语义产品 Ontos 可自动化 90% 以上的本体建模工作，效率提升 10 倍以上；与 Palantir 自上而下的方式不同，OceanBase 自下而上从企业现有数据系统提取语义，降低落地门槛
* CEO 杨冰坦言与 Databricks「殊途同归」，一个从在线走向离线、一个相反；团队押注多模态「就像当年赌分布式一样」，但底层湖库产品成熟度与原有数据库相比仍有差距

### [iPhone 相机掌门人麦考马克退休：「果味」影像的缔造者与争议](https://www.bestblogs.dev/article/06711b83df?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-24 21:40:49
![](https://media.bestblogs.dev/20261124054300_ifanr-paste-1795498754186-2.jpg)
**iPhone 相机掌门人乔恩·麦考马克宣布退休，其八年间塑造的「果味」计算摄影风格，正面临组织架构调整与生成式 AI 浪潮的双重挑战。**

* 从 2019 年的 Deep Fusion 开始，苹果通过多帧合成、神经网络融合等技术，配合夜间模式、智能 HDR、ProRAW 和 Photonic Engine，形成了清晰、稳定、忠于现场的影像基调。
* 这套逻辑的代价是算法过度处理：Tone Mapping 环节过度压低高光、提升阴影，导致画面「数码味」重、光影层次被平化。
* 在生成式 AI 能随意篡改现实的时代，麦考马克坚持「照片是对真实事件的个人礼赞」的伦理底线，苹果在 AI 编辑功能上也保持高度克制。
* 其退休后职责被拆分并入更大的 AI 团队，加上 OPPO、vivo 等竞争者在硬件与 AI 修图上的持续突破，苹果需要在用户体验、AI 协同与摄影伦理之间寻找新的平衡。

### [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)

来源：OpenAI News

发布时间：2026-11-24 08:00:00
![](https://images.ctfassets.net/kftzwdyauwt9/4Ts7RsLLSU4iEOxQwBkGgg/cbf56c075004a9ae2c41af4d5f7b428b/ifood-customer-story-social.png?w=1600&h=900&fit=fill)
**巴西外卖平台 iFood 构建 Remote Agents Platform，将 15,000 个代码仓库的工程任务封装为 REST API 调用，在隔离沙箱中远程执行并返回合并请求，平均每次运行成本仅 0.04 美元。**

* 运行器采用"确定性步骤 + 智能体执行"混合架构：克隆仓库、导入技能、发布合并请求等由固定流程处理，中间的核心任务由沙箱内的 GPT-5.6 Luna 完成，使工作流可预测。
* 沙箱预装 Python、Java、Kotlin、Rust、Go 等工具链，可访问 Nexus、GitLab、Docker、Snyk、Kubernetes 与 AWS；结果通过 Structured Outputs 强制符合预定义契约，实现任务成败的自动化判定。
* 迁移后内部安全平台的修复准确率与漏洞解决数量均翻倍以上；平台累计完成 25,000+ 次任务，消耗超 270 亿 token。
* 文章总结了五点经验：瓶颈往往在运行时而非用例、组合确定性与智能体执行、将单次成本视为架构决策、强制输出契约、异步执行免监督才是真正的生产力收益。
