---
title: "Daily News #2024-08-29"
date: "2024-08-29 09:37:58"
description: "A2Pico：基于树莓派Pico的Apple II外围卡
🎉 Meta如何通过隐私感知基础设施大规模实施目的限制
📸《黑神话：悟空》丨游戏摄影（一）
🎙️世界尽头的酒馆Vol.51丨亡命天涯
🌟 Feather：iOS 设备上的免费应用程序管理器/安装程序
🌟 Telegram iOS 源代码编译指南
🚀 一键安装黑客工具箱，无需虚拟机或 Docker
🕵️‍♂️ 跨 400 多个社交网络搜索社交媒体账户"
tags: 
- '应用程序管理'
- 'Telegram'
- '开源硬件'
- '隐私'
- '播客'
- '社交媒体搜索'
- '游戏摄影'
- '黑客工具'
- 'iOS'

---

> - A2Pico：基于树莓派Pico的Apple II外围卡
> - 🎉 Meta如何通过隐私感知基础设施大规模实施目的限制
> - 📸《黑神话：悟空》丨游戏摄影（一）
> - 🎙️世界尽头的酒馆Vol.51丨亡命天涯
> - 🌟 Feather：iOS 设备上的免费应用程序管理器/安装程序
> - 🌟 Telegram iOS 源代码编译指南
> - 🚀 一键安装黑客工具箱，无需虚拟机或 Docker
> - 🕵️‍♂️ 跨 400 多个社交网络搜索社交媒体账户

## Apple News

### [A2Pico：基于树莓派Pico的Apple II外围卡](https://github.com/oliverschmidt/a2pico)

来源：Hacker News - Newest: "apple"

发布时间：2024-08-28 11:48:12

A2Pico是一个关于基于树莓派Pico的Apple II外围卡的项目。它由两部分组成：硬件和软件。硬件完全由通孔组件组成，便于DIY组装。软件库避免了低级代码在共享相同硬件的不同固件项目中的重复。A2Pico硬件将/DEVSEL、/IOSEL和/IOSTRB通过AND门组合成ENBL。A0-A7和D0-D7复用到相同的GPIO。D0-D7方向由GPIO控制。A2Pico软件有三个PIO状态机：addr、read和write。ARM核心0以传统方式运行：从缓存的Flash运行，调用C库，被USB库中断等。然而，ARM核心1专门用于与三个PIO状态机交互。因此，它从RAM运行，只调用内联函数，并且永不被中断。

## Tech News

### [🎉 Meta如何通过隐私感知基础设施大规模实施目的限制](https://engineering.fb.com/2024/08/27/security/privacy-aware-infrastructure-purpose-limitation-meta/)

来源：Engineering at Meta

发布时间：2024-08-28 00:00:50

Meta在过去几年一直致力于将隐私融入其软件堆栈的不同系统中。今天，很高兴分享一些尖端技术，这些技术是我们隐私感知基础设施 (PAI) 计划的一部分。这些创新标志着我们持续致力于尊重用户隐私的一个重要里程碑。PAI 提供了 [...]

### [📸《黑神话：悟空》丨游戏摄影（一）](https://www.gcores.com/articles/187331)

来源：机核

发布时间：2024-08-28 19:19:43

《黑神话：悟空》是一款备受期待的国产动作冒险游戏。游戏的画面非常精美，场景设计也十分用心。本文作者通过游戏摄影的方式，展示了《黑神话：悟空》的独特魅力，让玩家可以从另一个角度欣赏这款游戏。

### [🎙️世界尽头的酒馆Vol.51丨亡命天涯](https://www.gcores.com/radios/187401)

来源：机核

发布时间：2024-08-28 21:00:00

《世界尽头的酒馆》是一档游戏播客节目，由机核网制作。节目内容主要围绕游戏展开，涵盖了游戏资讯、游戏评测、游戏文化等多个方面。本期节目邀请到了《猎杀对决》的制作人，聊了聊游戏的开发历程和设计理念。

## Daily Code

### [🌟 Feather：iOS 设备上的免费应用程序管理器/安装程序](https://github.com/khcrysalis/Feather)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-08-29 08:05:46

Feather 是一款免费的 iOS 设备应用程序管理器/安装程序，支持 Altstore 存储库、导入 IPA 文件、注入调整、无线安装应用程序、配置签名选项，并且不跟踪或分析用户数据。

### [🌟 Telegram iOS 源代码编译指南](https://github.com/TelegramMessenger/Telegram-iOS)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-08-29 08:05:46

Telegram iOS 源代码编译指南，详细介绍了如何获取 API ID、创建 Xcode 项目、生成 Xcode 项目以及解决常见问题。

### [🚀 一键安装黑客工具箱，无需虚拟机或 Docker](https://github.com/Z4nzu/hackingtool)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-08-29 07:04:53

该工具箱集合了各种黑客工具，包括匿名隐藏工具、信息收集工具、无线攻击工具、SQL 注入工具、网络钓鱼攻击工具、Web 攻击工具、后渗透工具、取证工具、有效载荷创建工具、漏洞利用框架、逆向工程工具、DDoS 攻击工具、远程管理工具、XSS 攻击工具、隐写术工具和其他工具，涵盖了黑客攻击的各个方面。

### [🕵️‍♂️ 跨 400 多个社交网络搜索社交媒体账户](https://github.com/sherlock-project/sherlock)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-08-29 07:04:53

Sherlock 是一款功能强大的工具，可以跨 400 多个社交网络搜索社交媒体账户。它可以帮助用户通过用户名查找目标的社交媒体资料，并将其存储在单独的文本文件中，方便后续分析和调查。
