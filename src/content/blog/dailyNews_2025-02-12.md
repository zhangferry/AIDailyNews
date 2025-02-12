---
title: "Daily News #2025-02-12"
date: "2025-02-12 20:59:33"
description: "精确掌控 SwiftUI 滚动：自定义 Paging 实现
将Android快照与GitHub Actions集成的指南
苹果账户内容迁移：轻松合并数字购买
深度解析Kafka磁盘故障对ELK日志处理的影响
免费获取DeepSeek API与searxng搜索域名
自动驾驶规控算法验证的场景仿真软件解析
Hero: 简化 iOS 视图控制器转场的库
PLCrashReporter: 可靠的实时崩溃报告框架"
tags: 
- "苹果"
- "算法验证"
- "动画"
- "故障处理"
- "iOS"
- "ELK"
- "崩溃报告"
- "库"
- "滚动行为"
- "技术"
- "Kafka"
- "账户迁移"
- "API"
- "自动驾驶"
- "SwiftUI"

---

> - 精确掌控 SwiftUI 滚动：自定义 Paging 实现
> - 将Android快照与GitHub Actions集成的指南
> - 苹果账户内容迁移：轻松合并数字购买
> - 深度解析Kafka磁盘故障对ELK日志处理的影响
> - 免费获取DeepSeek API与searxng搜索域名
> - 自动驾驶规控算法验证的场景仿真软件解析
> - Hero: 简化 iOS 视图控制器转场的库
> - PLCrashReporter: 可靠的实时崩溃报告框架

## 🍎 iOS Blog

### [精确掌控 SwiftUI 滚动：自定义 Paging 实现](https://fatbobman.com/zh/posts/mastering-swiftui-scrolling-implementing-custom-paging/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2025-02-12 08:12:00

本文探讨了从 iOS 17 开始 SwiftUI 提供的 scrollTargetBehavior 特性，帮助开发者实现更加精准的滚动控制。通过解决默认 paging 行为在横屏模式下的偏移问题，作者展示了如何通过自定义 ScrollTargetBehavior 实现自定义翻页逻辑。文章详细介绍了从最初识别问题到逐步优化的过程，最终设计出一个灵活且稳定的翻页解决方案，并扩展到更复杂的滚动控制。希望能够为开发者提供实用的启发，使他们轻松应对 SwiftUI 中的复杂滚动需求。

### [将Android快照与GitHub Actions集成的指南](https://www.emergetools.com/guides/integrating-android-snapshots-with-github-actions)

来源：Emerge Tools Blog

发布时间：2025-02-12 01:30:00

本文介绍了如何将Android快照与GitHub Actions集成，从而实现自动化构建和测试流程。通过使用GitHub Actions，开发者可以高效管理项目构建，提高开发效率。文章详尽说明了集成步骤，包括配置文件的编写和必要的环境设置，适合Android开发者阅读。

## 📥 Tech News

### [苹果账户内容迁移：轻松合并数字购买](https://www.macrumors.com/2025/02/11/apple-migrate-purchases-apple-account/)

来源：Hacker News - Newest: "apple"

发布时间：2025-02-12 13:17:53

苹果公司推出了将数字购买内容从一个账户迁移至另一个账户的功能，方便用户整合多个账户。该功能支持应用、音乐、书籍等转移，需满足双重身份验证等安全要求。用户可通过iPhone或iPad的设置完成迁移，但现阶段不支持欧盟、英国和印度用户。迁移后，原账户将无法继续购买，所有支付方式及订阅也会被转移至主账户。

### [深度解析Kafka磁盘故障对ELK日志处理的影响](https://mp.weixin.qq.com/s/-bgldir-fMOGljrTjjP1xA)

来源：值得一读技术博客

发布时间：2025-02-12 00:00:00

文章详细记录了在ELK系统中，Kafka因磁盘故障导致的日志写入失败问题。作者从客户端和服务端角度分析故障表现，探讨了Kafka对单块磁盘故障的处理机制和Filebeat的异常写入。通过对Kafka的KIP-112支持和go sarama客户端的版本分析，揭示了文件采集工具未感知领导者切换导致的持续报错。进一步提出解决方案，包括升级sarama版本及重启相关组件，给出深刻的技术洞察和对策。

### [免费获取DeepSeek API与searxng搜索域名](https://www.v2ex.com/t/1111033)

来源：V2EX-最新主题

发布时间：2025-02-12 20:14:13

本文介绍了如何获取免费的DeepSeek API及searxng搜索域名。当前DeepSeek的API不稳定，而腾讯云提供了相对快速的解决方案，免费使用至25号。用户也可以使用提供的域名进行联网搜索；若追求更高稳定性，可以选择自行部署searxng。最后，介绍了如何利用EdgeOne Pages封装OpenAI格式的API，以满足联网功能的需求，文中附有相关链接和源码。

### [自动驾驶规控算法验证的场景仿真软件解析](https://www.cnblogs.com/hirain123/p/18709720)

来源：值得一读技术博客

发布时间：2025-02-12 00:00:00

本文探讨了自动驾驶技术中规控算法的开发与验证需求，强调算法验证对乘客安全与舒适的重要性。介绍了自动驾驶算法的基本模块和仿真验证的优势，提出了经纬恒润的ModelBase-AD软件作为解决方案。文中详细描述了该软件的功能特性，包括道路模型和交通流模型，以及如何通过高精车辆动力学模型实现准确的算法验证，最终提升自动驾驶的整体研发效率。

## 💾 Daily Dev

### [Hero: 简化 iOS 视图控制器转场的库](https://github.com/HeroTransitions/Hero)

来源：iOS Development News - Telegram Channel

发布时间：2025-02-12 10:12:51

Hero 是一个为 iOS 视图控制器转场构建的库，它为 UIKit 繁琐的转场 API 提供了一层声明式抽象，使得自定义转场变得更加简单。类似于 Keynote 的 Magic Move，Hero 自动转换匹配视图的状态，并支持通过手势交互控制动画。它还包括多个模板转场，支持与 Auto Layout 和 UICollectionView 配合使用，非常适合开发者使用。

### [PLCrashReporter: 可靠的实时崩溃报告框架](https://github.com/microsoft/plcrashreporter)

来源：iOS Development News - Telegram Channel

发布时间：2025-02-12 10:07:55

PLCrashReporter 是一个开源库，提供用于 iOS、macOS 和 tvOS 的实时崩溃报告框架，能有效检测崩溃并生成报告，帮助开发人员进行故障排查。该库仅使用公开 API，支持多线程堆栈回溯，易于集成，并提供多种集成方式，确保有效的崩溃信息收集，是应用程序监控的重要工具。
