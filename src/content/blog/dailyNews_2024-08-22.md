---
title: "Daily News #2024-08-22"
date: "2024-08-22 09:36:48"
description: "🎉 SwiftNIO Oblivious HTTP：保护隐私的 HTTP 协议
🤔 解决 Swift 6 中的“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误
🤔 解决 Swift 6 中的“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误
🤯 Swift 并发：在 Swift 中同步调用异步代码
🌟《怪物猎人：荒野》试玩体验
🌟 Meta AI 基础设施的未来
🌟 阅小结：一个基于快捷指令的类原生 AI 阅读助手
🌟星球大战：青年文化的科幻电影
🌟乌尔善：推动中国电影工业化的技术先锋
The Composable Architecture 🧩
⚡️ es-toolkit：高性能 JavaScript 实用程序库
Lottie for iOS 🎨"
tags: 
- '科幻电影'
- '游戏评测'
- 'Architecture'
- 'SwiftNIO'
- 'JavaScript'
- 'Swift 6'
- '电影技术'
- 'Animation'
- '实用程序库'
- 'AI'
- 'Swift'

---

> - 🎉 SwiftNIO Oblivious HTTP：保护隐私的 HTTP 协议
> - 🤔 解决 Swift 6 中的“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误
> - 🤔 解决 Swift 6 中的“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误
> - 🤯 Swift 并发：在 Swift 中同步调用异步代码
> - 🌟《怪物猎人：荒野》试玩体验
> - 🌟 Meta AI 基础设施的未来
> - 🌟 阅小结：一个基于快捷指令的类原生 AI 阅读助手
> - 🌟星球大战：青年文化的科幻电影
> - 🌟乌尔善：推动中国电影工业化的技术先锋
> - The Composable Architecture 🧩
> - ⚡️ es-toolkit：高性能 JavaScript 实用程序库
> - Lottie for iOS 🎨


## iOS Blog

### [🎉 SwiftNIO Oblivious HTTP：保护隐私的 HTTP 协议](https://swift.org/blog/introducing-swift-nio-oblivious-http/)

来源：Swift.org

发布时间：2024-08-21 18:00:00

SwiftNIO Oblivious HTTP 是一种保护隐私的 HTTP 协议，它通过结合 HTTP 消息加密和可信第三方中继服务来实现，为用户提供更高的隐私性，而不会产生明显的性能开销。它支持 RFC 9292（二进制 HTTP 序列化标准）和 RFC 9457（Oblivious HTTP 本身）。该软件包分为两个库：ObliviousHTTP（提供 RFC 9292 中的二进制 HTTP 编码方案的实现）和 ObliviousX（提供更通用的 API，形成 Oblivious HTTP 使用的加密方案的基础）。

### [🤔 解决 Swift 6 中的“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误](https://www.donnywals.com/solving-task-isolated-value-of-type-async-void-passed-as-a-strongly-transferred-parameter/)

来源：Donny Wals

发布时间：2024-08-21 16:38:51

在 Swift 6 中启用严格并发模式后，可能会遇到“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误。这通常是因为在任务中捕获了不可发送的对象，导致潜在的数据竞争。解决方法包括使捕获类型可发送或使用演员，或在任务捕获列表中复制不可发送的值。

### [🤔 解决 Swift 6 中的“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误](https://www.donnywals.com/solving-task-isolated-value-of-type-async-void-passed-as-a-strongly-transferred-parameter/)

来源：Donny Wals

发布时间：2024-08-21 16:38:51

在 Swift 6 中启用严格并发模式后，可能会遇到“Task-isolated value of type ‘() async -> Void’ passed as a strongly transferred parameter”错误。这通常是因为在任务中捕获了不可发送的对象，导致潜在的数据竞争。解决方法包括使捕获类型可发送或使用演员，或在任务捕获列表中复制不可发送的值。

