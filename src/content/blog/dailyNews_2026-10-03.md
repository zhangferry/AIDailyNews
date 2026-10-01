---
title: "Daily News #2026-10-03"
date: "2026-10-03 08:00:00"
description: >
  在 Cloudflare Worker 上实现多租户 SaaS 规模的模块化边缘计算 苹果 Developer ID 证书签发机构（Sub-CA）将于 2027 年 2 月到期，开发者需提前更换证书 Claude Code 推出 Mods 机制：用 TypeScript 函数深度定制行为与界面 巴克莱银行规模化部署 Claude：2027 年将覆盖多数开发工程师 EmacsConf 演讲：普通 Emacs 用户如何搭建 Zettelkasten 精通是一个 Wicked Problem（棘手问题）
tags:
- "macOS"
- "AI"
- "Anthropic"
- "架构设计"
- "知识管理"
- "SaaS"
- "开发者工具"
- "Denote"
- "Claude Code"
- "TypeScript"
- "证书"
- "Zettelkasten"
- "AI 编程"
- "Claude"
- "企业级AI"
- "Apple"
- "观点"
- "AI Coding"
- "边缘计算"
- "多租户"
- "金融科技"
- "Emacs"
- "笔记系统"
- "安全"
- "Developer ID"
- "插件系统"
- "软件工匠"
- "Cloudflare Workers"
- "职业发展"
- "学习方法"

---

> - 在 Cloudflare Worker 上实现多租户 SaaS 规模的模块化边缘计算
> - 苹果 Developer ID 证书签发机构（Sub-CA）将于 2027 年 2 月到期，开发者需提前更换证书
> - Claude Code 推出 Mods 机制：用 TypeScript 函数深度定制行为与界面
> - 巴克莱银行规模化部署 Claude：2027 年将覆盖多数开发工程师
> - EmacsConf 演讲：普通 Emacs 用户如何搭建 Zettelkasten
> - 精通是一个 Wicked Problem（棘手问题）

## 📥 Tech News

### [在 Cloudflare Worker 上实现多租户 SaaS 规模的模块化边缘计算](https://www.infoq.cn/article/P5yCYKFiJfKAICrf8bfs)

来源：InfoQ 推荐

