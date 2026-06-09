---
title: "Daily News #2026-06-11"
date: "2026-06-11 08:00:00"
description: >
  在 Claude、Codex 和 Cursor 中使用 Xcode 27 的 Agent Skills Swift 6.4 新特性前瞻：已实现的 Swift Evolution 提案汇总 导致 Spark on Kubernetes 发生 OOM 故障的两个配置错误 美团 LongCat 开源 General 365：树立推理评测新标尺 用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践 Introducing Time Allowances Updated Apple Developer Program License Agreement and App Review Guidelines now available 在 Claude、Codex 和 Cursor 中使用 Xcode 27 的 Agent Skills
tags:
- "Kubernetes"
- "性能调优"
- "通用推理"
- "语言特性"
- "开发者协议"
- "AI Agent"
- "API"
- "研发效能"
- "Spark"
- "App Store"
- "AI编程"
- "家长控制"
- "Agent"
- "AI合规"
- "大模型评测"
- "AI辅助编程"
- "云原生"
- "Cursor"
- "架构重构"
- "Xcode"
- "年龄评级"
- "软件工程"
- "iOS"
- "苹果生态"
- "iOS开发"
- "Swift Evolution"
- "App审核"
- "Swift"
- "逻辑智能"
- "并发"
- "故障排查"
- "美团"
- "合规要求"

---

> - 在 Claude、Codex 和 Cursor 中使用 Xcode 27 的 Agent Skills
> - Swift 6.4 新特性前瞻：已实现的 Swift Evolution 提案汇总
> - 导致 Spark on Kubernetes 发生 OOM 故障的两个配置错误
> - 美团 LongCat 开源 General 365：树立推理评测新标尺
> - 用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践
> - Introducing Time Allowances
> - Updated Apple Developer Program License Agreement and App Review Guidelines now available
> - 在 Claude、Codex 和 Cursor 中使用 Xcode 27 的 Agent Skills

## 🍎 iOS Blog

### [在 Claude、Codex 和 Cursor 中使用 Xcode 27 的 Agent Skills](https://www.avanderlee.com/ai-development/using-xcode-27s-agent-skills-in-claude-codex-and-cursor/)

来源：SwiftLee

