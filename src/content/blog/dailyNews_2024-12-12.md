---
title: "Daily News #2024-12-12"
date: "2024-12-12 23:20:40"
description: "在Swift测试中模拟网络连接的最佳实践
智能眼镜与iOS 18.2新特性探讨
iOS 18.2推送新功能，包括ChatGPT集成
AI 保险客服的崛起：水滴公司如何通过 AI Agent 改变保险行业
AI Agent 时代来临：谷歌 Gemini 2.0 的颠覆创新
MLOps在提升电商履约时效中的应用
RocksDB内存使用问题的深入解析
庆祝全球开发者卓越成就，App Store 奖项揭晓
京东国际的资源机销售情况
Alamofire: 高效的 Swift HTTP 网络库
Nexus zkVM：高并发的模块化零知识虚拟机
Lottie: 动态渲染动画的跨平台库"
tags: 
- "优化"
- "人工智能"
- "电商"
- "动画"
- "网络请求"
- "新功能"
- "Gemini 2.0"
- "iOS"
- "MLOps"
- "区块链"
- "谷歌"
- "水滴公司"
- "内存管理"
- "时效"
- "保险行业"
- "智能科技"
- "网络库"
- "单元测试"
- "Swift"
- "RocksDB"
- "虚拟机"
- "开发者奖项"
- "跨平台"
- "iPhone"
- "AI技术"

---

> - 在Swift测试中模拟网络连接的最佳实践
> - 智能眼镜与iOS 18.2新特性探讨
> - iOS 18.2推送新功能，包括ChatGPT集成
> - AI 保险客服的崛起：水滴公司如何通过 AI Agent 改变保险行业
> - AI Agent 时代来临：谷歌 Gemini 2.0 的颠覆创新
> - MLOps在提升电商履约时效中的应用
> - RocksDB内存使用问题的深入解析
> - 庆祝全球开发者卓越成就，App Store 奖项揭晓
> - 京东国际的资源机销售情况
> - Alamofire: 高效的 Swift HTTP 网络库
> - Nexus zkVM：高并发的模块化零知识虚拟机
> - Lottie: 动态渲染动画的跨平台库

## 🍎 iOS Blog

### [在Swift测试中模拟网络连接的最佳实践](https://www.donnywals.com/mocking-a-network-connection-in-your-swift-tests/)

来源：Donny Wals

发布时间：2024-12-12 17:56:48

这篇文章讨论了如何在Swift单元测试中模拟网络连接，以确保测试的独立性和重复性。文章提出两种主要方法：一种是完全模拟网络层，另一种是使用URLProtocol来控制URLSession的请求和响应。通过定义协议和实现MockNetworkClient，开发者可以在不依赖真实网络的情况下验证代码逻辑。同时，文中还阐述了如何使用URLProtocol模拟服务器响应，以便进行更复杂的POST请求测试。整体上，该文对想要提高测试质量的开发者尤为重要，提供了实用的技巧和代码示例。

### [智能眼镜与iOS 18.2新特性探讨](https://sixcolors.com/podcast/2024/12/clockwise-584-hush-we-dont-have-time/)

来源：Six Colors

发布时间：2024-12-12 05:32:12

本文讨论了当前的智能眼镜，居家和宠物监控的智能科技，以及对iOS 18.2的新功能如Genmoji和Image Playground的看法。还分享了如何组织和管理节日赠礼清单的建议与想法，便于整理与跟踪。

## 📥 Tech News

### [iOS 18.2推送新功能，包括ChatGPT集成](https://www.theverge.com/2024/12/11/24317119/ios-18-2-apple-intelligence-chatgpt-genmoji)

来源：Hacker News - Newest: "apple"

发布时间：2024-12-12 02:53:56

iOS 18.2正式发布，新增多项苹果智能工具，包括与OpenAI的ChatGPT集成。用户可以通过Siri和撰写工具访问ChatGPT，同时还推出了图像游戏和自定义表情生成工具。这些新功能和语言支持的扩展将提升用户体验。

### [AI 保险客服的崛起：水滴公司如何通过 AI Agent 改变保险行业](http://www.geekpark.net/news/344137)

来源：极客公园

发布时间：2024-12-12 17:50:14

水滴公司推出的 AI 保险客服具备近似真人的对话能力，能够流畅应对复杂的保险咨询。此创新旨在弥补人类保险经纪人服务不足，通过自主学习和不断迭代，AI Agent达成了对话持续超过50分钟的能力，为用户提供高效、专业的咨询体验。水滴通过结合大数据与深度学习，构建了一套符合保险行业特点的智能客服系统，未来希望将这一技术推广到其他行业，大幅提升服务效率。

