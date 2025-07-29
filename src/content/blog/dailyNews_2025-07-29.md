---
title: "Daily News #2025-07-29"
date: "2025-07-29 23:23:38"
description: "从 Combine 到 Swift Concurrency：线程风险解析
ExecuTorch：Meta 推动边缘设备上的机器学习
专业级 WebSocket 调试插件
现代化的基于容器的依赖注入方法：Factory
自定义SwiftUI中的滚动行为
Swift并发中的线程与任务
现代Swift锁：互斥锁与同步框架
李汇川谈中国游戏的发展：从《仙剑》到《黑神话》
熊景明谈云南家族与历史的交织"
tags: 
- "滚动行为"
- "Swift"
- "依赖注入"
- "游戏发展"
- "历史"
- "Concurrency"
- "开发工具"
- "机器学习"
- "WebSocket"
- "SwiftUI"
- "SwiftConcurrency"

---

> - 从 Combine 到 Swift Concurrency：线程风险解析
> - ExecuTorch：Meta 推动边缘设备上的机器学习
> - 专业级 WebSocket 调试插件
> - 现代化的基于容器的依赖注入方法：Factory
> - 自定义SwiftUI中的滚动行为
> - Swift并发中的线程与任务
> - 现代Swift锁：互斥锁与同步框架
> - 李汇川谈中国游戏的发展：从《仙剑》到《黑神话》
> - 熊景明谈云南家族与历史的交织

## 🍎 iOS Blog

### [从 Combine 到 Swift Concurrency：线程风险解析](https://www.avanderlee.com/concurrency/combine-and-swift-concurrency-a-threading-risk/)

来源：SwiftLee

发布时间：2025-07-29 06:05:00

随着开发者逐渐从 Combine 迁移到 Swift Concurrency，后者被认为是未来的主流。虽然 Combine 作为一个成熟的框架，近期没有收到更新，但 Swift 团队显然在将重点放在 Swift Concurrency 上。文章深入探讨了在将 Combine 代码迁移至 Swift Concurrency 过程中的潜在线程风险，以及这种转变对开发者和应用程序的影响，强调了 Swift Concurrency 提供的优势和技术未来的趋势。

## 📥 Tech News

### [ExecuTorch：Meta 推动边缘设备上的机器学习](https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/)

来源：Engineering at Meta

发布时间：2025-07-29 04:30:33

ExecuTorch 是 Meta 开发的 PyTorch 推理框架，专为边缘设备而设计，得到 Arm、Apple 和 Qualcomm 等行业领头羊的支持。随着在设备上运行机器学习模型的重要性日益增加，该框架使 Meta 的应用程序能够提升延迟效果、保护用户隐私（通过在本地处理数据）以及实现离线功能。ExecuTorch 的推出标志着在 Meta 应用生态中优化机器学习处理的一个重要进展。

### [专业级 WebSocket 调试插件](https://www.v2ex.com/t/1148616)

来源：V2EX-最新主题

发布时间：2025-07-29 23:14:28

这款WebSocket调试插件适合需要调试WebSocket的开发者。它提供监控、拦截、模拟等多项功能，能够有效解决传统工具中存在的问题，如消息捕获丢失和实时监控，支持简化流量控制和JSON编辑，极大提升调试效率，适合前后端开发者使用。

## 💾 Daily Dev

### [现代化的基于容器的依赖注入方法：Factory](https://github.com/hmlongco/Factory)

来源：iOS Development News - Telegram Channel

发布时间：2025-07-29 10:13:12

Factory提供了一种灵活、安全且高效的Swift和SwiftUI依赖注入方法，使开发者能够根据需求选择不同的注入策略。它支持多种特性，如范围、参数传递和上下文设置，确保代码在编译时的安全性和高效性。同时，Factory文档详尽，示例丰富，帮助开发者轻松上手。该工具非常适合现代应用开发，尤其在测试和预览方面也表现尤为出色。

### [自定义SwiftUI中的滚动行为](https://www.createwithswift.com/define-how-scrolling-behaves-with-scroll-target-behavior-in-swiftui/)

来源：iOS Development News - Telegram Channel

发布时间：2025-07-29 21:03:37

本文介绍了如何使用ScrollTargetBehavior协议在SwiftUI中自定义滚动行为，包括如何实现分页和对齐效果等。通过具体的代码示例，展示了horizontal ScrollView的实现方法，涵盖了滚动目标的更新以及如何控制滚动数量等高级特性。这使开发者能够灵活调整内容滚动与对齐方式，提升用户体验。

### [Swift并发中的线程与任务](https://t.me/iosdevio/6141)

来源：iOS dev - Telegram Channel

发布时间：2025-07-29 19:24:42

本文深入探讨了Swift并发中线程与任务的区别，以及与传统线程方法的对比。通过详细的分析和实例，帮助开发者清晰理解这两者在并发编程中的应用及优势，增强其并发编程能力。

### [现代Swift锁：互斥锁与同步框架](https://t.me/iosdevio/6140)

来源：iOS dev - Telegram Channel

发布时间：2025-07-29 19:24:40

文章介绍了如何使用Swift锁创建线程安全的数据访问，作为Swift并发中actor的替代方案。详细解释了互斥锁的工作原理及其在实现同步机制中的重要作用，适合需要深入掌握多线程安全访问的开发者。

## 📻 Podcast

### [李汇川谈中国游戏的发展：从《仙剑》到《黑神话》](https://www.xiaoyuzhoufm.com/episode/68882c228e06fe8de7306ccf)

来源：三五环

发布时间：2025-07-29 20:00:00

在这期节目中，李汇川回顾了中国游戏的发展历程，特别是从经典的《仙剑奇侠传》到近年来备受关注的《黑神话：悟空》。他分享了自己作为玩家的碎片记忆，探讨了国产游戏在技术与文化上的演变，以及对玩家的影响。这段对话展现了中国游戏产业的不断成长与创新，反映了玩家对故事性和画面品质日益提升的期待。

### [熊景明谈云南家族与历史的交织](https://www.xiaoyuzhoufm.com/episode/68889c6bedf3fa32d51405bf)

来源：忽左忽右

发布时间：2025-07-29 18:16:04

本期节目中，熊景明分享了近代云南的家族往事，探讨了县自治、大后方的历史背景以及西南联大对云南社会的影响。通过叙述个人与家族的故事，揭示了这些历史事件对地方发展的重要性和复杂性，进而引发对当今社会的思考。
