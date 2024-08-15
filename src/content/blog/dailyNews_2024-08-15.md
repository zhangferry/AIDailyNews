---
title: "Daily News #2024-08-15"
date: "2024-08-15 09:23:48"
description: "🍎苹果开源其同态加密库，并提供iOS 18中的实际部署示例
🎉 开发者即将可以使用安全元件在应用内提供 NFC 交易
🎉iOS 18、iPadOS 18、macOS Sequoia 第四版公测版现已发布
🎉 SwiftData 中使用 Codable 和枚举的注意事项
🌟 SwiftUI 中使用 @Entry 宏创建自定义环境值
🌟 网络请求的逐步指南
🚀 GitHub Copilot 扩展现已开放等待名单
🌟AI 革命：重塑数据中心和数字格局
⚡️ Alamofire: Swift 中强大的 HTTP 网络库
📊 Grafana：监控和可观察性的开源平台"
tags: 
- '同态加密'
- '监控'
- 'iOS'
- 'SwiftData'
- '开发工具'
- 'SwiftUI'
- '网络请求'
- '人工智能'
- '可观察性'
- 'HTTP'

---

> - 🍎苹果开源其同态加密库，并提供iOS 18中的实际部署示例
> - 🎉 开发者即将可以使用安全元件在应用内提供 NFC 交易
> - 🎉iOS 18、iPadOS 18、macOS Sequoia 第四版公测版现已发布
> - 🎉 SwiftData 中使用 Codable 和枚举的注意事项
> - 🌟 SwiftUI 中使用 @Entry 宏创建自定义环境值
> - 🌟 网络请求的逐步指南
> - 🚀 GitHub Copilot 扩展现已开放等待名单
> - 🌟AI 革命：重塑数据中心和数字格局
> - ⚡️ Alamofire: Swift 中强大的 HTTP 网络库
> - 📊 Grafana：监控和可观察性的开源平台

## Apple News

### [🍎苹果开源其同态加密库，并提供iOS 18中的实际部署示例](https://www.thestack.technology/apple-open-sources-its-homomorphic-encryption-library/)

来源：Hacker News - Newest: "apple"

发布时间：2024-08-14 21:47:11

苹果开源了其同态加密库，并提供了iOS 18中的实际部署示例。同态加密是一种隐私增强技术，允许用户在不解密数据的情况下对加密数据进行查询和计算。苹果在iOS 18中使用同态加密来进行实时来电者身份查找，这表明同态加密正在变得越来越成熟并具有实际应用价值。

### [🎉 开发者即将可以使用安全元件在应用内提供 NFC 交易](https://www.apple.com/newsroom/2024/08/developers-can-soon-offer-in-app-nfc-transactions-using-the-secure-element/)

来源：Apple Newsroom

发布时间：2024-08-14 23:30:15

iOS 18.1 将允许开发者在自己的应用内使用安全元件提供 NFC 非接触式交易，独立于 Apple Pay 和 Apple Wallet。开发者将能够提供应用内非接触式交易，用于店内支付、车钥匙、闭环交通、公司徽章、学生证、家门钥匙、酒店钥匙、商家忠诚度和奖励卡以及活动门票，未来还将支持政府身份证。

### [🎉iOS 18、iPadOS 18、macOS Sequoia 第四版公测版现已发布](https://osxdaily.com/2024/08/13/4th-public-beta-of-ios-18-ipados-18-macos-sequoia-available-for-testing/)

来源：OS X Daily

发布时间：2024-08-14 04:07:25

iOS 18、iPadOS 18 和 macOS Sequoia 的第四个公开测试版现已向测试人员开放。第四个公开测试版与第六个开发者测试版相匹配。测试版系统软件适用于高级用户，通常会出现更多错误，性能低于预期，但任何人都可以安装 iOS 18 ...

## iOS Blog

### [🎉 SwiftData 中使用 Codable 和枚举的注意事项](https://fatbobman.com/zh/posts/considerations-for-using-codable-and-enums-in-swiftdata-models/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-08-14 22:00:00

