---
title: "Daily News #2026-11-18"
date: "2026-11-18 08:00:00"
description: >
  把「更好」放在「更快」之前 - 肘子的 Swift 周报 #162 从自动扩缩容到跨池调度：作业帮如何让 Flink 计算资源节省 30%？ 星云 Redis 容器化实践：资源降 63%-69%，交付从天级到分钟级 生成现实时代，人类该如何拥有彼此？ macOS 27.3 对设备控制、数据访问与全盘访问权限引入更细粒度管控 Science at the Frontier: How scientists use ChatGPT Broadening access to AI for scientists
tags:
- "云原生"
- "macOS"
- "Swift"
- "人机交互"
- "Flink"
- "AI 普惠"
- "安全"
- "Kubernetes"
- "iOS"
- "资源调度"
- "隐私"
- "苹果开发"
- "AI伦理"
- "实时计算"
- "OpenAI"
- "自动扩缩容"
- "信息生态"
- "社会议题"
- "生成式AI"
- "AI"
- "Redis"
- "调研报告"
- "科研"
- "AI 应用"
- "SwiftUI"
- "容器化"
- "权限管理"
- "ChatGPT"
- "高可用"
- "工具链"
- "平台工程"

---

> - 把「更好」放在「更快」之前 - 肘子的 Swift 周报 #162
> - 从自动扩缩容到跨池调度：作业帮如何让 Flink 计算资源节省 30%？
> - 星云 Redis 容器化实践：资源降 63%-69%，交付从天级到分钟级
> - 生成现实时代，人类该如何拥有彼此？
> - macOS 27.3 对设备控制、数据访问与全盘访问权限引入更细粒度管控
> - Science at the Frontier: How scientists use ChatGPT
> - Broadening access to AI for scientists

## 🍎 iOS Blog