发布时间：2026-06-09 21:58:37
![](https://swiftlee-banners.herokuapp.com/imagegenerator.php?title=Using+Xcode+27%26%238217%3Bs+Agent+Skills+in+Claude%2C+Codex%2C+and+Cursor)
**背景/问题**
随着 AI 辅助编程的爆发，开发者越来越依赖 Claude、Codex 和 Cursor 等第三方 AI 编码工具。然而，在苹果生态中，如何将这些外部工具与官方的开发环境进行深度、可靠的结合，一直是iOS开发者面临的痛点。

**核心观点/方案**
Apple 在 WWDC'26 上发布的 Xcode 27 引入了重大的“Agentic”开发改进，推出了官方的 Agent Skills。文章强调，在使用 AI Agent 时，选择权威来源的技能至关重要，而 Apple 官方提供的 Skills 显然具备最高的权威性。更重要的是，这些官方 Agent Skills 不仅限于 Xcode 内部，还能直接在 Claude、Codex 和 Cursor 等主流 AI 工具中交互使用，从而大幅提升应用构建的效率与规范性。

**结论/价值**
这篇资讯释放了一个强烈的信号：Apple 正式全面拥抱 AI Agent 驱动的开发模式，并且采取了开放兼容的策略。对于所有 iOS 和苹果生态开发者而言，掌握并应用 Xcode 27 的官方 Agent Skills 将是提升未来生产力的关键。由于本文属于概览性质，适合作为技术动向跟踪，但缺乏具体的接入配置细节，读者需等待后续更深入的实操文档。

### [Swift 6.4 新特性前瞻：已实现的 Swift Evolution 提案汇总](https://wadetregaskis.com/whats-coming-in-swift-6-4/)

来源：Wade Tregaskis

发布时间：2026-06-09 03:33:29

**背景/问题**：Swift 语言持续快速迭代，开发者需要及时了解每个版本中纳入的新语言特性与改进，以便在项目中合理规划和应用。本文对 Swift 6.4 版本中已标记为"Implemented"状态的 Swift Evolution 提案进行了汇总梳理。

**核心观点/方案**：文章逐一列出了 Swift 6.4 中已完成实现的提案，其中重点提及了 SE-493（Async inside defer）。该提案允许在 `defer` 块中使用 `async` 异步操作，前提是外层上下文本身必须是 `async` 的。此外，类型推断在闭包中也能正常工作，闭包会隐式继承异步上下文。

**结论/价值**：这是一篇版本更新追踪类文章，适合关注 Swift 语言演进的一线开发者快速了解 6.4 的变化动向。但需注意作者声明未亲自验证这些实现的完整性，且原文内容较短，信息深度有限，建议读者结合官方 Swift Evolution 仓库进一步查阅各提案的详细设计文档。

## 📥 Tech News

### [导致 Spark on Kubernetes 发生 OOM 故障的两个配置错误](https://www.infoq.cn/article/sElIC5qTiH6iTiFJvDEk)

来源：InfoQ 推荐

发布时间：2026-06-09 18:00:00
![](https://static001.infoq.cn/resource/image/20/d4/201190168c2162995bb3cb84ba73e9d4.jpg)
**背景/问题**

将 Spark 批处理任务从本地机房迁移至 Azure Kubernetes Service (AKS) 后，业务高峰期频繁触发 OOMKilled (Exit Code 137)。常规的堆内存扩容与增加执行器数量均告无效，节点内存异常飙升且执行器因 OOM 被内核频繁终止，导致任务彻底失败。

**核心观点/方案**

文章详细拆解了引发故障的三个复合因素：大规模 Shuffle 操作引发的内存压力、被错误配置为强制同节点调度的 podAffinity 规则，以及最致命的基于 RAM 的本地临时目录（tmpfs=true）。当所有执行器被强制分配到同一节点，且 Shuffle 溢出数据被写入节点内存而非磁盘时，节点内存瞬间被榨干。最终通过将调度策略改为 podAntiAffinity 分散执行器，关闭 tmpfs 转而使用磁盘溢出，并将 emptyDir 存储卷上限扩大至 10Gi 彻底解决了该问题。

**结论/价值**

这是一篇极具实战价值的云原生排障指南。它打破了“平移上云无需修改配置”的盲区假设，深刻揭示了基础设施差异带来的隐蔽风险。对于负责大数据迁移、Spark on K8s 运维以及云原生架构的工程师而言，文末附带的“OOM 预防检查清单”是一份难得的最佳实践，极具参考和落地价值。

### [美团 LongCat 开源 General 365：树立推理评测新标尺](https://tech.meituan.com/2026/05/15/LongCat-General-365.html)

来源：美团 · 技术团队

发布时间：2026-06-09 11:28:51
![](https://p0.meituan.net/meituantechblog/e1f3bc5188020ba970529b35ff865bce131464.png)
**背景/问题**
当前主流大模型在数学、物理等专业学科推理评测中屡获高分，但在日常生活中却常表现出缺乏常识的“智力盲区”。这暴露了现有评测基准过度依赖专业知识记忆，而忽视了对模型真正通用逻辑推理能力的有效衡量。

**核心观点/方案**
美团 LongCat 团队开源了 General 365 评测基准。该基准严格将背景知识限定在 K-12 水平，彻底解耦了专业知识与推理能力，通过 365 道原创种子题及其变体，精准覆盖复杂约束、时空推理、语义干扰等八大通用逻辑维度。对 26 款主流大模型的实测显示，即便是 Gemini 3 Pro 准确率也仅有 62.8%，绝大多数模型不及格，且模型在“语义干扰”和“最优策略”上普遍表现糟糕。

**结论/价值**
General 365 像一面照妖镜，精准戳破了当前大模型依靠“死记硬背”带来的高分假象，清晰地勾勒出大模型在处理真实世界逻辑问题时的能力边界。这项研究对大模型的基础能力评估具有突破性意义，为追求 AGI 的算法研究员和模型开发者指明了下一阶段“逻辑进化”的优化方向，是极具前瞻性和工程价值的优秀基准。

### [用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践](https://tech.meituan.com/2026/05/07/Agent-AI-Coding.html)

来源：美团 · 技术团队

发布时间：2026-06-09 11:28:51
![](https://p0.meituan.net/meituantechblog/1c5fff78273feaf4892b46ad3fb757956195300.png)
**背景/问题**
在 AI 辅助编码全面普及的当下，缺乏统一规范约束的 AI 生成代码极易导致系统加速腐化。面对 31 万行且高速膨胀的复杂业务代码库，如何在不停止业务交付的前提下，完成工程架构的重构与技术债的治理，是当前软件工程管理面临的巨大挑战。

**核心观点/方案**
团队创新性地将 Agent 评测中“人人对齐->人机对齐”的思路引入 AI Coding 管理。先由专家圈定高危边界，利用 AI 穷举扫描代码隐患；接着制定统一规范并固化为 AI 编码工具的 Always 级 Rule，确保团队共识转化为机器约束；在执行阶段，采用“主R打样->SOP分发->全组并行”的策略，将技术债拆解为日常业务迭代的“顺带动作”进行渐进式重构；同时，建立 Pre-PR 机制和引入“高阶模型审查低阶模型”的交叉 CR 流程，打破了 AI 提效带来的 Code Review 瓶颈。

**结论/价值**
这是一篇极具实战价值和思想深度的软件工程管理指南，打破了“重构必须推倒重来或申请专项排期”的传统思维。文章深刻揭示了 AI 时代工程师的核心价值正在从“看全代码”向“判断重要性”转移。所有正在推行 AI Coding、面临技术债压力的技术 Leader 和架构师都应阅读此文，其总结的落地 SOP 和管理心法可直接复用于任何大型复杂系统的渐进式演进中。

### [Introducing Time Allowances](https://developer.apple.com/news/?id=0d2gpmml)

来源：Latest News - Apple Developer

发布时间：2026-06-09 02:19:33
![](https://devimages-cdn.apple.com/wwdc-services/articles/images/5799005A-1399-42D8-81F9-593CA4841F77/2048.jpeg)
**背景/问题**：苹果在最新的操作系统（iOS 27 等）中引入了名为 Time Allowances 的家长控制功能，以基于专家研究及年龄段提供更灵活的儿童使用时间管理方案。

**核心观点/方案**：苹果明确了应用在 Screen Time 中的分类规则：娱乐和游戏类别依据 App Store Connect 的设定划分；而社交媒体类别则基于应用是否包含分发、放大用户生成内容的社交能力来判定。从 2026 年 7 月起，开发者必须声明应用是否具备社交能力，若且未对 13 岁以下儿童禁用，最低年龄评级将升至 13+，且需调用 Declared Age Range API。

**结论/价值**：这是苹果生态内一次重要的合规政策更新。对涉及 UGC 社交功能的应用开发者具有极高的实务参考价值，需密切关注 2026 年下半年的合规节点并提前完成配置和更新，以免面临拒审或版本停滞风险。

### [Updated Apple Developer Program License Agreement and App Review Guidelines now available](https://developer.apple.com/news/?id=a233fmpw)

来源：Latest News - Apple Developer

发布时间：2026-06-09 02:18:33
![](https://developer.apple.com/news/images/og/apple-developer-og.png)
**背景/问题**：配合苹果生态的演进与新功能发布，苹果官方对开发者计划许可协议和 App Store 审核指南进行了例行修订，以适应全新的技术和监管要求。

**核心观点/方案**：协议更新明确了多项新 API（如敏感内容分析、信任等）的调用规范，并特别增加了针对机器大模型及 AI 技术的使用条款。审核指南方面，进一步强化了儿童与青少年安全合规指导，明确了开发者对违规内容处置的连带责任，并补充“灵动岛”Live Activities 严禁用于推送垃圾信息或网络钓鱼的红线。

**结论/价值**：条款修改直接涉及底层 API 和应用上架的红线机制，具有很高的参考价值。建议苹果生态的开发和产品团队仔细研读其中与 AI 模型调用及数据隐私相关的条款要求，及时调整产品逻辑规避审核风险。

## 💾 Daily Dev

### [在 Claude、Codex 和 Cursor 中使用 Xcode 27 的 Agent Skills](https://www.avanderlee.com/ai-development/using-xcode-27s-agent-skills-in-claude-codex-and-cursor/)

来源：iOS Development News - Telegram Channel

发布时间：2026-06-09 22:02:30
![](https://cdn4.telesco.pe/file/I4sDXOFWnK8HeTHkVP5xoXCN4eA-Dxqh7c_iIiMFPKn-R42Sq_qUH3uttqGmubp3ymrzL030hf5nhs7umEJU3Fh9rcFFxQjwfb36-w8_sxfRlEBveV5OLLGZgXjjrgqmzSNY9JJAVN7J6ghPROsTfK-iB9vbGpaycdOaKtT2v-Z5pnDhkyDtgNKQyrWVeU-Blpkw32RhVjzSfmpKol5IC7sFJx_mtDvgdg6IU0mqvH0eiR5D8Cdkxs5sX36XcTkesV-bsil2_IJYTJmIJpQ_tcJekqca4VM_hLymxDkkcLCvE4LXgLyWCaBydFWS7-Lb9BV1k2GazvWT9PyFdWHVug.jpg)
**背景/问题**：随着 AI 辅助编程的普及，开发者经常在不同 IDE（如 Cursor、Claude、Codex）中切换。Xcode 27 虽然引入了强大的官方 Agent Skills，但开发者面临着如何将这些官方最佳实践无缝迁移到日常使用的第三方 IDE 中以提高开发效率的问题。

**核心观点/方案**：文章介绍了一个通过 Xcode 27 新增的 CLI 工具 (`xcrun agent skills export`) 将官方 Agent Skills 导出至本地目录（`~/.agents/skills`）的方案。这使得 Cursor 等支持该目录规范的第三方 IDE 能够直接读取并应用苹果官方的 7 种 Skill（如 SwiftUI 最佳实践、测试现代化、安全审计等）。同时，文章详细解析了这些 Skill 的适用边界：纯处理源代码的 Skill 可在任意 IDE 正常工作，而涉及设备交互（如模拟器控制）或 Xcode 项目配置的 Skill 则会降级或失效。

**结论/价值**：该方案极大地打破了 IDE 壁垒，让开发者能够结合苹果的权威指导与第三方 AI 编程工具的便捷性。对于同时使用 Xcode 和 AI IDE 的 Apple 生态开发者来说，这是一篇极具实战指导意义的配置指南，能帮助他们迅速利用最新的 AI 工具链重构和优化代码。
