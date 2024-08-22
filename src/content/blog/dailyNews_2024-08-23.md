---
title: "Daily News #2024-08-23"
date: "2024-08-23 00:55:46"
description: "💻 史蒂夫·乔布斯 Apple-1 电脑即将拍卖，预计创下天价
🎉欧盟用户迎新规！iOS 18 新增默认应用设置，App Store 等应用可删除
🎮 Netflix 游戏服务：专注于健康的游戏变现模式
🌟 如何为 SPM 包设置 Swift 语言模式
🤯 NSPasteboard 崩溃：处理文件 Promise 时内部并发内存突变不安全
🔥Meta发布Llama 3.1：功能强大的LLM，开启合成数据生成和模型蒸馏新时代
🎮《黑神话：悟空》Steam在线人数突破241万
🌟 Shire 0.5 发布：融合本地研发资产，构建数据安全 RAG
🎙️游戏茶话会：卡普空过去与未来
🎮 《黑神话：悟空》地图设计：美术很棒，问题很大"
tags: 
- '游戏地图设计'
- '游戏'
- 'Swift'
- '数据安全'
- '人工智能'
- 'iOS'
- 'iOS 18'
- '拍卖'

---

> - 💻 史蒂夫·乔布斯 Apple-1 电脑即将拍卖，预计创下天价
> - 🎉欧盟用户迎新规！iOS 18 新增默认应用设置，App Store 等应用可删除
> - 🎮 Netflix 游戏服务：专注于健康的游戏变现模式
> - 🌟 如何为 SPM 包设置 Swift 语言模式
> - 🤯 NSPasteboard 崩溃：处理文件 Promise 时内部并发内存突变不安全
> - 🔥Meta发布Llama 3.1：功能强大的LLM，开启合成数据生成和模型蒸馏新时代
> - 🎮《黑神话：悟空》Steam在线人数突破241万
> - 🌟 Shire 0.5 发布：融合本地研发资产，构建数据安全 RAG
> - 🎙️游戏茶话会：卡普空过去与未来
> - 🎮 《黑神话：悟空》地图设计：美术很棒，问题很大

## Apple News

### [💻 史蒂夫·乔布斯 Apple-1 电脑即将拍卖，预计创下天价](https://newatlas.com/technology/steve-jobs-apple-1-auction/)

来源：Hacker News - Newest: "apple"

发布时间：2024-08-22 08:19:43

史蒂夫·乔布斯曾使用过的 Apple-1 电脑将于 9 月 12 日在纽约佳士得拍卖行拍卖。由于乔布斯的影响力、Apple-1 的传奇地位以及保罗·艾伦收藏品的加持，预计该电脑将拍出天价。

### [🎉欧盟用户迎新规！iOS 18 新增默认应用设置，App Store 等应用可删除](https://developer.apple.com/news/?id=zglax7gc)

来源：Latest News - Apple Developer

发布时间：2024-08-22 22:00:36

欧盟用户在 iOS 18 中将迎来新变化，包括新增默认应用设置，允许用户选择拨号、发短信、翻译、导航、密码管理、键盘和呼叫垃圾邮件过滤器的默认应用。此外，App Store、信息、照片、相机和 Safari 等应用现在也可以删除。

### [🎮 Netflix 游戏服务：专注于健康的游戏变现模式](https://daringfireball.net/linked/2024/08/21/monument-valley-3-netflix)

来源：Hacker News - Newest: "apple"

发布时间：2024-08-22 20:43:42

Netflix 正在通过其订阅服务提供大量游戏，并专注于健康的变现模式，吸引厌恶赌场式付费获胜机制的游戏开发者。

## iOS Blog

### [🌟 如何为 SPM 包设置 Swift 语言模式](https://www.donnywals.com/setting-the-swift-language-mode-for-an-spm-package/)

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
        // 产品定义包生成的可执行文件和库，使它们对其他包可见。
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
请注意，该包的 Swift 工具版本设置为 6.0。例如，如果你希望你的项目引用 iOS18，则需要将 Swift 工具版本设置为 6.0。这样做的副作用是你的包现在将以 Swift 6 语言模式构建。这意味着你将在包中获得 Swift 的完整可发送性和并发性检查套件，并且编译器会将任何问题标记为错误。

你可能还没有准备好在新包中使用 Swift 6.0。在这些情况下，如果你不使用 6.0 工具链中的任何功能，你可以将 Swift 工具版本设置回 5.10，或者可以在保留 6.0 工具链的同时将包的语言模式设置为 Swift 5：

### [🤯 NSPasteboard 崩溃：处理文件 Promise 时内部并发内存突变不安全](https://wadetregaskis.com/nspasteboard-crashes-due-to-unsafe-internal-concurrent-memory-mutation-when-handling-file-promises/)

来源：Wade Tregaskis

发布时间：2024-08-22 13:01:02

NSPasteboard 在主线程和全局并发 Dispatch 池中同时修改自身，涉及内部类型缓存。这意外地简单... 更多内容

## Tech News

### [🔥Meta发布Llama 3.1：功能强大的LLM，开启合成数据生成和模型蒸馏新时代](https://engineering.fb.com/2024/08/21/production-engineering/bringing-llama-3-to-life/)

来源：Engineering at Meta

发布时间：2024-08-22 00:00:49

Meta发布了其迄今为止功能最强大的开放式LLM Llama 3，以及最新发布的Llama 3.1，它将支持新的工作流，例如合成数据生成和模型蒸馏，具有无与伦比的灵活性和控制力，其最先进的能力可与最好的闭源模型媲美。

### [🎮《黑神话：悟空》Steam在线人数突破241万](https://www.gcores.com/articles/186949)

来源：机核

发布时间：2024-08-22 23:12:00

《黑神话：悟空》发售两日后，Steam同时在线游玩人数突破241万人，受到玩家热烈追捧。游戏以其精美的画面、流畅的动作和丰富的剧情，获得了广泛好评。

### [🌟 Shire 0.5 发布：融合本地研发资产，构建数据安全 RAG](http://www.phodal.com/blog/shire-0.5-secure-rag-and-shireql/)

来源：Blog | Phodal - A Growth Engineer

发布时间：2024-08-22 16:10:37

Shire 0.5 版本发布，新增功能可以更好地融合本地研发资产，同时构建数据安全 RAG，提升数据安全保障。

### [🎙️游戏茶话会：卡普空过去与未来](https://www.gcores.com/radios/186823)

来源：机核

发布时间：2024-08-22 23:00:00

本期游戏茶话会节目探讨了卡普空的过去与未来，回顾了卡普空经典游戏，并展望了卡普空未来的发展方向。节目内容丰富，观点独到，值得游戏爱好者收听。

### [🎮 《黑神话：悟空》地图设计：美术很棒，问题很大](http://www.zhihu.com/question/664877196/answer/3601519631?utm_campaign=rss&utm_medium=rss&utm_source=rss&utm_content=title)

来源：知乎每日精选

发布时间：2024-08-22 11:07:16

《黑神话：悟空》的地图美术设计出色，但引导性、易读性和空气墙设计存在不足，导致玩家探索体验割裂感和不自由感。游戏缺乏明确的探索规则，导致玩家对自身能力和路径选择产生不确定性。此外，地图中颜色的运用不足，加重了探索的迷失感。
