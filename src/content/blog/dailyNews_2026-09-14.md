---
title: "Daily News #2026-09-14"
date: "2026-09-14 08:00:00"
description: >
  Codex 想让 Harness 消失，Claude Code 却要把它做成“承重墙” 两个 Token 就让 Kimi“变成”Claude？前Google DeepMind研究员意外撞上大模型的蒸馏疑云 扒完 DeepSeek 最新论文，我发现了 V4.1 Flash 便宜大碗的秘密 iPhone Duo 人机界面指南速览：折叠屏应用的适配要点
tags:
- "DeepSeek"
- "模型蒸馏"
- "推理轨迹"
- "LLM"
- "AI Agent"
- "Codex"
- "越狱"
- "大模型安全"
- "推理优化"
- "iOS"
- "KV Cache"
- "折叠屏"
- "架构设计"
- "HIG"
- "iPhone Duo"
- "Claude Code"
- "UI设计"

---

> - Codex 想让 Harness 消失，Claude Code 却要把它做成“承重墙”
> - 两个 Token 就让 Kimi“变成”Claude？前Google DeepMind研究员意外撞上大模型的蒸馏疑云
> - 扒完 DeepSeek 最新论文，我发现了 V4.1 Flash 便宜大碗的秘密
> - iPhone Duo 人机界面指南速览：折叠屏应用的适配要点

## 📥 Tech News

