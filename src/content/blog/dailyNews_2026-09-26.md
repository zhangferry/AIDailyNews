---
title: "Daily News #2026-09-26"
date: "2026-09-26 08:00:00"
description: >
  JEV：一个不会写代码的模型，为什么拿下 4000 万美元？ 百万级仿真资产，正在重构机器人训练场：阿里巴巴 RoboFlywheel 首发 数据、模型、算力越来越难分开，Data+AI 基础设施怎么进化？ Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind. iOS Code Review #88：Xcode 27.2 引入 JSON 项目格式，iPhone Duo 模拟器与垂直工具栏落地
tags:
- "AI Coding"
- "基础设施"
- "仿真"
- "开源"
- "iOS"
- "AI 架构"
- "AI Agent"
- "Data+AI"
- "模型推理"
- "iPhone Duo"
- "概率校准"
- "Claude"
- "SwiftUI"
- "Xcode"
- "AI"
- "具身智能"
- "阿里云"
- "机器人"
- "LLM"
- "架构"
- "工具链"
- "成本优化"
- "缓存优化"

---

> - JEV：一个不会写代码的模型，为什么拿下 4000 万美元？
> - 百万级仿真资产，正在重构机器人训练场：阿里巴巴 RoboFlywheel 首发
> - 数据、模型、算力越来越难分开，Data+AI 基础设施怎么进化？
> - Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.
> - iOS Code Review #88：Xcode 27.2 引入 JSON 项目格式，iPhone Duo 模拟器与垂直工具栏落地

## 📥 Tech News

