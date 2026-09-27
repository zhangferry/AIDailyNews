---
title: "Daily News #2026-09-29"
date: "2026-09-29 08:00:00"
description: >
  谷歌发布 Kotlin 版 ADK 1.0：与 Python/Java 功能对齐，支持 Android 端侧与混合 AI 当 AI 比哲学家更会思考，人类该怎么办？ Replacing the old battery on rechargeable bike lights App Store 审核失守：Meta Muse 遭山寨应用 blatant 抄袭仍过审 使用 Bazel 的 --run_under 标志在包装器下运行目标
tags:
- "AI对齐"
- "构建工具"
- "教育"
- "macOS"
- "ADK"
- "Monorepo"
- "AI Agent"
- "创客空间"
- "电子DIY"
- "电池更换"
- "App Store"
- "应用诈骗"
- "思想实验"
- "硬件维修"
- "焊接"
- "Meta"
- "Kotlin"
- "平台治理"
- "哲学"
- "AI"
- "性能分析"
- "Android"
- "端侧 AI"
- "Bazel"

---

> - 谷歌发布 Kotlin 版 ADK 1.0：与 Python/Java 功能对齐，支持 Android 端侧与混合 AI
> - 当 AI 比哲学家更会思考，人类该怎么办？
> - Replacing the old battery on rechargeable bike lights
> - App Store 审核失守：Meta Muse 遭山寨应用 blatant 抄袭仍过审
> - 使用 Bazel 的 --run_under 标志在包装器下运行目标

## 📥 Tech News

### [谷歌发布 Kotlin 版 ADK 1.0：与 Python/Java 功能对齐，支持 Android 端侧与混合 AI](https://www.infoq.cn/article/sQV4EomjPP0J3hM3lyF9)

来源：InfoQ 推荐