### [Codex 想让 Harness 消失，Claude Code 却要把它做成“承重墙”](https://www.bestblogs.dev/article/b441ba432e?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-12 11:35:00
![](https://image.jido.dev/20260527130453_c4b7ab1.jpeg)
**背景/问题**：随着大模型能力持续跃升，模型外围的工程系统（Harness）究竟会变轻还是变重？OpenAI Codex 团队的 Tibo 与 Anthropic Claude Code 团队的 Thariq 给出了方向相反的判断，这场辩论直指 AI Agent 系统架构的演进核心。

**核心观点/方案**：Tibo 认为模型理解力增强后，过去依赖 Harness 的约束与示例可被模型自学取代，Harness 会变轻；Thariq 则指出当模型能连续数小时高自主运行时，沙箱、自动模式、工作流、Artifacts 等安全与编排机制正成为系统“承重结构”。两人还分享了一线实践：Prompting 的本质是前置的上下文准备与验证；用 HTML/Figma 等结构化文件作参考可让模型产出更有“品位”；大规模代码生成需为每个 PR 附带含失败尝试的 Artifact，测试代码量应比过去多约百倍。

**结论/价值**：对构建 AI Agent 系统的工程师极具参考价值，揭示了“模型变强”与“工程变重”并存而非互斥的行业趋势。访谈篇幅较长但信息密度极高，适合深度精读；观点来自两家头部公司的实践者，权威性与实操性兼备。

### [两个 Token 就让 Kimi“变成”Claude？前Google DeepMind研究员意外撞上大模型的蒸馏疑云](https://www.infoq.cn/article/GhA2VWxo6JTGyKIb7KdT)

来源：InfoQ 推荐

发布时间：2026-09-12 10:19:25
![](https://static001.infoq.cn/resource/image/b0/56/b0c1cbe46242e640695147e034895356.png)
**背景/问题**：前沿大模型回答前生成的加密推理数据块（reasoning blob）会随响应返回用户端以支持无状态架构，前 Google DeepMind 研究员 Ilia Shumailov 等人发现这个“密封信封”形同虚设，构成影响 Anthropic、OpenAI、Google 三大实验室的架构级漏洞。

**核心观点/方案**：加密推理块可跨用户、跨会话、跨同家族模型重放，借助小模型即可让服务端解密并“亲口说出”思考内容。研究者从公开 Agent 轨迹解码出 31.5 万条隐藏推理，暴露出 API 密钥、邮箱、内部 IP 等隐私；最诡异的发现是仅预填充 2 个来自 Opus 的 token，Kimi-K3 的最终答案风格就变为 Opus，成为公开互联网上最接近蒸馏的证据（但非因果证明）；此外还揭示 Agent 轨迹投毒、模型用“外星语言”思考致监控失效等风险。

**结论/价值**：研究已做负责任披露，厂商正实施链式加密等缓解措施，但“追问思路”式越狱将永远存在。对理解大模型安全边界、思维链监控与反蒸馏防御极具前沿价值，适合 AI 安全研究者与平台工程师深读；预填充实验属轶事级证据，解读时需克制。

### [扒完 DeepSeek 最新论文，我发现了 V4.1 Flash 便宜大碗的秘密](https://www.bestblogs.dev/article/aa01f29b61?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-12 11:00:00
![](https://image.jido.dev/20260603033035_ec32c61.jpeg)
**背景/问题**：DeepSeek V4.1 Flash 为何能在 Agent 任务上比肩顶级模型，同时做到极低的推理成本与显存占用？文章通过拆解其技术报告寻找答案。

**核心观点/方案**：核心是三项架构创新：CED（因果编码器-解码器）架构让解码器直接利用编码器输出投影生成全局 KV Cache，长文本预处理计算量近乎减半，特别适配 Agent 频繁调用工具的负载；CSA2 注意力机制实现网络层间缓存共享，配合 FP4 KV Cache 量化大幅压缩持久缓存占用；Engram 条件记忆模块支持通过 SWA Bounded Replay 机制低成本恢复会话状态。强化学习层面，重心已从新算法转向数据工程，构建“问题-执行环境-验证系统”的可验证闭环。

**结论/价值**：对理解推理成本优化路径与 Agent 专用模型架构演进极有价值，“RL 军备竞赛的主战场在数据工程的水电煤”这一判断值得从业者深思。局限是模型在高难度科学问答等极端任务上与顶尖模型仍有差距，且部分技术细节来自论文推断而非实测验证。

## 💾 Daily Dev

### [iPhone Duo 人机界面指南速览：折叠屏应用的适配要点](https://www.sagarunagar.com/blog/iphone-duo-human-interface-guidelines/)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-12 14:42:28
![](https://cdn4.telesco.pe/file/vYenE3Py1e1LWsO0iFQzJVR4JEEbndVAbDjJrP7Dy9cnLKaPDUxf5p_X3048f_B5Wn82GFTE9fmWID4BVZQjeVfuiMw4jiZqxGSCnJSudXTSgHsZRcvJKxu6dFoieKxq27aOSY5ssX5xziYKhu-1U3aoST5BFmDVK6I8JQtv0dVz-nbeLkxPdTFgPktFWSLlvlwJ5DswfgMzBIlElMi58Ca6vrs_xl4CmFucJw_mzzhaGlPGCwUGUl52YB3u6Fepg6uj_qTulSaBpL_wOjQCYvxrSavXJNOxTU5KlxoMqQY3OQdhqdkv5ooW6Hp4EWhaxM6qv-S6yMwKXd9I1TDjDw.jpg)
**背景/问题**：Apple 发布首款折叠屏手机 iPhone Duo 并同步更新 Human Interface Guidelines，配套三场开发者 Tech Talks。开发者面临的核心问题是：现有应用如何适配可折叠设备的多姿态、折叠缝隙与全新的交互模式，而官方文档篇幅较长，需要一份快速可消化的梳理。

**核心观点/方案**：文章提炼出关键设计原则：不要为每种握持姿态单独设计布局，应围绕外屏 Compact、内屏 Regular 两个尺寸级别构建；外屏上导航栏与工具栏移至屏幕右侧呈竖排，仅图标类控件适合竖排；折叠缝隙附近遵循 displacement 规则，能独立移动的元素独立移动，滚动内容豁免；系统新增 reserved regions（折叠线与内屏摄像头）供代码查询；新容器 Arrangement 提供 Split 与 Overlay 两种样式；内屏扩容推荐 split view、reflow、sidebar 三种布局。相关 API 绑定 iOS 27.1，Xcode 27.1 beta 撰文时尚未发布。

**结论/价值**：这是对官方 HIG 与 Tech Talks 的高质量浓缩，结构清晰、可操作性强，适合所有 iOS 开发者与设计师快速评估现有界面的适配工作量并制定改造计划；需注意时效性风险，动手实现前应核实 beta 工具链的实际发布状态与 API 细节。
