---
title: "Daily News #2024-12-18"
date: "2024-12-18 23:19:49"
description: "Swift 6中的Sending与Sendable的区别与联系
SwiftUI onAppear 异常调用的陷阱与应对策略
Meta的Threads团队如何优化iOS性能
Dify的全球化路径：意外的成功与挑战
Apache Gravitino：B站的元数据管理最佳实践
使用Shortcuts JS创建iOS快捷指令
组装NAS的必要性与成本
地平线科技的成长与未来展望
轻松集成Stripe iOS SDK，打造出色支付体验
Gemini API 食谱 - 开启多模态应用开发之旅
Swift Package Manager：简化代码管理与依赖管理
小米家居集成 - Home Assistant 完美搭档"
tags: 
- "Swift"
- "SwiftUI"
- "元数据管理"
- "性能优化"
- "Concurrency"
- "自动驾驶"
- "AI创业"
- "开发"
- "支付"
- "代码管理"
- "SDK"
- "JavaScript"
- "存储技术"
- "API"
- "智能家居"
- "工具"
- "开发经验"
- "iOS"

---

> - Swift 6中的Sending与Sendable的区别与联系
> - SwiftUI onAppear 异常调用的陷阱与应对策略
> - Meta的Threads团队如何优化iOS性能
> - Dify的全球化路径：意外的成功与挑战
> - Apache Gravitino：B站的元数据管理最佳实践
> - 使用Shortcuts JS创建iOS快捷指令
> - 组装NAS的必要性与成本
> - 地平线科技的成长与未来展望
> - 轻松集成Stripe iOS SDK，打造出色支付体验
> - Gemini API 食谱 - 开启多模态应用开发之旅
> - Swift Package Manager：简化代码管理与依赖管理
> - 小米家居集成 - Home Assistant 完美搭档

## 🍎 iOS Blog

### [Swift 6中的Sending与Sendable的区别与联系](https://www.donnywals.com/sending-vs-sendable-in-swift/)

来源：Donny Wals

发布时间：2024-12-18 17:50:16

随着Swift 6的推出，语言引入了新的sending关键字，替代了Swift 5中的@Sendable。文章详细探讨了这两者在语义和使用上的不同。Swift 6强化了数据竞争保护，特别是在多线程和任务中，sending可以安全地捕获非可发送对象，而不允许其被其他任务访问，增加了并发安全性。作者建议开发者尝试各自定义sending和@Sendable闭包，以熟悉它们的特性和局限性。整体而言，Swift 6的变化提供了更好的并发编程支持，是提升应用安全性的重要进步。

### [SwiftUI onAppear 异常调用的陷阱与应对策略](https://fatbobman.com/zh/posts/traps-and-countermeasures-for-abnormal-onappear-calls-in-swiftui/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-12-18 08:12:00

本文探讨了 SwiftUI 中 onAppear 方法异常调用的问题，结合实际案例分析了在 NavigationStack 中触发 onAppear 多次的问题，并确认这是一个 iOS 15 及后版本的 Bug。作者提出针对不同情况的解决方案，如使用 onceAppear 或 Binding 类型的 onAppear 来限制调用次数。文章最后反映了在 SwiftUI 发展中依然存在的一致性问题，并分享了向苹果反馈的经历，值得关注 SwiftUI 开发者参考。

## 📥 Tech News

### [Meta的Threads团队如何优化iOS性能](https://engineering.fb.com/2024/12/18/ios/how-we-think-about-threads-ios-performance/)

来源：Engineering at Meta

发布时间：2024-12-18 23:00:44

本文探讨了Meta的Threads iOS团队在应用快速增长期间如何保持性能，聚焦于关键监控指标以确保应用健康。同时，通过案例研究分析了发布的可靠性与导航延迟对用户体验的影响。Threads自2023年推出以来，团队采取了一系列措施以应对挑战，确保用户能流畅地使用该应用。

### [Dify的全球化路径：意外的成功与挑战](http://www.geekpark.net/news/344369)

来源：极客公园

发布时间：2024-12-18 22:17:08

Dify成立于2023年3月，快速在全球多个国家推出产品，尤其在日本市场发展迅速，成为全球增速最高的开源LLM工具。尽管面对大公司竞争和商业化困境，Dify仍凭借中立性和多模型工具箱的优势，赢得众多财富500强企业的青睐。创始人张路宇在大会上分享了团队成功的经验，强调全球化、产品导向和开源策略的重要性。

