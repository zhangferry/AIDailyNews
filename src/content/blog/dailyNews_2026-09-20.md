---
title: "Daily News #2026-09-20"
date: "2026-09-20 08:00:00"
description: >
  OpenAI：多 Agent 让 RSI 更可行 Claude 主导 Anthropic 26% 的 AI 研发、3 万 Agent 同时运行：头部 AI 公司的 RSI 路线正在分化 打造一个卓越的产品管理团队 Ask LukeW：用更好的图片检索让 AI 回答告别“文字墙”
tags:
- "RAG"
- "AGI"
- "AI"
- "产品管理"
- "招聘面试"
- "AI Agent"
- "检索"
- "自动化研发"
- "团队建设"
- "用户体验"
- "高增长"
- "LLM"
- "RSI"
- "多模态"
- "AI 安全与对齐"
- "Anthropic"
- "OpenAI"

---

> - OpenAI：多 Agent 让 RSI 更可行
> - Claude 主导 Anthropic 26% 的 AI 研发、3 万 Agent 同时运行：头部 AI 公司的 RSI 路线正在分化
> - 打造一个卓越的产品管理团队
> - Ask LukeW：用更好的图片检索让 AI 回答告别“文字墙”

## 📥 Tech News

### [OpenAI：多 Agent 让 RSI 更可行](https://www.bestblogs.dev/podcast/05a2a4231?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-18 13:09:38
![](https://image.jido.dev/20260605145427_78cff8f.png)
**OpenAI 研究员 Noam Brown（o1 推理模型奠基级贡献者）在与 Dwarkesh Patel 的对谈中，以一万个 Agent 在 88 小时内消耗 1300 亿 token 攻克一道千禧年难题的实验为引，讨论多 Agent 并行扩展测试时计算的机制，以及 RSI 与对齐的真正难点。**

* Noam 强调攻克难题的核心功劳属于「极其强大的通用模型」，多 Agent 最多占不到 10%，且缺少关于协同效率的扎实消融实验数据。
* 相比复杂的协调脚手架，他更倾向只给 Agent 发消息等基础工具，让它们自行摸索协作，由此自发涌现出类似 Slack 频道与中层管理的行为。
* 多 Agent 的本质是让测试时计算从串行走向并行，在数学、深度研究等易并行任务上收益明显，对写小说等创造性任务几乎无用。
* 关于 RSI，实验、算力与串行执行构成非智力瓶颈，他估计约三倍加速，不会是「一夜之间的智能爆炸」。
* 对齐的核心困境在于无法确认评测指标是否真的测到了对齐：思维链监控可能促使模型隐藏意图，且模型发布周期可能短于任务跨度，完整评估来不及覆盖。

### [Claude 主导 Anthropic 26% 的 AI 研发、3 万 Agent 同时运行：头部 AI 公司的 RSI 路线正在分化](https://www.infoq.cn/article/CEphwKjzAe7LzbOriLcq)

来源：InfoQ 推荐

发布时间：2026-09-18 17:00:24
![](https://static001.infoq.cn/resource/image/e3/4c/e326c8yy71cd8c79cf687b351fd9324c.png)
**Anthropic 披露内部数据：Claude 已能"主导"约 26% 的 AI 研发工作，超 90% 达到"AI 协作"水平，内部平台约 3 万个 Agent 同时运行，但完整意义上的 RSI 尚无公司宣称达到。**

* "主导"即 AL4 级：人类定目标与监督，AI 完成大部分端到端执行；该比例从今年 2 月的不足 1% 半年内升至 26%，由 Claude 抽样阅读员工 Slack 与文档构建任务树测算，与人类评级相差不超过一级的一致率达 97%
* OpenAI 主攻规模化"AI 研究员"，已实现自动化研究实习生目标，计划 2028 年 3 月前迈向自动化研究员；当前人类每工作 1 天，Agent 并行运行约 24.8 小时
* Google 路线偏向搜索与发现机制：Gemini 3.8 用 Agent 循环递归评估改进底层模型，Dream-RSI 通过 Replay Simulator 在元探索层闭合 RSI 循环，验证始终是整个循环的锚点
* 田渊栋联合创办的 Recursive 直接以 RSI 为核心目标，强调研究循环的长期积累与复利，并把越来越严格的正确性检查纳入循环以对抗 reward hacking
* 各家共识是人类在研究品味与判断力上仍保有比较优势，且业界对 RSI 的定义本身存在明显分歧

### [打造一个卓越的产品管理团队](https://www.bestblogs.dev/article/ccd1b8f76a?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-18 11:03:09
![](https://images.stripeassets.com/3sz5ney9ml0h/K3ReOAHQ6AnjETRznub9X/c4fd3297ed7908747d8da1733448d46f/Generic_Social_Card.png?q=80)
**本文基于 Elad Gil 的《高增长手册》，系统阐述高增长公司如何构建卓越的产品管理团队，覆盖 PM 核心职责、人才能力模型、四类角色定位与面试评估框架。**

* PM 是产品成功的单一跨职能所有者，负责战略愿景、优先级取舍、执行推进与跨职能沟通，并充当保护工程师的「缓冲器」，与项目经理有本质区别。
* 优秀 PM 需具备六项特质：品味、排序能力、执行力、战略洞察、沟通技巧与数据驱动，其中指标定义直接决定产品演进方向。
* PM 可分为业务型、技术型、设计导向型和增长型四类，公司应根据产品的技术含量与业务重心匹配人才配比。
* 面试时应重点考察候选人面对冲突与资源受限时的「取舍框架」而非最终结果，深挖其在成功产品中的具体个人贡献，并重视背景调查。

## 💾 Daily Dev

### [Ask LukeW：用更好的图片检索让 AI 回答告别“文字墙”](https://www.lukew.com/ff/entry.asp?2162)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-18 23:52:26
![](https://cdn4.telesco.pe/file/cr7DriGT6ziPCFkKjsVNYZmmXTAheHI2c_YX4jh9-uHM0CV4eKFbAgRIllVTMf6oqmejpUCSLLlGXxpxhxSkKfu1UnSV-UoCZ_sEbNS2siTcpupwifRkHFbLVUdX31SLj-oooxdziF3LMQ9-Jsu9eg_oPFi9P5WKjNAifE134vqILKPAcSl0pkgrzOoz60Phioxa02L0Ulf5GwoWdMdnUUVspZGZ1I3gdb1fCYemlZgUwUkHpykvd4-XF3oI4MYPai0W7XiOkP6VDKW2pp9ka0JQZoahM65_6xXCXwlkeFgXQwzqUsRe0wj3w9iKkWMN9hUgFGq_114ViZbNLAHJhw.jpg)
**Luke Wroblewski 分享了为其个人 AI 问答系统 Ask LukeW 增加“可视化回答”的完整实践：通过改进图片入库与检索管线，让 AI 回答能自动配上相关插图，缓解 AI 应用输出大段单调文字的通病。**

* 入库机制：新图片上传后由 AI 模型生成标题与描述，并各自转为 embedding 支持语义检索；用户提问时，检索系统结合语义搜索与传统关键词搜索返回排序后的候选图片，供生成回答的模型选用。
* 核心问题与解法：仅凭图片内容生成的标题（如 "Green block layout comparison"）技术正确却与用户真实提问难以匹配，导致图片很少被引用；作者转而利用 30 年来为无障碍沉淀的 ALT 标签，让另一个 AI 模型将 ALT、原标题与完整视觉描述融合为更贴近用户意图的新标题，图片引用率明显提升。
* 动态更新：同一图片出现在后续文章中会被重新命名，修改旧文的 ALT 标签也会触发更新；但人工手动命名的图片不会被管线覆盖，体现“AI 服务于人”的最后决定权。
* 该方案对构建带图文检索的 RAG 问答、内容站内搜索具有直接参考价值。
