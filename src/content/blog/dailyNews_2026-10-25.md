---
title: "Daily News #2026-10-25"
date: "2026-10-25 08:00:00"
description: >
  从 LOOP 到图探索 —— 算法模型的 AutoResearch 自进化系统架构演进之路 PostgreSQL 19 发不出来？AI“找茬”太快，人类修 Bug 的速度跟不上了 Token 经济的终点，依然是人 OpenAI 存储系统扩展系列（二）：支撑 10 亿 ChatGPT 用户的基础设施实践 OpenAI 与波兰 NASK 达成合作，共同推进 AI 安全与安全保障 iOS Dev Weekly 第 773 期：iPhone Duo 适配热潮与拟物化设计回归
tags:
- "商业模式"
- "iOS"
- "周刊"
- "治理"
- "OpenAI"
- "架构设计"
- "模糊测试"
- "软件工程"
- "架构"
- "PostgreSQL"
- "SwiftUI"
- "制度设计"
- "经济学"
- "AI 商业化"
- "合作"
- "开发者生态"
- "Azure Cosmos DB"
- "系统设计"
- "AI 代码审查"
- "AI 安全"
- "性能优化"
- "iPhone Duo"
- "AI Agent"
- "开源"
- "分布式存储"
- "AutoResearch"
- "Token 经济"

---

> - 从 LOOP 到图探索 —— 算法模型的 AutoResearch 自进化系统架构演进之路
> - PostgreSQL 19 发不出来？AI“找茬”太快，人类修 Bug 的速度跟不上了
> - Token 经济的终点，依然是人
> - OpenAI 存储系统扩展系列（二）：支撑 10 亿 ChatGPT 用户的基础设施实践
> - OpenAI 与波兰 NASK 达成合作，共同推进 AI 安全与安全保障
> - iOS Dev Weekly 第 773 期：iPhone Duo 适配热潮与拟物化设计回归

## 📥 Tech News

