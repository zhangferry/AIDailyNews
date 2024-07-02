---
title: "Daily News #2024-07-02"
date: "2024-07-02 09:24:22"
description: "🤯 CocoaPods 漏洞暴露设备于恶意软件攻击
🎉 Swift 6 来了！编译时数据竞态安全检查
🎉 SwiftUI 滚动几何和位置视图修改器
⌛️ SwiftUI 生命周期管理：AppPhase API 提案
🇪🇺欧盟调查微软-OpenAI和谷歌-三星人工智能交易
🌟 IINA：macOS 上的现代视频播放器
💻 ImHex: 专为逆向工程师、程序员和重视视网膜健康的人设计的十六进制编辑器"
tags: 
- '工具'
- 'SwiftUI'
- '反垄断'
- 'macOS'
- '视频播放器'
- '欧盟'
- '安全漏洞'
- '人工智能'
- 'Swift'

---

> - 🤯 CocoaPods 漏洞暴露设备于恶意软件攻击
> - 🎉 Swift 6 来了！编译时数据竞态安全检查
> - 🎉 SwiftUI 滚动几何和位置视图修改器
> - ⌛️ SwiftUI 生命周期管理：AppPhase API 提案
> - 🇪🇺欧盟调查微软-OpenAI和谷歌-三星人工智能交易
> - 🌟 IINA：macOS 上的现代视频播放器
> - 💻 ImHex: 专为逆向工程师、程序员和重视视网膜健康的人设计的十六进制编辑器

## Apple News

### [🤯 CocoaPods 漏洞暴露设备于恶意软件攻击](https://www.darkreading.com/cloud-security/apple-cocoapods-bugs-expose-apps-code-injection)

来源：Hacker News - Newest: "apple"

发布时间：2024-07-01 22:45:05

CocoaPods 存在严重漏洞，导致数百万设备在过去十年中面临任意恶意软件攻击的风险。该漏洞与 RubyGem 中的一个远程代码执行漏洞有关，攻击者可以利用该漏洞在受影响设备上注入恶意代码。

## iOS Blog

### [🎉 Swift 6 来了！编译时数据竞态安全检查](https://swift.org/blog/ready-for-swift-6/)

来源：Swift.org

发布时间：2024-07-01 17:00:00
![](https://www.swift.org/assets/images/ready-for-swift-6-blog/packages-with-no-data-race-errors.png)
Swift 6 引入了编译时数据竞态安全检查，可以消除一类潜在的并发错误，提升代码安全性。文章介绍了 Swift 6 的数据竞态安全检查功能，以及如何跟踪 Swift 6 的普及进度。鼓励开发者更新自己的软件包，并关注 Swift Package Index 上的生态系统进展。

### [🎉 SwiftUI 滚动几何和位置视图修改器](https://augmentedcode.io/2024/07/01/scroll-geometry-and-position-view-modifiers-in-swiftui-on-ios-18/)

来源：Blog – Augmented Code

发布时间：2024-07-01 23:00:00

WWDC'24 更新了滚动功能，其中之一是 onScrollGeometryChange(for:of:action:)，我们可以用它来响应滚动几何变化。视图修改器有两个闭包，第一个闭包将滚动几何转换为我们喜欢的任意可等同类型。如果该值发生变化，则会调用操作闭包。

### [⌛️ SwiftUI 生命周期管理：AppPhase API 提案](https://fatbobman.com/zh/weekly/issue-038/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-07-01 22:00:00

自WWDC 2020起，SwiftUI引入了ScenePhase API，本文建议开发一个更全面的AppPhase API，以便于窗口场景事件分离，独立管理应用级的生命周期事件。作者指出，当前的ScenePhase API过度依赖窗口管理，未能全面覆盖应用状态的变化，特别是在macOS上表现不佳，而在iOS上虽表现更佳，但仍有改进空间。

## Tech News

### [🇪🇺欧盟调查微软-OpenAI和谷歌-三星人工智能交易](https://www.artificialintelligence-news.com/2024/07/01/eu-probes-microsoft-openai-and-google-samsung-ai-deals/)

来源：AI News

发布时间：2024-07-01 21:09:57

欧盟对人工智能交易加强了反垄断审查，从微软-OpenAI和谷歌-三星之间的备受瞩目的合作开始。欧盟委员会负责竞争政策的执行副主席玛格丽特·维斯塔格警告称，人工智能正在“以惊人的速度发展”，并透露正在对各种人工智能相关市场行为进行多项初步调查。

## Daily Code

### [🌟 IINA：macOS 上的现代视频播放器](https://github.com/iina/iina)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-07-02 07:18:28

IINA 是一款专为 macOS 设计的现代视频播放器，基于 mpv 构建，拥有出色的解码能力。它提供了视频和音乐所需的所有功能，包括字幕、播放列表、章节等。此外，它还支持 Force Touch、画中画和高级 Touch Bar，并具有可自定义的用户界面和键盘、鼠标、触控板和手势控制。

### [💻 ImHex: 专为逆向工程师、程序员和重视视网膜健康的人设计的十六进制编辑器](https://github.com/WerWolv/ImHex)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-07-02 08:22:54

ImHex 是一款功能强大的十六进制查看器，专为逆向工程师、程序员和重视视网膜健康的人设计。它具有许多功能，包括字节修补、补丁管理、无限撤消/重做、多种数据类型显示、自定义 C++ 类似模式语言用于解析和突出显示文件内容、主题支持、导入和导出数据、数据检查器、基于节点的数据预处理器、从许多不同数据源加载数据、数据搜索、数据哈希支持、差异支持、集成反汇编器、书签、功能强大的数据分析器和可视化器、YARA 规则支持、有用的工具、内置内容更新器、现代界面、易于上手。
