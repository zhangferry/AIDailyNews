---
title: "Daily News #2025-01-21"
date: "2025-01-21 23:18:24"
description: "SwiftUI @Observable 类观察属性的实用指南
探索SwiftUI中的颜色混合新特性
Apple面临的AI挑战与技术监管的未来
DeepSeek推出对比OpenAI的国产大模型
比亚迪官网重构，设计升级值得关注
荣耀迎来新CEO，IPO在即
苹果地图的四大优势超越谷歌地图
可组合架构 - The Composable Architecture
LLM课程：从基础到应用的全覆盖
React Native 视频组件 - react-native-video
Cursor AI自定义规则库：提升编码效率
从负债到品牌崛起：刘世超的创业之路"
tags: 
- "编程"
- "网站设计"
- "AI技术"
- "工具"
- "导航"
- "颜色混合"
- "AI"
- "架构"
- "课程"
- "React Native"
- "开发"
- "SwiftUI"
- "技术监管"
- "创业"
- "企业动态"
- "深度学习"
- "Swift"

---

> - SwiftUI @Observable 类观察属性的实用指南
> - 探索SwiftUI中的颜色混合新特性
> - Apple面临的AI挑战与技术监管的未来
> - DeepSeek推出对比OpenAI的国产大模型
> - 比亚迪官网重构，设计升级值得关注
> - 荣耀迎来新CEO，IPO在即
> - 苹果地图的四大优势超越谷歌地图
> - 可组合架构 - The Composable Architecture
> - LLM课程：从基础到应用的全覆盖
> - React Native 视频组件 - react-native-video
> - Cursor AI自定义规则库：提升编码效率
> - 从负债到品牌崛起：刘世超的创业之路

## 🍎 iOS Blog

### [SwiftUI @Observable 类观察属性的实用指南](https://www.donnywals.com/observing-properties-on-an-observable-class-outside-of-swiftui-views/)

来源：Donny Wals

发布时间：2025-01-21 18:59:24

本文深入探讨了在 SwiftUI 视图外部观察 @Observable 类属性的方法，特别是在 iOS 17 及更高版本中。介绍了如何使用 WithObservationTracking 函数观察属性，以及 onChange 闭包的工作方式。作者指出与传统的 ObservableObject 协议相比，@Observable 的观察机制存在一些局限性，如 onChange 只在属性变更时触发一次等。为解决观察中遇到的问题，提出了使用 DispatchQueue.main.async 来获取最新值的建议。此外，还讨论了如何在 Swift 6 中使用观察时面临的挑战，强调 Combine 的 @Published 提供了更好的解决方案。

### [探索SwiftUI中的颜色混合新特性](https://swiftwithmajid.com/2025/01/21/color-mixing-in-swiftui/)

来源：Swift with Majid

发布时间：2025-01-21 08:00:00

在最新发布的SwiftUI中，苹果引入了一项新功能——颜色混合。这是一个单一的函数，能够帮助开发者实现多种创意任务。本文将深入探讨SwiftUI中的颜色混合特性及其应用潜力，为开发者提供新的设计思路和实践可能性。

### [Apple面临的AI挑战与技术监管的未来](https://sixcolors.com/podcast/2025/01/upgrade-547-figure-out-and-find-out/)

来源：Six Colors

发布时间：2025-01-21 06:48:03

本文总结了苹果在AI功能方面的两难境地，以及科技监管未来的动荡局面，以TikTok为例。探讨了Apple TV+在《离职》和《穹顶之下》时代的表现，显示出苹果在内容创作和技术创新方面的复杂态度。

## 📥 Tech News

### [DeepSeek推出对比OpenAI的国产大模型](http://www.geekpark.net/news/345468)

来源：极客公园

发布时间：2025-01-21 11:35:29

DeepSeek发布了推理模型DeepSeek-R1，展现了对OpenAI最大程度的竞争意愿，开源了模型权重与训练报告，采用全面的MIT许可证，允许用户进行二次开发。该模型的性能与OpenAI的同等级别，但成本更低，展现出中国AI独立研究的潜力。DeepSeek还推出了移动端AI助手App，预示着其在应用层面的布局，未来值得期待。

### [比亚迪官网重构，设计升级值得关注](https://www.v2ex.com/t/1106915)