### [从 LOOP 到图探索 —— 算法模型的 AutoResearch 自进化系统架构演进之路](https://www.bestblogs.dev/article/e5031a99c8?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-23 06:02:06
![](https://media.bestblogs.dev/20261023070455_f96887d93b880574e0fb9ebad114faba529816.png)
**美团技术团队分享如何将 Karpathy 的 AutoResearch 理念从单线程循环扩展为分布式图探索架构，历经三次重构构建出可在企业云端运行的自进化系统，两个业务场景单任务耗时分别下降约 85% 和 83%，其中一个方案已推全上线。**

* 架构从单线程 LOOP 升级为 CyclicGraph Engine 图探索引擎，实现并行探索与集中决策，解决上下文爆炸和状态同步问题，提升迭代速度与资源利用率。
* 采用状态机驱动的异步触发机制，Agent 不再同步等待训练，而是通过状态文件恢复现场，保障长周期运行的稳定性，也为并行化奠定基础。
* 针对通用 Agent 缺乏业务理解的问题，构建业务知识库并利用真实大闭环反馈实现经验自动沉淀，使系统在垂直场景越用越好。
* 错误治理遵循“凡是能用代码表达的约束一律不放在 Prompt 里”的原则，以状态文件为唯一事实源并实施交叉验证，确保无人值守决策的可靠性与可审计性。

### [PostgreSQL 19 发不出来？AI“找茬”太快，人类修 Bug 的速度跟不上了](https://www.infoq.cn/article/Q6mgHWCSqV6KeZzee3NT)

来源：InfoQ 推荐

发布时间：2026-10-23 17:48:25
![](https://static001.infoq.cn/resource/image/27/1b/273f3083bf2bb7a1a815914d561bf91b.png)
**PostgreSQL 19 正式版推迟至 11 月 19 日并新增 RC2，约 8-10 项重要功能被撤回；核心提交者指出关键变量是 AI 辅助代码审查与模糊测试——它们把原本需 5 年才能陆续暴露的边缘缺陷提前翻出，人类修复速度已跟不上 AI 的发现速度。**

* 被撤回功能多在 LLM 审查成熟前完成开发，并非 vibe coding 产物；SQL/PGQ 经历 17 次修复仍被撤回，预计修正后进入 PostgreSQL 20，反为其留下一批接近完成的候选功能。
* AI 模糊测试擅长枚举 PostgreSQL 复杂功能组合（domain 嵌套、分区 detach、security-definer 触发器等），社区判断其未来需前移至功能开发阶段而非 Beta 后期集中使用。
* 社区争论聚焦误报治理：有开发者反馈内部 AI 审查仅约八分之一报告有效；但也有案例显示对运行 10 年的系统审查出 39 个问题、30 个确认为从未触发的真实 Bug。
* 深层担忧是“发布瘫痪”——AI 可无限挖出边缘问题，软件修到什么程度才允许发布将比“能找到多少 Bug”更难回答；瓶颈正从“发现问题”转向人类对问题分类、取舍的判断力。

### [Token 经济的终点，依然是人](https://www.bestblogs.dev/article/0e6b5568f8?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-23 17:50:00
![](https://media.bestblogs.dev/20260827095624_dbb7c8f.jpeg)
**腾讯研究院分析 Token 经济的本质：认知能力首次以细密、连续、可编程的方式进入经济系统，改写了成本结构与价值分布，但其终点应是让人调用智能而非依附智能。**

* Token 意味着一部分智力劳动脱离人脑、进入机器系统，成为可规模化生产、调度和分配的新型经济资源；Token 只记录消耗而非价值，且背后是芯片、能源、网络等真实物理成本，颠覆了传统软件低边际成本的认知。
* 需求侧不再只来自人，机器间协作成为新需求来源；竞争从模型能力之争转向 Token 的生产效率、消耗效率、价值转化效率与定价权，横跨芯片、模型、应用层的全产业链。
* 商业模式正从单纯 API 调演讲化为订阅、套餐、结果付费等形态，并引发跨境贸易、税收、责任归属等制度层面挑战。
* 作者强调，当智能成为公共资源，需通过制度建设决定其分配方式与约束条件，避免新的依赖与分配不公，确保智能服务于人的目的。

### [OpenAI 存储系统扩展系列（二）：支撑 10 亿 ChatGPT 用户的基础设施实践](https://openai.com/index/scaling-storage-one-billion-users-part-two)

来源：OpenAI News

发布时间：2026-10-24 01:00:00

**OpenAI 发布存储扩展系列文章第二篇，介绍其如何通过可靠的多租户架构、全球缓存以及引入 Azure Cosmos DB，使 Habitat 存储系统实现 12 倍的读取性能提升，从而支撑超过 10 亿 ChatGPT 用户。**

* Habitat 是 ChatGPT 背后的在线存储系统，本篇聚焦超大规模用户场景下的可靠性与性能工程实践；
* 多租户机制与全球缓存用于解决海量并发访问下的隔离性和延迟挑战；
* Azure Cosmos DB 作为关键存储组件参与整体架构，最终带来 12 倍的读取加速；
* 适合关注大规模分布式存储、云架构设计与缓存策略的工程师与架构师阅读。

### [OpenAI 与波兰 NASK 达成合作，共同推进 AI 安全与安全保障](https://openai.com/index/openai-nask-ai-safety-security-partnership)

来源：OpenAI News

发布时间：2026-10-23 08:00:00

**OpenAI 宣布与波兰研究机构 NASK 建立合作伙伴关系，双方将在 AI 安全、安全保障与技术研究方向展开合作，旨在强化防护能力并支撑更有韧性的数字生态。**

* 合作范围涵盖 AI 安全、安全保障以及技术层面的联合研究；
* 双方将共同强化安全防护措施，以应对 AI 相关的安全与滥用风险；
* 该公告属于新闻性质，暂未披露合作的具体技术细节与推进时间表，关注 AI 安全治理与国际协作的读者可留意后续进展。

## 💾 Daily Dev

### [iOS Dev Weekly 第 773 期：iPhone Duo 适配热潮与拟物化设计回归](https://main--iosdevweekly.netlify.app/issues/773/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-23 20:42:39
![](https://cdn4.telesco.pe/file/Vijm3LpoqAGb1MlJIlJosbpjCW3cg9MvecRq9r87Oogu-qc45kwsEbAirqmC1aq83zJyaivkLHFSlHu5o9FwiOQB6vBLeIV3Hm0r8k97ZG0fRq6NpNfUu_pfoWBOGV5FTOYJCu3f75BmJlvqfr5uXKcEAOYQfDoWKi-n5dBEVhUTk_s-Ojuuo1PKIEO1DazhE41deDQdjWYQ9gNFsGzlz1vk6KzHG2pwSKOJqqA8DbE58pR9t_NdT6t_RBbU0Uso1zEGP-fBpJgAfQy6qKf1dVJsYPXXJPGNSkzdG5qz6imBmbpu-A_cpYvLECFHjRLAPV3bvjAJY1aO7t44iN8nTA.jpg)
**iOS Dev Weekly 第 773 期聚焦 iPhone Duo 发售前后的开发者生态：独立开发者掀起适配热潮，拟物化设计随折叠屏强势回归，同时知名 iOS 教育者 Sean Allen 因 AI 冲击宣布关闭在线学校。**

* iPhone Duo 今日开始发货，但供应延迟严重，许多开发者短期内拿不到设备；苹果正于全球多个开发者中心举办线下适配工作坊，供开发者实际上手体验
* FoldHunt 网站收录 Duo 风格的创意应用并追踪已适配的现有应用；索尼 Walkman 风格应用 Deck-man 病毒式传播，拟物化设计明显回潮
* Sean Allen 因“AI 导致 iOS 开发课程销量暴跌”关闭在线学校，部分课程降价、部分免费开放，折射出 AI 对在线技术教育的冲击
* 技术文章亮点：Pockity 创造性地用网格渐变串联多屏应用设计；iPad 优先应用 Lake 分享 Duo 适配经验（迁移成本并不算高）；Sarun 详解布局边距的正确设置方式
* 工具推荐：exploreswiftui.com 以可视化方式展示 SwiftUI 原生能力并含 Duo 专属示例页；开源节点式图像编辑器 ImageFlow 值得一试