SwiftData 中使用 Codable 和枚举时需要注意的几个关键点，包括 Codable 的持久化策略、使用 Codable 类型属性作为查询谓词、在 Codable 中使用基础类型、调整 Codable 类型属性对轻量迁移的影响、在模型中使用 Codable 数组、模型中枚举类型的持久化方式、枚举类型不能直接作为查询谓词等。

### [🌟 SwiftUI 中使用 @Entry 宏创建自定义环境值](https://www.avanderlee.com/swiftui/entry-macro-custom-environment-values/)

来源：SwiftLee

发布时间：2024-08-14 02:33:02

SwiftUI 中的 @Entry 宏允许您定义自定义环境值，而无需编写样板代码。虽然在 Xcode 16 中引入，但您可以从 iOS 13 及更高版本使用它，因为它是一个生成向后兼容代码的 Swift 宏。新宏可用于环境值，以及事务、容器和...

### [🌟 网络请求的逐步指南](https://massicotte.org/step-by-step-network-request)

来源：massicotte.org

发布时间：2024-08-14 12:00:00

这篇文章提供了网络请求的逐步指南，对于初学者来说非常有用。它涵盖了从设置请求到处理响应的所有步骤。文章中还包含了一些有用的代码示例。

## Tech News

### [🚀 GitHub Copilot 扩展现已开放等待名单](https://github.blog/changelog/2024-08-13-sign-up-for-the-github-copilot-extensions-waitlist)

来源：GitHub Changelog

发布时间：2024-08-14 00:55:03

GitHub Copilot 扩展现已开放等待名单，允许开发人员注册以试用该功能。这些扩展使开发人员能够通过自定义提示和集成其他工具来扩展 Copilot 的功能，从而提高编码效率和生产力。

### [🌟AI 革命：重塑数据中心和数字格局](https://www.artificialintelligence-news.com/news/the-ai-revolution-reshaping-data-centres-and-the-digital-landscape/)

来源：AI News

发布时间：2024-08-14 17:43:06

人工智能正在改变世界，预计到 2030 年全球市场价值将达到 2-4 万亿美元。未来就在当下，感觉每隔几个月我们就会见证一次技术大爆炸。人工智能已经渗透到我们生活的方方面面，从根本上改变了我们的工作和...

## Daily Code

### [⚡️ Alamofire: Swift 中强大的 HTTP 网络库](https://github.com/Alamofire/Alamofire)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-08-15 08:37:58

Alamofire 是一个用 Swift 编写的 HTTP 网络库。它具有以下特点：可链接的请求/响应方法、Swift 并发支持、Combine 支持、URL/JSON 参数编码、上传文件/数据/流/MultipartFormData、使用请求或恢复数据下载文件、使用身份验证、HTTP 响应验证、上传和下载进度闭包、cURL 命令输出、动态适应和重试请求、TLS 证书和公钥固定、网络可达性、全面的单元和集成测试覆盖、完整的文档。Alamofire 的紧凑语法和广泛的功能集允许使用自动重试等强大功能编写请求，只需几行代码。

### [📊 Grafana：监控和可观察性的开源平台](https://github.com/grafana/grafana)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-08-15 08:22:54

Grafana 允许您查询、可视化、发出警报并了解您的指标，无论它们存储在哪里。与您的团队创建、探索和共享仪表盘，并培养以数据为导向的文化：可视化：快速灵活的客户端侧图表，具有多种选项。面板插件提供了多种可视化指标和日志的方法。动态仪表盘：使用模板变量创建动态且可重用的仪表盘，这些变量显示为仪表盘顶部的下拉菜单。探索指标：通过临时查询和动态向下钻取探索您的数据。并排拆分视图并比较不同的时间范围、查询和数据源。探索日志：体验从指标切换到日志的魔力，同时保留标签过滤器。快速搜索您的所有日志或实时流式传输它们。警报：为您的最重要指标直观地定义警报规则。Grafana 将持续评估并向 Slack、PagerDuty、VictorOps、OpsGenie 等系统发送通知。混合数据源：在同一图表中混合不同的数据源！您可以逐个查询指定数据源。这甚至适用于自定义数据源。
