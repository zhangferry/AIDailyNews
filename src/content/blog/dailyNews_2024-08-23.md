---
title: "Daily News #2024-08-23"
date: "2024-08-23 09:29:05"
description: "💻史蒂夫·乔布斯 Apple-1 电脑即将拍卖，预计创下天价
🎉 苹果遵守欧盟数字市场法案，iOS 18 将允许用户删除内置应用
🎮Netflix 正在做 Apple Arcade 本该做的事
🌟 如何设置 SPM 包的 Swift 语言模式
🤯 NSPasteboard 崩溃：处理文件 Promise 时内部并发内存突变不安全
🔥Meta推出Llama 3：功能强大的开源LLM
《黑神话：悟空》游玩体验：美轮美奂的西游世界
🎮抗日题材游戏《黑鹄》引发讨论
时间不贫困：如何便捷、准确地记录自己的一天
🎮《黑神话：悟空》Steam同时在线游玩人数突破241万人
🌟Shire 0.5 发布：融合本地研发资产，构建数据安全 RAG
⚡️ uv: 极速 Python 包和项目管理器"
tags: 
- 'Python'
- 'iOS'
- '人工智能'
- 'Apple-1'
- '游戏'
- '黑神话：悟空'
- '数据安全'
- '时间管理'
- 'Swift'
- '效率'
- 'Netflix'
- 'iOS 18'

---

> - 💻史蒂夫·乔布斯 Apple-1 电脑即将拍卖，预计创下天价
> - 🎉 苹果遵守欧盟数字市场法案，iOS 18 将允许用户删除内置应用
> - 🎮Netflix 正在做 Apple Arcade 本该做的事
> - 🌟 如何设置 SPM 包的 Swift 语言模式
> - 🤯 NSPasteboard 崩溃：处理文件 Promise 时内部并发内存突变不安全
> - 🔥Meta推出Llama 3：功能强大的开源LLM
> - 《黑神话：悟空》游玩体验：美轮美奂的西游世界
> - 🎮抗日题材游戏《黑鹄》引发讨论
> - 时间不贫困：如何便捷、准确地记录自己的一天
> - 🎮《黑神话：悟空》Steam同时在线游玩人数突破241万人
> - 🌟Shire 0.5 发布：融合本地研发资产，构建数据安全 RAG
> - ⚡️ uv: 极速 Python 包和项目管理器

## Apple News

### [💻史蒂夫·乔布斯 Apple-1 电脑即将拍卖，预计创下天价](https://newatlas.com/technology/steve-jobs-apple-1-auction/)

来源：Hacker News - Newest: "apple"

发布时间：2024-08-22 08:19:43

史蒂夫·乔布斯曾经使用过的 Apple-1 电脑将于 9 月 12 日在纽约佳士得拍卖行拍卖。由于乔布斯的影响力、Apple-1 的稀有性以及保罗·艾伦收藏的加持，这台电脑预计将拍出天价。

### [🎉 苹果遵守欧盟数字市场法案，iOS 18 将允许用户删除内置应用](https://developer.apple.com/news/?id=zglax7gc)

来源：Latest News - Apple Developer

发布时间：2024-08-22 22:00:36

苹果宣布，为了遵守欧盟数字市场法案，iOS 18 将允许用户删除内置应用，包括 App Store、信息、照片、相机和 Safari。此外，用户还可以在设置中选择默认应用，包括拨号、发短信、翻译、导航、密码管理、键盘和呼叫垃圾邮件过滤器。

### [🎮Netflix 正在做 Apple Arcade 本该做的事](https://daringfireball.net/linked/2024/08/21/monument-valley-3-netflix)

来源：Hacker News - Newest: "apple"

发布时间：2024-08-22 20:43:42

Netflix 正在通过其游戏订阅服务提供高质量的游戏，而 Apple Arcade 却未能达到预期。游戏开发者对 Apple 严格的合作条件感到不满，导致 Apple Arcade 难以取得成功。

## iOS Blog

### [🌟 如何设置 SPM 包的 Swift 语言模式](https://www.donnywals.com/setting-the-swift-language-mode-for-an-spm-package/)

来源：Donny Wals

发布时间：2024-08-22 01:59:32

在 Xcode 16 中创建新的 Swift 包时，Package.swift 内容可能如下所示：

Package.swift
// swift-tools-version: 6.0
// swift-tools-version 声明构建此包所需的最低 Swift 版本。

import PackageDescription

let package = Package(
    name: "AppCore",
    products: [
        // 产品定义包生成的可执行文件和库，使其对其他包可见。
        .library(
            name: "AppCore",
            targets: ["AppCore"])
    ],
    targets: [
        // 目标是包的基本构建块，定义模块或测试套件。
        // 目标可以依赖于此包中的其他目标和依赖项中的产品。
        .target(
            name: "AppCore"
        )
    ]
)
请注意，包的 Swift 工具版本设置为 6.0。例如，如果你希望你的项目引用 iOS18，则需要将 Swift 工具版本设置为 6.0。这样做的副作用是你的包现在将以 Swift 6 语言模式构建。这意味着你将在包中获得 Swift 的完整可发送性和并发性检查套件，并且编译器会将任何问题标记为错误。