来源：V2EX-最新主题

发布时间：2025-01-21 22:45:50

作者指出，比亚迪官网经过重构后使用统一的 byd.com 域名，设计上有显著改善，如字体与玻璃效果的变化、国家或地区选择功能的优化等，整体浏览体验接近苹果官网，显示出前沿设计理念的融入。

### [荣耀迎来新CEO，IPO在即](http://www.geekpark.net/news/345481)

来源：极客公园

发布时间：2025-01-21 15:06:56

荣耀在经历了品牌独立和市场重回后迎来了新CEO李健，此时正准备启动IPO。赵明在其任内为品牌发展做出重大贡献，而新任的李健则是继往开来，期待在AI和高端化市场中推动技术创新。他将依靠丰富的市场经验，继续加强荣耀在国内外市场的竞争能力。面对不断变化的市场环境，荣耀需快速反应以巩固其在智能手机市场的地位。

### [苹果地图的四大优势超越谷歌地图](https://www.wired.com/story/things-apple-maps-does-better-than-google-maps/)

来源：Hacker News - Newest: "apple"

发布时间：2025-01-21 22:25:36

苹果地图自2012年发布以来经历了重大的改进，现今在转弯指示及清晰度等方面优于谷歌地图。用户表示苹果地图能更直观地指示行驶路线，同时提供实时公共交通信息，令人更加便捷。此外，其与苹果生态系统的深度整合，使得使用者体验更加流畅。不过，尽管苹果地图表现不俗，但在商业信息的覆盖率上仍逊色于谷歌。

## 💾 Daily Code

### [可组合架构 - The Composable Architecture](https://github.com/pointfreeco/swift-composable-architecture)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2025-01-21 23:16:35

可组合架构（TCA）是用于构建应用程序的库，强调一致性、易理解性和易测试性。支持 SwiftUI、UIKit 和所有 Apple 平台。提供状态管理、组件分解、侧效应处理及易于使用的 API，适合各类复杂特性开发和测试。文档齐全，包含大量示例和使用教程。

### [LLM课程：从基础到应用的全覆盖](https://github.com/mlabonne/llm-course)

来源：Trending repositories on GitHub today · GitHub

发布时间：2025-01-21 23:16:38

此课程分为三部分：LLM基础知识、LLM科学家和LLM工程师。基础部分涵盖数学、Python和神经网络知识，科学家部分专注于最新技术的LLM构建，而工程师部分则强调LLM应用的创建与部署。课程内容丰富，资源齐全，包括从量化到微调的实践指导，适合对大语言模型（LLM）感兴趣的学习者。

### [React Native 视频组件 - react-native-video](https://github.com/TheWidlarzGroup/react-native-video)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2025-01-21 23:16:35

react-native-video 是一个用于 React Native 的视频组件，支持多种视频播放需求。文档提供了详细的使用说明，包括基本使用示例和 DRM 示例。社区支持通过 Discord 服务器提供，专为企业级需求提供整合和定制服务。

### [Cursor AI自定义规则库：提升编码效率](https://github.com/PatrickJS/awesome-cursorrules)

来源：Trending repositories on GitHub today · GitHub

发布时间：2025-01-21 23:16:38

这个作品集列出了丰富的.cursorrules文件，可用于增强Cursor AI的使用体验。这些文件允许开发者根据项目需求自定义AI行为，确保生成的代码符合项目标准。包含前端、后端、移动开发等多领域的具体规则，支持团队协作和提升生产力，是希望充分利用Cursor AI功能的开发者的宝贵资源。

## 📻 Podcast

### [从负债到品牌崛起：刘世超的创业之路](https://www.xiaoyuzhoufm.com/episode/678f526c9420ede9d18efa6a)

来源：三五环

发布时间：2025-01-21 20:00:00

本期节目邀请了「溪木源」品牌创始人刘世超分享其创业经历。从背负700万债务，到抓住电商机遇发展至2000万规模，他的故事充满挑战与启发。谈及产品开发和品牌建设，他强调专注细分市场、坚持自研配方是成功的关键。此外，刘世超分享了团队创新的重要性，预示着未来品牌发展的独特路径。这些经验将给产品经理和创业者带来深刻启示。