发布时间：2026-09-27 10:00:00
![](https://static001.infoq.cn/resource/image/fb/17/fbe60b4d62f64b6c19bdd270be271517.jpg)
**谷歌正式发布 Kotlin 版 Agent Development Kit（ADK）1.0，这是在 Kotlin、Android 和 JVM/服务器应用中构建 AI 智能体的生产级框架，使 Kotlin 与 Python、Java 版 ADK 功能对齐，并新增面向 Android 的端侧与混合 AI 能力。**

* 框架基于 Kotlin Multiplatform 构建，可运行于服务器与移动设备，架构不绑定特定模型后端、会话提供程序或记忆系统；新增层级化多智能体任务委派、自动上下文压缩与历史摘要（降低 token 消耗）、支持暂停/序列化/恢复的会话管理，以及一流的 Java 互操作性。
* 工具调用通过 @Tool、@Param 注解由 KSP 在编译期生成描述规约，无需运行时反射，兼顾类型安全与移动端启动性能；人在回路工作流只需设置 requireConfirmation，即可在银行转账等敏感操作前强制人工确认。
* 技能（SKILL.md）采用渐进式披露机制按需加载领域知识，避免占满模型上下文；端侧推理支持 LiteRT-LM 与测试版 ML Kit，云端及混合场景可集成 Firebase AI Logic。项目已开源。

### [当 AI 比哲学家更会思考，人类该怎么办？](https://www.bestblogs.dev/video/cc0a61dd1?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-27 10:35:04
![](https://media.bestblogs.dev/20260927133339_hq720.jpg)
**复旦哲学教授孙向晨基于用自己著作训练的哲学智能体实验，探讨 AI 创造的思想归属、德性对齐与人类判断力等核心议题。**

* 智能体提出「有根的自由」概念，恰好概括了他此前关于家与自由的思考，但造词不等于独立的理论创造——真正的哲学创新需要可追溯的论证、解释具体问题的力量，以及接受反驳的能力。
* 在对齐问题上，规则是底线，但复杂情境还需德性与多文明思想资源支撑，儒家等传统应进入公开讨论，单一文明不能替全人类决定价值。
* 教育层面的警示尤为有力：若学生只读顺畅的 AI 摘要，会失去在艰难阅读与争辩中形成判断力的过程，好问题来自长期训练而非便捷获取。
* 面对多元智能，人类需从控制幻想转向有边界的共生，「止」、留白、和而不同是反思技术加速的思想资源；访谈明确区分了当前模型能力与具身自主 AI 的未来设想，提出的问题多于现成方案。

### [Replacing the old battery on rechargeable bike lights](https://jvns.ca/blog/2026/09/27/replacing-the-old-battery-on-rechargeable-bike-lights/)

来源：Julia Evans

发布时间：2026-09-27 08:00:00
![](https://jvns.ca/images/pcb.png)
**知名博主 Julia Evans 分享了一次几乎零电子基础的维修实践：两盏十年前购买的可充电自行车灯因电池老化只能亮 5 分钟，她在创客空间自行更换锂电池，零件总花费约 20 加元即成功修复。**

* 维修流程包括切开硅胶外壳、拆螺丝取出电路板，参考 iFixit 拆焊指南并结合朋友建议完成首次拆焊；过程中注意间歇操作让电池冷却以防过热，电池顶部焊接的金属连接片无需拆除，替换电池自带该部件。
* 旧电池型号标印模糊，作者借助 LLM 判断为 LIR2477，随后在 AliExpress 以每颗 3 美元购入两颗，另花 8 美元买硅胶胶水重新粘合外壳，等件约两周。
* 局限与遗留问题：操作中丢失了部分极小的螺丝，胶合工艺较粗糙，且 Mini USB 线尚未到手，新电池实际续航仍未验证；作者也明确说明本文不含安全建议。
* 对想入门硬件维修的读者而言，这是一个低成本、低门槛的示范案例，也顺带展示了社区创客空间对新手的帮助价值。

## 💾 Daily Dev

### [App Store 审核失守：Meta Muse 遭山寨应用 blatant 抄袭仍过审](https://lapcatsoftware.com/articles/2026/9/8.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-27 23:27:22
![](https://cdn4.telesco.pe/file/ekMQ6jRhnkywubaJvzaSCKWJDxEVPttAQvaPTPjTudBKAn8xMI8qLHl48GSsxuodYbkrNmnrBQJmmz6f0oA3gCxCqwYKyk2rwmGdweiqEmLj5vPCcy_sg5mNeiealaIqe_WW7jpDL9baUixnC6oZIfOT8n_dmh34955RMhdoKGZsNRKlcFnS26A2sXS-0siK1BcNAIhRTKXfvwpqmr551_hHhp9pR4WiQNV6ceXjBHY32V2ezDBlaTRhwCTDFkS8qGMB46lUU8nzqr6y9HwglNKBkbqs9XR7yj8-ppy_tzJLySO0yVQCo4b8Dtu3oY_6ejFCgRve3u2pNAN4QHVQYQ.jpg)
**App Store 审核再次失守：一款名为 Muse AI 的应用公然抄袭 Meta 的 Muse（当前美区 iOS 下载榜第一），图标、副标题、截图文案和应用描述几乎逐句照搬，仅做同义词微调便通过审核，三周内已冲上 Mac App Store 美区下载榜第 20 名。**

* 抄袭手法隐蔽但明显：将 "Your personal AI agent" 改为 "Your professional AI Agent"、"SMART" 改为 "POWERFUL" 等；最新更新说明甚至直言"引入了新的 Muse 品牌标志"，审核仍未察觉
* 已有用户误认其为 Meta Muse 而订阅了每月 20 美元的高额内购，事后才发觉是不同服务
* 作者同时曝光 "App for Instagram º" 与 "Video Player for VLC" 等同类山寨应用，均利用官方应用未上架 Mac App Store 的空档抢占搜索首位
* 山寨应用的典型红旗：隐私政策托管在免费的 sites.google.com、无官方网站、3 天自动续订试用、弹出的付费窗口无法关闭，甚至阻止用户退出应用或重启系统
* 文章揭示了苹果审核流程与 Mac App Store 搜索排序机制的系统性漏洞，对开发者和普通用户都有警示价值

### [使用 Bazel 的 --run_under 标志在包装器下运行目标](https://adincebic.com/2026/09/27/running-bazel-targets-under-another.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-27 20:57:08
![](https://cdn4.telesco.pe/file/ekMQ6jRhnkywubaJvzaSCKWJDxEVPttAQvaPTPjTudBKAn8xMI8qLHl48GSsxuodYbkrNmnrBQJmmz6f0oA3gCxCqwYKyk2rwmGdweiqEmLj5vPCcy_sg5mNeiealaIqe_WW7jpDL9baUixnC6oZIfOT8n_dmh34955RMhdoKGZsNRKlcFnS26A2sXS-0siK1BcNAIhRTKXfvwpqmr551_hHhp9pR4WiQNV6ceXjBHY32V2ezDBlaTRhwCTDFkS8qGMB46lUU8nzqr6y9HwglNKBkbqs9XR7yj8-ppy_tzJLySO0yVQCo4b8Dtu3oY_6ejFCgRve3u2pNAN4QHVQYQ.jpg)
**Bazel 的 --run_under 标志可以在执行二进制前自动 prepend 一个包装命令或脚本，免去手动构建再包装的繁琐流程，适用于性能分析、调试器挂载、环境注入等场景。**

* 基本用法：`bazel run //:xcodeproj --run_under="time"` 会在目标前加上 time 命令输出耗时统计；也支持带参数的命令前缀，如 `time -p`
* 该标志并非 bazel run 专属，同样适用于 bazel test
* 进阶用法：--run_under 的值可以直接引用仓库内的另一个 Bazel 目标（如 `//tools:my_wrapper`），Bazel 会同时构建两者并用前者包装后者，无需依赖宿主机上单独安装的工具
* 这个 2015 年就存在的功能较为冷门，但在包装脚本本身就在 monorepo 中、希望由 Bazel 统一管理构建的场景下非常实用
