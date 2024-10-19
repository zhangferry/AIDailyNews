---
title: "Daily News #2024-10-19"
date: "2024-10-19 21:27:56"
description: "揭露iOS Find My中的通知权限绕过漏洞
挑战自我的数字华容道游戏
Meta与Blumhouse合作开发AI电影生成模型
洞悉人生的智慧：《纳瓦尔宝典》读书笔记
Kingfisher：强大的Swift图片下载与缓存库
Manim：精准动画引擎
ManimCommunity：开源动画引擎
DeskPad：虚拟显示器解决屏幕分享问题"
tags: 
- "读书笔记"
- "益智游戏"
- "macOS"
- "AI"
- "安全漏洞"
- "Swift"
- "动画技术"
- "图像处理"
- "屏幕分享"

---

> - 揭露iOS Find My中的通知权限绕过漏洞
> - 挑战自我的数字华容道游戏
> - Meta与Blumhouse合作开发AI电影生成模型
> - 洞悉人生的智慧：《纳瓦尔宝典》读书笔记
> - Kingfisher：强大的Swift图片下载与缓存库
> - Manim：精准动画引擎
> - ManimCommunity：开源动画引擎
> - DeskPad：虚拟显示器解决屏幕分享问题

## 📥 Tech News

### [揭露iOS Find My中的通知权限绕过漏洞](https://blog.devin.dog/posts/find-my-consent-bypass/)

来源：Hacker News - Newest: "apple"

发布时间：2024-10-19 20:22:23

本文作者发现，在使用越狱iPhone进行HTTPS流量拦截时，发现iOS Find My应用的重复通知功能存在漏洞。该功能允许用户与他人共享位置，同时要求对方同意通知。然而，经过详细分析后，发现通知的‘acceptanceStatus’字段可以被客户端操控，导致用户未授权即可创建位置通知。作者利用这一点成功绕过权限控制。此漏洞已向苹果报告并已修复，作者也获得了苹果安全奖励。文章对安全研究人员具有重要启示，强调在发现平台安全问题时，考虑多种策略探查系统的隐蔽部分。

### [挑战自我的数字华容道游戏](https://www.v2ex.com/t/1081789)

来源：V2EX-最新主题

发布时间：2024-10-19 21:06:11

这款数字华容道游戏是一款旨在提高玩家逻辑思维和空间推理能力的在线益智游戏，适合各个年龄段的玩家。提供多样化的棋盘选择和实时反馈，鼓励休闲娱乐和智力训练。产品采用响应式设计，支持多种操作方式，完全免费且不需要注册，非常适合作为教育工具和智力挑战。

### [Meta与Blumhouse合作开发AI电影生成模型](http://www.geekpark.net/news/342008)

来源：极客公园

发布时间：2024-10-19 09:14:06

Meta宣布与Blumhouse合作开发AI视频生成模型Movie Gen。此技术将创建逼真的视频与音频片段，标志着技术与影视创作的深度结合。

### [洞悉人生的智慧：《纳瓦尔宝典》读书笔记](https://www.v2ex.com/t/1081791)

来源：V2EX-最新主题

发布时间：2024-10-19 21:08:15

《纳瓦尔宝典》汇集了纳瓦尔·拉维坎特的智慧与实用建议。作者以读书笔记的形式分享了个人收获，包括财富的本质、内在修炼幸福、积累财富的方法及人生策略等核心内容。书中强调拥有时间和选择自由的重要性，鼓励读者关注长期目标与良好习惯，是一本值得反复阅读的经典。

## 💾 Daily Code

### [Kingfisher：强大的Swift图片下载与缓存库](https://github.com/onevcat/Kingfisher)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-10-19 21:25:44

Kingfisher是一个功能强大的纯Swift库，专门用于从网络下载和缓存图像。它支持异步下载、数据缓存、图像处理及多层混合缓存，提供细致的缓存控制和自定义选项。支持SwiftUI，并兼容最新的Swift版本，能实现简单的API调用和复杂的链式方法。开发者可以轻松实现图像的下载、处理及展示，极大简化开发流程。

### [Manim：精准动画引擎](https://github.com/3b1b/manim)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-10-19 21:25:47

Manim是一个用于创建解释性数学视频的动画引擎，支持精确的程序动画。最初由3Blue1Brown的作者开发，后于2020年分叉出社区版，旨在提高稳定性、可测试性和易用性。其安装需依赖Python 3.7及以上和FFmpeg等工具，且分不同版本。文档和社区持续维护着安装和使用指南，鼓励开发者贡献代码。

### [ManimCommunity：开源动画引擎](https://github.com/ManimCommunity/manim)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-10-19 21:25:47

ManimCommunity是一个开源的动画引擎，专为数学视频而设计，能够精确地进行动画编程。此仓库由Manim社区维护，与3Blue1Brown无直接关联。提供丰富的安装指南、使用示例和文档，支持在Jupyter等环境中使用。社区鼓励贡献，并提供多种支持平台，积极接收使用和功能的反馈。

### [DeskPad：虚拟显示器解决屏幕分享问题](https://github.com/Stengo/DeskPad)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-10-19 21:25:44

DeskPad是一个用于屏幕分享的虚拟监视器，适用于需要同时展示多个应用的场景。它可以在应用窗口中镜像显示虚拟显示器，轻松创建专用、可分享的工作区。该应用在macOS中用作实际显示器，支持系统偏好设置更改分辨率，并在鼠标移动至虚拟显示器时提供视觉提示，提升用户体验。
