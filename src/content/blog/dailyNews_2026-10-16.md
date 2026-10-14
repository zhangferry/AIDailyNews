---
title: "Daily News #2026-10-16"
date: "2026-10-16 08:00:00"
description: >
  SSR-Merge：把 LoRA 合并从'参数算术'变成'信号路由' | ICML 2026 手把手带工程同学从零实现一个完整的 LLM（CS336）——Transformer 篇 九成具身智能公司在东部沿海，长沙抢走了“制造权” Apple 开发者计划许可协议更新，新增 HomeView 小组件、团体购买等多项条款 Apple 推送 iOS / iPadOS / macOS 等 27.2 beta 4 测试版更新 SentinelOne 借助 OpenAI Daybreak，将恶意软件分析从数周缩短至数小时 Third Moment Research 如何同时运行 1 万个智能体并持续工作 36 小时以上 Anthropic 在新加坡开设亚太第五个办公室，并与新加坡政府签署 AI 合作备忘录 macOS Golden Gate 是个 Bug 满地的版本：从密码 App 键盘焦点回归说起
tags:
- "Transformer"
- "机器人"
- "LLM"
- "AI安全"
- "GPT-6"
- "UI_UX"
- "软件质量"
- "智能制造"
- "新加坡"
- "开发者协议"
- "系统更新"
- "模型合并"
- "AI 安全"
- "App Store"
- "Apple"
- "政策更新"
- "macOS"
- "OpenAI"
- "恶意软件分析"
- "iOS"
- "智能体规模化"
- "具身智能"
- "Anthropic"
- "ICML"
- "Claude"
- "Beta"
- "灵巧手"
- "实战教程"
- "Daybreak"
- "网络安全"
- "长时程任务"
- "AI Agent"
- "深度学习"
- "扩散模型"
- "政企合作"
- "产业分析"
- "自然语言处理"
- "AI"
- "LoRA"

---

> - SSR-Merge：把 LoRA 合并从'参数算术'变成'信号路由' | ICML 2026
> - 手把手带工程同学从零实现一个完整的 LLM（CS336）——Transformer 篇
> - 九成具身智能公司在东部沿海，长沙抢走了“制造权”
> - Apple 开发者计划许可协议更新，新增 HomeView 小组件、团体购买等多项条款
> - Apple 推送 iOS / iPadOS / macOS 等 27.2 beta 4 测试版更新
> - SentinelOne 借助 OpenAI Daybreak，将恶意软件分析从数周缩短至数小时
> - Third Moment Research 如何同时运行 1 万个智能体并持续工作 36 小时以上
> - Anthropic 在新加坡开设亚太第五个办公室，并与新加坡政府签署 AI 合作备忘录
> - macOS Golden Gate 是个 Bug 满地的版本：从密码 App 键盘焦点回归说起

## 📥 Tech News

