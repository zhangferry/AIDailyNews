---
title: "Daily News #2026-07-05"
date: "2026-07-05 08:00:00"
description: >
  sim-use - 给 agent 装上眼睛和手，让 mobile 开发跟上 AI 时代 Code is cheap. Don't write any.——AI Native，程序员如何提升五倍 coding 效率 从 AI Coding 到 Harness Engineering 的端到端工程开发实践 美团 LongCat-2.0 正式发布：在国产算力集群上完成全流程训练与推理的万亿参数模型 Claude Code 80%的提示词说删就删，Anthropic用Fable 5打了个样：AI行业的“降本”才刚刚开始 ICML 2026 | 美团技术团队学术论文精选 iOS Dev Weekly 第757期：SwiftUI底层解析、iOS 27新特性与AI编程辅助 SBBI China 2025 解读：如何在市场喧嚣中寻找长期投资的参照系
tags:
- "长期主义"
- "Agentic Coding"
- "智能体"
- "SwiftUI"
- "大类资产配置"
- "美团"
- "AI降本"
- "开源模型"
- "大模型训练"
- "WWDC"
- "System Prompt"
- "提示工程"
- "国产算力"
- "iOS开发"
- "投资"
- "CLI"
- "移动开发"
- "上下文工程"
- "Token优化"
- "iOS 27"
- "A股"
- "架构设计"
- "机器学习"
- "SBBI"
- "Anthropic"
- "强化学习"
- "DevOps"
- "LLM"
- "AI 编程"
- "ICML 2026"
- "多模态"
- "知识库工程"
- "自动化测试"
- "研发效能"
- "AI Agent"
- "AI编程"
- "Claude Code"

---

> - sim-use - 给 agent 装上眼睛和手，让 mobile 开发跟上 AI 时代
> - Code is cheap. Don't write any.——AI Native，程序员如何提升五倍 coding 效率
> - 从 AI Coding 到 Harness Engineering 的端到端工程开发实践
> - 美团 LongCat-2.0 正式发布：在国产算力集群上完成全流程训练与推理的万亿参数模型
> - Claude Code 80%的提示词说删就删，Anthropic用Fable 5打了个样：AI行业的“降本”才刚刚开始
> - ICML 2026 | 美团技术团队学术论文精选
> - iOS Dev Weekly 第757期：SwiftUI底层解析、iOS 27新特性与AI编程辅助
> - SBBI China 2025 解读：如何在市场喧嚣中寻找长期投资的参照系

## 🍎 iOS Blog

### [sim-use - 给 agent 装上眼睛和手，让 mobile 开发跟上 AI 时代](https://onevcat.com/2026/07/sim-use/)

来源：OneV's Den

发布时间：2026-07-03 22:50:00

**背景/问题**：当前 AI Agent 已经能高效生成代码，但在移动端（iOS/Android）UI 开发中，面临“验证难”的痛点。Agent 无法自行运行应用、查看 UI 效果并据此反馈修改，导致开发闭环中断，人机交互效率低下。

**核心观点/方案**：介绍了一款开源的跨平台 CLI 工具 sim-use。该工具相当于给 Agent 装上了“眼睛和手”，使其能够直接在移动端模拟器中识别屏幕画面、执行点击等交互操作，并自动验证 UI 结果，从而补齐了 Agent 驱动的移动端开发的最后一块拼图。

**结论/价值**：该工具突破了传统 AI 辅助编程仅停留在纯代码生成阶段的局限，极大地提升了移动端开发的自动化程度和调试效率。对于希望深度集成 AI Agent 以优化开发流程的移动端开发者而言，具有极高的实战参考价值。

## 📥 Tech News

