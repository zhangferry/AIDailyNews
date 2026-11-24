---
title: "Daily News #2026-11-25"
date: "2026-11-25 08:00:00"
description: >
  大众的 macOS，还是开发者的 macOS？ - 肘子的 Swift 周报 #163 OpenAI and Cisco introduce Shirudo GLM-5.4：瞄向泛 Coding，首个 Loop Transformer 带来的惊喜 当智力可以被计量：我们熟悉的规则会被怎样被改写？ 黄仁勋杀回英伟达，董事会全票同意！老黄：迫不及待投入工作 Richpanel helps companies automate 50% of support in 30 days
tags:
- "英伟达"
- "OpenAI"
- "开源"
- "科技行业"
- "公司治理"
- "Swift"
- "Token 经济"
- "推理优化"
- "客服自动化"
- "大模型"
- "漏洞防护"
- "AI 社会影响"
- "黄仁勋"
- "macOS"
- "GPT-6"
- "Linux 安全"
- "eBPF"
- "未来就业"
- "SwiftUI"
- "iOS"
- "智谱"
- "AI Agent"
- "版权制度"
- "UBI"
- "AI 编程"
- "SaaS"
- "AI 芯片"
- "Loop Transformer"

---

> - 大众的 macOS，还是开发者的 macOS？ - 肘子的 Swift 周报 #163
> - OpenAI and Cisco introduce Shirudo
> - GLM-5.4：瞄向泛 Coding，首个 Loop Transformer 带来的惊喜
> - 当智力可以被计量：我们熟悉的规则会被怎样被改写？
> - 黄仁勋杀回英伟达，董事会全票同意！老黄：迫不及待投入工作
> - Richpanel helps companies automate 50% of support in 30 days

## 🍎 iOS Blog