你可能还没有准备好在新包中使用 Swift 6.0。在这些情况下，如果你不使用 6.0 工具链中的任何功能，你可以将 Swift 工具版本设置回 5.10，或者可以在保留 6.0 工具链的同时将包的语言模式设置为 Swift 5：

// swift-tools-version: 6.0
// swift-tools-version 声明构建此包所需的最低 Swift 版本。

import PackageDescription

let package = Package(
    name: "AppCore",
    platforms: [.iOS(.v18)],
    // ... 包描述的其余部分
    swiftLanguageModes: [.v5]
)
你还可以为包中的特定目标分配 swift 语言模式。如下所示：

targets: [
  // 目标是包的基本构建块，定义模块或测试套件。
  // 目标可以依赖于此包中的其他目标和依赖项中的产品。
  .target(
    name: "AppCore",
    swiftSettings: [.swiftLanguageMode(.v5)]
  )
]
通过使用 Swift 5 语言模式，你可以继续像往常一样编写代码，直到你准备好开始迁移到 Swift 6。例如，你可能希望首先启用严格的并发性检查。

### [🤯 NSPasteboard 崩溃：处理文件 Promise 时内部并发内存突变不安全](https://wadetregaskis.com/nspasteboard-crashes-due-to-unsafe-internal-concurrent-memory-mutation-when-handling-file-promises/)

来源：Wade Tregaskis

发布时间：2024-08-22 13:01:02

NSPasteboard 在主线程和全局并发调度池中同时修改自身，涉及内部类型缓存。这意外地简单... 更多内容

## Tech News

### [🔥Meta推出Llama 3：功能强大的开源LLM](https://engineering.fb.com/2024/08/21/production-engineering/bringing-llama-3-to-life/)

来源：Engineering at Meta

发布时间：2024-08-22 00:00:49

Meta 推出了其迄今为止功能最强大的开源 LLM Llama 3，最近发布的 Llama 3.1 将支持新的工作流，例如合成数据生成和模型蒸馏，具有无与伦比的灵活性和控制力，以及与最佳闭源模型相媲美的最先进功能。

### [《黑神话：悟空》游玩体验：美轮美奂的西游世界](https://sspai.com/post/91709)

来源：少数派

发布时间：2024-08-22 15:20:54

本文分享了《黑神话：悟空》的游戏体验，赞扬了其精美的画面、丰富的场景设计和动人的故事背景，但也指出了一些不足，如缺乏引导和部分关卡设计缺失。

### [🎮抗日题材游戏《黑鹄》引发讨论](https://www.gcores.com/articles/187098)

来源：机核

发布时间：2024-08-22 21:45:57

黑鹄工作室首个游戏《黑鹄》采用虚幻5打造，以抗日题材为背景，引发了广泛讨论。这款游戏以其写实的画面、感人的剧情和丰富的玩法，让玩家身临其境地体验抗日战争的残酷与悲壮。

### [时间不贫困：如何便捷、准确地记录自己的一天](https://sspai.com/prime/story/ios-time-logging-suite)

来源：少数派

发布时间：2024-08-22 17:30:13

本文介绍了一种便捷且准确的时间记录方案，使用日历、Calflow 和时间记录 app，可以高效管理时间，统计项目投入时间，并生成可视化图表。

### [🎮《黑神话：悟空》Steam同时在线游玩人数突破241万人](https://www.gcores.com/articles/186949)

来源：机核

发布时间：2024-08-22 23:12:00

《黑神话：悟空》在发售两天后，Steam同时在线游玩人数突破241万人，受到玩家热烈追捧。这款游戏以其精美的画面、流畅的动作和丰富的剧情，为玩家带来了沉浸式的游戏体验。

### [🌟Shire 0.5 发布：融合本地研发资产，构建数据安全 RAG](http://www.phodal.com/blog/shire-0.5-secure-rag-and-shireql/)

来源：Blog | Phodal - A Growth Engineer

发布时间：2024-08-22 16:10:37

Shire 0.5 版本发布，新增功能可以更好地融合本地研发资产，同时构建数据安全 RAG，提升数据安全保障。

## Daily Code

### [⚡️ uv: 极速 Python 包和项目管理器](https://github.com/astral-sh/uv)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-08-23 06:29:54

uv 是一个用 Rust 编写的极速 Python 包和项目管理器。它可以替代 pip、conda、virtualenv、poetry、flit、hatch 和 pex 等多个工具，速度比 pip 快 10-100 倍。uv 可以安装和管理 Python 版本，运行和安装 Python 应用程序，运行单文件脚本，并支持内联依赖项元数据。它提供了全面的项目管理，并具有通用的锁定文件。uv 还包括一个与 pip 兼容的接口，可以在熟悉的 CLI 中获得性能提升。它支持 Cargo 风格的工作区，适用于可扩展的项目，并通过全局缓存进行依赖项去重，从而节省磁盘空间。uv 可以通过二进制安装程序或 PyPI 安装，支持 macOS、Linux 和 Windows。