### [SSR-Merge：把 LoRA 合并从'参数算术'变成'信号路由' | ICML 2026](https://www.bestblogs.dev/article/fff4064e32?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-14 20:00:00
![](https://image.jido.dev/20251127045420_f18cd4b9)
**SSR-Merge 提出在信号空间而非参数空间进行多 LoRA 合并，通过子空间信号路由解决任务间的相互干扰问题，实现了无训练、无调参且零额外推理开销的高保真合并。**

* 传统任务算术、稀疏化等合并在参数空间操作，导致不同任务信号相互干扰，出现画风串味、角色崩坏；SSR-Merge 转而统计通道内信号的相关结构，反向拆解混合信号，并用方向引导矩阵将信号路由到正确出口
* 路由器 R = QG⁻¹ 由数据的二阶统计量直接解出，等价于最小二乘的唯一解析解，无需训练与调参，且可重参数化为标准 LoRA
* 实验表明其在单任务保真度、多任务组合生成及人像精修上均显著优于现有基线，稳定性突出
* 该工作入选 ICML 2026，对需要组合多个 LoRA 能力的图像生成场景有直接实用价值，适合关注扩散模型与模型合并方向的研究者和工程师阅读

### [手把手带工程同学从零实现一个完整的 LLM（CS336）——Transformer 篇](https://www.bestblogs.dev/article/93e8cbc5d5?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-14 18:00:00
![](https://image.jido.dev/20260527050038_b20a9a1.jpeg)
**本文面向工程同学，以循序渐进的方式讲解如何从零实现一个基于 Transformer 的语言模型，覆盖数据预处理、模型架构设计与训练优化的完整链路，并配有可执行的 Python 代码示例。**

* 从线性回归实验入手，说明模型参数初始化、损失函数计算与梯度下降的优化过程，为理解更复杂的神经网络奠定基础
* 逐步实现 MLP 与 TinyGPT，重点拆解 Transformer 核心组件：因果自注意力、前馈网络与位置编码，并解释它们如何协同处理序列数据
* 训练实践涵盖文本转数字编码、训练批次构造、交叉熵损失优化，利用"下一个字符即答案"的自监督方式完成文字自动生成
* 全文约 2.5 万字，源自斯坦福 CS336 课程体系，适合想系统理解 LLM 底层原理的工程师学习，阅读门槛低但内容完整扎实

### [九成具身智能公司在东部沿海，长沙抢走了“制造权”](https://www.infoq.cn/article/ZqJq0uHBPvvEewkc0ZFC)

来源：InfoQ 推荐

发布时间：2026-10-14 17:35:33
![](https://static001.infoq.cn/resource/image/b0/c5/b0cedb0760a44e637d7bc5e5dda971c5.jpg)
**具身智能的竞争焦点正从“大脑”算法转向“身体”量产，长沙凭借三十年制造家底，通过“优势制造能力转化工程”卡位灵巧手、腱绳、指节等硬件制造环节，避开与东部沿海在算法和整机品牌上的正面竞争。**

* 产业逻辑：样机靠 3D 打印和手工装配三个月即可攒出，但万台级量产拼的是良率管理、成本控制与供应链组织；一双灵巧手指尖皮肤含 30 多项专利、近 20 个关节，上百家企业参与研发
* 典型企业路径：岱勒新材把超细钨丝工艺转化为 0.005 毫米仿生腱绳（抗疲劳超 150 万次）；华曙高科用金属 3D 打印一体成型仿生指节消除装配误差；蓝思科技建成年产 50 万台机器人产能；中联重科将挖掘机工厂变为训练场，积累 18 万条数据和 120 个训练工位
* 区域协同：湘江新区以 200 亿元母基金和训练场地等资源集聚超 1600 家 AI 相关企业，2025 年产业链规上企业营收 440 亿元；全省 14 个市州错位分工，覆盖零部件、整机、数据与场景验证
* 三道短板：核心部件多停留在送样验证阶段，验证不等于量产；缺乏具备生态主导力的链主企业；东部沿海同行已领先数年，时间窗口紧张
* 文章判断“灵巧操作是机器人走进真实世界的最后一厘米”，靠制造体系而非算法跨越，并指出关键部件、整机场景、数据仿真、芯片算法四类待补位机会

### [Apple 开发者计划许可协议更新，新增 HomeView 小组件、团体购买等多项条款](https://developer.apple.com/news/?id=17mwd36z)

来源：Latest News - Apple Developer

发布时间：2026-10-14 06:00:09
![](https://developer.apple.com/news/images/og/apple-developer-og.png)
**Apple 更新了开发者计划许可协议，新增了 Live Assistance API、App Replacement Entitlement、HomeView 小组件及订阅团体购买等多项条款规范，开发者需登录账户接受新协议后方可继续使用相关服务。**

* 第 3.2 节更新了使用 Apple 软件与服务的安全及相关要求；
* 新增 Live Assistance API 与 App Replacement Entitlement 的专用条款（3.3.8(j)(k)）；
* 规范了 iOS 应用小组件在 Apple HomeView 上的展示，以及 iOS 应用中 CarPlay 功能在 HomeView 上的可用性（6.4 系列条款）；
* 附表 2、附表 3 明确了订阅多席位"团体购买"（Group Purchases）及面向 Apple Business / Apple School Manager 组织的"批量购买"（Volume Purchasing）条款；
* 税务合规方面，Apple 将依法向税务机关申报税务、销售及联系方式等信息，开发者仅可在法律要求范围内使用 Apple 共享的客户税务信息。

新协议的各语言翻译版本将在一个月内上线 Apple 开发者网站。对上架 App Store 或使用上述新能力的开发者而言，需及时审阅变更并完成签署，避免影响账号及应用状态。

### [Apple 推送 iOS / iPadOS / macOS 等 27.2 beta 4 测试版更新](https://t.me/AppleNuts/2540)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-15 01:00:26
![](https://cdn5.telesco.pe/file/OdFI0dfBdFv1I5blPQW9gI_fRpiYVDryu-QSUhuijx33E5pOn2FIC3-jz9cqvo5Ha7u8b3_O98PykUMs4vQsa1m_LP3CH-uMEPwu9cayInTKvzgAzrP-g01WquqIX5xzn7pWL5Eyo0rCoXX9Kk4omYt1mCW5nxZcilA-P80kBwVZ44xh9HbPhfk4BwfF23PBn-MGJWQ_1w1d5LpEN5mvvw7bOJmSmXMO6geknRdKiYH-MwW-6ADjnVdoO-H_DT6hu0xsVy0AoXs4jnlqEJhEtgeKzUFB9Mgp4yRRLEuFdChtqr-ipV5btFybPsSNdrDfafgtnObHMKeZJ_JbWduMyg.jpg)
**Apple 面向测试渠道发布了 27.2 版本系列的第四个测试版更新，一次性覆盖 iPhone、iPad、Mac、Vision Pro 与 Apple Watch 五大平台。**

* iOS 27.2 beta 4（构建号 24B5110a）
* iPadOS 27.2 beta 4（构建号 24B5110a）
* macOS 27.2 beta 4（构建号 26B5112a）
* visionOS 27.2 beta 4（构建号 24N5114a）
* watchOS 27.2 beta 4（构建号 24S5112a）

各平台构建号末尾均带有字母“a”后缀，按照苹果惯例，这类构建通常出现在接近正式发布的阶段，意味着本周期已进入以稳定性和缺陷修复为主的收敛期。原消息仅列出版本号与构建号，未附具体功能更新说明，适合跟踪苹果系统更新节奏的开发者与尝鲜用户参考；测试版仍可能存在不稳定因素，普通用户建议等待正式版推送。

### [SentinelOne 借助 OpenAI Daybreak，将恶意软件分析从数周缩短至数小时](https://openai.com/index/sentinelone)

来源：OpenAI News

发布时间：2026-10-14 20:00:00

**网络安全厂商 SentinelOne 借助 OpenAI Daybreak 模型，将恶意软件分析周期从数周压缩至数小时。**

* 分析效率的大幅提升释放了安全团队的人力，使其从繁重的分析任务中腾出精力，有能力调查更多威胁
* 这是 Daybreak 模型在安全领域落地的代表性案例，展示了大模型在恶意软件分析场景中的实用价值
* 对关注 AI 赋能安全运营的团队具有参考意义；不过当前内容仅为案例导语，缺少具体技术路径、准确率与量化对比等细节，深度有限

### [Third Moment Research 如何同时运行 1 万个智能体并持续工作 36 小时以上](https://openai.com/index/third-moment-research)

来源：OpenAI News

发布时间：2026-10-14 15:00:00

**AI 实验室 Third Moment Research 展示了超大规模、长时程的智能体运行实践：同时运行 1 万个智能体，且可持续工作超过 36 小时。**

* 技术栈涵盖 GPT-6 Astra、GPT-6.1 Sol、Codex，以及用于网络安全的 Daybreak 模型
* 其构建的智能体具备长时间专注执行的能力，并能在使用过程中持续改进，形成「越用越好」的效果
* 该案例对研究智能体规模化调度、长时程稳定性与持续学习的团队具有参考价值；当前文章为简讯形式，具体架构与工程细节待原文展开

## 🤖 AI Coding

### [Anthropic 在新加坡开设亚太第五个办公室，并与新加坡政府签署 AI 合作备忘录](https://www.anthropic.com/news/singapore-office-opening)

来源：Anthropic News

发布时间：2026-10-14 08:00:00
![](https://www-cdn.anthropic.com/images/4zrzovbb/website/5f455d24ea80569b34eb4347f06152d8a5508722-1000x1000.svg)
**Anthropic 宣布在新加坡开设亚太区第五个办公室，并与新加坡数字发展及新闻部签署谅解备忘录（MOU），双方将在 AI 安全、模型评估与负责任采用等领域深化合作。**

* 新加坡是 Anthropic 最活跃的市场之一：在最新经济指数中，其 Claude.ai 人均使用量在 121 个国家中排名第二，约为按人口规模预测值的 6 倍。
* MOU 涵盖 AI 安全/模型评估的技术交流、AI 采用及影响研究、公私部门负责任推广等；双方合作始于 2023 年 IMDA 与 AI Verify 基金会的生成式 AI 评估沙盒，此后还完成了英、中、马、泰四语红队测试项目。
* 落地案例：GovTech 超 1500 名工程师使用 Claude Code 现代化政府系统；DBS 在软件开发与生产力场景应用 Claude；GIC 在投资及公司服务团队推广；Grab 的销售助手 BriX 每季度节省约 4 万小时；Sea 与 Supabase 也在基于 Claude 构建。
* 受监管行业（如金融服务）可通过 Amazon Bedrock 的区域内推理运行 Claude，以满足严格的数据处理合规要求。

## 💾 Daily Dev

### [macOS Golden Gate 是个 Bug 满地的版本：从密码 App 键盘焦点回归说起](https://lapcatsoftware.com/articles/2026/10/5.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-15 00:32:49
![](https://cdn4.telesco.pe/file/h9-vn5vGpZcfgWYh0fWJdMsEVsi3wjJA6XQj2yQ2pEj51qc3ybupWH6vmr_xVkVVMdJpw8eZDVw8VWot3VGW3ZthmgFir8Sgg1JfF9PXBf3OQJ-RIDBUq0lRpz-0zv-h0_BRTxqHJBQ22ogir8dvBJXlxvjVl1Uhk475_-zoOacPPl9TEHNPmaCCJaIY0oSvYpBq3TdVgFHeqZOuzG2pxZFss5-j6BpMJuo4oByrYQYGTnAxuNtYI1htwsn-7XGY8HDane6HCuVvdjes8Kmy2Quv0CK4HyYSIR2O8izMBIix4dqFFSBg1QtiEoH19_dnvpmWXiIBfQeZ6ZSuVctvLg.jpg)
**资深 Mac 开发者撰文批评 macOS 27 Golden Gate 充满 Bug，驳斥其是"Snow Leopard 式稳定修复版"的说法，并以密码 App 的键盘焦点回归问题为实例佐证。**

* 作者指出 Snow Leopard 的稳定口碑是近两年小版本迭代修出来的，10.6.0 本身距 10.5.0 发布也近两年；如今苹果严格按年发布大版本，只会不断累积新 Bug，却无暇修复旧问题。
* 他早在今年 6 月发现的"App 正在后台运行"通知相关问题，至今公开正式版仍未修复；同时因 Feedback Assistant 如黑洞般毫无反馈而选择抵制，不再逐一上报 Bug。
* 具体回归案例：在没有 Touch ID 的 Mac 上，密码 App 启动时密码输入框未获得键盘焦点，直接输入只会触发系统提示音，必须先按 Tab 键才行；该问题与系统设置中的"键盘导航"开关无关，且 macOS Tahoe 上行为正常。
* 作者质疑苹果连键盘焦点这类基础功能都会出错，戏称他们是否在用"氛围编程"（vibe-coding）的方式开发 macOS。
