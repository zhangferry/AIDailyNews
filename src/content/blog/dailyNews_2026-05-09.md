---
title: "Daily News #2026-05-09"
date: "2026-05-09 23:44:07"
description: >
  新华三于英涛：在AI的亢奋与焦虑中做时代的筑基者 苹果更新巴西 App Store 博彩应用上架政策 Apple 发布 iOS 26.5 及 iPadOS 26.5 RC 2 测试版更新 我与 AI 编程代理的外循环工作流 SDWebImageAVIFCoder
tags:
- "软件工程"
- "Apple"
- "新华三"
- "编解码"
- "企业战略"
- "政策更新"
- "大模型"
- "巴西"
- "iOS"
- "系统更新"
- "AVIF"
- "图像处理"
- "AI"
- "合规"
- "Swift"
- "工作流"
- "App Store"
- "架构"
- "iPadOS"
- "AI基础设施"
- "SDWebImage"

---

> - 新华三于英涛：在AI的亢奋与焦虑中做时代的筑基者
> - 苹果更新巴西 App Store 博彩应用上架政策
> - Apple 发布 iOS 26.5 及 iPadOS 26.5 RC 2 测试版更新
> - 我与 AI 编程代理的外循环工作流
> - SDWebImageAVIFCoder

## 📥 Tech News

### [新华三于英涛：在AI的亢奋与焦虑中做时代的筑基者](https://www.infoq.cn/article/QEu6wrKMO0ADmCUUakBm)

来源：InfoQ 推荐

发布时间：2026-05-09 18:19:41

面对AI行业普遍存在的亢奋与焦虑，新华三提出应做智能时代的“筑基者”。文章指出行业面临三大命题：Token经济正在重塑产出价值、AI自主权是生存挑战、系统瓶颈比单点算力更关键。为此，新华三发布涵盖“算、网、存、云、安、维”六大维度的全栈新品，推出UniPoD S80000超节点平台，通过软硬协同解决算力损耗与效率问题。此外，公司还构建“图灵小镇”与“芯模社区”推动产业落地，强调以全栈协同和精耕务实应对AI时代的结构性挑战。

### [苹果更新巴西 App Store 博彩应用上架政策](https://developer.apple.com/news/?id=x4eyetnp)

来源：Latest News - Apple Developer

发布时间：2026-05-09 00:30:46

针对巴西固定赔率博彩法规的变更，苹果调整了 App Store 的分发政策，现在允许拥有巴西 Secretariat of Prizes and Bets (SPA) 有效许可的固定赔率博彩应用上架。核心方案要求开发者必须提交新的应用版本以触发许可证验证流程，并在 App Review Information 中填写许可证详情及附件。凡包含此类功能的应用，其在巴西的年龄评级将自动变为 A18。此次更新明确了博彩应用进入巴西市场的合规门槛，开发者需确保应用符合所有披露、年龄限制及风险警告的法律要求，必要时需咨询法律顾问以确保合规。

### [Apple 发布 iOS 26.5 及 iPadOS 26.5 RC 2 测试版更新](https://t.me/AppleNuts/2425)

来源： Apple Nuts - Telegram Channel

发布时间：2026-05-09 01:50:25

Apple 正在持续推进其移动操作系统的迭代，向相关用户推送了新的测试版软件更新。此次发布的重点在于 iOS 26.5 RC 2 和 iPadOS 26.5 RC 2，构建号均为 23F77。RC（Release Candidate）版本通常被视为正式版发布前的最后环节，主要用于收集关键错误反馈并进行最终的系统稳定性打磨。对于开发者而言，这一版本是验证应用兼容性的关键节点；对于普通测试用户，这意味着体验相对稳定的新特性的机会。总体而言，此次更新是软件生命周期中的常规流程，预示着正式版本即将面向公众发布。

## 💾 Daily Dev

### [我与 AI 编程代理的外循环工作流](https://www.cocoanetics.com/2026/05/my-outer-loop/)

来源：iOS Development News - Telegram Channel

发布时间：2026-05-09 16:37:32

文章深入探讨了在长期使用 AI 编程代理后，资深工程师工作模式的根本性转变：从具体的代码编写者升级为宏观架构的“愿景家”。作者详细描述了其“外循环”工作流，即由人类工程师构思项目蓝图和验收标准，后续的文档撰写、代码实现、测试及 PR 审查全权交由 AI 代理执行。文章通过 SwiftBash、SwiftScript 等四个项目在周末快速整合为统一 ShellKit 基座的实战案例，详细展示了该模式如何利用 AI 处理跨平台兼容性等繁琐任务。虽然目前仍面临人工介入不及时和 CI 构建缓慢等协调性挑战，但这一实践极具前瞻性地揭示了未来软件工程的核心价值将在于对系统复杂度的审美把控与架构决策，而非机械的实现细节。

### [SDWebImageAVIFCoder](https://github.com/SDWebImage/SDWebImageAVIFCoder)

来源：iOS Development News - Telegram Channel

发布时间：2026-05-09 10:12:26

SDWebImageAVIFCoder 是 SDWebImage 的一个插件组件，旨在为 iOS 和 macOS 应用添加 AV1 图像文件格式（AVIF）的支持。该插件基于 libavif 编解码库构建，不仅支持基本的 AVIF 静态与序列图像解码，还兼容 Alpha 通道、HDR 图像以及动画功能。为了适应不同场景的性能需求，它允许开发者通过 CocoaPods 选择底层 AV1 编解码器，如针对速度优化的 dav1d 解码器和针对编码效率优化的 rav1e。此外，该插件还支持缩略图编解码及运行时编解码器选择。该工具极大降低了开发者在 Apple 平台集成 AVIF 格式的门槛，通过简单的 API 即可实现高效加载与编码，有助于提升应用的图片加载性能并节省带宽。