### [AI Agent 时代来临：谷歌 Gemini 2.0 的颠覆创新](http://www.geekpark.net/news/344096)

来源：极客公园

发布时间：2024-12-12 03:23:26

谷歌的 Gemini 2.0 模型发布引起关注，针对 Agent 功能进行多项创新，包括自动化搜索、编程支持和游戏辅助。其推出的 Project Astra 和 Jules 展现了 AI 在提高生产力方面的潜力，未来有望改变用户与设备的交互方式。该技术的进步显示出 AI Agent 将在更广泛领域中应用，可能重塑我们使用智能设备的体验，成为日常生活中不可或缺的部分。

### [MLOps在提升电商履约时效中的应用](https://mp.weixin.qq.com/s/xvoFCV8oMblvlKSXphZoDg)

来源：值得一读技术博客

发布时间：2024-12-12 00:00:00

本文探讨了MLOps在得物电商平台优化订单履约时效的实践，通过模型复现与一致性保障，提出了时效仿真产品，并在供应链复杂环境中实现了效率与准确率的平衡。作者分享了如何通过算法改进用户购物体验，以及MLOps在模型生命周期管理中的核心理念，强调了在动态运营中提升履约效率的重要性。

### [RocksDB内存使用问题的深入解析](https://mp.weixin.qq.com/s/K515eohtfOhP9ZZZ03yRrA)

来源：值得一读技术博客

发布时间：2024-12-12 00:00:00

本文详细解析了在使用RocksDB时内存超限现象的成因，重点探讨了其内存管理机制及内存使用优化策略。通过对不合理内存使用情况的分析，作者提供解决方案，建议使用jemalloc替代ptmalloc，显著提升了系统性能和内存利用率，为读者解决类似问题提供了宝贵的经验。

### [庆祝全球开发者卓越成就，App Store 奖项揭晓](https://developer.apple.com/news/?id=t9ha5xqc)

来源：Latest News - Apple Developer

发布时间：2024-12-12 01:00:25
![](https://devimages-cdn.apple.com/wwdc-services/articles/images/572DF998-E42E-4EA8-A2E2-EE9F05DF58B6/2048.jpeg)
发布了全球优秀开发者的表彰活动，以表扬他们在 App Store 中的杰出贡献。文章简要介绍了获奖者，传达了对开发者工作的认可和庆祝。

### [京东国际的资源机销售情况](https://www.v2ex.com/t/1097144)

来源：V2EX-最新主题

发布时间：2024-12-12 22:55:44

文章探讨了京东国际平台上的资源机销售情况，揭示这些资源机是由苹果代工厂生产并经过测试的二手设备。用户对这些资源机的购买价值表示疑虑，希望更多的买家能对此保持警惕。

## 💾 Daily Code

### [Alamofire: 高效的 Swift HTTP 网络库](https://github.com/Alamofire/Alamofire)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-12-12 23:18:26

Alamofire 是一个功能强大的 HTTP 网络库，专为 Swift 语言设计，支持链式请求和响应处理。其特点包括对 Swift Concurrency 和 Combine 的支持、全面的文档以及丰富的功能，如文件上传下载、自动重试和网络可达性监测。Alamofire 提供简单的集成方法，支持 CocoaPods、Carthage 和 Swift Package Manager。适合开发者快速构建高质量网络请求。在多平台上测试较为全面，但在 Linux、Windows 和 Android 上存在已知问题，使用需谨慎。

### [Nexus zkVM：高并发的模块化零知识虚拟机](https://github.com/nexus-xyz/nexus-zkvm)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-12-12 23:18:29

Nexus zkVM 是一个开源的高性能模块化零知识虚拟机，设计目标是在强大的计算能力下达到每秒亿亿次 CPU 周期确认。用户需先安装 Rust 和 CMake，并配置 RISC-V 目标。创建新的 Nexus 项目后，可以运行 Rust 程序并生成证明。项目代码遵循 MIT 和 Apache 双重许可，欢迎贡献。Nexus 非常支持开源社区的参与。

### [Lottie: 动态渲染动画的跨平台库](https://github.com/airbnb/lottie-ios)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-12-12 23:18:26

Lottie 是一个跨平台库，支持 iOS、macOS、Android 和 Web，用于实时渲染基于矢量的动画。通过简单的 JSON 格式导入动画，Lottie 使设计师能够无需编码即可实现复杂动画。其安装支持 Swift Package Manager、CocoaPods 和 Carthage，并在隐私和安全方面提供了保护措施。Lottie 还允许在运行时改变动画属性，充分展现了其灵活性。适合需要快速实现动态视觉效果的开发者。

