---
title: "Daily News #2026-10-28"
date: "2026-10-28 08:00:00"
description: >
  当应用不再属于特定操作系统 - 肘子的 Swift 周报 #159 Xcode 27 MCP 在模拟器导航中可能导致更高的 Token 成本 国产算力·昇腾 910C 大模型推理优化（下）：源码修改与算子优化，TPOT 延迟降低 64.8%｜得物技术 中层技术经理要么重新学技术，要么考虑退休：前 Stripe 工程高管警告，未来三年工程管理将彻底变样 AI 写作是一种命运 苹果发布全新 iPad mini：A20 Pro 芯片 + 8.5 英寸 OLED 屏幕 OpenAI 与学术社区合作推进科学认知：公开多项前沿课题的模型研究结果 第八代 iPad mini 发布：OLED 与 A20 Pro 齐升级，60Hz 与高价引争议
tags:
- "AI 伦理"
- "媒介理论"
- "iOS"
- "工程管理"
- "OpenAI"
- "开发工具"
- "Xcode"
- "iPad mini"
- "量子色动力学"
- "iPad"
- "AI 写作"
- "科研"
- "MCP"
- "A20 Pro"
- "LLM 推理优化"
- "CTO"
- "OLED"
- "iPadOS"
- "硬件"
- "数学猜想"
- "组织变革"
- "AI Agent"
- "AI编程"
- "Token 成本"
- "AI for Science"
- "AI 基础设施"
- "iOS Simulator"
- "职业发展"
- "内容创作"
- "vLLM"
- "Swift"
- "跨平台"
- "AI"
- "昇腾 910C"
- "Apple"
- "性能优化"

---

> - 当应用不再属于特定操作系统 - 肘子的 Swift 周报 #159
> - Xcode 27 MCP 在模拟器导航中可能导致更高的 Token 成本
> - 国产算力·昇腾 910C 大模型推理优化（下）：源码修改与算子优化，TPOT 延迟降低 64.8%｜得物技术
> - 中层技术经理要么重新学技术，要么考虑退休：前 Stripe 工程高管警告，未来三年工程管理将彻底变样
> - AI 写作是一种命运
> - 苹果发布全新 iPad mini：A20 Pro 芯片 + 8.5 英寸 OLED 屏幕
> - OpenAI 与学术社区合作推进科学认知：公开多项前沿课题的模型研究结果
> - 第八代 iPad mini 发布：OLED 与 A20 Pro 齐升级，60Hz 与高价引争议

## 🍎 iOS Blog