### [Apache Gravitino：B站的元数据管理最佳实践](https://mp.weixin.qq.com/s/WnPhlJSex7lGBNFWAlbJPg)

来源：值得一读技术博客

发布时间：2024-12-18 00:00:00

本文介绍了B站在大数据元数据管理中引入Apache Gravitino的最佳实践，针对传统HiveMetaStore架构的痛点，通过实现中心化的元数据管理，降低了元数据使用成本，解决了数据治理能力不足和信息不一致的问题。文章详细概述了Gravitino的架构、功能及其在生产环境中的实践，包括对半结构化和非结构化数据的管理、用户自定义接口扩展及其为用户所带来的多项收益，展望了未来的发展方向及计划。

### [使用Shortcuts JS创建iOS快捷指令](https://farrant.me/posts/creating-ios-12-shortcuts-with-shortcuts-js/)

来源：Hacker News - Newest: "apple"

发布时间：2024-12-18 08:54:23

Josh Farrant开发的Shortcuts JS库允许用户使用JavaScript创建iOS快捷指令。该库解决了原快捷指令界面的局限性，支持更灵活的功能构建，使用户能够以编程方式创建和管理快捷指令。Farrant希望通过社区协作不断扩展库的功能。

### [组装NAS的必要性与成本](https://www.v2ex.com/t/1098629)

来源：V2EX-最新主题

发布时间：2024-12-18 22:52:03

用户探讨组装NAS的需求，认为与普通PC相比，NAS配件尤其机箱价格偏高，且家庭用户在高可用性需求上较低。用户希望了解是否真的需要NAS机箱，以及在使用PVE时系统盘的合理大小，体现了对家庭存储方案的思考。

### [地平线科技的成长与未来展望](http://www.geekpark.net/news/344367)

来源：极客公园

发布时间：2024-12-18 18:11:01

地平线创立于2015年，致力于智能驾驶芯片的研发。创始人余凯回顾了公司的三大关键节点，包括聚焦自动驾驶领域、赴港上市等，强调自动驾驶将迎来新的飞跃期。余凯希望地平线能成为下一个科技巨头，推动人类解放体力劳动，实现机器人的广泛应用。

## 💾 Daily Code

### [轻松集成Stripe iOS SDK，打造出色支付体验](https://github.com/stripe/stripe-ios)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-12-18 23:17:51

Stripe iOS SDK 提供简便的方式，在iOS应用程序中创建出色的支付体验。SDK包括可自定义的UI界面组件与底层API，支持Apple Pay，自动处理符合强客户身份认证的原生3D Secure，保障敏感数据的安全收集，确保PCI合规。此外，SDK支持多种语言，并能处理数字产品支付，提供更新与迁移指南，适合开发者快速上手和定制化支付流程。

### [Gemini API 食谱 - 开启多模态应用开发之旅](https://github.com/google-gemini/cookbook)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-12-18 23:17:54

Gemini API 食谱是一个包含快速入门教程和示例的指南，帮助开发者了解并利用 Gemini API 进行多模态应用开发。用户可通过 Google AI Studio 创建 API 密钥并访问 REST API。最新的 Gemini 2.0 特性包括多模态处理和音频流应用，提供一系列快速入门教程，涵盖认证、文件处理、函数调用等功能。食谱还介绍了如何上传文件和生成高质量的嵌入，鼓励社区参与并提出贡献使用建议。

### [Swift Package Manager：简化代码管理与依赖管理](https://github.com/swiftlang/swift-package-manager)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-12-18 23:17:51

Swift Package Manager 是用于管理源码分发的工具，使分享与复用代码变得更加简单。它解决了编译、链接Swift包、依赖管理等挑战，并支持在macOS和Linux上构建。自Xcode 11起，该工具得到了Xcode的集成，支持iOS、macOS等应用程序。此外，包管理器还提供文档、使用指南与贡献指引，适合开发者快速上手与代码共享。

### [小米家居集成 - Home Assistant 完美搭档](https://github.com/XiaoMi/ha_xiaomi_home)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-12-18 23:17:54

小米家居集成是一个为 Home Assistant 提供支持的小米 IoT 设备的集成组件。它要求 Home Assistant 核心版本在 2024.11.0 及以上，并提供多种安装方式（如 Git clone、HACS、手动安装）。集成后，用户可以通过小米账户添加多个小米设备，并支持本地和云端控制。尽管大多数小米设备都受支持，但蓝牙和红外设备等部分设备仍不支持。用户需谨慎管理配置文件中的敏感信息以防止安全隐患。
