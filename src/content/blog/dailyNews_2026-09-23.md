---
title: "Daily News #2026-09-23"
date: "2026-09-23 08:00:00"
description: >
  一场关于 SwiftUI 动画的“原生”之争 - 肘子的 Swift 周报 #154 从 AI Coding 到 Harness Engineering 的端到端工程开发实践 阿里达摩院医疗 AI，十年拼出一张图 70强项目观察之前沿探索：AI进入科学发现，答案之外还要验证什么 OpenAI 阐述构建 AI 下一发展阶段全球标准的路径 Apple 发布 iOS 27.2 beta 2 等全平台测试版更新 OpenAI 成立数学与人工智能咨询小组 macOS 26.4 静默为登录钥匙串开启 Data Protection，破坏灾难恢复能力 让端侧 AI 摘要适应真实文章长度：token 预算、裁剪与缓存实践
tags:
- "AI 安全"
- "macOS"
- "Keychain"
- "医学影像"
- "AI 工程"
- "苹果开发"
- "Swift"
- "beta"
- "标准"
- "Foundation Models"
- "AI"
- "技术周报"
- "Data Protection"
- "科学前沿"
- "系统更新"
- "数据恢复"
- "可验证性"
- "端侧AI"
- "性能优化"
- "OpenAI"
- "DevOps"
- "AI 应用"
- "数学"
- "AI Agent"
- "成果评审"
- "科学发现"
- "安全"
- "iOS"
- "知识库"
- "AI for Science"
- "SwiftUI"
- "动画"
- "软件架构"
- "大模型"
- "AI 医疗"
- "Apple"
- "评估"
- "科研范式"
- "治理"
- "负结果"

---

> - 一场关于 SwiftUI 动画的“原生”之争 - 肘子的 Swift 周报 #154
> - 从 AI Coding 到 Harness Engineering 的端到端工程开发实践
> - 阿里达摩院医疗 AI，十年拼出一张图
> - 70强项目观察之前沿探索：AI进入科学发现，答案之外还要验证什么
> - OpenAI 阐述构建 AI 下一发展阶段全球标准的路径
> - Apple 发布 iOS 27.2 beta 2 等全平台测试版更新
> - OpenAI 成立数学与人工智能咨询小组
> - macOS 26.4 静默为登录钥匙串开启 Data Protection，破坏灾难恢复能力
> - 让端侧 AI 摘要适应真实文章长度：token 预算、裁剪与缓存实践

## 🍎 iOS Blog

