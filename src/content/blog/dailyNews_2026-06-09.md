---
title: "Daily News #2026-06-09"
date: "2026-06-09 08:00:00"
description: >
  和产品一起成长 - 从 AI 猫娘到 Prowl 终端 深度访谈田渊栋：解析RSI的AI自进化技术路线与行业洞察 得物推荐 AI Harness：从“狂野代码”到“按目标生产”｜AICon上海 How to notarize a Mac app with notarytool How to use Apple signing certificates
tags:
- "AI商业化"
- "软件工程"
- "个人效率"
- "开发者体验"
- "Security"
- "职业发展"
- "RSI"
- "推荐系统"
- "DevOps"
- "macOS"
- "AI自进化"
- "AI架构"
- "Code Signing"
- "工作流"
- "强化学习"
- "AI Agent"
- "Xcode"
- "xcodebuild"
- "研发效能"
- "Notarization"
- "CI_CD"
- "iOS"

---

> - 和产品一起成长 - 从 AI 猫娘到 Prowl 终端
> - 深度访谈田渊栋：解析RSI的AI自进化技术路线与行业洞察
> - 得物推荐 AI Harness：从“狂野代码”到“按目标生产”｜AICon上海
> - How to notarize a Mac app with notarytool
> - How to use Apple signing certificates

## 🍎 iOS Blog

### [和产品一起成长 - 从 AI 猫娘到 Prowl 终端](https://onevcat.com/2026/06/develop-with-ai/)

来源：OneV's Den

发布时间：2026-06-07 20:10:00

**背景/问题**：随着 AI Agent 编程助手的普及与进化，传统的依赖长时间坐在电脑前、保持连续专注“心流”状态的开发模式正在受到冲击。开发者亟需调整工作习惯，以适应人机协同的新节奏。

**核心观点/方案**：作者基于大半年的 AI Agent 协同经验，提出了一种“持续调度”的新工作模式。日常编码不再是单线执行，而是让多个 Agent 在后台并行推进。开发者可以在碎片时间通过不同设备（如手机、墨水屏）进行监控和批复，仅在遇到复杂难题时才需要大段专注时间做决策。这种模式打破了设备的边界感，使所有终端都成为统一工作空间的入口。

**结论/价值**：文章以资深开发者的第一视角，揭示了 AI 时代软件工程师角色从“深度执行者”向“全局调度者”转变的趋势。对于希望利用 AI 突破生产力瓶颈、优化工作流的开发者和独立创作者而言，提供了极具前瞻性和可借鉴的实战洞察。

## 📥 Tech News

