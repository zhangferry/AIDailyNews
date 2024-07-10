---
title: "Daily News #2024-07-10"
date: "2024-07-10 09:25:41"
description: "🍎 Apple 操作系统的开源根源：macOS 和 iOS 背后的 BSD 传承
🎉在 Apple Silicon Mac 上运行 Ubuntu Linux
🎉Apple Arcade 8 月新游来袭！
🧐 Xcode 模拟器中检查网络流量
🎉 SwiftUI 中的 Entry 宏介绍
🔒 增强推送保护的秘密扫描绕过控制
🎉 SenseTime发布SenseNova 5.5：中国首个实时多模态AI模型
WhisperKit: 🗣️ Integrate OpenAI's Whisper speech recognition model with Apple's CoreML framework"
tags: 
- 'CoreML'
- 'SwiftUI'
- 'AI模型'
- '游戏'
- '虚拟机'
- 'Speech Recognition'
- 'GitHub Security'
- 'Xcode'
- '技术'
- 'Swift'

---

> - 🍎 Apple 操作系统的开源根源：macOS 和 iOS 背后的 BSD 传承
> - 🎉在 Apple Silicon Mac 上运行 Ubuntu Linux
> - 🎉Apple Arcade 8 月新游来袭！
> - 🧐 Xcode 模拟器中检查网络流量
> - 🎉 SwiftUI 中的 Entry 宏介绍
> - 🔒 增强推送保护的秘密扫描绕过控制
> - 🎉 SenseTime发布SenseNova 5.5：中国首个实时多模态AI模型
> - WhisperKit: 🗣️ Integrate OpenAI's Whisper speech recognition model with Apple's CoreML framework

## Apple News

### [🍎 Apple 操作系统的开源根源：macOS 和 iOS 背后的 BSD 传承](https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/)

来源：Hacker News - Newest: "apple"

发布时间：2024-07-09 01:40:15

尽管人们经常声称 Apple 的 macOS、iOS、iPadOS、watchOS、visionOS 和 tvOS 直接源自 FreeBSD，但这实际上是一个误解。这些操作系统的真正基础在于 Apple 较旧的操作系统技术与 NeXTSTEP 的结合，后者本身是 Mach 和 BSD 的混合体，早于 FreeBSD。虽然多年来这些操作系统中加入了一些 FreeBSD 用户空间元素，但 Apple 内核 (XNU) 并不直接源自 FreeBSD。然而，它们确实共享一个共同的 BSD 传统。

### [🎉在 Apple Silicon Mac 上运行 Ubuntu Linux](https://osxdaily.com/2024/07/08/how-to-run-ubuntu-linux-on-apple-silicon-mac/)

来源：OS X Daily

发布时间：2024-07-09 01:46:23

在 Apple Silicon Mac 上运行 Ubuntu Linux 变得非常简单，无需分区、安装、双启动或丢失 Mac 操作系统。借助虚拟机，您可以轻松地在 MacOS 旁边运行 Ubuntu。

### [🎉Apple Arcade 8 月新游来袭！](https://www.apple.com/newsroom/2024/07/three-new-games-come-to-apple-arcade-in-august-including-temple-run-legends/)

来源：Apple Newsroom

发布时间：2024-07-09 21:59:09

Apple Arcade 将于 8 月迎来三款新游戏：Temple Run: Legends、Vampire Survivors+ 和 Castle Crumble。Temple Run: Legends 是该系列首款基于关卡的跑酷游戏，将于 8 月 1 日独家登陆 Apple Arcade。屡获殊荣的 Vampire Survivors+ 也将加入该服务，最多支持同一设备上的四人游戏。而 Apple Vision Pro 用户则可以在 8 月 29 日体验 Castle Crumble 的空间版本，在任何他们想要的物理空间中用手指轻扫和轻弹来拆除奇幻城堡。

## iOS Blog

### [🧐 Xcode 模拟器中检查网络流量](https://www.avanderlee.com/xcode/inspect-network-traffic-simulator/)

来源：SwiftLee

发布时间：2024-07-09 07:00:00

检查网络流量是应用程序开发人员的一项基本技能。有许多工具允许您监视进出应用程序的请求，每个工具都有其优点和缺点。在构建应用程序时，您可能会执行网络调用以获取视图的数据。无论您是在调试请求失败还是希望验证...

### [🎉 SwiftUI 中的 Entry 宏介绍](https://swiftwithmajid.com/2024/07/09/introducing-entry-macro-in-swiftui/)

来源：Swift with Majid

发布时间：2024-07-09 08:00:00

Swift 宏功能去年在社区和苹果内部变得非常流行。因此，SwiftUI 框架引入了一组宏类型，帮助我们减少了代码库中的样板。本周，我们将讨论 Entry 宏类型。

## Tech News

### [🔒 增强推送保护的秘密扫描绕过控制](https://github.blog/changelog/2024-07-08-secret-scanning-bypass-controls-for-push-protection-covers-pushes-from-the-web-file-editor)

来源：Changelogs Archive - The GitHub Blog

发布时间：2024-07-09 04:07:54

GitHub 博客宣布增强了推送保护的秘密扫描绕过控制，以涵盖通过 Web 文件编辑器进行的推送。此更新有助于防止意外泄露敏感信息，并提高代码库的安全性。

### [🎉 SenseTime发布SenseNova 5.5：中国首个实时多模态AI模型](https://www.artificialintelligence-news.com/2024/07/09/sensetime-sensenova-china-real-time-multimodal-ai-model/)

来源：AI News

发布时间：2024-07-09 22:06:23

SenseTime发布了SenseNova 5.5，这是其LLM的增强版本，其中包括SenseNova 5o，号称是中国首个实时多模态模型。SenseNova 5o代表了AI交互的飞跃，提供了与GPT-4o的流交互功能相当的能力。这一进步使用户能够以类似于与人交谈的方式与模型进行交互。

## Daily Code

### [WhisperKit: 🗣️ Integrate OpenAI's Whisper speech recognition model with Apple's CoreML framework](https://github.com/argmaxinc/WhisperKit)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-07-10 09:00:05

WhisperKit 是一个 Swift 包，它将 OpenAI 流行耳语语音识别模型与 Apple 的 CoreML 框架集成在一起，以便在 Apple 设备上进行高效的本地推理。WhisperKit 可以使用 Swift 包管理器集成到您的 Swift 项目中。要开始使用 WhisperKit，您需要在项目中初始化它。WhisperKit 会自动下载推荐的设备模型（如果未指定）。您还可以通过传入模型名称来选择特定模型。此方法还支持 glob 搜索，因此您可以使用通配符来选择模型。WhisperKit 还附带支持库，它允许您创建和部署自己的精细调整的 Whisper 版本，采用 CoreML 格式，以 HuggingFace。一旦生成，只需将存储库名称更改为用于上传模型的名称，即可加载它们。