### [🤯 Swift 并发：在 Swift 中同步调用异步代码](https://wadetregaskis.com/calling-swift-concurrency-async-code-synchronously-in-swift/)

来源：Wade Tregaskis

发布时间：2024-08-21 08:09:00

有时你需要将圆钉塞进方孔中。有时这确实是最好的选择（或者更准确地说：最不坏的选择）。我发现我经常被迫使用我无法控制的 API（最常见的是 Apple 的 API）。例如，数据源或委托回调是同步的，并且需要...

## Tech News

### [🌟《怪物猎人：荒野》试玩体验](https://www.gcores.com/articles/187030)

来源：机核

发布时间：2024-08-21 19:11:03

《怪物猎人：荒野》是一款即将发售的游戏，文章提供了试玩体验。游戏画面精美，玩法丰富，让人期待不已。文章还提醒玩家，游戏将于2025年发售，需要耐心等待。

### [🌟 Meta AI 基础设施的未来](https://engineering.fb.com/2024/08/20/data-infrastructure/aparna-ramani-future-of-ai-infrastructure-meta/)

来源：Engineering at Meta

发布时间：2024-08-21 00:00:26

大规模交付新的 AI 技术也意味着重新思考我们基础设施的每一层——从硅和软件系统，甚至我们的数据中心设计。Meta 的工程和基础设施团队连续第二年参加 AI Infra @ Scale 会议，他们讨论了扩大 AI 规模所面临的挑战。

### [🌟 阅小结：一个基于快捷指令的类原生 AI 阅读助手](https://sspai.com/post/91597)

来源：少数派

发布时间：2024-08-21 17:33:35

文章介绍了一个基于快捷指令的类原生 AI 阅读助手「阅小结」，可以帮助用户在手机端快速总结文章内容，提升阅读效率。文章详细介绍了「阅小结」的功能、使用指南和后记，并对 Apple Intelligence 的发展前景进行了展望。

### [🌟星球大战：青年文化的科幻电影](https://www.gcores.com/radios/183679)

来源：机核

发布时间：2024-08-21 21:00:00

星球大战作为一部科幻电影，在不同时代都具有共同的故事逻辑，它不仅包含了科学知识，还辐射到了二次元和电影领域，值得游戏爱好者分享。

### [🌟乌尔善：推动中国电影工业化的技术先锋](http://zhuanlan.zhihu.com/p/715661517?utm_campaign=rss&utm_medium=rss&utm_source=rss&utm_content=title)

来源：知乎每日精选

发布时间：2024-08-21 10:25:55

导演乌尔善以其独特的艺术视角和不懈的技术探索，成为推动中国电影工业化的重要力量。从《寻龙诀》到《封神第一部》，再到《异人之下》，乌尔善不断挑战自我，凭借不断拓新电影类型将新技术融入电影制作，为中国电影产业注入了新的活力。

## Daily Code

### [The Composable Architecture 🧩](https://github.com/pointfreeco/swift-composable-architecture)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-08-22 08:34:20

The Composable Architecture (TCA) is a library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. It can be used in SwiftUI, UIKit, and more, and on any Apple platform (iOS, macOS, visionOS, tvOS, and watchOS).

### [⚡️ es-toolkit：高性能 JavaScript 实用程序库](https://github.com/toss/es-toolkit)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-08-22 05:08:18

es-toolkit 是一款最先进的高性能 JavaScript 实用程序库，具有小包大小和强类型注释。它提供各种日常实用程序函数，如去抖动、延迟、块、求和和选择，并针对性能进行了设计，在现代 JavaScript 环境中实现了 2-3 倍的性能提升。

### [Lottie for iOS 🎨](https://github.com/airbnb/lottie-ios)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-08-22 08:34:20

Lottie is a cross-platform library for iOS, macOS, tvOS, visionOS, Android, and Web that natively renders vector-based animations and art in realtime with minimal code. Lottie loads and renders animations and vectors exported in the bodymovin JSON format.