### [深度访谈田渊栋：解析RSI的AI自进化技术路线与行业洞察](https://www.bestblogs.dev/article/03279223?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-06-07 12:35:00
![](https://image.jido.dev/20251127045520_f3caed2e)
**背景/问题**
随着大模型技术的快速迭代，AI行业的竞争日益激烈，大公司发展路线趋向同质化。在此背景下，前Meta FAIR研究总监田渊栋选择加入估值46.5亿美金的新型AI实验室RSI（Recursive Superintelligence）。访谈聚焦于RSI试图解决的核心问题：如何突破当前大模型的发展瓶颈，通过递归自我改进实现AI自动化科研，从而最大化人类知识发现的速率。

**核心观点/方案**
RSI押注“自我进化”范式，致力于构建一个输入算力即可输出新知识的系统。在技术路线上，田渊栋强调预训练是模型能力的基础，而强化学习只是放大器，无法无中生有，预训练的上限决定了整体上限。同时，可解释性不仅是安全护栏，更是提升训练效率、避免算力浪费的关键指标。面对巨头竞争，小公司应避开趋同热点，切入自动化科研等具有窗口期的差异化路线。对于个人而言，在AI替代传统岗位的趋势下，必须摆脱“螺丝钉”思维，寻找独立的价值创造方向，进化为“四维生物”。

**结论/价值**
本文提供了来自顶尖AI研究员的一手技术判断与行业洞察，对理解大模型前沿技术演进（如预训练与强化学习的边界、连续思维链）和未来行业格局具有极高的参考价值。非常适合AI领域的研究者、技术决策者以及关注AI时代个人职业规划的从业者深度阅读。需要留意的是，RSI的自动化科研愿景目前仍处于早期阶段，其技术闭环的商业化落地效果仍需长期观察。

### [得物推荐 AI Harness：从“狂野代码”到“按目标生产”｜AICon上海](https://www.infoq.cn/article/pOwoNlmEL9zV0aodLVB9)

来源：InfoQ 推荐

发布时间：2026-06-07 10:00:00
![](https://static001.infoq.cn/resource/image/a6/da/a6fe27e22311d9062d7d0f1621e852da.jpg)
**背景/问题**：随着 AI Agent 逐步进入生产环境，工程师面临的核心挑战不再局限于“AI 能否实现功能”，而是如何确保 AI 生成的“黑盒”代码在极其复杂的推荐系统环境（如 AP 架构、动态调参）中稳定、安全地规模化运行，避免代码“能跑但不能用”。

**核心观点/方案**：得物技术团队提出构建贯穿推荐生命周期的 AI Harness（围栏）体系以实现“按目标生产”。方案包含 7 阶段护栏，将标准研发流程与环境强制绑定，覆盖从需求生成到自动化观测的全生命周期。此外，针对工业场景提出了一种 Highway & ATV 混合智能体架构：Highway 模式基于 Flow Engineering 处理 80% 的高频确定性任务，ATV 模式作为自主智能体解决 20% 动态反思的长尾复杂问题，并通过进化层将经验固化。

**结论/价值**：该方案通过结构化护栏和混合架构设计，有效化解了 AI 编码在复杂工程中的不确定性风险，满足了工业级应用对高稳定性的严苛要求。对于致力于大型推荐系统架构演进及 AI 研发效能提升的架构师和工程师而言，这套包含 7 阶段护栏的落地方法论和混合 Agent 架构具有极高的实战参考价值。

## 💾 Daily Dev

### [How to notarize a Mac app with notarytool](https://onmyway133.com/posts/how-to-notarize-a-mac-app-with-notarytool/)

来源：iOS Development News - Telegram Channel

发布时间：2026-06-07 16:52:05
![](https://cdn4.telesco.pe/file/owbG_PlfYV0z0n5vFM3Qk8kO73Aq-FqRg1KaJ576ykXiUT7Y6EcgWqifbWadScFS9hWVLyNrJWK2fRg5PrUVGeV6XiHU0nlx9ye07D08rezPPb5K6uQ2pn8MMuJ4DFrKuZdD4oan4XzX907KpIGVOm06I8t0EgNOR12yl_JKyS0DQWlrpAWXF8_1tLxsIBod_YirzkcHuIe6o2IpJlo3uQYQIEwd0ttqiiMpRSUf85bB9hNXxAjzJDvZJ3Qj2NZOB_E1zsTdd48VRubc42tBXZP8wxxucDcVnwR1_M-UfwAhaC-HevVA504AwjnrJOVJ0Uebs1tWztw9V3k0qMAa3Q.jpg)
**背景/问题**：自macOS 10.15起，未经Apple公证（Notarization）的应用在非App Store渠道分发时，会被Gatekeeper直接拦截。随着老旧的 `altool` 被弃用，开发者必须掌握基于现代 `notarytool` 的自动化公证流程。

**核心观点/方案**：文章提供了一套完整的命令行实战方案。从通过API Key配置Keychain凭证，到使用 `xcodebuild` 进行Archive和Developer ID导出，再到提交审核及装订票据，全流程均通过CLI实现。此外，文章深入剖析了文件拷贝引发的“unsealed contents”报错，指出macOS产生的 `._` AppleDouble扩展属性文件会破坏代码签名密封，并给出排查建议。

**结论/价值**：这是Mac独立开发和DevOps工程师不可或缺的实操宝典，对构建自动化发布流水线极具参考价值。文章不仅涵盖了标准操作，还披露了诸如隐藏文件破坏签名、特定路径下假阳性报错等隐蔽的工程陷阱，极大地节省了开发者排错时间。

### [How to use Apple signing certificates](https://onmyway133.com/posts/how-to-use-apple-signing-certificates/)

来源：iOS Development News - Telegram Channel

发布时间：2026-06-07 16:52:05
![](https://cdn4.telesco.pe/file/BvGy4TLDwMTeeA22l3x2mMUBpTnheAPPJ8pOxrf4C0w4BidLGi2bS2mhrt2MgVk1NeJvYtazSnvFnJft7hp56WHWIBnKbe0fWmGzFzMBXcNMj1xyeTO31F4YF6vHsnN6tRC1efaJSqsqZB-64SquJdl4deiJEDJPIxxX5aHsu5TTusyjSXvGCTdhhq2YSmsUpvGsp7usYvXz5XYfCie3NZjRZonVyzPIFcfShCCUidnRBCAdLJc9X1u0I0sYv-P1Qc42uwFwiBgp69L8-EWIrhzY9QHYvXZ72AKSrFzQHqsnFOkY2d6zTuiiV7lXLSxCoJxLMLKeb8KsdLfknPXsXA.jpg)
**背景/问题**：在Apple平台开发中，代码签名是应用安装和运行的基础，但Xcode背后管理的证书类型繁多。在排查签名失败或配置CI/CD环境时，开发者往往需要清楚各类证书的具体用途与权限限制。

**核心观点/方案**：文章系统梳理了三大类核心证书：用于本地开发和测试的个人级“Apple Development”证书；用于App Store和TestFlight发布的团队级“Apple Distribution”证书；以及专门用于Mac应用在App Store外部分发的“Developer ID”证书。文中明确区分了各证书的归属主体、数量上限，并建议开发者使用Xcode 11后推出的跨平台统一证书来简化管理。

**结论/价值**：本文是一份清晰实用的Apple签名证书避坑指南，非常适合初中级Apple生态开发者或负责配置自动化构建流水线的工程师阅读。掌握这些底层认证逻辑，能有效减少团队协作开发中的证书冲突，并提升CI/CD环境的配置效率。