### [当应用不再属于特定操作系统 - 肘子的 Swift 周报 #159](https://fatbobman.com/zh/weekly/issue-159/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2026-10-26 22:00:00
![](https://og.fatbobman.com/weekly/issue159.webp)
**本期周报以「应用不再属于特定操作系统」为主题，探讨了跨平台运行技术的新趋势，并收录多篇 iOS 开发深度文章与开源项目。**

* 核心观点：Cutefish（Linux 运行原生 Mac 应用）、SimRun（iOS 模拟器应用独立窗口运行于 Mac）、Mac Android Subsystem（Android 应用融入 Mac 桌面）采用兼容层、直跑模拟器构建产物、后台虚拟系统三条不同路线，共同模糊应用与宿主系统的边界；AI Coding Agent 正大幅降低打破平台壁垒的成本，未来硬件购买决策或从「独占应用」转向「跨平台使用体验」。
* 推荐文章涵盖：iOS 触觉反馈 API 完整指南、AVFoundation 音频闪退与平滑混音的工程实践、SwiftUI 与 AppKit 混用中 NSHostingView 意外重建问题的排查实录（同时展示了 AI Agent 通过实验建立证据链的调试方法）。
* 其他内容：通过统一 JSON 工具契约接入六种实时语音模型的实践经验；Tuist 联合创始人关于开发工具应构建于 Compute 之上而非编辑器的反思；利用 /context 等指令分析并优化 Claude Code 初始上下文占用（高达 39.6k Token）的方法。

适合 Swift/iOS 开发者及关注跨平台与 AI 辅助开发趋势的读者阅读。

### [Xcode 27 MCP 在模拟器导航中可能导致更高的 Token 成本](https://www.avanderlee.com/ai-development/xcode-mcp-simulator-token-costs/)

来源：SwiftLee

发布时间：2026-10-26 20:09:51
![](https://swiftlee-banners.herokuapp.com/imagegenerator.php?title=How+the+Xcode+27+MCP+can+lead+to+higher+token+costs+when+navigating+the+Simulator)
**Xcode 27 内置的 MCP 在 AI 代理操作 iOS 模拟器时，每次动作后读取的文本量约为 RocketSim CLI 的七倍，会显著推高 token 消耗。**

* 作者通过基准测试发现，Xcode 27 MCP 在代理执行每个操作后读取的文本量约是 RocketSim CLI 的 7 倍。
* 高效导航的关键在于代理每次点击后读取的内容形式：截图可以直接呈现界面状态，而纯文本读取方式往往冗长得多。
* 对使用 MCP 驱动模拟器自动化导航或测试的 iOS 开发者而言，需留意这种读取方式带来的 token 成本差异，并权衡替代工具。

## 📥 Tech News

### [国产算力·昇腾 910C 大模型推理优化（下）：源码修改与算子优化，TPOT 延迟降低 64.8%｜得物技术](https://www.bestblogs.dev/article/6d9c06f1f2?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-26 18:30:00
![](https://image.jido.dev/20251127045403_cb8f24c8)
**得物技术团队在华为昇腾 910C 上对大模型推理进行了源码级与算子层的深度优化，通过多流重叠、host 开销削减、融合算子与静态 kernel 编译等手段，将 TPOT 延迟从基线 14.1ms 降至 5.0ms，降幅达 64.8%，并在真实业务场景中验证有效。**

* MoE 共享专家多流重叠：将 shared expert 计算与 AllReduce 放入独立 side stream，与 routed experts 并行执行，并移除冗余同步事件，显著缩短 MoE 层执行时间
* decode host 侧开销优化：针对 c=1 decode 时 host 侧拷贝与提交耗时过高的问题，引入上一轮状态跟踪，跳过不必要的 block table 提交与数据拷贝，并优化 positions 计算路径
* 算子层融合：利用 FUSED_MC2 实现通信-计算融合，通过 SuperKernel 合并多个小 kernel，自研 matmul_allreduce_add_rmsnorm_910c 融合算子，减少 kernel launch 次数与 HBM 访问
* 修复静态 kernel 编译路径问题实现 100% 编译成功率，并调整 cudagraph 捕获尺寸以兼容 MTP 投机解码，保证该模式下的性能稳定
* 文章强调“优化的另一半工作是证伪”：MatmulAllReduce、FlashComm 等文档推荐的特性在 910C 实测中支持不完整或无收益，甚至有负向影响

### [中层技术经理要么重新学技术，要么考虑退休：前 Stripe 工程高管警告，未来三年工程管理将彻底变样](https://www.infoq.cn/article/hhxL1M65UU3Iwr4ovALT)

来源：InfoQ 推荐

发布时间：2026-10-26 15:18:06
![](https://static001.infoq.cn/resource/image/84/65/84bf754a601684aaed2c4fe4a7ab5565.png)
**前 Stripe 工程高管、曾出任 Carta 与 Calm CTO 的 Will Larson 预测：未来三年传统工程管理职业可能不复存在，中层技术经理要么重新深入技术一线，要么考虑退休。他本人已践行这一判断——从管理 250 人团队转任 Imprint 约 25 人团队负责人，一年半内提交 500+ 个生产环境 PR。**

* 核心判断：2010 年代“管理者不做技术决策”的理念已失效，企业需要既懂管理又能写代码的 TLM（技术负责人兼经理）；理想经理是“有能力处理管理事务，却更愿意花时间开发的人”
* 历史反思：零利率时代几乎解释了 2010 年代工程管理的全部异化——管理者被禁止碰技术，只能靠招聘、流程和满意度证明价值，导致组织臃肿
* 工程师价值：软件实现成本趋近于零，但理解业务、在模糊中做权衡、判断“该不该做”仍需人完成；Staff Engineer 的核心始终是在模糊中做出重要决策
* 访谈包含大量一手细节：Yahoo 服务器“黑市”、Digg v4 灾难重写（Cassandra 读写互斥、Python 可变默认参数致内存泄漏）、Uber 两年内团队从 6 人扩至 70 人
* 组织建议：长期稳定的小团队胜过往延期项目塞人；好产品背后往往有一两个被充分授权、敢于做不受欢迎决策的人
* 写作态度：拒绝用 AI 大量产文，“一两篇真正有影响力的文章，远比几百篇没人看的内容更有价值”

### [AI 写作是一种命运](https://www.bestblogs.dev/article/e299e67b46?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-26 17:10:00
![](https://media.bestblogs.dev/20260827095624_dbb7c8f.jpeg)
**腾讯研究院这篇文章提出，AI 写作已不是可选项而是一种“命运”：即使不主动使用，AI 产生的文字也在重塑语言习惯与“合格写作”的标准，应对之道是专注打磨机器无法复制的“承重句”。**

* 伦理讨论的焦点应从“是否使用 AI”转向“如何分工”，即明确人与机器的边界，保留需要人类独特判断和经验的写作环节
* “承重句”指包含锋利判断、专属个人经验和立场修正的句子，构成写作真正的个性签名，是模型难以复制的部分；依赖通用性表达则容易沦为“商品内容”
* 当越来越多人的文字向同一中位数收敛，该中位数就成了新标准；而个性一旦被证明可商品化，个性就会被商品化
* AI 让更多人拥有了写作能力，但只有不完全服从于它的人，才真正拥有自己的文字

### [苹果发布全新 iPad mini：A20 Pro 芯片 + 8.5 英寸 OLED 屏幕](https://t.me/AppleNuts/2558)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-26 21:13:18
![](https://cdn5.telesco.pe/file/qB0Shd62_GHJfzuid6y0Hyyvq8nmq3UQL3bzEuJI8s8Kp606T2DyWBpm7ghuR-yFVQ8sW7H2dpFVeDgVy72wSdW19U9roGlMmiGJudCbQry5XJnjwjDteDo51H6zadzXNEyCEbU1qlVOsntj0sKnrWKZZ-Awwbmd0vg9CbfvalNMSoigRbsStotQz4Q2M-pDPoittnC2EDpW0Izyvi4FhgTrPMah0LoI2nZwk5ncNpg1186X634fVW3QjzSIErCKK-s7-llRRka9zYyjmAQYO4dEhucG9nV5EUXAFYdB4NC3prjAR_LiXo_-m4QiLEiY8SypgO_73PMCKDcwjaVbSA.jpg)
**苹果发布被官方称为史上最大更新的 iPad mini，搭载 A20 Pro 芯片并首次采用 8.5 英寸 OLED 显示屏，10 月 28 日开启订购，11 月 6 日正式发售。**

* 核心规格：A20 Pro 芯片（搭配 N1 芯片与 C2 模块）、1200 万像素 Center Stage 摄像头；借助 Acoustic Display 屏幕发声技术取消传统开孔，实现 IP67 级防尘防水。
* 明显限制：屏幕刷新率仍为 60Hz，不支持 ProMotion；仅 512GB 机型搭载完整版 A20 Pro，低容量版本锁掉 1 个能效核心。
* 定价：WiFi 版 RMB 5,499 起，WiFi + 蜂窝版 RMB 6,799 起。
* 适合关注小尺寸平板的用户，但低容量机型的芯片阉割与 60Hz 刷新率是选购时需要权衡的因素。

### [OpenAI 与学术社区合作推进科学认知：公开多项前沿课题的模型研究结果](https://openai.com/index/building-scientific-understanding-with-academic-communities)

来源：OpenAI News

发布时间：2026-10-26 22:30:00

**OpenAI 公开了其模型在多个前沿科学问题上的研究结果，并邀请学界验证与延续这些工作。**

* 涉及课题包括 Kakeya 猜想（挂谷猜想）、指数时间假设（ETH）以及量子色动力学（QCD）
* 文章同时阐述了研究人员如何对这些模型产生的结果进行验证和进一步研究
* 体现了大模型能力向纯数学与理论物理等基础科学场景延伸的趋势
* 对关注 AI for Science 的研究者和开发者具有参考价值，具体方法与结论需阅读原文

## 💾 Daily Dev

### [第八代 iPad mini 发布：OLED 与 A20 Pro 齐升级，60Hz 与高价引争议](https://mjtsai.com/blog/2026/10/26/ipad-mini-8th-generation/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-27 03:27:05
![](https://cdn4.telesco.pe/file/EhLZriydTJEQdpsClp0SeYjDVIKnDeFcxt0IWfdIGJzk9c8wQzm9rAKEy9h2lvjwb7RNdtW-RDrTVVnZasvKo6u_AJdNoe5J_l7HPGbwvkXDslmxTkFO50RvCiQ70RTmJziHa_JA8TLLsVf7iAg_tU9bfEEMcBsjYmf_i4vOF29q8pfz0qEbYmEj4Rjo7JObGEdmmSX9YShwvlPcmRSdI795JnWYYweAj3iWEkMauCNvMLSMkekkvjdSwWOABSRHofaf_rIkQjHla2yCYQTbGjvoIazqOnGoXncos5U2BJ-bIGq0ZJAaS4xSO0plvZE-CSd7K-2ey-jZzQfNJeoHsQ.jpg)
**苹果发布第八代 iPad mini，首次配备 OLED XDR 屏幕并搭载 A20 Pro 芯片，但 60Hz 刷新率、沿用 Touch ID 以及 699 美元起售价引发评论界强烈批评。**

* 屏幕升级至 8.5 英寸（上代 8.3），边框缩窄 25%，峰值亮度翻倍，可选 nano-texture 防眩光；机身更薄更轻（5.4mm/255g，上代 6.3mm/293g）
* 定价 699 美元起、最高 1249 美元，而上代发布价为 499 美元；据技术规格页，除 512GB 顶配外，其余配置均采用降规格的 A20 Pro 芯片
* John Gruber 等多位评论者不满其仍无 Face ID 与 ProMotion 高刷，认为在这个价位上不可接受，有用户明确表示因此放弃购买
* 新增 Acoustic Display 声学显示技术（低音单元与屏幕共振、高音单元藏于玻璃与铝壳之间），前置 12MP Center Stage 摄像头移至横边，首次支持防水防尘；配合 iPadOS 27.2 可在外接显示器时使用扩展显示模式