### [把「更好」放在「更快」之前 - 肘子的 Swift 周报 #162](https://fatbobman.com/zh/weekly/issue-162/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2026-11-16 22:00:00
![](https://og.fatbobman.com/weekly/issue162.webp?imageView2/1/w/1600)
**本期周报以「把更好放在更快之前」为主题，探讨 AI 时代开发者应将效率提升转化为更高的完成度，而非单纯加速交付；同时汇集了 Shopify 原生化重构、Swift 生态动态、SwiftUI 特性实测等精选内容。**

* Shopify 借助 Coding Agent 在 12 周内将应用从 React Native 重构为原生 Swift/Kotlin，Android 启动时间缩短约 50%、体积减少 40%、iOS 峰值内存降低 70%，并通过 Reflex 架构与 Helix 工具应对 Agent 时代的验证瓶颈。
* Swift 动态：CocoaPods 将于 2026 年 12 月 2 日进入只读状态，SwiftPM 的 SE-0545（构建性能调试）、SE-0547（编译缓存）等提案相继获得接受。
* 技术细节：Xcode 27 开启 Tuist 编译缓存后断点失效，根因是调试信息中的虚拟路径缺少 LLDB target.source-map 映射；GlassEffectContainer 的 spacing 与 glassEffectID、以及 inspector 与 .sheet 的行为差异均有实测发现。
* 开源工具：Yardlet（Swift 构建的 macOS 多 Agent 原生工作台）与 Heimdall（强调密钥安全与人工确认的 App Store Connect MCP Server）值得关注。

## 📥 Tech News

### [从自动扩缩容到跨池调度：作业帮如何让 Flink 计算资源节省 30%？](https://www.infoq.cn/article/UTrbuCiAG5H9TiqcwgxI)

来源：InfoQ 推荐

发布时间：2026-11-16 18:01:06
![](https://static001.infoq.cn/resource/image/9e/26/9e571f4798853736d65a7581d1df5d26.png)
**作业帮基于 Flink Kubernetes Operator 的 Autoscaler 与集群重调度体系，让实时作业按真实负载自动调整并行度，实测节省约 30% 计算资源。**

* Autoscaler 从 Source 持续输入与积压追赶速率出发，沿 JobGraph 传播处理需求，结合各 JobVertex 满负载处理速率换算目标并行度；通过 in-place 原地扩缩复用已有 JM/TM Pod，减少重建开销与节点负载扰动。
* 针对 Flink 1.19.1 缩容后 TM 无法回收的问题，回补 FLINK-33977（最少 TM 策略）、FLINK-36201（Slot 分配器选择）、FLINK-37813（Slot 数量统计）等修复，并增加「最旧 TM 优先」策略。
* 通过并行度上下界与缩容步长公式控制扩缩震荡；同步修复 metrics reporter 内存泄漏与 Iceberg 孤儿文件问题。
* 集群层面用 Crane 水位控制与任务级 Descheduler 疏解热点，晚高峰将高负载作业分流至 Serverless 与错峰的离线 K8s 集群，高峰后经内存预检分阶段回迁，并以 Kubernetes Lease 实现调度器主备容错。

### [星云 Redis 容器化实践：资源降 63%-69%，交付从天级到分钟级](https://www.bestblogs.dev/article/067b231eb0?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-16 12:29:00
![](https://image.jido.dev/20260527130453_c4b7ab1.jpeg)
**星云团队完整分享了 Redis 从虚拟机迁移到容器化并落地生产的实践：通过八大专项系统化优化，交付从天级缩短到分钟级，资源成本降低 63%-69%，实现故障自动收敛与业务自助开通。**

* 容器化从立项到上线仅用两个月，但从"能部署"到"敢上生产"又花近一年做专项优化，核心思路是把过去靠供应商、靠熟练度、靠人盯着的运维能力逐条沉淀进平台
* 专项覆盖高可用（多套哨兵+固定服务地址）、持久化与 IO 治理（主关从开+猝死保护）、数据与元数据分离（本地盘+共享存储）、参数按规格自动推导、备份与 Key 治理、日志告警拨测可观测体系、自助 SKU 交付等
* 收益数据：测试环境同批集群 CPU、内存、存储降至原来三分之一左右，降幅 63%-69%；生产环境通过资源池化吸收峰值预留，长期成本变得可控
* 哨兵切换、主节点空数据保护、哨兵全挂后自动切主等场景全部自动化，值班从"登机器救火"转为处理平台告警；文章同时强调对数据库类产品，"暂时不可用"与"数据丢失"是完全不同量级的后果

### [生成现实时代，人类该如何拥有彼此？](https://www.bestblogs.dev/article/ffba5fc498?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-16 17:00:00
![](https://media.bestblogs.dev/20260827095624_dbb7c8f.jpeg)
**腾讯研究院系统阐释了生成式 AI 时代"现实可被凭空生成"引发的因果律倒置、证据机制崩塌与"单人宇宙"困境，并提出追查源头、看清滤镜、适时离屏才是未来最稀缺的"元能力"。**

* 屏幕已从观察世界的窗口演变为重构现实的介质，AI 不再只是推荐既有内容，而是实时生成专属的报道、视频与证据逻辑，人类从世界的参与者沦为终身观众
* AI 生成内容可"先于现实发生"并产生真实物理后果：五角大楼虚构爆炸图引发美股暴跌、斯洛伐克选举合成音频干扰结果、AI 设计的全新蛋白质在实验室被成功合成
* 随着生成内容逼真度提升，法院开始拒绝真实视频作为证据、伪造录音稀释政治丑闻，举证责任被逆转，法庭、记忆与艺术创作的真伪边界日益模糊
* 算法为每个用户拼接逻辑自洽却互斥的证据链，催生"单人宇宙"，公共现实被解构，共识维护成本陡增，人类可能失去与真实之人和真实之物深度相遇的机会
* 文章最后呼吁：未来最关键的不是辨别真伪的技术，而是看清滤镜由谁裁剪、知道何时追查源头、何时暂别屏幕走出门去的能力

### [macOS 27.3 对设备控制、数据访问与全盘访问权限引入更细粒度管控](https://developer.apple.com/news/?id=oqng0zjk)

来源：Latest News - Apple Developer

发布时间：2026-11-17 00:00:11
![](https://developer.apple.com/news/images/og/full-disk-access-og.png)
**苹果在 macOS 27.3 beta 2 中对 Device Control and Data Access 与 Full Disk Access 两项高权限 API 进行拆分与细化，显著提升权限授予的透明度与用户控制粒度。**

* 原 Device Control and Data Access 拆分为 System & App Protection Override 与 Accessibility 两个独立设置，授权方式统一为从列表中选择请求应用，并支持配置为“每次需要时询问”
* 系统会引导用户仅授予工作流所必需的特定应用（System & App Protection Override）或文件夹（Full Disk Access），并在应用控制其他应用时显示透明度指示器
* 已授权的应用权限保持不变；开发者需调整用户引导流程，确保应用能优雅处理仅获得有限目录或应用访问权限的情形
* 使用 Full Disk Access 做磁盘备份或依赖 Accessibility 提供辅助功能的开发者，可申请 entitlement 以在新安装中维持原有体验，目前已知应用暂不受影响，具体细节稍后公布

### [Science at the Frontier: How scientists use ChatGPT](https://openai.com/index/science-at-the-frontier)

来源：OpenAI News

发布时间：2026-11-16 20:00:00

**OpenAI 发布调研报告《Science at the Frontier》，基于对 1800 多名科学家使用 ChatGPT 情况的调查，呈现 AI 在科研一线的真实应用图景。**

* 调研覆盖三个维度：科学家日常工作流中的使用方式、自述的生产力变化，以及对 AI 辅助科学发现的预期
* 数据为理解大模型在科研场景的渗透程度与典型用法提供了第一手参考，对科研管理者、AI 工具开发者及政策研究者均有借鉴价值
* 原文为报告概要形式，样本构成、调研方法与更细颗粒度的结论需查阅完整报告

### [Broadening access to AI for scientists](https://openai.com/index/expanding-chatgpt-for-academic-researchers)

来源：OpenAI News

发布时间：2026-11-17 01:00:00

**OpenAI 宣布扩大 "ChatGPT for Academic Researchers"（学术研究者版）计划，向全球 20 万名研究人员免费开放其前沿模型的使用权限。**

* 这是该计划的一次显著扩容，免费规模从原有较小范围的学术用户扩展至全球 20 万研究者，大幅降低科研群体使用旗舰模型的门槛
* 研究者可在零成本条件下将前沿模型用于文献梳理、数据分析、代码辅助等科研工作流，属于 AI 普惠与科研生态建设层面的举措
* 原文为公告性质，具体的申请资格、审核流程与开放模型范围等细节未展开，需关注后续说明
