---
title: "Daily News #2024-04-12"
date: "2024-04-12 09:16:00"
description: "🚀 Safari 和 WebKit 性能大幅提升 60%！
🎉 苹果扩展维修选项，支持使用原装二手零件
🌟Mac 硬盘健康检查指南
👻 @State 魅影：多窗口 SwiftUI 应用的 Bug 分析
🌟 演员重入：Swift 中的微妙陷阱
🎉 美日宣布全面合作 AI 和技术
🎉 CodeQL 2.17.0 支持 Java 22、Swift 5.10、TS 5.4、C# 12
💪 Alamofire：Swift 中强大的 HTTP 网络库
🌟 C语言实现LLM训练，无需PyTorch或cPython"
tags: 
- '网络'
- 'LLM'
- '维修'
- '技术'
- 'Mac'
- 'SwiftUI'
- 'Swift'
- 'CodeQL'
- '国际合作'

---

> - 🚀 Safari 和 WebKit 性能大幅提升 60%！
> - 🎉 苹果扩展维修选项，支持使用原装二手零件
> - 🌟Mac 硬盘健康检查指南
> - 👻 @State 魅影：多窗口 SwiftUI 应用的 Bug 分析
> - 🌟 演员重入：Swift 中的微妙陷阱
> - 🎉 美日宣布全面合作 AI 和技术
> - 🎉 CodeQL 2.17.0 支持 Java 22、Swift 5.10、TS 5.4、C# 12
> - 💪 Alamofire：Swift 中强大的 HTTP 网络库
> - 🌟 C语言实现LLM训练，无需PyTorch或cPython

## Apple News

### [🚀 Safari 和 WebKit 性能大幅提升 60%！](https://9to5mac.com/2024/04/10/apple-touts-major-leap-in-safari-and-webkit-performance/)

来源：Hacker News - Newest: "apple"

发布时间：2024-04-11 22:57:33

苹果的 WebKit 团队宣布，他们通过 Speedometer 3.0 测试，将 Safari 的性能提升了约 60%。这些改进使开发人员能够构建比以往更快的网站和网络应用程序。苹果表示，他们通过数十项优化实现了这一目标，包括改进 JavaScript 引擎和减少内存使用。

### [🎉 苹果扩展维修选项，支持使用原装二手零件](https://www.apple.com/newsroom/2024/04/apple-to-expand-repair-options-with-support-for-used-genuine-parts/)

来源：Apple Newsroom

发布时间：2024-04-11 20:59:51

苹果宣布将允许客户和独立维修商在维修中使用原装二手零件，以提高维修便利性和延长产品寿命，同时加强隐私和安全保护。

### [🌟Mac 硬盘健康检查指南](https://osxdaily.com/2024/04/10/how-to-check-disk-health-on-mac-with-smartctl/)

来源：OS X Daily

发布时间：2024-04-11 00:29:53

本文介绍了使用 SMART 技术检查 Mac 硬盘健康状况的多种方法，从使用磁盘工具检查 SMART 状态到使用命令行工具 smartctl 获取更详细的信息。

## iOS Blog

### [👻 @State 魅影：多窗口 SwiftUI 应用的 Bug 分析](https://fatbobman.com/zh/posts/the-state-specter-analyzing-a-bug-in-multi-window-swiftui-applications/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-04-11 08:12:00

文章分析了 SwiftUI 多窗口模式下 @State 使用的 Bug，提出了临时解决策略，并探讨了 @State 的未来展望，鼓励开发者深入理解问题本质。

### [🌟 演员重入：Swift 中的微妙陷阱](https://www.donnywals.com/actor-reentrancy-in-swift-explained/)

来源：Donny Wals

发布时间：2024-04-11 19:37:05

文章深入浅出地解释了 Swift 中演员重入的概念，并通过一个数据缓存的例子展示了如何解决重入问题。文章强调了在演员中使用异步方法时需要小心，并考虑重入调用可能产生的影响。文章还提供了避免重入相关问题的建议，并鼓励读者分享自己的重入相关问题和解决方案。

## Tech News

### [🎉 美日宣布全面合作 AI 和技术](https://www.artificialintelligence-news.com/2024/04/11/us-and-japan-sweeping-ai-tech-collaboration/)

来源：AI News

发布时间：2024-04-11 18:38:04

美国和日本宣布了一系列新的 AI、量子计算、半导体和其他关键技术举措。这些雄心勃勃的计划是拜登总统和日本首相岸田文雄在岸田对白宫进行正式访问后于本周宣布的。两位领导人确认了他们在广泛领域的承诺。

### [🎉 CodeQL 2.17.0 支持 Java 22、Swift 5.10、TS 5.4、C# 12](https://github.blog/changelog/2024-04-11-codeql-2-17-0-support-for-java-22-swift-5-10-ts-5-4-c-12)

来源：Changelogs Archive - The GitHub Blog

发布时间：2024-04-11 21:00:25

CodeQL 2.17.0 现已发布，它为 Java 22、Swift 5.10、TS 5.4 和 C# 12 提供了支持。此版本还包括许多错误修复和改进。

## Daily Code

### [💪 Alamofire：Swift 中强大的 HTTP 网络库](https://github.com/Alamofire/Alamofire)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-04-12 08:00:27

Alamofire 是一个功能强大的 Swift HTTP 网络库，它提供了全面的功能，包括：

- 链式请求/响应方法
- Swift 并发支持
- Combine 支持
- URL/JSON 参数编码
- 文件/数据/流/MultipartFormData 上传
- 文件下载
- 身份验证
- HTTP 响应验证
- 上传和下载进度闭包
- cURL 命令输出
- 动态适应和重试请求
- TLS 证书和公钥固定
- 网络可达性

Alamofire 的语法简洁，功能丰富，可以轻松编写出具有自动重试等强大功能的请求，只需几行代码即可。

### [🌟 C语言实现LLM训练，无需PyTorch或cPython](https://github.com/karpathy/llm.c)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-04-12 06:15:25

该项目使用纯C/CUDA实现LLM训练，无需PyTorch或cPython，代码简洁高效，可与PyTorch参考实现完全匹配。目前正在开发CUDA实现，以进一步提升速度，并支持更多现代架构。
