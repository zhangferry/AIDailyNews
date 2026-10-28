---
title: "Daily News #2026-10-30"
date: "2026-10-30 08:00:00"
description: >
  不再逐个生成 Token：扩散模型迈向 35B，开始挑战 Agent 编程 Apple 发布全新触屏 MacBook Pro：信仰灯回归、灵动岛取代刘海 Legora is building the agentic operating system for legal work iOS 27.2 发布：UIView 默认边距归零、iPhone Duo 首周适配实录与 Xcode 新工具 智能体时代的新核心技能：Granola 一线工程实践
tags:
- "LLM"
- "AI智能体"
- "Codex"
- "Agentic Engineering"
- "法律科技"
- "M5"
- "MoE"
- "SwiftUI"
- "扩散语言模型"
- "OLED"
- "OpenAI"
- "iPhone Duo"
- "UIKit"
- "AI"
- "ChatGPT"
- "硬件"
- "Agent"
- "开源模型"
- "最佳实践"
- "软件工程"
- "Xcode"
- "Apple"
- "MacBook Pro"
- "iOS"

---

> - 不再逐个生成 Token：扩散模型迈向 35B，开始挑战 Agent 编程
> - Apple 发布全新触屏 MacBook Pro：信仰灯回归、灵动岛取代刘海
> - Legora is building the agentic operating system for legal work
> - iOS 27.2 发布：UIView 默认边距归零、iPhone Duo 首周适配实录与 Xcode 新工具
> - 智能体时代的新核心技能：Granola 一线工程实践

## 📥 Tech News

### [不再逐个生成 Token：扩散模型迈向 35B，开始挑战 Agent 编程](https://www.infoq.cn/article/0tgCLAMXFiFo0Dco5P9m)

来源：InfoQ 推荐