发布时间：2026-10-01 14:00:00
![](https://static001.infoq.cn/resource/image/9d/d0/9db12b1124d920767559ccbe5b1fced0.jpg)
**文章系统阐述多租户 SaaS 边缘平台从单体 Worker 演进为模块化架构的实践，核心是利用 Cloudflare 服务绑定在同机沙箱内近似函数调用的开销特性，构建“精简网关 + 单一职责功能 Worker”的组合。**

* 单体 Worker 在数十万租户规模下存在部署耦合、故障爆炸半径波及全部租户、共享资源配额、权责错配四大痛点；
* 网关仅持有组合逻辑与横切关注点，通过 shouldApply() 纯函数内联决策、服务绑定远程执行；功能 Worker 异常时降级返回源站原始响应；
* 采用单代码库加包边界，兼得服务所有权隔离与契约一致性；
* Cloudflare 与 Akamai 的计算原语（fetch 处理器 vs property 规则引擎）与 KV 语义（全局 vs 区域化）差异巨大，可跨平台复用的只有设计意图与经过验证的不变量；
* 图片优化强调安全策略：拒绝处理带认证信号的请求以防缓存泄露私有图，按 Accept 头协商格式，优化失败必降级；
* 部署采用不可变版本集合加标签，回滚即重新部署上一标签，金丝雀滚动提前暴露回归；测试分为纯函数单测、降级集成测试与生产合成监控三层。

### [苹果 Developer ID 证书签发机构（Sub-CA）将于 2027 年 2 月到期，开发者需提前更换证书](https://developer.apple.com/news/?id=w4atic4c)

来源：Latest News - Apple Developer

发布时间：2026-10-02 01:00:11
![](https://developer.apple.com/news/images/og/apple-developer-og.png)
**苹果官方宣布，原 Developer ID Certification Authority（Sub-CA）将于 2027 年 2 月 1 日到期，届时由该机构签发的所有证书将停止工作，分发 Mac 软件的开发者需提前更换证书并按需重新签名。**

* 应对步骤：先在 Certificates, Identifiers & Profiles 中检查证书是否在 2027 年 2 月 1 日或之前到期，确认受影响后从当前有效的 Developer ID Certification Authority (G2) 生成替代证书。G2 机构本身有效期至 2031 年，但其签发的证书每年到期一次，需逐年续期。
* 注意事项：使用 Xcode 11.4 或更早版本需先升级；创建证书时在 Developer ID Certificate Intermediary 提示中务必选择 G2 Sub-CA，选错选项可能签出同样于 2027 年失效的证书。
* 重新签名要求：2027 年 2 月 1 日起，用受影响证书签名的 .pkg 安装包将无法安装，须在此之前用新证书重签所有安装包；此前已签名并公证（含安全时间戳）的 Mac 应用可继续正常运行，无需处理，但后续版本更新必须使用新证书签名并附安全时间戳。

## 🤖 AI Coding

### [Claude Code 推出 Mods 机制：用 TypeScript 函数深度定制行为与界面](https://claude.com/blog/claude-code-mods)

来源：Claude Blog

发布时间：2026-10-01 08:00:00
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6abe945ed70dd868af96f9df_og_claude-code-mods.jpg)
**Anthropic 为 Claude Code 推出 mods 机制，用少量 TypeScript 代码即可改写提示词、替换内置功能、新增 UI 或拦截工具调用，开发者无需等待官方发版即可深度定制 Claude Code。**

* 工作原理：Claude Code 的每次操作（调用工具、请求权限、绘制界面）都会发出事件，mod 作为钩子函数可在事件前、后运行，也可替代或包裹事件；多个 mod 钩住同一事件时按加载顺序执行，支持多作者叠加使用。
* 典型能力：改写发送给模型的提示词、阻止或重试工具调用、审批权限请求、在模型读取前对工具输出脱敏；还能修改界面、添加按钮，甚至让 Claude Code 自己编写、安装并热重载 mod。
* 内置功能模块化：/diff 等内置功能已改为 mod 实现，可在 /plugin 中关闭或替换；官方计划逐步迁移更多内置功能，使 Claude Code 收缩为可按需组装的小内核。
* 安全与限制：mod 与 Claude Code 本身拥有同等机器权限且不受沙箱隔离，仅应安装可信来源；企业版通过 sec-default 内置 mod 阻止用户 mod 覆盖权限拒绝规则，团队还可借此实现 CI/CD 状态展示、生产命令二次确认和审计日志等管控能力。

### [巴克莱银行规模化部署 Claude：2027 年将覆盖多数开发工程师](https://www.anthropic.com/news/barclays-scales-claude)

来源：Anthropic News

发布时间：2026-10-01 08:00:00
![](https://www-cdn.anthropic.com/images/4zrzovbb/website/6d4a0d28992ade92d6fa63646fd9c9d318245c6c-2400x1260.jpg)
**巴克莱银行宣布扩大与 Anthropic 的战略合作，将 Claude 企业级 AI 系统部署至全球业务体系，用于加速软件开发、现代化遗留系统并提升运营效率。**

* Claude Code 预计在 2026 年底覆盖该行 50% 的开发者，2027 年扩展至多数软件工程师；
* 2025 年上线的员工知识助手基于 RAG 架构构建，已有超 1.6 万名员工采用，累计处理超 100 万次搜索，支撑超 2000 万英国零售客户的客服工作；
* 全球市场业务中，Claude 模型每天处理约 12 万封客户邮件，自动完成分类、信息补全并规划最优处理路径，减少人工操作；
* 双方强调以严格治理、安全控制与人工监督保障 AI 的负责任部署。该案例展示了大型受监管金融机构规模化落地 AI 的实际路径与量化成果，但内容源自厂商官方发布，带有一定宣传性质。

## 💾 Daily Dev

### [EmacsConf 演讲：普通 Emacs 用户如何搭建 Zettelkasten](https://christiantietze.de/posts/2026/09/watch-zettelkasten-for-regular-emacs-hackers/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-02 02:32:47
![](https://cdn4.telesco.pe/file/YNxXo32H44IkmCS-aWPLriUNl3M7iqiYTC7IusjTYY1Dcv-9oYzcatCh7ZGCaQaGUXob6m5CjMmzkB62RT43SWD4bI2TrbIrYsCti2vGLe5-mdy5Rg08QPkAj-7Swp4R0Rf03WlXv8H7_7HUx0iqqWcvRoiMOLYfar__N9x0NMjV00zgqrDXzVEc2FTpnXP0kw6K5g4CvF_THkjKGGbbH7wwias61zE8X4IRxUYv8JUIQLkUGCnAJq3ndcK47sZeWsy5MSUBZE66aCjNTdhko_uiRodkDyL0eBn9wNNmDlYzOCIWDYXPhd5ZHbLB69DiXmw69ZcqG-bi6BNDWWAYMA.jpg)
**Christian Tietze 发布了其在 EmacsConf 2025 的演讲录像，核心观点是：写作能提升思考质量，Zettelkasten 是"通过写作来思考"的环境而非单纯的笔记仓库，没人能递给你一个现成的思考环境，必须自己搭建，而 Emacs 是最具可塑性的平台。**

* 演讲归纳三大核心机制：写（付出努力）、连接（用链接建立路径）、修正（随认知提升改进笔记）；以及让系统可持续数十年的习惯：为使用而设计、创造结构、从 Zettelkasten 内开始、以链接为起点新建笔记以避免孤儿笔记。
* 强调 GIGO（垃圾进、垃圾出）原则同样适用于笔记，输入质量决定思考产出。
* 现场演示用极简 init.el 配合 Denote 包完成笔记的创建、链接、重命名与反向链接，文章附完整配置代码和演示笔记，读者可直接复现。
* 演示笔记还列举了 Zettelkasten 的常见结构类型（对立对、目录、论证/反驳、图表等）与"原子—分子—有机体"的组合隐喻。

### [精通是一个 Wicked Problem（棘手问题）](https://christiantietze.de/posts/2026/09/mastery-wicked-problem/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-02 02:32:46
![](https://cdn4.telesco.pe/file/YNxXo32H44IkmCS-aWPLriUNl3M7iqiYTC7IusjTYY1Dcv-9oYzcatCh7ZGCaQaGUXob6m5CjMmzkB62RT43SWD4bI2TrbIrYsCti2vGLe5-mdy5Rg08QPkAj-7Swp4R0Rf03WlXv8H7_7HUx0iqqWcvRoiMOLYfar__N9x0NMjV00zgqrDXzVEc2FTpnXP0kw6K5g4CvF_THkjKGGbbH7wwias61zE8X4IRxUYv8JUIQLkUGCnAJq3ndcK47sZeWsy5MSUBZE66aCjNTdhko_uiRodkDyL0eBn9wNNmDlYzOCIWDYXPhd5ZHbLB69DiXmw69ZcqG-bi6BNDWWAYMA.jpg)
**作者重读自己 2016 年关于"达到精通"的旧文后提出：精通本质上是一个 wicked problem——规则模糊、反馈迟滞且环境持续剧变，因此永远无法宣称"完成"，人只能做到足够好以适应变化并把智慧带走。**

* 文章引用 Robin Hogarth《Educating Intuition》中"恶劣学习环境"的概念：技术行业的工作方式在一代人内多次颠覆（互联网、云计算、再到 AI），规则本身不断改变。
* 观察：2025 年有人质疑"AI 编程工具若真强大，垃圾软件在哪"，如今答案反而是 shovelware 泛滥；作者所在的软件工匠社区，讨论重心也已从 TDD 和开发工具转向 AI 工具与 Agentic Engineering，社区仍在集体摸索如何保持卓越并培养下一代。
* 观点：任何行业的大师都不产出完全相同的作品，木工、屋顶工、面包师各有风格，大师会把"人性"注入作品；软件工匠同样在代码、架构、可维护性与用户体验中体现这种人性。
* 结论：通往精通可以有路线图，但没有捷径能替代亲身经历，精通首先是一种实践行为。
