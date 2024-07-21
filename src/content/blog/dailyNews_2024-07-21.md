---
title: "Daily News #2024-07-21"
date: "2024-07-21 09:37:20"
description: "🌟 如何在 Apple Watch 上安装 watchOS 11 公开测试版
Go 的原生 Mac API。以前称为 MacDriver
✨ 安全概览仪表盘、秘密扫描指标和启用趋势报告现已全面可用
🌟 Stirling-PDF：本地托管的 PDF 操作神器
🌟 RxSwift：响应式编程的 Swift 实现"
tags: 
- '响应式编程'
- '安全'
- '编程'
- 'watchOS 11'
- 'PDF'

---

> - 🌟 如何在 Apple Watch 上安装 watchOS 11 公开测试版
> - Go 的原生 Mac API。以前称为 MacDriver
> - ✨ 安全概览仪表盘、秘密扫描指标和启用趋势报告现已全面可用
> - 🌟 Stirling-PDF：本地托管的 PDF 操作神器
> - 🌟 RxSwift：响应式编程的 Swift 实现

## Apple News

### [🌟 如何在 Apple Watch 上安装 watchOS 11 公开测试版](https://osxdaily.com/2024/07/19/how-to-install-watchos-11-public-beta-on-apple-watch/)

来源：OS X Daily

发布时间：2024-07-20 00:18:08

如果您是一位高级 Apple Watch 用户，您可能会对在 Apple Watch 上运行 watchOS 11 公开测试版感兴趣，以配合运行 iOS 18 公开测试版的配对 iPhone。当然，测试版系统软件比最终版本有更多错误，并且可能存在性能和电池续航问题，但运行 watchOS 11 公开测试版可以让您抢先体验即将推出的新功能和改进。

### [Go 的原生 Mac API。以前称为 MacDriver](https://github.com/progrium/darwinkit)

来源：Hacker News - Newest: "apple"

发布时间：2024-07-20 02:31:36

DarwinKit 允许您使用受支持的 Apple 框架并使用 Go 构建原生应用程序。有了 XCode 和 Go 1.18+，您可以在 main.go 文件中编写此程序：
main.go
然后在此目录中运行：
go mod init helloworld
go get github.com/progrium/darwinkit@main
go run main.go
这可能需要一段时间，但一旦窗口弹出，您就可以在不使用 XCode 或 Objective-C 的情况下制作一个 macOS 程序。运行 go build 以获取可执行文件。
go build
虽然目前超出本项目的范围，但如果您愿意，可以将此可执行文件放入应用程序包中。您甚至可以添加权利，然后对该包或可执行文件进行签名和公证，以允许其他人运行它。理论上甚至可以将其放在 App Store 上。理论上，它可以放在 iOS、tvOS 或 watchOS 设备上，尽管您必须使用不同的特定于平台的框架。

## Tech News

### [✨ 安全概览仪表盘、秘密扫描指标和启用趋势报告现已全面可用](https://github.blog/changelog/2024-07-19-security-overview-dashboards-secret-scanning-metrics-and-enablement-trends-reports-are-now-generally-available)

来源：Changelogs Archive - The GitHub Blog

发布时间：2024-07-20 07:58:37

GitHub 的安全概览仪表盘、秘密扫描指标和启用趋势报告现已全面可用。这些功能可帮助你跟踪和改进组织的安全态势。安全概览仪表盘提供了一个集中视图，显示组织的安全关键指标，如代码扫描警报、秘密泄露和依赖项漏洞。秘密扫描指标提供有关组织秘密扫描活动和结果的见解。启用趋势报告跟踪组织内安全功能的采用和使用情况。

## Daily Code

### [🌟 Stirling-PDF：本地托管的 PDF 操作神器](https://github.com/Stirling-Tools/Stirling-PDF)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-07-21 05:43:32

Stirling-PDF 是一款功能强大的本地托管式 PDF 操作工具，可执行各种 PDF 操作，包括拆分、合并、转换、重新组织、添加图像、旋转、压缩等。

### [🌟 RxSwift：响应式编程的 Swift 实现](https://github.com/ReactiveX/RxSwift)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-07-21 07:57:41

RxSwift 是 Rx 标准在 Swift 中的实现，它提供了一个通用的抽象概念，允许你广播和订阅流中的值和事件。RxSwift 旨在保持 Rx 的原始精神和命名约定，同时提供一个真正的 Swift 优先的 API。它将异步操作和数据流统一在序列的抽象概念下，使其简单、优雅且强大。
