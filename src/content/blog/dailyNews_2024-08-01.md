---
title: "Daily News #2024-08-01"
date: "2024-08-01 09:40:05"
description: "🧠 脑机接口与 Apple Vision Pro
✨ macOS Sonoma 14.6 更新发布，修复错误并更新安全性
🌟 SwiftUI 图片平铺技巧
解决 Swift 中并发执行代码中对捕获变量的引用
七月技术新知：移动麻将、安卓上的收割者、自动优化图片
🍎苹果选择谷歌芯片用于人工智能基础设施，绕过英伟达
🎉 GitHub 仓库更新 7 月 31 日
👍 Composable Architecture: 构建应用的利器
🌟 DiceDB：基于 SQL 的实时响应式 Redis 替代品"
tags: 
- '技术'
- 'SwiftUI'
- '脑机接口'
- '人工智能硬件'
- 'Swift'
- 'GitHub'
- '数据库'
- 'Redis'
- 'macOS'
- 'SQL'
- '技术资讯'
- 'Apple Vision Pro'

---

> - 🧠 脑机接口与 Apple Vision Pro
> - ✨ macOS Sonoma 14.6 更新发布，修复错误并更新安全性
> - 🌟 SwiftUI 图片平铺技巧
> - 解决 Swift 中并发执行代码中对捕获变量的引用
> - 七月技术新知：移动麻将、安卓上的收割者、自动优化图片
> - 🍎苹果选择谷歌芯片用于人工智能基础设施，绕过英伟达
> - 🎉 GitHub 仓库更新 7 月 31 日
> - 👍 Composable Architecture: 构建应用的利器
> - 🌟 DiceDB：基于 SQL 的实时响应式 Redis 替代品

## Apple News

### [🧠 脑机接口与 Apple Vision Pro](https://www.businesswire.com/news/home/20240730923591/en/Synchron-Announces-First-Use-of-Apple-Vision-Pro-with-a-Brain-Computer-Interface)

来源：Hacker News - Newest: "apple"

发布时间：2024-07-31 14:01:35

文章报道了 Synchron 公司首次将 Apple Vision Pro 与脑机接口结合使用，使瘫痪患者能够通过大脑控制来选择项目，无需手势或语音。

### [✨ macOS Sonoma 14.6 更新发布，修复错误并更新安全性](https://osxdaily.com/2024/07/30/macos-sonoma-14-6-update-released-with-bug-fixes-security-updates/)

来源：OS X Daily

发布时间：2024-07-31 06:42:09

macOS Sonoma 14.6 主要专注于大多数 Mac 的错误修复和安全更新，但它确实包含一个专门针对 14 英寸 M3 MacBook Pro 系列的不错的新功能，允许该 Mac 支持两个外部显示器。

## iOS Blog

### [🌟 SwiftUI 图片平铺技巧](https://fatbobman.com/zh/posts/how-to-tile-images-in-swiftui/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-07-31 22:20:00

本文介绍了 SwiftUI 中图片平铺的两种实现方式：使用 resizable 修饰符和使用 foregroundStyle + ImagePaint。前者兼容性好但限制较多，后者更符合 SwiftUI 直觉且控制能力更强。此外，文章还探讨了使用自定义 Image 来平铺 SF Symbol 的方法，展示了 SwiftUI 的潜力和灵活性。

### [解决 Swift 中并发执行代码中对捕获变量的引用](https://www.donnywals.com/solving-reference-to-captured-var-in-concurrently-executing-code-in-swift/)

来源：Donny Wals

发布时间：2024-07-31 22:42:57

在 Swift 6 严格并发模式下，可能会遇到“并发执行代码中对捕获变量的引用”警告。这表示在异步运行的代码块中捕获了一个变量。为了解决此问题，可以将变量声明为常量或在完成闭包中进行显式捕获。

### [七月技术新知：移动麻将、安卓上的收割者、自动优化图片](https://www.emergetools.com/newsletter/july-2024)

来源：Emerge Tools Blog

发布时间：2024-07-31 23:45:00

本期技术新知涵盖了移动麻将、安卓上的收割者和自动优化图片等内容，为技术爱好者提供了丰富的资讯。

## Tech News

### [🍎苹果选择谷歌芯片用于人工智能基础设施，绕过英伟达](https://www.artificialintelligence-news.com/news/apple-opts-google-chips-ai-infrastructure-sidestepping-nvidia/)

来源：AI News

发布时间：2024-07-31 19:16:34

据周一发布的一份报告披露，苹果公司放弃了行业领导者英伟达，转而采用谷歌设计的芯片。苹果不会为其人工智能软件基础设施采用英伟达的 GPU，而是将谷歌芯片作为即将推出的与人工智能相关的功能和工具的基石。苹果选择谷歌芯片这一事实表明，该公司正在寻求减少对英伟达的依赖，并加强其在人工智能领域的内部能力。

### [🎉 GitHub 仓库更新 7 月 31 日](https://github.blog/changelog/2024-07-31-repository-updates-july-31st-2024)

来源：Changelogs Archive - The GitHub Blog

发布时间：2024-07-31 23:30:12

GitHub 仓库更新 7 月 31 日，主要更新内容包括：
- 仓库现在可以包含多达 100GB 的文件。
- 仓库现在可以包含多达 100 万个文件。

## Daily Code

### [👍 Composable Architecture: 构建应用的利器](https://github.com/pointfreeco/swift-composable-architecture)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-08-01 07:17:06

Composable Architecture 是一个用于构建应用程序的库，它以一致且易于理解的方式进行设计，同时兼顾了可组合性、可测试性和人体工程学。它可以在 SwiftUI、UIKit 等框架中使用，并且适用于任何 Apple 平台（iOS、macOS、visionOS、tvOS 和 watchOS）。

### [🌟 DiceDB：基于 SQL 的实时响应式 Redis 替代品](https://github.com/DiceDB/dice)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-08-01 07:05:45

DiceDB 是一款基于 SQL 的实时响应式 Redis 替代品，它支持多线程和无共享架构，并提供了一个名为 `listen` 的新命令，允许客户端监听 SQL 查询并在发生更改时实时收到通知。