### [Code is cheap. Don't write any.——AI Native，程序员如何提升五倍 coding 效率](https://www.bestblogs.dev/article/c25f459e?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-03 08:30:00
![](https://image.jido.dev/20260527050139_5335db5.jpeg)
**背景/问题**：在 AI Native 时代，代码本身的生成成本正变得极其低廉。然而，由于大模型本质上是非确定性的概率生成器，且上下文窗口存在“中间遗忘”等局限性，直接让 AI 编写复杂代码极易产生偏差和幻觉，难以保证工程质量。

**核心观点/方案**：作者结合超大规模代码产出的实战经验，提出了一套名为 Harness 的 AI 编程方法论。核心在于“人定方向，模型推进”：引入“水流理论”将控制点前移至系统边界和检查点，而非逐行控制代码；运用“最小混沌单元”拆解任务，并通过编写 Spec、CodeMap 和定期开新对话等设施严格控制上下文环境，确保模型在受控空间内自主推进。

**结论/价值**：本文是一篇罕见的兼具底层理论深度与极强实操性的 AI 编程指南，适合所有渴望成倍提升研发效能的开发者深度阅读。它彻底重塑了程序员与 AI 的协作模式，指出在 AI 时代，程序员的核心竞争力已从编写代码转变为定义目标、控制边界和验收结果的能力。

### [从 AI Coding 到 Harness Engineering 的端到端工程开发实践](https://www.bestblogs.dev/article/e06a6c5e?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-03 17:36:00
![](https://image.jido.dev/20260527045543_19fddfe.jpeg)
**背景/问题**：当前大热的对话式 AI Coding 在真实的复杂业务工程中，正面临着上下文窗口快速膨胀、大模型缺乏完整业务知识、缺乏工程自动化闭环以及无法高效并行执行四大核心瓶颈，难以真正实现端到端的自动化开发。

**核心观点/方案**：腾讯应用宝活动平台团队提出并实践了 Harness Engineering 架构。该方案以结构化知识库工程为底座，通过 AI 自动生成与渐进式分层检索（替代传统 RAG）保障业务上下文的精准与新鲜。在执行层，采用状态文件驱动流程持久化，设计单一职责的专家 Agent 体系，结合 DAG 并行编排与冲突治理策略。同时，将确定性操作全面脚本化，彻底贯彻"AI 负责认知、脚本负责执行"的核心工程原则。

**结论/价值**：该实践为大型复杂业务工程落地 AI 编程提供了极具参考价值的破局思路，非常适合架构师及资深后端开发者阅读。文章总结出的“工程化设计优于 Prompt 调优”等原则，对提升企业级 DevOps 全流程闭环和开发效能具有极强的指导意义。

### [美团 LongCat-2.0 正式发布：在国产算力集群上完成全流程训练与推理的万亿参数模型](https://tech.meituan.com/2026/06/30/LongCat2.0.html)

来源：美团 · 技术团队

发布时间：2026-07-03 14:33:46
![](https://p1.meituan.net/meituantechblog/ef19600fdb0e6868a3574c4a8c7ff746220482.png)
**背景/问题**：随着大模型参数量迈向万亿级，如何在算力受限的条件下（特别是依赖国产算力集群）稳定、高效地完成大规模MoE模型的预训练与推理，同时解决模型在超长上下文和复杂Agentic Coding任务中的性能衰减问题，是当前AI工程领域的重大挑战。

**核心观点/方案**：美团开源了总参数1.6T的LongCat-2.0模型，业界首次在五万卡国产算力集群上完成全流程训练与推理。工程层面，通过确定性算子、弹性扩缩卡等技术将日故障率降低70%，并实现流水线调度和算子级控核使MFU提升1.5倍。模型架构层面，采用稀疏注意力机制（LSA）原生支持1M超长上下文，结合零计算专家与ScMoE实现Token级动态激活，并引入MOPD多专家融合架构，让模型在编程、推理与交互任务上按需调度算力。

**结论/价值**：LongCat-2.0在多项权威代码与复杂办公场景评测中达到甚至超越国际前沿闭源模型水平。该成果验证了国产算力支撑万亿参数模型稳定运行的可行性，对关注算力国产化替代、MoE架构底层优化及Agent应用落地的开发者和架构师具有极高的实战参考价值。

### [Claude Code 80%的提示词说删就删，Anthropic用Fable 5打了个样：AI行业的“降本”才刚刚开始](https://www.infoq.cn/article/GEkEm7rkUJfF8bdwTuBt)

来源：InfoQ 推荐

发布时间：2026-07-03 19:27:10
![](https://static001.infoq.cn/resource/image/df/aa/df136245afd543b373e714f352e0bfaa.png)
**背景/问题**：随着AI深度应用，企业算力成本失控，甚至引发了“Token末日”。许多公司限制模型等级或设定个人配额来抑制成本。以Claude Code为代表的产品为了营造“高产”错觉，在设计上大量消耗Token，导致资源浪费与效率低下。

**核心观点/方案**：为了应对高昂的算力成本，行业开始转向极限降本策略。Anthropic果断删减了Claude Code 80%的系统提示词，因为过度冗长的提示词已成为隐蔽的“Prompt债”，不仅占用上下文还拉低效率。同时，通过类似Caveman的插件精简输出语言，以及借鉴OpenAI压缩内部推理链路的技术，大幅减少无效Token的生成。

**结论/价值**：AI行业已从盲目追求Token消耗量迈入追求极致效率的新阶段。这篇文章深刻揭示了过度包装的AI工具背后的成本陷阱，对开发者和企业极具警示意义：精简提示词、优化输出与推理链路，是实现AI规模化盈利的必经之路。

### [ICML 2026 | 美团技术团队学术论文精选](https://tech.meituan.com/2026/06/29/ICML-2026.html)

来源：美团 · 技术团队

发布时间：2026-07-03 14:33:46
![](https://p0.meituan.net/meituantechblog/53ce71427cc5fb26c883af36a738b10569202.webp)
**背景/问题**：随着大语言模型向通用智能体演进，模型在长程推理中的记忆瓶颈、强化学习训练中的策略对齐与评估难题，以及多模态（尤其是高分辨率视频和长程交互世界模型）生成中的一致性与算力冲突，成为制约AI技术突破的核心痛点。

**核心观点/方案**：美团技术团队精选了13篇被ICML 2026收录的论文，从多维度提出了创新方案。在智能体推理方面，提出了基于版面感知的视觉记忆机制（MemOCR）以高效压缩交互历史；在强化学习训练上，推出解耦策略参数的通用价值模型（V_0）和联合自我验证机制。同时，针对评测痛点构建了评估噪声鲁棒性（AgentNoiseBench）和智能体裁判能力（AJ-Bench）的新基准。在多模态领域，提出了双频专家潜空间级联框架（LUVE）和层级化记忆架构（Infinite-World），显著提升了超高分辨率视频生成与1000帧以上长程交互的连贯性。

**结论/价值**：这批论文全方位展示了美团在AI前沿技术上的深厚积累，不仅提供了丰富的理论创新，还紧密结合了实际业务场景（如已落地的LongCat-Video模型）。对于从事大模型对齐、强化学习、智能体评测及视频生成的学术和工程研究人员而言，是一份不可多得的技术演进路线图。

## 💾 Daily Dev

### [iOS Dev Weekly 第757期：SwiftUI底层解析、iOS 27新特性与AI编程辅助](https://main--iosdevweekly.netlify.app/issues/757/)

来源：iOS Development News - Telegram Channel

发布时间：2026-07-03 23:17:32
![](https://cdn4.telesco.pe/file/AB-DTXlipe8hrEOrNTJNWN758arDewWcv7u23iVCNgWNz0_o52cVbBT3mjrky-OObipNCqgrOsS3J78ri1ipbHa-9XHhwaFRKpBagHC-PbyV7VbUCt0IKAQSCHwvGTrFFci2jVbN05PCUU3kn5CyU9yuU8dWm-3UYcUbwUM9ke6RPXNhU_aqAJdRF-wRjogBNEWlo93nvqa8jfGjasMSSE0Ai-3p3g7v8mf_tl8J2uYnTSb-4MawgXw0-Pbq6hhNEgWAO7QsHChnlsEpwsdmA_P6REoriYltxB0CsBM_dBIGzTKsV9tN7kwJ65x0EmdjqBez7uvEvElSwZGOBOAeEw.jpg)
**背景/问题**：WWDC 结束后，Swift 6.4 和 v27 SDKs 随 Xcode 27 beta 发布，iOS 开发社区正处于新工具链落地与旧架构演进的关键过渡期，开发者面临着适配新 API、解决复杂 UI 框架 Bug 以及探索 AI 编程落地等诸多挑战。

**核心观点/方案**：本期周报精选了数篇深度技术文章。探讨了通过差分测试“Oracle技术”从零重构 SwiftUI 引擎的硬核实践；剖析了由结构身份（如 `if/else` 与三元运算符的差异）引起的 SwiftUI 动画与 List 机制 Bug；介绍了 iOS 27 中支持原生拖拽排序的 `.reorderable()` 新 API；还分享了在 UIKit 与 SwiftUI 混用架构下构建设计系统时动态颜色解析的底层差异。此外，针对 AI 编程代理的局限性，介绍了一款旨在提升运行时可观测性的 `Broadcast` 日志库。

**结论/价值**：这是一份高价值的 iOS 技术雷达，适合中高级 iOS 开发者快速掌握后 WWDC 时代的核心技术动态。其价值不仅在于技术更新预告，更在于强调了深入理解 SwiftUI 底层视图树机制以及提升 AI 代理运行时调试能力的重要性，具有极强的实战指导意义。

## 📻 Podcast

### [SBBI China 2025 解读：如何在市场喧嚣中寻找长期投资的参照系](https://www.xiaoyuzhoufm.com/episode/6a4762cf2e335a35a80d789e)

来源：知行小酒馆

发布时间：2026-07-03 20:00:00
![](https://image.xyzcdn.net/Fgy2PobYbGHbU8AQWvHa5LPv5_hL.png)
**背景/问题**：面对当下A股市场风格切换、热门赛道（如AI、芯片）大涨等现象，普通投资者容易陷入迷茫和情绪内耗，常常怀疑“这次是不是真的不一样”以及长期投资是否依然有效。

**核心观点/方案**：《中国大类资产投资 2025 年报》（SBBI China 2025）提供了一个客观、长期的数据参照系。数据显示，长期承担更高波动的资产通常带来更高回报，且A股长期收益的核心驱动力是上市公司盈利的实际增长而非估值扩张。投资者应基于不同资产的相关性进行分散配置，并根据自身风险承受力进行动态再平衡，同时发挥个人投资者“等得起”的时间优势。

**结论/价值**：该播客通过翔实的历史数据，帮助投资者拨开短期市场情绪的迷雾，回归风险与收益相匹配的投资常识。对于普通投资者制定长期资产配置规划、克服追涨杀跌的人性弱点具有极高的指导价值和心理抚慰作用。
