---
title: "Daily News #2026-07-16"
date: "2026-07-16 08:00:00"
description: >
  Apple’s notarytool can’t handle Zip64 files 正式开源！美团 LongCat-2.0 同步开放国产卡推理代码 美团 LongCat-2.0 正式发布：在国产算力集群上完成全流程训练与推理的万亿参数模型 从 Coder 到 Designer：电商团队数据研发的 Harness Engineering 实践 极致量化，近三千亿参数 Hy3 单卡即可部署 Claude Artifacts 全面升级：打通公开分享、多人协作与 Slack 集成 AppleOS 27 Public Beta 首个公测版发布及开发者测试版更新策略 Apple 发布新一轮操作系统测试版更新 销售团队如何利用 ChatGPT Work 提升效率 数据科学团队如何借助 ChatGPT Work 辅助分析 Swift 并发演进：深入解析 Continuation、CheckedContinuation 与 UnsafeContinuation 对话 AI 虚拟偶像 Yuri 打造者：构建硅基人格与商业化探索
tags:
- "llama.cpp"
- "AI应用"
- "工作流"
- "大模型"
- "知识工程"
- "数据科学"
- "自动化报告"
- "模型部署"
- "Apple"
- "AIGC"
- "Anthropic"
- "ChatGPT"
- "Multi-Agent"
- "腾讯混元"
- "AI辅助分析"
- "Swift Concurrency"
- "并发编程"
- "虚拟偶像"
- "macOS"
- "NL2SQL"
- "销售自动化"
- "万亿参数模型"
- "系统更新"
- "AI协作"
- "MoE架构"
- "OpenAI"
- "AI"
- "商业化"
- "watchOS"
- "生产力工具"
- "硅基人格"
- "推理优化"
- "DMG"
- "Apple 公证"
- "开源"
- "Agentic Coding"
- "架构设计"
- "Artifacts"
- "Swift"
- "避坑指南"
- "大模型量化"
- "iOS"
- "国产算力"
- "打包"
- "Claude"
- "测试版"

---

> - Apple’s notarytool can’t handle Zip64 files
> - 正式开源！美团 LongCat-2.0 同步开放国产卡推理代码
> - 美团 LongCat-2.0 正式发布：在国产算力集群上完成全流程训练与推理的万亿参数模型
> - 从 Coder 到 Designer：电商团队数据研发的 Harness Engineering 实践
> - 极致量化，近三千亿参数 Hy3 单卡即可部署
> - Claude Artifacts 全面升级：打通公开分享、多人协作与 Slack 集成
> - AppleOS 27 Public Beta 首个公测版发布及开发者测试版更新策略
> - Apple 发布新一轮操作系统测试版更新
> - 销售团队如何利用 ChatGPT Work 提升效率
> - 数据科学团队如何借助 ChatGPT Work 辅助分析
> - Swift 并发演进：深入解析 Continuation、CheckedContinuation 与 UnsafeContinuation
> - 对话 AI 虚拟偶像 Yuri 打造者：构建硅基人格与商业化探索

## 🍎 iOS Blog

### [Apple’s notarytool can’t handle Zip64 files](https://wadetregaskis.com/apples-notarytool-cant-handle-zip64-files/)

来源：Wade Tregaskis

发布时间：2026-07-14 01:21:35

**背景/问题**：Mac 开发者在向 Apple 提交应用进行公证时，如果应用捆绑包内包含单个体积超过 4 GiB 的大文件，传统的 ZIP 压缩打包方式会导致提交流程失败。

**核心观点/方案**：文章指出 Apple 的 `notarytool` 工具目前存在兼容性局限，无法正确解析支持超大文件的 Zip64 标准压缩包。针对这一缺陷，开发者必须调整打包策略，改用磁盘映像（DMG）格式来封装包含超大文件的应用，从而绕过此限制并顺利完成公证。

**结论/价值**：这是一篇简明扼要但极其精准的实战避坑指南。对于开发大型游戏、专业软件或包含海量媒体资源库的 macOS 开发者而言，该文章提供了直接有效的解决方案，能够帮助他们在应用发布阶段少走弯路，节省大量的构建与排错时间。

## 📥 Tech News

