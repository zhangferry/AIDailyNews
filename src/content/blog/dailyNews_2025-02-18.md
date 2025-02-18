---
title: "Daily News #2025-02-18"
date: "2025-02-18 23:18:50"
description: "用 Swift 实现跨平台开发：迈向 Android 的可能性
深入Swift并发：让任务让步与去抖动
微软推出全新数据迁移应用
金融时报订阅服务的深度探讨
SwifterSwift: 超过500个Swift扩展工具
Syncthing: macOS上的本地同步解决方案
Swift并发中的任务取消
掌握SwiftUI滚动：实现自定义分页
战火之外：俄乌战争下的社会现状与人性"
tags: 
- "订阅服务"
- "Windows 11"
- "战争"
- "社会观察"
- "并发"
- "Swift"
- "任务取消"
- "SwiftUI"
- "分页"
- "跨平台"
- "滚动控制"
- "编程工具"
- "同步工具"
- "开发"

---

> - 用 Swift 实现跨平台开发：迈向 Android 的可能性
> - 深入Swift并发：让任务让步与去抖动
> - 微软推出全新数据迁移应用
> - 金融时报订阅服务的深度探讨
> - SwifterSwift: 超过500个Swift扩展工具
> - Syncthing: macOS上的本地同步解决方案
> - Swift并发中的任务取消
> - 掌握SwiftUI滚动：实现自定义分页
> - 战火之外：俄乌战争下的社会现状与人性

## 🍎 iOS Blog

### [用 Swift 实现跨平台开发：迈向 Android 的可能性](https://fatbobman.com/zh/weekly/issue-071/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2025-02-18 22:00:00

Swift 社区成立了 Swift on Android Community Workgroup，旨在推动 Swift 在 Android 平台的应用，标志着跨平台开发的重要一步。对于熟悉苹果生态的开发者而言，这是一项令人期待的尝试。然而，Swift 的基础设施与苹果平台息息相关，要实现真正的跨平台还需构建无关平台的 API 体系。开源社区如 OpenSwiftUI 和 Point-Free 团队正为此贡献力量，但技术和生态的挑战依然存在。苹果进一步开放相关框架，将助于 Swift 成为“世界的语言”，推动开发者社区的创新和发展。

### [深入Swift并发：让任务让步与去抖动](https://swiftwithmajid.com/2025/02/18/yielding-and-debouncing-in-swift-concurrency/)

来源：Swift with Majid

发布时间：2025-02-18 08:00:00

本文继续探讨Swift并发的主题，重点介绍任务让步（yielding）和去抖动（debouncing）的相关知识。文章指出，Swift并发语言特性提供了两个简单而强大的功能：yield和sleep。作者将阐明如何以及何时使用这些功能，以便更好地管理并发任务，提升代码的执行效率和响应性。

## 📥 Tech News

### [微软推出全新数据迁移应用](https://www.v2ex.com/t/1112456)

来源：V2EX-最新主题

发布时间：2025-02-18 23:12:10

微软正在开发一款全新的数据迁移应用程序，意图简化Windows 11用户在更换设备时的数据转移。这款工具利用OneDrive与近场WiFi特性，支持通过一次性密码实现设备间配对与数据传输，功能非常实用。

### [金融时报订阅服务的深度探讨](https://www.ft.com/content/d46e0faa-33f2-41a5-9c09-3957b0deac6f)

来源：Hacker News - Newest: "apple"

发布时间：2025-02-18 15:58:13

本文介绍了金融时报的订阅服务，强调了超过百万读者选择付费阅读的原因，突出了其内容的高价值和独特性。然而，文章内容较为简略，缺乏具体的服务细节和读者反馈，适合对FT服务有初步了解的读者。

## 💾 Daily Dev

### [SwifterSwift: 超过500个Swift扩展工具](https://github.com/SwifterSwift/SwifterSwift)

来源：iOS Development News - Telegram Channel

发布时间：2025-02-18 10:12:48

SwifterSwift是一个集合了500多个Swift原生扩展的库，旨在为iOS、macOS及其他平台提升开发效率。该库包含便利方法、语法糖及性能改进，分别适用于标准库、UIKit等多种类。支持主流的集成方式（CocoaPods、Carthage等），是Swift开发者提升代码质量和生产力的强大助手。

### [Syncthing: macOS上的本地同步解决方案](https://github.com/syncthing/syncthing-macos)

来源：iOS Development News - Telegram Channel

发布时间：2025-02-18 10:17:32

Syncthing-macos是一个为macOS量身打造的本地同步工具，通过简单的系统托盘应用为用户提供更友好的使用体验。此应用程序集成了Syncthing的后台进程，实现了一键访问Syncthing WebGUI、托盘状态指示和自动更新等功能。支持OS X 10.13及以上版本，用户体验良好，符合Apple的人机界面指南。

### [Swift并发中的任务取消](https://t.me/iosdevio/5889)

来源：iOS dev - Telegram Channel

发布时间：2025-02-18 19:28:07

文章介绍了Swift并发提供的合作式任务取消模型。通过学习如何使用此模型，开发者可以更好地处理任务的取消，提升程序的响应性与效率。文章强调了良好的编程习惯，以便正当地处理任务取消，确保应用的稳定性。

### [掌握SwiftUI滚动：实现自定义分页](https://t.me/iosdevio/5890)

来源：iOS dev - Telegram Channel

发布时间：2025-02-18 19:28:11

本文探讨了SwiftUI中的滚动目标行为，虽然可以提供精确的滚动控制，但在横屏模式下默认分页存在对齐问题。作者实现了一种自定义的ScrollTargetBehavior，以保证分页的完美对齐，适合需要高精度滚动体验的开发者。

## 📻 Podcast

### [战火之外：俄乌战争下的社会现状与人性](https://www.xiaoyuzhoufm.com/episode/67b451b105a90dfd0d437b3b)

来源：忽左忽右

发布时间：2025-02-18 17:45:31

在此次节目录中，公爵与汪伦宇回顾了自俄乌战争爆发以来的三年，重点探讨了战争背后的社会变化及普通人的生活现状。他们深入到基辅及其他地区，记录了记者群解散后的不安、乌克兰民众的分化心理以及两国新常态的出现。此外，也分析了物价上涨对社会的影响，特别是在俄罗斯观察中提到的国际教育资源的缺失等问题。整个节目通过不同角度折射出战争对人们生活的深刻影响，让听众更全面地理解这一时局。