### [JEV：一个不会写代码的模型，为什么拿下 4000 万美元？](https://www.bestblogs.dev/article/6694786bc0?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-24 08:45:00
![](https://image.jido.dev/20251127045410_4d44587a)
**TypeSafe AI 发布的 JEV 模型将判断从生成中解耦：通过非自回归并行采样与 RLCD 概率校准，构建低时延、概率可信的 System 1 决策器，拿下 4000 万美元融资。**

* 传统自回归模型处理分类、路由等控制流任务时存在延迟高、格式不稳定、概率不可信的问题；JEV 放弃逐 token 生成，直接在预定义类型空间采样，规避线性延迟与 JSON 解析失败风险。
* 核心价值在概率校准而非单纯速度：RLCD 训练使输出概率与实际正确率对齐，模型说 0.9 就能真的当 90% 用，置信度可直接作为业务代码中的 if-else 门限。
* 文章据此提出 System 1（快判断）与 System 2（慢推理）的分层架构：高频时延敏感任务交给小模型，仅在置信度不足或需复杂推理时升级至大模型，兼顾效果与算力成本，并给出基于 ModernBERT 复现决策器的工程思路。
* 需注意校准保证的是诚实而非能力，架构层面判断与生成的分工是理解本文的关键。

### [百万级仿真资产，正在重构机器人训练场：阿里巴巴 RoboFlywheel 首发](https://www.bestblogs.dev/article/47c6b617d6?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-24 18:02:00
![](https://image.jido.dev/20260527050038_b20a9a1.jpeg)
**阿里巴巴开源 RoboFlywheel 仿真基础设施，构建覆盖刚体、铰链与柔性物体的百万级资产库，为具身智能提供从资产生成、物理建模到跨引擎评测的闭环训练支撑。**

* 刚体数据集 RoboFlywheel-Rigid 将处理粒度下沉至部件级别，通过多凸体分解保留可交互结构（如杯把孔洞），补齐碰撞几何、质量、质心、惯量与摩擦等属性，使视觉模型与物理对象的差距可被检查，支持抓取与提举评测。
* 铰链物体生成器通过编码结构规则与关节约束，批量产出柜门、抽屉等长尾物体，运动学通过率达 99.93%，并验证了被动稳定性与跨仿真引擎兼容性。
* 柔性资产 RoboFlywheel-Soft 将可变形材质分为五类几何家族，以视觉先验与仿真反馈循环生成物理信息包，支持布料、袋子等复杂交互及完整性与安全施力评估。
* 项目核心理念是造出机器人真正能上手的世界，而不仅是看起来很真的世界，适合具身智能与机器人研发方向的读者关注。

### [数据、模型、算力越来越难分开，Data+AI 基础设施怎么进化？](https://www.infoq.cn/article/amffXXMpr23rX3eoJDhv)

来源：InfoQ 推荐

发布时间：2026-09-24 16:34:30
![](https://static001.infoq.cn/resource/image/35/8b/351a8173b8c8568a87d4362f8223d18b.jpeg)
**文章基于云栖大会信息深度分析AI进入真实世界后数据基础设施的演进：数据从模型训练前的“原料”变为贯穿智能产生、应用与进化全程的“血液”，阿里云据此提出“从数据到智能、从智能到应用、从应用到进化”三阶段框架。**

* 具身智能数据链路极为复杂，一个数据版本从采集到进入训练需两周至一个月；生产训练数据本身已成为同时消耗CPU、GPU、模型Token、存储与网络的异构资源协同计算，MaxCompute AI计算引擎因此将三者纳入统一调度，穹彻智能数据吞吐提升超10倍
* 数据墙的内涵已从“数据够不够”转向“已有数据能否低成本、高速度地被筛选、质检、标注并转化为可用训练数据”，精细化管理成为新瓶颈
* 面向Agent时代，OpenLake向Agentic Lake演进，提出数据沙箱与“Data Agent Ready”概念，让Agent在受约束环境中发现资产、理解语义并调用多引擎
* 自进化方向：PAI-CrystalLLM训练“风洞”用32卡仿真8192卡训练，资源节省超99%、迭代时间预测误差0.58%；Hologres自优化循环带来3.2倍性能提升并登顶TPC-H榜单

文章的核心判断是：AI基础设施的竞争单位正从“一次计算”变成“一次智能迭代”的完整周期，数据流动与反馈闭环效率直接决定智能演进速度。

## 🤖 AI Coding

### [Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.](https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context)

来源：Claude Blog

发布时间：2026-09-24 08:00:00
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab54d371474ec5e28cb0912_0dfedac7.png)
**Anthropic 发布 Claude Opus 5.5，针对更长、更高上下文消耗的编码会话优化定价与模型行为，典型工作负载的运行成本较 Opus 5 降低约 40%。**官方数据显示，2026 年 3-9 月间 Claude Code 使用模式发生明显变化：单个提示的工作时长增至 3.3 倍，每提示的模型调用增加 40% 以上，人工打断减少 68%；单请求上下文量增长 2.6 倍，输入输出 token 比从 189:1 升至 324:1，开发者正将 Claude 指向更大规模的开放式任务。

* 成本优化来自三方面：按 token 计费下输入输出价格下调 20%，缓存读取价格下调 60%（缓存读取占代理编码成本的大头）；Claude Code 通过修复缓存误伤问题（未命中输入减少 50% 以上）、支持一小时缓存生命周期、派生子代理复用父级缓存等方式提升缓存利用率；模型在开放式任务上完成同样工作所需轮次更少。
* 实测方面，Zeta Labs 在成本近半的情况下完成了两倍的最难任务；输出速度比 Opus 5 快 30% 以上。但轮次节省主要体现在开放式任务，边界清晰的小任务收益有限。
* 文末给出实践建议：会话开始即选定模型避免中途切换、离开前主动 compact、长会话设置一小时缓存生命周期，可用 /usage 命令检查缓存读取占比。

## 💾 Daily Dev

### [iOS Code Review #88：Xcode 27.2 引入 JSON 项目格式，iPhone Duo 模拟器与垂直工具栏落地](https://ioscodereview.com/issues/issue-88-your-project-file-goes-json-the-duo-simulator-lands-and-toolbars-turn-sideways/)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-25 01:47:29
![](https://cdn4.telesco.pe/file/gGUHlDBGRQkMSVYQz-5q6bda0Sqp5tVWFEPevOtk6-KmyHTT52hiqZYLfdrHeqepjIVFWBS0-ZwCFihvA-1LD7CHlMeA-j3p_uX6FSxwvix6r4fOIIu7e4JvUD0rsfpcmrLVubGXoNda95RKhfKbjTvcjMbyN83Hjz5hLSUddQkxlOoiMQwhvmBno9jWgbGq0miZnurspUfWquTxDCSwkQlJOYXjQW_aplsqVqCLcme4_if9eNinuHFxwOPCbiHgY9b-9opu-qC9DypihlzZ-kaLUTfhIzic9Eq9zLc2rIv2mcoANUO81lNFZCH8MAtF8LEMjD28CeAPWDM2eEADQQ.jpg)
**本期聚焦两个重要 beta：Xcode 27.2 引入 JSON 项目格式 project.xcproj，有望让 project.pbxproj 的合并冲突成为历史；Xcode 27.1 则带来 iPhone Duo 模拟器及其适配 API。**

* Xcode 27.2 beta 的 JSON 格式更可读、合并友好、便于 AI 编码代理编辑，新项目默认启用，旧项目可在 File inspector 中切换。注意仅 Xcode 27+ 可打开，且只替换构建图（schemes、Package.resolved 不变），Tuist 暂不受影响、XcodeGen 需等适配，回退可从版本控制恢复 pbxproj。
* Xcode 27.1 beta 含 iOS 27.1 SDK、Swift 6.4 与 Duo 模拟器运行时，需 macOS Tahoe 26.6+。iOS 27.1 仅服务 10 月 23 日发售的 iPhone Duo，其余设备从 27.0 直升 27.2。已知问题包括模拟器首启慢、App 扩展无法调试；Catalyst 构建需用 #if !targetEnvironment(macCatalyst) 包裹 27.1 专属 API。社区 CLI 工具 hinge 可从命令行控制模拟器折叠角度。
* iPhone Duo 垂直工具栏通过 axisBehavior、toolbarVerticalEdge、toolbarVerticalCompressionBehavior、toolbarVerticalBehavior 四个新 API 控制条目迁入屏幕边缘竖条；sheets、alerts 等系统组件已内置避折行为，自定义覆盖层需优先测试。
* 另附实用的低版本回退方案：用 @available 引入/废弃标记封装新 API，待部署目标提升后编译器会自动提醒删除包装层。
