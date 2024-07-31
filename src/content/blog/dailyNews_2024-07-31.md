---
title: "Daily News #2024-07-31"
date: "2024-07-31 09:12:32"
description: "🌟 苹果使用谷歌 Tensor 芯片开发 Apple Intelligence
🎉 苹果发布 iOS 18.1、macOS Sequoia 15.1、iPadOS 18.1 首个测试版，搭载 Apple Intelligence 人工智能功能
🎉 Swift 同态加密库发布！
🌟 非可发送类型：并发编程中的重要角色
🤖️ AI赋能金融，摩根大通推出内部AI聊天机器人
✨ 手动运行 workflow_dispatch 设置的工作流
RxSwift: 用 Swift 编写响应式编程
MinerU：基于 PDF-Extract-Kit 的端到端 PDF 解析工具，支持将 PDF 转换为 Markdown"
tags: 
- '并发编程'
- 'RxSwift'
- 'GitHub'
- '人工智能'
- '响应式编程'
- 'PDF'
- '苹果'
- 'Swift'
- '金融'
- 'iPadOS'
- 'macOS'
- '加密'
- '数据提取'
- 'iOS'

---

> - 🌟 苹果使用谷歌 Tensor 芯片开发 Apple Intelligence
> - 🎉 苹果发布 iOS 18.1、macOS Sequoia 15.1、iPadOS 18.1 首个测试版，搭载 Apple Intelligence 人工智能功能
> - 🎉 Swift 同态加密库发布！
> - 🌟 非可发送类型：并发编程中的重要角色
> - 🤖️ AI赋能金融，摩根大通推出内部AI聊天机器人
> - ✨ 手动运行 workflow_dispatch 设置的工作流
> - RxSwift: 用 Swift 编写响应式编程
> - MinerU：基于 PDF-Extract-Kit 的端到端 PDF 解析工具，支持将 PDF 转换为 Markdown

## Apple News

### [🌟 苹果使用谷歌 Tensor 芯片开发 Apple Intelligence](https://www.macrumors.com/2024/07/30/google-chips-used-to-develop-apple-intelligence/)

来源：Hacker News - Newest: "apple"

发布时间：2024-07-30 21:05:44

苹果使用谷歌开发的张量处理单元 (TPU)，而不是英伟达广泛使用的图形处理单元 (GPU)，来构建 Apple Intelligence 的两个关键组件。考虑到英伟达在人工智能处理器市场的主导地位，以及苹果极少透露其用于开发目的的硬件选择，这一决定值得注意。英伟达的 GPU 因其性能和效率而备受人工智能应用的青睐。与将芯片和系统作为独立产品销售的英伟达不同，谷歌通过云服务提供对 TPU 的访问。使用谷歌 TPU 的客户必须在谷歌的生态系统中开发他们的软件，该生态系统提供集成工具和服务，以简化人工智能模型的开发和部署。

### [🎉 苹果发布 iOS 18.1、macOS Sequoia 15.1、iPadOS 18.1 首个测试版，搭载 Apple Intelligence 人工智能功能](https://osxdaily.com/2024/07/29/beta-1-of-ios-18-1-macos-sequoia-15-1-ipados-18-1-released-with-apple-intelligence/)

来源：OS X Daily

发布时间：2024-07-30 06:06:02

苹果发布了 iOS 18.1、macOS Sequoia 15.1 和 iPadOS 18.1 的第一个测试版，这些版本都搭载了 Apple Intelligence 人工智能功能。这些 .1 测试版与 iOS 18、iPadOS 18 和 macOS Sequoia 15 的并发测试版是分开的，每个测试版目前仍为测试版 4。测试版 1 版本...

## iOS Blog

### [🎉 Swift 同态加密库发布！](https://swift.org/blog/announcing-swift-homomorphic-encryption/)

来源：Swift.org

发布时间：2024-07-30 18:00:00

Swift 同态加密库发布，它是一种加密技术，可以在不透露底层未加密数据的情况下对加密数据进行计算。它为客户端提供了一种将加密数据发送到服务器的方法，服务器对加密数据进行操作并返回客户端可以解密的结果。在执行请求期间，服务器本身永远不会解密原始数据，甚至无法访问解密密钥。这种方法为云服务在保护用户数据隐私和安全的同时进行操作提供了新的机会，这显然对许多场景极具吸引力。

### [🌟 非可发送类型：并发编程中的重要角色](https://massicotte.org/non-sendable)

来源：massicotte.org

发布时间：2024-07-30 12:00:00

可发送类型在 Swift 并发中备受关注，但非可发送类型同样重要。它们通常被视为并发问题，但有时却是完美的解决方案。

## Tech News

### [🤖️ AI赋能金融，摩根大通推出内部AI聊天机器人](https://www.artificialintelligence-news.com/news/jpmorgan-introduces-in-house-ai-chatbot-for-research-analysis/)

来源：AI News

发布时间：2024-07-30 18:44:49

摩根大通推出了一款尖端的生成式人工智能产品，突显了人工智能在金融业日益增长的影响力。这款名为 LLM Suite 的新工具被誉为颠覆者，能够执行传统上分配给研究分析师的任务。据《金融时报》获得的一份内部备忘录显示...

### [✨ 手动运行 workflow_dispatch 设置的工作流](https://github.blog/changelog/2024-07-30-run-workflows-set-as-workflow_dispatch-manually)

来源：Changelogs Archive - The GitHub Blog

发布时间：2024-07-30 23:57:40

现在，您可以手动运行设置为 workflow_dispatch 的工作流，而无需创建新的事件。这对于需要在特定时间或根据需要运行工作流的情况非常有用。

## Daily Code

### [RxSwift: 用 Swift 编写响应式编程](https://github.com/ReactiveX/RxSwift)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-07-31 07:26:57

RxSwift 是 Reactive Extensions 标准的 Swift 特定实现。虽然此版本旨在忠实于 Rx 的原始精神和命名约定，但此项目也旨在为 Rx API 提供真正的 Swift 优先 API。可以在 ReactiveX.io 上找到跨平台文档。与其他 Rx 实现一样，RxSwift 的目的是轻松组合异步操作和数据流，这些数据流采用序列对象的形式，并提供了一套方法来转换和组合这些异步工作。KVO 观察、异步操作、UI 事件和其他数据流都统一在序列抽象之下。这就是 Rx 如此简单、优雅和强大的原因。

### [MinerU：基于 PDF-Extract-Kit 的端到端 PDF 解析工具，支持将 PDF 转换为 Markdown](https://github.com/opendatalab/MinerU)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-07-31 06:51:35

MinerU 是一款一站式、开源、高质量的数据提取工具，包括以下主要功能：

Magic-PDF PDF 文档提取
Magic-Doc 网页和电子书提取

Magic-PDF 是一款旨在将 PDF 文档转换为 Markdown 格式的工具，能够处理存储在本地或支持 S3 协议的对象存储上的文件。