### [大众的 macOS，还是开发者的 macOS？ - 肘子的 Swift 周报 #163](https://fatbobman.com/zh/weekly/issue-163/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2026-11-23 22:00:00
![](https://og.fatbobman.com/weekly/issue163.webp?imageView2/1/w/1600)
**本期周报以 macOS 27.3 beta 2 对完全磁盘访问权限弹出更强警告为引，探讨苹果的强权限管控与 AI Agent 自动化工作流之间的矛盾：作者认为在主流版本放松管控并不现实，但可在 macOS 虚拟机中借助隔离边界，为开发者与 Agent 提供一次性授权的宽松模式。**

* Raycast 发现在键盘扩展中嵌入 WKWebView，通过 JavaScript 的 getUserMedia() 采集音频实现语音输入，绕过 Apple 对第三方键盘访问麦克风的长期限制，社区已有开源实现，但存在被系统更新封禁或审核拒绝的风险
* 一篇 SwiftUI 动画底层研究显示：macOS 上动画依赖主线程逐帧更新 Layer，而 iOS/iPadOS 由独立 AsyncRenderer 线程计算动画值并经私有 Presentation Modifier 传给 Render Server，SwiftUI 正成为整个 Apple UI 生态的基石而非仅是抽象层
* 其他推荐涵盖 Apple TV 实时视频插帧工程实践、适配 iPhone Duo 的 ArrangementView 布局理念、Liquid Glass 形变教程、为并行 Coding Agent 租用 Mac mini 搭建共享构建与分层验证环境等
* 工具收录 App Store 送审自查清单、可在 M1 MacBook Pro 直接启动的开源 Darwin 系统 SiliconForest（GPL 与 APSL 许可证冲突待解）、玻璃质感引导组件 GlassIntroKit，以及无需越狱在 iOS 上运行 Android 13 的 Twoyi

## 📥 Tech News

### [OpenAI and Cisco introduce Shirudo](https://openai.com/index/introducing-shirudo)

来源：OpenAI News

发布时间：2026-11-24 05:20:00
![](https://images.ctfassets.net/kftzwdyauwt9/bScTLq9smNJq5XAlaHIQW/fab0e70b1aab8ca8dffb70a747056fd7/guardian-agent-desktop-light.png?w=3840&q=90&fm=webp)
**OpenAI 与 Cisco 联合开源 Shirudo，一个基于 eBPF 的运行时防护系统，让 Linux 服务在等待补丁和重启的窗口期内仍能抵御漏洞利用。**

* 核心机制：利用 eBPF 在内核关键点运行小型程序，部署称为 shield 的临时防护，精准阻断暴露漏洞的代码路径同时放行合法请求；运维可在强制执行前先观察 shield 对应用的实际影响。
* 四大能力：实时防护（无需重启）、机器速度防御（AI agent 可编程地调查漏洞、生成并验证针对性 shield）、可信部署（shield 需加密签名并通过 eBPF verifier 校验）、硬件级验证（基于 TPM 的防护加载/移除审计记录）。
* 实测案例：团队用 Codex 生成 shield，直接附加到运行中的 Elasticsearch 进程，为 Java Base64 解码器注入输入检查，成功拦截 Java4Shell 攻击且服务不中断。
* 采用 BSD 2-Clause 许可（BPF 程序双许可 BSD/GPL），长期愿景是让经过验证的 shield 随漏洞披露同步发布，成为永久补丁落地前的标准临时防线。适合安全运维、基础设施团队关注。

### [GLM-5.4：瞄向泛 Coding，首个 Loop Transformer 带来的惊喜](https://www.bestblogs.dev/article/b1dc1b415a?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-23 17:42:00
![](https://image.jido.dev/20260527050446_1362653.jpeg)
**智谱发布 GLM-5.4，首个采用 Loop Transformer 架构的旗舰模型，通过共享权重层的循环执行在不增加参数量的前提下实现更深推理，智能水平达到 2-3T 级，并将编程能力扩展至视频、3D、机械设计等泛 Coding 场景。**

* Loop Transformer 让一组共享权重的层循环执行多轮，每轮在上一轮隐状态基础上继续推演，配合门控渐进更新、KV Cache 全局共享+滑窗独立、稀疏注意力索引复用等技术，显著降低了部署成本；
* 在 GPQA、MMLU-Pro 等基准上，Loop 模型平均输出长度下降 10%-14%，推理深度从 token 流转移到循环带来的额外深度中，数学推理、长上下文和代码任务提升显著；
* 实战案例包括从 0 到 1 视频创作、GLSL 着色器 3D 互动观鸟体验、FreeCAD 机械臂建模并通过 Blender 可视化；
* 非高峰时段速度最高 200 token/s，高峰时段 70-80 token/s，Coding Plan V2/V3/团队版用户额度提升至 1.5 倍，已上线 ZCode、Trae、WorkBuddy、Qoder 等平台。

### [当智力可以被计量：我们熟悉的规则会被怎样被改写？](https://www.bestblogs.dev/article/ea86c2ae35?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-23 17:00:00
![](https://media.bestblogs.dev/20260827095624_dbb7c8f.jpeg)
**文章基于腾讯研究院与多位学者的对谈，探讨智力可计量化对版权、UBI、教育与就业等社会规则的重构，核心判断是 AI 将智力转化为可计量、可调用的 Token 服务，打破了知识传播与生产技术的二元结构。**

* 版权制度面临根本性挑战，大模型打破了「保护表达不保护思想」的边界，表达可随时切换，传统著作权需重新定义，目前暂无完美解法；
* AI 革命压缩了社会变迁的缓冲期，过去几代人完成的转型可能在半代人内完成，教育、就业等制度难以及时适应；注意力成为新的经济物理上限，算力、电力、散热等物理资源成为新约束；
* UBI 未来可能由超级平台通过数字币发放，形成国家与平台的双重保障体系；大学的「定价」功能减弱，招聘机制面临重构；
* 关于职业形态回归狩猎采集式自由、长阅读或只剩少数人等判断较为前瞻，属观点性探讨而非实证研究，适合关注 AI 社会经济影响的读者参考。

### [黄仁勋杀回英伟达，董事会全票同意！老黄：迫不及待投入工作](https://www.infoq.cn/article/4t3EvHtmI11QEgmV23Iz)

来源：InfoQ 推荐

发布时间：2026-11-24 08:00:00
![](https://static001.infoq.cn/resource/image/ac/fe/acb3ee0d134b662c8a34307ec7c677fe.png)
**英伟达宣布恢复创始人黄仁勋的总裁、CEO 及董事会董事职务，任命立即生效，董事会全票通过，结束了这场仅持续 11 天的高层动荡。**

* 时间线：11 月 12 日黄仁勋辞去全部职务，CFO Colette Kress 临时接任；11 月 17 日董事长 Harvey Jones 还公开表示董事会不打算重新任命他；11 月 23 日态度彻底反转，全票通过复职。
* 复职推手：一项支持复职的请愿获得超 18 万签名（马斯克参与），特朗普公开表态支持；董事会称在听取美国政府高级官员意见后，认为复职不构成国家安全风险。
* 市场反应：消息公布后英伟达股价盘前一度上涨超 31%，反映市场对管理层稳定性的高度敏感，以及黄仁勋在客户关系与战略层面的不可替代性。
* 遗留问题：针对黄仁勋被报道成为外国情报活动目标的独立调查仍将继续，公司已设立国家安全与出口管制委员会并招聘首席合规官；董事会决策的快速转向及继任者计划缺失，仍是长期治理挑战。

### [Richpanel helps companies automate 50% of support in 30 days](https://openai.com/business/customer-stories/richpanel-ai-customer-support)

来源：OpenAI News

发布时间：2026-11-23 16:00:00
![](https://images.ctfassets.net/kftzwdyauwt9/5B8tYqcVtztQ9PNAvMLPLO/8f2fc1472cb497b2d2b8ff82c0c1eeba/Gondola-Option-A-Art-Card-1080x1080.png?w=3840&q=90&fm=webp)
**客服 SaaS 公司 Richpanel 基于 OpenAI 系列模型构建分层 AI 客服体系，承诺 30 天内实现 50% 客服自动化（未达标退款），并称 AI 客服满意度已超越人工。**

* 架构思路：用 GPT-6 Astra 和 GPT-6.1 Sol 驱动被称为 Boss AI 的管理 agent，负责编写流程并定义一线客服 agent 的工具调用方式；用成本更低的 GPT-6 Luna 承接海量对话，体现准备阶段用深度推理模型、执行阶段用经济模型的成本平衡策略。
* 设计起点是替代前置部署工程师：传统 AI 客服上线需要工程师接入客户系统，Richpanel 让 AI 自己完成这套配置。其 CEO 称智能已不是瓶颈，瓶颈在其周边的工程。
* 截至 2026 年 10 月的六个月内完成约 300 个部署，全部兑现 50% 自动化承诺。
* 属厂商客户案例，数据来自 Richpanel 自述，参考时需注意宣传成分。
