---
title: "Daily News #2024-09-12"
date: "2024-09-12 09:39:24"
description: "发布设备树补丁以在 Apple A7 至 A11 设备上启动 Linux
星际战士：堕落的九大军团
基于模拟器的强化学习，用于数据中心冷却优化
前端使用加解密方式容易暴露密钥，使用 wasm-pack 隐藏密钥
在 Zoom 房间定时推流视频
Composable Architecture
Stats
HivisionIDPhotos：证件照智能制作算法
Linutil：Linux 实用工具箱
互联网拆墙史：从淘宝封杀微信到小程序的诞生
哈里斯对战特朗普：辩论中的攻守易势与关键政策互殴"
tags: 
- 'Composition'
- 'Ergonomics'
- 'Sensors information'
- '星际战士'
- 'UIKit'
- '互联网'
- 'Side effects'
- '加密'
- 'Bluetooth devices'
- 'State management'
- 'wasm-pack'
- 'Fan's control'
- '战锤40K'
- 'Linux'
- '美国大选'
- '技术'
- 'Network usage'
- 'Multiple time zone clock'
- 'Disk utilization'
- 'Testing'
- '数据中心'
- 'Zoom'
- '荷鲁斯之乱'
- 'System monitor'
- '混沌邪神'
- '工具箱'
- '前端'
- 'CPU utilization'
- '证件照'
- 'Memory usage'
- 'Battery level'
- '推流'
- 'SwiftUI'
- 'GPU utilization'
- 'macOS'

---

> - 发布设备树补丁以在 Apple A7 至 A11 设备上启动 Linux
> - 星际战士：堕落的九大军团
> - 基于模拟器的强化学习，用于数据中心冷却优化
> - 前端使用加解密方式容易暴露密钥，使用 wasm-pack 隐藏密钥
> - 在 Zoom 房间定时推流视频
> - Composable Architecture
> - Stats
> - HivisionIDPhotos：证件照智能制作算法
> - Linutil：Linux 实用工具箱
> - 互联网拆墙史：从淘宝封杀微信到小程序的诞生
> - 哈里斯对战特朗普：辩论中的攻守易势与关键政策互殴

## 📥 Tech News

### [发布设备树补丁以在 Apple A7 至 A11 设备上启动 Linux](https://www.phoronix.com/news/Linux-DT-Patches-A7-To-A11)

来源：Hacker News - Newest: "apple"

发布时间：2024-09-11 22:22:37

已发布设备树补丁，供审查在 Apple A7 至 A11 设备上启动 Linux。这些补丁使在这些设备上运行 Linux 成为可能，为开发人员和用户提供了更多选择。

### [星际战士：堕落的九大军团](http://www.zhihu.com/question/666669754/answer/3621783069?utm_campaign=rss&utm_medium=rss&utm_source=rss&utm_content=title)

来源：知乎每日精选

发布时间：2024-09-11 11:50:22

在战锤40K的世界中，星际战士是强大的战士，但有九个军团在荷鲁斯之乱中堕落，原因包括对帝皇的失望、极端理念和混沌邪神的腐化。这些堕落军团与邪神结盟，成为混沌在现实世界中的代言人。

### [基于模拟器的强化学习，用于数据中心冷却优化](https://engineering.fb.com/2024/09/10/data-center-engineering/simulator-based-reinforcement-learning-for-data-center-cooling-optimization/)

来源：Engineering at Meta

发布时间：2024-09-11 00:00:31

Meta 分享了强化学习在优化数据中心环境控制中所扮演的角色。基于强化学习的方法帮助 Meta 在各种天气条件下降低了数据中心能耗和用水量。Meta 正在改造其新的数据中心设计，以优化人工智能和机器学习模型的训练和部署。

### [前端使用加解密方式容易暴露密钥，使用 wasm-pack 隐藏密钥](https://www.v2ex.com/t/1072132)

来源：V2EX-最新主题

发布时间：2024-09-11 23:33:45

在前端使用加解密方式容易暴露密钥，作者使用 wasm-pack 将密钥隐藏在二进制中，并提供了踩坑指南和使用说明。该项目使用国密库 smcrypto，支持 PKCS5Padding 模式，并使用 dotenv 达成编译阶段注入变量的目的。

### [在 Zoom 房间定时推流视频](https://www.v2ex.com/t/1072129)

来源：V2EX-最新主题

发布时间：2024-09-11 23:02:03

作者想要定时向 Zoom 房间推流视频，希望在 Linux 服务器上部署 srs 等软件实现，但 Zoom 设置中只找到了把 Zoom 推流到 YouTube 等平台的选项。作者希望有大佬解答 Zoom 房间是否可以接入推流。

## 💾 Daily Code

### [Composable Architecture](https://github.com/pointfreeco/swift-composable-architecture)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-09-12 08:12:12

The Composable Architecture is a library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. It can be used in SwiftUI, UIKit, and more, and on any Apple platform (iOS, macOS, visionOS, tvOS, and watchOS).

### [Stats](https://github.com/exelban/stats)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-09-12 08:12:12

Stats is an application that allows you to monitor your macOS system. It provides real-time information on CPU utilization, GPU utilization, memory usage, disk utilization, network usage, battery level, fan's control, sensors information, Bluetooth devices, and multiple time zone clock.

### [HivisionIDPhotos：证件照智能制作算法](https://github.com/Zeyi-Lin/HivisionIDPhotos)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-09-12 04:44:10

HivisionIDPhotos 是一款证件照智能制作算法，它利用一套完善的 AI 模型工作流程，实现对多种用户拍照场景的识别、抠图与证件照生成。它可以做到轻量级抠图、根据不同尺寸规格生成不同的标准证件照、六寸排版照，支持纯离线或端云推理、美颜（等待中）、智能换正装（等待中）。

### [Linutil：Linux 实用工具箱](https://github.com/ChrisTitusTech/linutil)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-09-12 04:44:10

Linutil 是一款面向 Linux 系统的实用工具箱，它可以帮助用户简化日常任务，设置应用程序并针对特定用例优化系统。该工具箱使用 Rust 语言开发，具有高性能和可靠性。Linutil 目前仍在积极开发中，用户可能会遇到一些问题，欢迎提交反馈。

## 📻 Podcast

### [互联网拆墙史：从淘宝封杀微信到小程序的诞生](https://www.xiaoyuzhoufm.com/episode/66e18715ee04007d88d3eacf)

来源：乱翻书

发布时间：2024-09-11 20:03:32

本期节目邀请阑夕和戴某DEMO两位嘉宾，围绕互联网平台之间的开放与封闭展开讨论。他们回顾了淘宝封杀微信等平台的“二选一”事件，分析了互联网平台开放和封闭的历程，以及小程序作为最优解的原因。节目深入浅出，内容丰富，对理解互联网行业的发展有很大帮助。

### [哈里斯对战特朗普：辩论中的攻守易势与关键政策互殴](https://www.xiaoyuzhoufm.com/episode/66e1868b79de2cd416c86ac1)

来源：声东击西

发布时间：2024-09-11 20:00:00

在首场总统辩论中，哈里斯表现稳健，力压特朗普。特朗普的攻击性言论被哈里斯巧妙化解，在关键政策上双方展开激烈交锋。哈里斯在移民问题上成功反击特朗普，并得到泰勒·斯威夫特等名人的支持。辩论结果对哈里斯有利，为其竞选增添了动力。
