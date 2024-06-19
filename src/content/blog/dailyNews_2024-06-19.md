---
title: "Daily News #2024-06-19"
date: "2024-06-19 09:23:57"
description: "🛠️ Apple II 的基于 ROM 的 March-U RAM 测试
🎉 Apple Vision Pro 即将登陆更多地区！
🌟苹果开发者学院为所有学生和校友推出人工智能培训
🌟苹果发布 iOS 17.6、macOS Sonoma 14.6、iPadOS 17.6 测试版
🛡️ App Store 为儿童提供更安全的保障
🌟Swift 6：逐步迁移你的 Xcode 项目和包
NVIDIA 视觉 AI 最新进展
The Composable Architecture 🧩
✨ LibreChat：多模态 AI 对话的新时代"
tags: 
- 'iPadOS'
- 'AI'
- '人工智能'
- 'App Store 安全'
- 'State Management'
- 'macOS'
- '计算机视觉'
- 'iOS'
- 'Apple Vision Pro'
- 'Swift'
- '技术'

---

> - 🛠️ Apple II 的基于 ROM 的 March-U RAM 测试
> - 🎉 Apple Vision Pro 即将登陆更多地区！
> - 🌟苹果开发者学院为所有学生和校友推出人工智能培训
> - 🌟苹果发布 iOS 17.6、macOS Sonoma 14.6、iPadOS 17.6 测试版
> - 🛡️ App Store 为儿童提供更安全的保障
> - 🌟Swift 6：逐步迁移你的 Xcode 项目和包
> - NVIDIA 视觉 AI 最新进展
> - The Composable Architecture 🧩
> - ✨ LibreChat：多模态 AI 对话的新时代

## Apple News

### [🛠️ Apple II 的基于 ROM 的 March-U RAM 测试](https://github.com/misterblack1/appleII_deadtest)

来源：Hacker News - Newest: "apple"

发布时间：2024-06-18 23:32:38

这个 ROM 旨在测试 Apple II 的 RAM，而无需使用 RAM。它最初是由 Frank 开发的快速测试 ROM，用于在文本模式下显示满屏字符，所有这些都不使用零页。然后，作者希望做更多的事情，所以他找到了世界 Janni 上的 C64 “Dead Test” ROM 的反汇编代码，并将其移植到了 Apple II。他不得不调整该 ROM 初始阶段的功能以适用于 Apple II，但它实际上即使使用他有限的汇编技能也能工作。使此测试如此出色的主要原因是它根本不依赖 DRAM。它完全在 ROM 内运行，不使用零页（$00-$FF）或堆栈（$100-$1FF）。

### [🎉 Apple Vision Pro 即将登陆更多地区！](https://developer.apple.com/news/?id=is9ltg6s)

来源：Latest News - Apple Developer

发布时间：2024-06-18 18:00:46

Apple Vision Pro 将于 6 月 28 日在中国大陆、香港、日本和新加坡推出，并于 7 月 12 日在澳大利亚、加拿大、法国、德国和英国推出。你的应用和游戏将自动在 App Store 中你选择的地区提供。

### [🌟苹果开发者学院为所有学生和校友推出人工智能培训](https://www.apple.com/newsroom/2024/06/apple-developer-academy-introduces-ai-training-for-all-students-and-alumni/)

来源：Apple Newsroom

发布时间：2024-06-18 21:00:04

苹果开发者学院宣布将为所有学生和导师提供人工智能（AI）技术和工具培训。新核心课程将从今年秋季开始提供给六个国家 18 所开发者学院的数千名学生和校友，以增加开发者、设计师和企业家在不断增长的 iOS 应用程序经济及其他领域开启职业生涯的机会。

### [🌟苹果发布 iOS 17.6、macOS Sonoma 14.6、iPadOS 17.6 测试版](https://osxdaily.com/2024/06/17/beta-1-of-ios-17-6-macos-sonoma-14-6-ipados-17-6-released-for-testing/)

来源：OS X Daily

发布时间：2024-06-18 04:46:35

苹果发布了 iOS 17.6、macOS Sonoma 14.6、iPadOS 17.6 的第一个测试版，为现有 iOS 和 macOS 版本的即将到来的系统更新继续进行测试。

### [🛡️ App Store 为儿童提供更安全的保障](https://developer.apple.com/news/?id=7byvco78)

来源：Latest News - Apple Developer

发布时间：2024-06-18 17:06:41

在未来几个月内，你需要在 App Store Connect 中注明你的应用是否包含可供购买的战利品箱。此外，基于当地法律的区域年龄分级将自动显示在澳大利亚和韩国 App Store 上下列应用的产品页面上。无需执行其他操作。区域年龄分级显示在 Apple 全球年龄分级之外。

## iOS Blog

### [🌟Swift 6：逐步迁移你的 Xcode 项目和包](https://www.avanderlee.com/concurrency/swift-6-migrating-xcode-projects-packages/)

来源：SwiftLee

发布时间：2024-06-18 16:56:49

Swift 6 作为其编程语言的主要版本，于 WWDC 2024 年发布。它旨在创造一种奇妙的开发体验，我们今天所知的许多最新功能都是朝着这个主要版本迈进的一部分。Swift 开发团队分享了他们 2023 年的重点领域，并发布了 ...

## Tech News

### [NVIDIA 视觉 AI 最新进展](https://www.artificialintelligence-news.com/2024/06/17/nvidia-presents-latest-advancements-visual-ai/)

来源：AI News

发布时间：2024-06-18 00:05:03

NVIDIA 研究人员在西雅图举行的计算机视觉和模式识别 (CVPR) 会议上展示了新的视觉生成 AI 模型和技术。这些进展涵盖了自定义图像生成、3D 场景编辑、视觉语言理解和自动驾驶感知等领域。

## Daily Code

### [The Composable Architecture 🧩](https://github.com/pointfreeco/swift-composable-architecture)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-06-19 08:32:33

The Composable Architecture (TCA) 是一个用于以一致且易于理解的方式构建应用程序的库，同时考虑了组合、测试和人体工程学。它可以在 SwiftUI、UIKit 等中使用，并且可以在任何 Apple 平台（iOS、macOS、visionOS、tvOS 和 watchOS）上使用。

### [✨ LibreChat：多模态 AI 对话的新时代](https://github.com/danny-avila/LibreChat)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-06-19 09:02:47

LibreChat 是一款功能强大的聊天机器人平台，它将 ChatGPT 的未来与 OpenAI 的革命性技术相结合。它允许您集成多个 AI 模型，并增强原始客户端功能，如对话和消息搜索、提示模板和插件。告别 ChatGPT Plus，使用免费或按次付费的 API。