### [正式开源！美团 LongCat-2.0 同步开放国产卡推理代码](https://tech.meituan.com/2026/07/12/LongCat-2.0-Open-source.html)

来源：美团 · 技术团队

发布时间：2026-07-14 10:25:40
![](https://p1.meituan.net/meituantechblog/368b1cd0634db5c41b127242d8feee08118728.png)
**背景/问题**：随着大模型参数量迈向万亿级，如何在受限的显存和带宽条件下，特别是使用国产算力芯片，实现高效、稳定的大规模推理与部署，是当前 AI 基础设施建设面临的核心挑战。

**核心观点/方案**：美团正式开源万亿参数大模型 LongCat-2.0 并开放国产卡推理代码。该模型专为 Agentic Coding 任务设计，引入了 LongCat 稀疏注意力和 N-gram Embedding 以提升长上下文与 Token 级表现。团队从模型架构、芯片适配和部署策略三个维度进行深度协同优化，结合 PD 分离部署和物理核心级并行，成功突破算力瓶颈，在存量国产硬件上实现了万亿参数模型的流畅推理。

**结论/价值**：LongCat-2.0 的开源不仅验证了国产芯片承载复杂大模型任务的能力，更提供了一套可复现的存量算力盘活方案。对关注大模型推理优化、MoE 架构部署及国产算力生态建设的算法与系统工程师具有极高的实战参考价值。

### [美团 LongCat-2.0 正式发布：在国产算力集群上完成全流程训练与推理的万亿参数模型](https://tech.meituan.com/2026/06/30/LongCat2.0.html)

来源：美团 · 技术团队

发布时间：2026-07-14 10:25:40
![](https://p1.meituan.net/meituantechblog/ef19600fdb0e6868a3574c4a8c7ff746220482.png)
**背景/问题**：构建万亿参数级别的稀疏混合专家模型，并在非顶级的国产算力集群上完成全流程的稳定训练与高效推理，面临着通信延迟、硬件故障率以及显存带宽等多重底层工程瓶颈。

**核心观点/方案**：美团发布了在 5 万卡国产集群上完成全流程训练与推理的 LongCat-2.0。团队通过自研确定性算子与一致性验证保障训练正确性，利用流水线调度将训练 MFU 提升 1.5 倍。架构层面，采用稀疏注意力（LSA）实现 100 万 Token 的超长上下文处理，结合零计算专家和 ScMoE 实现动态激活，并通过 MOPD 架构融合多专家能力，使模型在真实编程与复杂任务处理中表现卓越。

**结论/价值**：LongCat-2.0 在各项基准评测中已达到或接近国际前沿闭源模型水平。其底层训练优化与系统架构经验，为国内算力生态提供了极具价值的万亿模型落地范本，强烈推荐大模型系统架构师和 AI 基础设施研发人员深入研读。

### [从 Coder 到 Designer：电商团队数据研发的 Harness Engineering 实践](https://www.bestblogs.dev/article/c7a89e8181?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-14 18:08:00
![](https://image.jido.dev/20260527050038_b20a9a1.jpeg)
**背景/问题**：AI 在复杂的企业级数据研发任务（如垂直领域的 NL2SQL）中，常面临严重的不稳定性、幻觉以及行为漂移问题，难以在要求高准确性的业务场景中规模化落地。

**核心观点/方案**：阿里电商团队提出将“知识工程”与“Harness Engineering”结合的 Multi-Agent 系统架构。一方面通过三层结构化知识库沉淀专家经验，让 AI“有据可依”；另一方面，引入人工 Gate 审批、空间隔离与配置治理等约束机制保障运行稳定。同时，系统采用 7-Agent 顺序协作流，并创新性地加入“心跳机制”，使 Agent 能够从历史执行中提取模式，实现自动补充知识和自我迭代。

**结论/价值**：AI 在垂直领域的深度落地不仅是模型能力问题，更是复杂的系统工程问题。该实践提供了一套高可靠、可回溯的工业级 Agent 架构落地范式，对解决大模型在企业级复杂任务中的不稳定性具有极高的参考价值，强烈推荐架构师及 AI 应用开发者研读。

### [极致量化，近三千亿参数 Hy3 单卡即可部署](https://www.bestblogs.dev/article/f37d5dd27b?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-14 16:56:00
![](https://image.jido.dev/20251127045433_c2ea00c4)
**背景/问题**：千亿参数级别的旗舰大模型通常受限于庞大的显存需求，难以在资源受限的本地设备或单卡环境中部署运行，阻碍了其更广泛的普及与应用。

**核心观点/方案**：腾讯混元团队对其 295B 参数的 Hy3 模型进行了极致的 1bit 和 4bit 量化，并适配 llama.cpp。1bit 版本将权重压缩至约 85.5 GiB，成功实现单张 96GB 显卡运行；4bit 版本（约 169.9 GiB）在 Agent、代码等实际任务中表现与原模型高度一致。更令人瞩目的是，1bit 版本性能掉点也在可接受范围内。此外，团队开发并开源了 MTP 投机解码补丁，使解码速度大幅提升 50%-60%。

**结论/价值**：此项量化及加速工程显著降低了超大规模模型的使用硬件门槛，证明了极端压缩下模型能力的鲁棒性，为个人开发者及中小型企业低成本探索千亿级大模型提供了极具实用价值的方案，适合 AI 工程师和本地部署爱好者实践。

### [Claude Artifacts 全面升级：打通公开分享、多人协作与 Slack 集成](https://www.infoq.cn/article/Pqcx0ktTdljvoQ3OMxze)

来源：InfoQ 推荐

发布时间：2026-07-14 22:01:15
![](https://static001.infoq.cn/resource/image/f4/06/f40abf4yyc1c74a785c432d5d4275106.png)
**背景/问题**：随着 AI 模型能力的逐渐趋同，企业级 AI 应用的竞争已从单一比拼模型性能，转向争夺工作流入口和任务交付链路。如何让 AI 生成的工作结果无缝接入团队真实协作场景并形成交付闭环，成为当前亟待解决的问题。

**核心观点/方案**：Anthropic 对 Claude Artifacts 进行了重大更新，支持 Claude Code 生成的 Artifact 公开分享与真正的多人版本化协作编辑。同时，打通了 Slack 中的 Claude Tag，允许团队在群聊中直接触发任务并生成可持续维护的成果页面。这标志着 Claude 正从单纯的对话模型，转变为集成代码理解、任务委派和成果交付的企业工作流执行节点。

**结论/价值**：文章深入剖析了此次更新的战略意义，指出构建完整的协作闭环和强大的企业级权限治理才是 AI 厂商的真正护城河。适合关注 AI 商业化落地、企业工作流自动化及大模型产品架构的读者阅读，能为其提供极具价值的前瞻性参考。

### [AppleOS 27 Public Beta 首个公测版发布及开发者测试版更新策略](https://t.me/AppleNuts/2470)

来源： Apple Nuts - Telegram Channel

发布时间：2026-07-14 09:03:58
![](https://cdn5.telesco.pe/file/fFORtnYvxnXFlk-KGAsDWtjIQtdphA21sDX54BrbBViPkpu7hXGOj2YXUZ9wtCdKl1DAHaolob5WTKcMVok5la7fb2woshPMsNs1AJQvtikH19KHZOgGEEzL1qHBgkgeq3ZmXq_29OM8BzwfOf6tjEtzzLa0JyRRrylwZeii79XU_NSGNZCGmXcnfIFTTcQrAw-mK85mkLRPgTqo13u6_KjUB3OW8r-lk9VYWYEeo4WUjTwg8V7a2EN_dIfthEMrdZVtxoBLUuhZh9p1xy2sBkeS-VPiuZ_2LoaM5WF0HC_JNpIHDKo1X_EnncVw5KOsuTU01AVDtjW0XkXHGYKDQg.jpg)
**背景/问题**：Apple 发布了首个 AppleOS 27 公测版（Public Beta 1），并重新发布了开发者测试版（DB3 v.2），以修复此前 DB3 版本中存在的问题并提升系统稳定性。

**核心观点/方案**：此次发布的 PB1 是基于修正版 DB3 v.2 构建的。对于 iPadOS 27 和 macOS 27 而言，初版 DB3 与当前的 PB1 存在差异。官方建议已升级 DB3 的用户切换至 Public Beta 频道，以获取更稳定的体验；后续若两者编译版本号一致，则依然可通过 Developer Beta 固件线刷升级。

**结论/价值**：文章为苹果生态的开发者和早期测试用户提供了关键的版本切换操作指南，对追求系统稳定性的尝鲜者具有较高参考价值，能帮助用户避免因测试版 Bug 导致的日常使用阻碍。

### [Apple 发布新一轮操作系统测试版更新](https://t.me/AppleNuts/2469)

来源： Apple Nuts - Telegram Channel

发布时间：2026-07-14 04:50:25
![](https://cdn5.telesco.pe/file/fFORtnYvxnXFlk-KGAsDWtjIQtdphA21sDX54BrbBViPkpu7hXGOj2YXUZ9wtCdKl1DAHaolob5WTKcMVok5la7fb2woshPMsNs1AJQvtikH19KHZOgGEEzL1qHBgkgeq3ZmXq_29OM8BzwfOf6tjEtzzLa0JyRRrylwZeii79XU_NSGNZCGmXcnfIFTTcQrAw-mK85mkLRPgTqo13u6_KjUB3OW8r-lk9VYWYEeo4WUjTwg8V7a2EN_dIfthEMrdZVtxoBLUuhZh9p1xy2sBkeS-VPiuZ_2LoaM5WF0HC_JNpIHDKo1X_EnncVw5KOsuTU01AVDtjW0XkXHGYKDQg.jpg)
**背景/问题**：Apple 持续推进其各操作系统的测试周期，面向开发者和公测用户发布了新一轮的测试版软件更新。

**核心观点/方案**：本次更新主要包含针对下一代大版本的 iPadOS 27.0 beta 3 v.2 和 macOS 27.0 beta 3 v.2，以及针对当前代版本的迭代更新，包括 iOS/iPadOS/macOS/tvOS/visionOS/watchOS 26.6 beta 5。

**结论/价值**：这是一则常规的系统版本推送资讯，内容相对简略，仅列出了更新的版本号。适合持续关注 Apple 软件生态更新进度和修复细节的极客或开发者追踪版本记录使用。

### [销售团队如何利用 ChatGPT Work 提升效率](https://openai.com/academy/codex-for-work/how-sales-teams-use-codex)

来源：OpenAI News

发布时间：2026-07-14 08:00:00

**背景/问题**：销售团队在日常运作中需要处理大量繁琐的案头工作，包括制作销售管线简报、会议准备材料、销售预测审查、客户规划以及停滞交易的诊断分析，这些工作往往会挤占实际的业务拓展时间。

**核心观点/方案**：OpenAI 展示了 ChatGPT Work 在销售场景的具体应用方案。通过输入真实的业务数据，销售团队可以利用该工具快速自动化生成上述各类文档和报告，从而优化案头工作流程并提高信息整合效率。

**结论/价值**：这是一篇典型的 AI 产品应用场景介绍资讯。对于希望提升日常工作效率的销售管理者或从业者具有初步的启发作用，但内容缺乏技术实现细节和深度的使用测评，更适合作为了解大模型商业化落地场景的快速阅读材料。

### [数据科学团队如何借助 ChatGPT Work 辅助分析](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex)

来源：OpenAI News

发布时间：2026-07-14 08:00:00

**背景/问题**：数据科学团队的工作不仅限于构建模型和处理数据，还经常需要耗费大量精力撰写各类业务沟通文档，如根因分析简报、业务影响报告、KPI 备忘录、范围界定分析以及数据看板规范等，这些案头工作往往重复且耗时。

**核心观点/方案**：文章介绍了 ChatGPT Work 针对数据科学团队痛点的辅助能力。该工具能够基于团队提供的真实工作输入，帮助快速构建和生成上述标准化的分析报告与数据规范文档，让数据人员更专注于核心的数据挖掘工作。

**结论/价值**：适合数据分析师、数据工程师以及管理者了解生成式 AI 在优化数据团队汇报和沟通效率上的潜力。但该资讯本质上偏向于产品功能宣传，仅停留在表层的场景罗列，并未涉及具体的 API 集成或底层技术架构设计，技术参考价值较为有限。

## 💾 Daily Dev

### [Swift 并发演进：深入解析 Continuation、CheckedContinuation 与 UnsafeContinuation](https://livsycode.com/swift/continuation-vs-checkedcontinuation-vs-unsafecontinuation-in-swift/)

来源：iOS Development News - Telegram Channel

发布时间：2026-07-14 23:47:37
![](https://cdn4.telesco.pe/file/ZYI15HARqBvzHE5US4EDEnK03ZwY6GsqNepsxRBT2Php5bllIHB9zfyqXiZbRii4Rf8Z-QfkkqKuDWIrlIjWzlTisXaICw4OW4mlJG8oFkMSv-MBXaxQ1DDOqlaaN1fijbMboQHntRu7GfqUOMrCtGTao3oicwsk2Xzq0dvcdC95b_2WRL8kBd6oWUGHMWU3PM_CLtqbDTv8lxoj_C5P33ICFA5QcIpRf9t8y623hbZxvCW3lYdnGQj8XolK1oNCBcuV3amT1THeWgwstnO_9PqzPWinRAX524TOx8JKFSaa677JvpUmU1QqAoaRdP7E32B-zicYG9DJSOTWws8kNA.jpg)
**背景/问题**：在 Swift 中将旧的基于回调的代码桥接到 async/await 时，必须使用 Continuation，且其严格要求“仅被恢复（resume）一次”。过去 Swift 仅提供消耗性能的 CheckedContinuation 和无安全保护的 UnsafeContinuation，开发者难以在编译期安全和运行性能之间取得完美平衡。

**核心观点/方案**：Swift 6.4 引入了基于 `~Copyable`（不可复制）特性的全新 `Continuation` 类型。通过所有权机制，调用 `resume` 会直接消耗掉该对象，从而将“多次恢复”的严重错误从运行时拦截提前到了编译期。同时，通过新的 `withContinuation` API 统一了抛错与非抛错的类型表达。但对于存在多个互斥闭包（如分别提供成功和失败回调）的复杂第三方遗留代码，编译器难以推断其唯一执行路径，此时仍需依赖支持运行时检查的 CheckedContinuation。

**结论/价值**：文章清晰地界定了三种 Continuation 的适用边界：新 `Continuation` 适合单一回调路径且对性能敏感的底层代码；`CheckedContinuation` 依然是包装复杂代理和多回调 API 的首选；`UnsafeContinuation` 则保留给极致性能场景。非常适合中高级 iOS 开发者阅读，有助于深入理解 Swift 编译器所有权模型在并发安全控制中的实际落地，并在日常开发中做出最合理的 API 选型。

## 📻 Podcast

### [对话 AI 虚拟偶像 Yuri 打造者：构建硅基人格与商业化探索](https://www.xiaoyuzhoufm.com/episode/6a547b7e1e32575f5eb5951d)

来源：三五环

发布时间：2026-07-14 20:00:00
![](https://image.xyzcdn.net/FuNJZCKSazUqutO8XGXVKWPPh7K4.png)
**背景/问题**：随着AI生成技术的成熟，内容创作已从技术猎奇走向常态化应用。然而，如何利用AI打造一个有血有肉、不会“塌房”的原创虚拟偶像，并突破商业化瓶颈，是当前行业面临的核心挑战。

**核心观点/方案**：以原创虚拟歌手Yuri为例，探讨了AI“造人”的实验过程。AI偶像的核心资产并非单纯的形象或声线复刻，而是通过文本、音频、影像等多层创作构建的“硅基人格”。在这个过程中，人类的审美和决策至关重要，AI只是辅助工具。真正的长期价值在于拥抱独特的“AI味”，而非一味模仿真人。此外，开放实时对话存在伦理底线风险，且AIGC内容的爆发仍受限于当前的移动端硬件载体。

**结论/价值**：该内容为AI数字人赛道提供了极具启发性的产品与商业洞察，明确指出虚拟偶像的核心壁垒在于“人格化”设定与人类独特的创意审美。适合关注AIGC商业化、虚拟数字人及AI产品设计的从业者阅读，有助于从业者跳出“AI焦虑”，重新审视技术、内容与情感连接的本质关系。