### [一场关于 SwiftUI 动画的“原生”之争 - 肘子的 Swift 周报 #154](https://fatbobman.com/zh/weekly/issue-154/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2026-09-21 22:00:00
![](https://og.fatbobman.com/weekly/issue154.webp)
**本期周报聚焦 SwiftUI 动画“原生”之争：React Native 核心开发者演示主线程阻塞时 UIKit 动画仍正常执行而 SwiftUI 动画停滞，SwiftUI 共同创造者 Kyle Macomber 回应称，这是有意放弃 render-server animation、改为在应用进程中推进动画以换取可中断性与交互性的设计取舍；且从 iOS 18 起，UIKit 与 AppKit 也已采纳这套 client-side animation 模型。**

* Xcode 27.2 beta 引入 JSON 格式的 project.xcproj，替代 .xcodeproj 中的 project.pbxproj
* iOS 27 新增 CrashReportExtension，崩溃后由独立 Extension 检查进程，是对系统 .ips 报告的补充而非替代
* iPhone Duo 适配：新增 ToolbarItemAxisBehavior 等 API 控制 Toolbar 方向与压缩策略，Sheet 等系统组件已内置折痕规避
* Vapor 5 Beta 历时两年重写约 4.9 万行代码，彻底告别 EventLoopFuture，全面转向 Swift Concurrency，要求 Swift 6.4
* 另有 Devin 云端 Mac 开发环境构建经验、SwiftUI 动画运作机制解析、命令行调节折叠角度的 Hinge、不依赖 WebView 的 Enriched Markdown 等精选内容

## 📥 Tech News

### [从 AI Coding 到 Harness Engineering 的端到端工程开发实践](https://www.bestblogs.dev/article/217da0f037?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-21 19:14:27
![](https://media.bestblogs.dev/20260921191241_v2-6cb93e773857220628040d36656a60ce_720w.jpg)
**腾讯应用宝活动平台团队在系统重构中落地 Harness Engineering，将 AI 从对话式编码升级为覆盖需求拆解到代码提交的全流程自动化系统。**

* 对话式 AI Coding 在规模化任务中暴露四大痛点：单窗口上下文膨胀、业务知识缺失、缺乏自动化闭环、无法并行，团队据此构建“知识库工程 + 端到端开发工程”两层体系。
* 底层知识库通过 Skill 自动生成 8 类结构化文档，覆盖 90+ 微服务、800+ 文档，放弃传统 RAG 向量检索，改用渐进式分层加载 + grep，并以 git hash 对比检测文档新鲜度——团队强调“过期知识比没有知识更危险”。
* 上层以状态文件为唯一真相源，配合 hook 机制强制流程推进，设计 12 个单一职责专家 Agent，通过 DAG 编排与 Fork-Join 实现并行，并集成 TAPD 等内部平台打通 DevOps 全流程。
* 确定性操作（解析 JSON、编译发布等）交给脚本而非 AI 推理，已沉淀近 15 个脚本；并行冲突治理遵循“能事前隔离的就事前隔离，必须共享的就串行收口”。
* 核心结论：未来比拼的不是“用了多少 AI”，而是能否把 AI 当作一个工程系统来设计。适用于正在规模化引入 AI 编码的研发团队参考。

### [阿里达摩院医疗 AI，十年拼出一张图](https://www.bestblogs.dev/article/ef4a18d41e?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-21 18:21:00
![](https://image.jido.dev/20251127045514_06f3979d)
**阿里达摩院医疗 AI 团队十年演进，从单病模型突围，经“一扫多查”策略落地多癌筛查，最新通用医疗影像模型 RADAR 登上 Science，实现腹部增强 CT 上 146 种病症的专家级识别与零样本诊断。**

* 胰腺癌平扫 CT 筛查模型 PANDA（Nature Medicine）将误报率压至千分之一，真实世界连续筛查两万人发现两例漏诊早癌；iAorta 将主动脉夹层初诊漏诊率从 48.8% 降至 4.8%。
* “一扫多查”策略下，一次 200 元平扫 CT 覆盖七大高发癌症，成本仅为传统 3000 元筛查组合的 1/15，已在宁波等地落地 24 万例、发现 84 例胰腺癌（含 43 例早期）。
* RADAR 采用“器官级拆解 + 自适应对比建模”，将腹部增强 CT 拆解为 18 个解剖单元逐器官对齐报告文本；4 万真实检查平均 AUC 0.913，外部验证 0.895，单独读片超越 26 名医生中的 23 人，首次系统证明医疗影像 AI 可摆脱“一病一模”走向通用。
* 局限在于 RADAR 目前仅适配增强 CT，平扫精度仍不及专病模型；团队判断专病模型（大规模筛查）与通用模型（复杂诊断）将长期并行，十年目标始终是“在已拍 CT 上发现更多健康信息”。

### [70强项目观察之前沿探索：AI进入科学发现，答案之外还要验证什么](https://www.infoq.cn/article/ihH1ltOG7d2YCelYKJYe)

来源：InfoQ 推荐

发布时间：2026-09-21 18:21:03
![](https://static001.infoq.cn/resource/image/f7/75/f72122912f06d866477232960f4b6675.jpg)
**GOAI「前沿探索 AI for Research」赛道 20 个项目表明，AI 正从科研辅助工具进入科学发现流程本身，但高分结果不等于科学发现，核心问题转向结果能否被验证、解释与复现。**

* 从“预测结果”走向“发现问题”：SAGE-Mat 等系统让 AI 参与问题形成，并通过同义词复检、反例检索核查所谓“新问题”是否只是旧工作换种说法；古文字项目把证据冲突与学术分歧变得可检查
* 从“追求高分”走向“验证发现”：天线项目用两套独立求解器交叉验证，识别出一次评分高出基线 17.6% 的假发现；“谁来给尺子打分”项目直接研究代理指标可能被刷分的漏洞并反向设计更可靠指标
* 负结果成为重要产出：完整记录失败路径、研究条件与边界，若明确某方法在何种条件下失效，同样减少未来研究的不确定性
* 竞争维度从单一精度扩展到泛化、对照实验与机制解释，需回答“为什么有效、在哪些条件下有效”
* 成熟标志是形成可检查、可复现、可质疑、可延续的科学发现链，而非“AI 独立发现多少成果”

### [OpenAI 阐述构建 AI 下一发展阶段全球标准的路径](https://openai.com/index/building-standards-next-phase-ai)

来源：OpenAI News

发布时间：2026-09-21 18:00:00

**OpenAI 发文阐述构建全球共享 AI 标准的路径，主张通过协同的评估、报告与治理机制提升 AI 安全性。**

* 核心观点：AI 发展进入新阶段后，需要全球范围内协调一致的标准体系，而非各机构各自为政；
* 提出的关键方向包括统一的评估方法、规范化的结果报告机制，以及跨区域的治理协作；
* 该文属于政策倡导性质，反映头部 AI 厂商对标准化框架的公开立场，面向监管机构、行业从业者及关注 AI 治理的读者；
* 具体标准落地路径与各方分工仍需观察后续进展。

### [Apple 发布 iOS 27.2 beta 2 等全平台测试版更新](https://t.me/AppleNuts/2534)

来源： Apple Nuts - Telegram Channel

发布时间：2026-09-22 01:40:25
![](https://cdn5.telesco.pe/file/qw-sbLldfXahnm-Eqi_TcVnv4Jf8XWdRh13ieqOJWLUDN8gO-1IZIbDz6Bbewul79ITUcAzRmlXFRpNaEOymwTs-5XkpGFNedo3PCpf09zmswk8RWxvlV-uwm3SdXcdGNLmsay9pLJxoMluCS9Qbc5eK_IV5ha2Olf5DilBcyXg-RPtVo1D_LOD0n7bGj_87qSeYjUPPJPGhxv1XCj7D9lAzfXmlc5mCjdVl_X8abCEwxgzdAa5j33wFHjbnMHFaNb2Q1O6a1By6e2Zl8rzM_3f7yaN2lm51j2p7J4HMT_5aOKY7Oflo7CvILl-310ff1YcqAe3OHFQa8IRHGYu31w.jpg)
**Apple 同步推送了 27.2 版本周期的第二个测试版更新，一次性覆盖旗下全部六大操作系统平台。**

* 本次更新包括 iOS 27.2 beta 2 (24B5089g)、iPadOS 27.2 beta 2 (24B5089g)、macOS 27.2 beta 2 (26B5091g)
* tvOS 27.2 beta 2 (24K5093g)、visionOS 27.2 beta 2 (24N5093f)、watchOS 27.2 beta 2 (24S5091f) 也一同发布
* 原文仅列出各系统的版本号与 build 号，未提供具体功能变化或已知问题说明
* 适合跟踪苹果系统更新节奏的开发者和尝鲜用户作为版本参考，普通用户建议等待正式版推送

### [OpenAI 成立数学与人工智能咨询小组](https://openai.com/index/advisory-group-on-mathematics-and-ai)

来源：OpenAI News

发布时间：2026-09-21 20:00:00

**OpenAI 宣布与一个独立的“数学与人工智能咨询小组”展开合作，用于指导新兴 AI 数学成果的审查与对外沟通。**

* 该小组定位为独立咨询机构，将协助 OpenAI 审核 AI 系统产出的数学类结果，并规范其发布与传播方式；
* 此举背景是 AI 在数学等前沿领域的产出日益增多，其结果的可信度验证与沟通机制需要更严谨的外部把关；
* 对关注 AI 科研应用与成果验证机制的读者而言，这一动向意味着头部厂商开始在数学领域引入外部专家评审流程；
* 目前公开信息有限，小组具体成员构成与运作方式有待后续披露。

## 💾 Daily Dev

### [macOS 26.4 静默为登录钥匙串开启 Data Protection，破坏灾难恢复能力](https://lapcatsoftware.com/articles/2026/9/5.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-22 03:47:13
![](https://cdn4.telesco.pe/file/Hx_oA4DA8E7e5Gr4sJmLeIHcu3q9T7IzK2EWhYsM4wxjM5dsWFN3EMQZBGU_za7-6_XMX3we1smDikd5UP15JELsle-ATZ4WX4t_Zy6gUigQD2k6edfzWaJ6ZKmj2jyg6R0742Kp1k1ss2Rd7cxSaPVAcCQwhYjFB2IJlCkdaT111NCKeydrFV-ie88Uz11VMEhfNWCZMPLJGSTsfvNwC2lhvaRWIeIGCo7Juk74dWE6esXzEhwgaVJt62VNEu4ReksWQC7wcO8MNSttdSYvxn2-ihyLbWu4_QgKpN3CNo4vaVTbf684MuurQrz5CzXxzMWt8nqNvgegYnKnONyxnQ.jpg)
**macOS 26.4 通过启用 Data Protection（DP）机制使登录钥匙串不可移植、无法在原始环境之外解锁，导致 Mac 丢失或损坏时用户可能无法从备份恢复密码数据。作者通过苹果开源代码确认了这一变化的实现细节。**

* 源码中 `ProtectLoginKeychainWithDP` 特性开关启用后，`security unlock-keychain` 会接受任意密码——这是设计行为而非漏洞，因为钥匙串实际由 DP 与 Secure Enclave 解锁；该行为在 VM 中不生效，但 VM 的钥匙串同样不可移植
* 登录钥匙串的加密与每个 macOS 启动卷绑定，同一台 Mac 的不同卷、不同 VM 之间均无法互相解锁或移植钥匙串
* 一位 Reddit 用户升级 macOS 27 后迁移钥匙串，输入正确密码仍被拒绝，100+ 个密码险些全部丢失，最终依靠 macOS 26.4 更新之前的 Time Machine 备份才得以恢复
* 苹果未同步更新过时的支持文档，而 iCloud 钥匙串不提供版本化备份且存在账户锁定风险，作者批评此举实质上破坏了用户的灾难恢复能力
* 依赖本地钥匙串的用户应保留 26.4 之前的备份，并重新评估密码备份策略

### [让端侧 AI 摘要适应真实文章长度：token 预算、裁剪与缓存实践](https://www.ioscoffeebreak.com/issue/issue77)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-22 02:22:19
![](https://cdn4.telesco.pe/file/rZ_5YvLjWfNhNPEe2_5kB0EmD-YqQLxN9C93A1IiNBUBhRsyUTTvJ6KVuG8YZmRrlYrbgj3noGEbBLYVLbk5FF1tC3bi2JQ3BNysMLxSPBaYs3IBY0py_lU2e83Q4JtATFWJwAdDO-o-QQoIX6gdo8FdXjoz7iGwBAP7zqDfbNtxNjPG4kQvSN8xAkJZ8kGBnSrKjNGERwHnYiQbwJhNs1s9A7rXQoeqh92TPgw6pEG007rE6BGfKzjs5dZfEd-qDw-bg-FoIx-tUusEvQ7-vDSg3O_KJNorqjfsjXZeW8IseEooJWK44jQoER9WEgY5T_QaDXYPeVWeeB_TrLWFNQ.jpg)
**本文是 "Building a Newsletter App" 系列第 77 期，作者对基于 Apple Foundation Models 的端侧摘要功能进行加固：生成前先做 token 预算、超长内容自动裁剪、按期缓存结果，以应对真实长度的内容并避免重复生成的开销。**

* iOS 26.4 起可通过 `contextSize` 与 `tokenCount(for:)` 在运行时读取上下文窗口（iOS 26 系统模型为 4,096 token，iOS 27 为 8,192），不应硬编码
* 预算需同时覆盖指令、提示词与预留的响应空间（如 256 token）；超出时保留前 75% 内容迭代裁剪，设最小长度兜底并抛出明确的 `contextWindowExceeded` 错误
* 生成前用 SwiftSoup 剥离 HTML，避免标记浪费 token；裁剪前缀是妥协方案，长文更好的处理方式留待后续探讨
* 摘要按期缓存于 UserDefaults，缓存键为覆盖 id、标题、描述与正文的 SHA256 哈希，内容变化自动失效，另有缓存版本号作为第二重失效杠杆
* 适合正在接入端侧模型的 iOS 开发者参考，核心观点是：端侧模型不是无限云端 API 的缩小版，功能必须围绕 token 预算设计