发布时间：2026-10-28 22:53:53
![](https://static001.infoq.cn/resource/image/65/59/65b8f62defda53450bd90fed1c454059.png)
**深圳 AI 创业公司扩散智能开源发布 Clover-35B-A3B-Preview，将扩散语言模型规模推至 350 亿参数，生成速度达 680 tokens/s，在多项 Agent 基准上达到或超过同规模自回归模型。**

* 采用 MoE 架构（总参数 35B、激活约 3B），基于 Qwen3.6-35B-A3B 构建，对门控 Delta 网络（GDN）进行双向化改造并引入块级扩散生成：历史上下文经递归状态压缩，当前生成块内使用双向注意力，兼顾长上下文与并行解码。
* Agent 能力方面，SWE-bench Verified 得分 73.6、Terminal-Bench 2.1 为 51.7、τ³ Overall 为 65.3，超过 Mercury 2.5 与同规模 Qwen3.6；无人机空域管理 Demo 耗时 7.32 秒，约为对照模型的 1/8.5；WindTunnel 测试中位执行时间 1.52 秒，领先多个对照组合。
* 局限在于：通用能力并非全面占优（部分数学、代码评测仍落后），Demo 数据受部署环境与工具调用流程影响，且 Agent 任务总耗时可能集中在外部工具环节，生成速度优势未必直接转化为端到端收益。
* 模型以 Apache-2.0 许可开源，支持 SGLang、llama.cpp 等推理后端；团队后续规划决策模型与多模态模型。

### [Apple 发布全新触屏 MacBook Pro：信仰灯回归、灵动岛取代刘海](https://t.me/AppleNuts/2564)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-29 01:14:39
![](https://cdn5.telesco.pe/file/Hqupmk_dPp_GsY-JAxUY5BLmcWRobXAwRRwsq2WJMgMz0sPLpaNeTj5Q1dTm1Z9WeyDw9YyNbotBeRmdp_e42puX9jQNJMgu2ckYeRVAY1upC4VTGCHxCyqxS55dySoRDv9qThmgbE0b3q94hCIoAiSe2mn5mqyAcAYRWXFaJiHj6helEbVJRoMqorGku_qynz6fzsQ_tHRAaQnKQ1tm1mxaSRRQNhsTS0NU6PtO4HHZv6_gUKd3gthkjk8c4aIwO7_bWXxyYjjJ0IQEMB-Yh6xybZhGgfwWmEjaExwlCMDLb--Pw7DdmOba7M_V8UchxviAmYdmXFaps6p0m5uV6g)
**Apple 发布全新一代 MacBook Pro，首次采用触控 OLED 屏幕，经典发光 Logo（信仰灯）回归，刘海被灵动岛取代。**

* 提供两种尺寸：14 寸售价 ¥22,999 起，16 寸售价 ¥27,999 起，搭载 M5 Pro 或 M5 Max 芯片
* 屏幕升级为可触控 OLED（官方称 ProLED XDR 显示屏），标志 Mac 产品线对触屏交互的正式妥协/尝试
* 预购时间为 10 月 30 日上午 9 点，11 月 6 日正式发售
* 属于产品新闻类资讯，信息密度尚可但无技术深度，适合关注 Mac 硬件迭代的读者

### [Legora is building the agentic operating system for legal work](https://openai.com/index/legora)

来源：OpenAI News

发布时间：2026-10-28 17:30:00

**OpenAI 发布客户故事，介绍法律科技公司 Legora 正在为法律行业构建“智能体操作系统”。**

* Legora 的产品基于 OpenAI 技术栈构建，综合使用了 OpenAI 的底层模型、ChatGPT 以及编程智能体工具 Codex
* 核心目标是加速法律工作流，典型场景包括合同分析，通过自动化处理重复性法律事务，让律师将精力转向更高价值的工作
* 该案例可视为 AI 智能体在法律这一垂直行业落地的代表性实践，适合关注 AI 应用与企业级法律科技的读者
* 需注意本文属于 OpenAI 官方的合作案例宣传，提供的摘要信息有限，具体技术实现与落地细节需进一步参阅原文链接

## 💾 Daily Dev

### [iOS 27.2 发布：UIView 默认边距归零、iPhone Duo 首周适配实录与 Xcode 新工具](https://ioscodereview.com/issues/issue-93-ios-27-2-is-out-uiview-margins-went-to-zero-and-the-duo-is-in-peoples-hands/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-29 00:47:42
![](https://cdn4.telesco.pe/file/svHA8XZKKA0ImhhAMKNfS8lTc8asIHMw4N9zc45LtNtK7EI-1lADdpPpYmPwSs5u-BkYNUX80tV32vgoJs8nLS-ABWdOubvqNdKWI067QaR-3yavMJw4Ts_-P5JiOXD9kgF37HFZmiRYZh1QiHWliuesiuZoNwqgUZdTteSKuH6HDVuqcMPLHeWovJS87Ij77FfFbyZqUfDNJNni7ggb6spT49Nnu-ay3288267Ef23316dImgFQogvf6WtXM0PU2QMs2PX5kGsu8hu1g1kNj1O7ikAuzIdKQkfoZzofbklVtoD8NNWdAiS1pEhM4A7xBUeWOc-zEkhbKFhjcVcqsA.jpg)
**iOS 27.2 正式发布，UIKit 默认布局边距归零成为最可能改变应用外观的变化，iPhone Duo 折叠机也已到用户手中，多项破坏性变更需要开发者立即排查。**

* iOS 27.1 起 UIView 默认 layout margins 从 8 点变为零，依赖 layoutMarginsGuide 的子视图会贴边；可设置 preservesSuperviewLayoutMargins 或显式设置边距修复，SwiftUI 新增 contentMargins(for: .container) 以对齐系统容器边距（部分机型为 20 点而非统一的 16 点 padding）。
* ATT 扩展弹窗 API 在正式版中更名（usingExpandedInterface 改为 preferExpandedInterface），针对 beta 编写的代码无法通过最终 SDK 编译；面向企业和学校的多席位订阅已默认开启，可在 App Store Connect 关闭。
* Xcode 27.2 RC 新增内存压力等模拟器测试工具，以及 xcodeproj 命令行工具，使 CI 脚本和编码代理无需打开 Xcode 即可读写工程文件。
* Duo 首周反馈：SwiftUI Table 存在兼容问题正与苹果工程师排查；Safari 以特性开关预览 Device Posture 与 Viewport Segments API；onHingeChange 可按铰链角度驱动动画。
* URL.path 的官方迁移建议有坑：path(percentEncoded:) 默认返回编码字符串且相对 URL 行为不同，含空格的文件路径会出错，建议改用 absoluteURL.path(percentEncoded: false)。

### [智能体时代的新核心技能：Granola 一线工程实践](https://blog.jacobstechtavern.com/p/the-new-core-skills)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-29 00:12:36
![](https://cdn4.telesco.pe/file/wB7TVm46TlWG-NZwsZjEihoy35qCBiWLKx9dSA5EZm8JG_gaLkJgcmR56MupZeQOR71cA_W1UNAc0J2uffRBCvjCj9WN3oDo6jtCI4WDAzA6vNT_vk1vEEOMmkAwp_rpetp7ugDicq_Mq290lUSXbmowMy0bwEgPT7MNZjetisv2SFlB1ocBga2O5TalnjKYIB2qj86yk_gG1J1pICDpUzXjd2wywI-IGQXVPqRfFYCJLCeVpI4B51B5yu0gG91bddG9Tr38AOBErj_ybJg2XpB5kCZwF1y4eUeDDeLfPFyk39NmF8geab9UUl7AgnR7xBIR6ujdie9ZiC1mT-Smqw.jpg)
**作者以 AI 笔记应用 Granola 工程师的亲身经历，描绘软件开发从手写代码转向智能体工程后核心技能的重构，该文获 Pragmatic Engineer 征文比赛奖项。**

* 抽象层级在过去一年快速跃迁：从逐行编码、照看代理写文件，到用前沿模型直接构建完整系统；许多曾被视为最高价值的技能受到质疑，但定义架构、规划与验证等基本功愈发关键。
* 核心实践包括：先用详细 prompt 定义组件架构与接口，再让 Claude、Codex 等多个代理并行执行并择优；借助语音输入快速传递意图（"just talk to it"）；为代理设计自验证环节——自行编译、跑冒烟测试、读日志并修复问题，从而敢于委派小时级任务。
* 多代理并行的动机并非单纯求快：高投入档位的模型错误更少但速度更慢，只有执行可被可靠委派后，并行运行多个项目才能真正提升吞吐。
* 文章警示"知识债"（knowledge debt）风险：不手写代码时大脑容易懈怠，微小改动也可能产生巨大 diff；应借鉴 Riot Games 技术债"传染性"框架，主动选择在何处投入认知与注意力去控制复杂度。
