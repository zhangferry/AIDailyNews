---
title: "Daily News #2026-10-10"
date: "2026-10-10 08:00:00"
description: >
  谷歌借助 AI 与差分模糊测试将 C 语言依赖库改写为 Rust OpenAI 打击两起利用 AI 的“虚假前台”影响力行动 Anthropic 发布 2026 年使用政策更新：整合欺骗性行为规则、收紧武器与监控条款 Anthropic 推出 Cyber Mission 网络安全计划：发布关键基础设施防御项目与免费 OSS Scanner 软件工程先驱、阿波罗计划软件负责人 Margaret Hamilton 逝世，享年 90 岁 手腕骨折亲测：iOS 27 听写终于支持文本编辑命令，macOS 仍未跟进
tags:
- "虚假信息治理"
- "内存安全"
- "关键基础设施"
- "计算机历史"
- "无障碍"
- "语音控制"
- "影响力行动"
- "OpenAI"
- "iOS"
- "Anthropic"
- "网络安全"
- "漏洞挖掘"
- "Rust"
- "NASA"
- "讣告"
- "模糊测试"
- "内容审核"
- "听写"
- "开源安全"
- "软件工程"
- "阿波罗计划"
- "合规"
- "Claude"
- "macOS"
- "AI"
- "使用政策"
- "AI安全"
- "谷歌"

---

> - 谷歌借助 AI 与差分模糊测试将 C 语言依赖库改写为 Rust
> - OpenAI 打击两起利用 AI 的“虚假前台”影响力行动
> - Anthropic 发布 2026 年使用政策更新：整合欺骗性行为规则、收紧武器与监控条款
> - Anthropic 推出 Cyber Mission 网络安全计划：发布关键基础设施防御项目与免费 OSS Scanner
> - 软件工程先驱、阿波罗计划软件负责人 Margaret Hamilton 逝世，享年 90 岁
> - 手腕骨折亲测：iOS 27 听写终于支持文本编辑命令，macOS 仍未跟进

## 📥 Tech News

### [谷歌借助 AI 与差分模糊测试将 C 语言依赖库改写为 Rust](https://www.infoq.cn/article/LVsjSV4pIlh3Liz0KZZE)

来源：InfoQ 推荐

发布时间：2026-10-08 17:12:00
![](https://static001.infoq.cn/resource/image/3e/d0/3e6abbc8c458c8e064e985e88f561bd0.jpg)
**谷歌安全团队利用 Gemini 将约 3000 行的 C 语言图像库 giflib 翻译为 ABI 兼容的 Rust 库，经大规模差分测试验证语义等价，并在 CVE-2026-26740 公开披露前就从底层免疫该堆写入零日漏洞。**

* 迁移采用三阶段自动化流程：一次性提示词完成整体移植、人工细化 FFI 裸指针的所有权与生命周期不变量、差分测试引擎将失败执行轨迹反馈给模型迭代生成补丁
* 验证规模可观：对超 3000 万个真实 GIF 文件做逐比特回归解码，差分模糊测试器连续六天累计 2 亿次迭代未发现功能漂移，还揪出谷歌自家旧 C 补丁遗留的越界写入漏洞
* 生产收益明确：Rust 版与 C 版性能持平，因内存安全内建于类型系统，得以移除进程隔离沙箱，P99 尾部延迟显著降低
* 社区争议在于人工审计语义退化、修复不安全 FFI 边界的工作量远超代码生成本身，更大规模项目更适合 c2rust 转译器加 AI 重构的路线；成果已开源为 giflib-rs

### [OpenAI 打击两起利用 AI 的“虚假前台”影响力行动](https://openai.com/index/disrupting-ai-enabled-false-front-operations)

来源：OpenAI News

发布时间：2026-10-08 08:00:00

**OpenAI 宣布打击了两起利用 AI 开展的影响力行动：行动方伪装成记者并设立虚假智库，借“虚假前台”身份传播地缘政治信息。**

* 此类行动以虚构的媒体机构和研究组织为掩护，增强传播内容的可信度
* 该报告属于平台安全治理与防御分析性质，是观察 AI 滥用形态及平台应对策略的一手资料
* 原文仅提供概要信息，未披露行动归属、规模、技术手法等详细分析，深度有待查看全文

## 🤖 AI Coding

### [Anthropic 发布 2026 年使用政策更新：整合欺骗性行为规则、收紧武器与监控条款](https://www.anthropic.com/news/2026-usage-policy-update)

来源：Anthropic News

发布时间：2026-10-08 08:00:00
![](https://www-cdn.anthropic.com/images/4zrzovbb/website/6d4a0d28992ade92d6fa63646fd9c9d318245c6c-2400x1260.jpg)
**Anthropic 发布新版使用政策，11 月 12 日生效，大部分改动是对既有规则的澄清，并针对 Claude 承担更长时程、更独立任务的新能力补充了执行示例。**

* 新增“不得从事欺骗性活动”章节，将原先分散在选举、欺诈、隐私和虚假信息部分的规则整合为统一禁令，覆盖政治或商业性质的假账号网络、虚假新闻站点及影响力行动工具链；选举章节更名为“不得破坏民主进程”，同时取消了对个性化投票和竞选定向的一揽子禁令，以避免误伤多语言选民信息等合法工作，但依赖欺骗或滥用个人数据的定向仍被禁止
* 武器禁令明确扩展到使武器运作的软件与组件（如制导控制软件、武装无人机等自主载具）；监控条款更精确：禁止未经同意的实时或事后数据追踪，禁止用 Claude 决定或推荐执法调查、逮捕或指控对象，已同意的追踪（如反欺诈监控）、内容审核、新闻和法律研究仍被允许
* 高风险用例（影响健康、法律权利、财务、生计等）维持“人在回路”和告知 AI 参与的要求，并新增模型连接可造成伤害的自主硬件时的条件：合格操作员须能观察并停止设备，断连时设备须能保持安全状态
* 新增对模型持续且无目的虐待行为的禁令（仅限极端情况，普通用户挫败、黑暗创作主题、测试与研究不适用），并澄清了支持地区政策对位于不支持地区的人员和实体的执行口径

### [Anthropic 推出 Cyber Mission 网络安全计划：发布关键基础设施防御项目与免费 OSS Scanner](https://www.anthropic.com/news/anthropic-cyber-mission)

来源：Anthropic News

发布时间：2026-10-08 08:00:00
![](https://www-cdn.anthropic.com/images/4zrzovbb/website/e6614df689675126bb32ceb5cfcaaae016050c36-2000x1125.jpg)
**Anthropic 启动长期网络安全计划 Cyber Mission，聚焦关键基础设施防护与开源软件安全两大方向，同步推出 Critical Infrastructure Defense Program（CIDP）和免费的开源项目安全扫描服务 OSS Scanner。**

* CIDP 面向保护电力、水务、交通等运营技术（OT）的可信服务商，提供前沿 Claude 模型、驻场工程师和威胁研究支持，创始伙伴包括 CrowdStrike、Palo Alto Networks、Dragos、Booz Allen、Accenture、德勤、普华永道、Rockwell Automation 等；OT 设备难以停机打补丁、漏洞常长期未修，是该计划的切入点
* OSS Scanner 受 Google OSS-Fuzz 启发、项目自愿加入，定期用最强模型免费扫描，报告包含可利用性 PoC、漏洞解释和建议修复，均为模型生成、无人工审核，预期真阳性率超 90%，但可能出现严重性评级不准等误差，适合有能力消化结果的项目；其余项目仍走人工验证的协同披露（CVD）流程
* 计划背景是 Project Glasswing 的经验教训：找漏洞容易、验证排序修复难；Glasswing 已并入扩展版 Cyber Verification Program，向更多防御者开放最强模型
* 开源方向后续目标包括更快送达漏洞发现、自动化 triage 与补丁、探索更安全的架构与编码实践；Anthropic 已资助 Python Software Foundation、OpenSSF（Linux 基金会）、Apache 软件基金会等，8 月推出的 Defender Advantage Fund 为相关试点提供资金并维持 OSS Scanner 免费

## 💾 Daily Dev

### [软件工程先驱、阿波罗计划软件负责人 Margaret Hamilton 逝世，享年 90 岁](https://mjtsai.com/blog/2026/10/08/margaret-hamilton-rip/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-08 23:27:10
![](https://cdn4.telesco.pe/file/q4JhZivcK-47DCPlxSvHbgAuAZljj5FeFgKZAuoBNa_jX6ryN38QMKNUTPUh3t6WXHvY1sxtncxh90pxxk_PjOZBUzULbv6Qsc0gSGNKSgEgi-jdylldAfjf4phRS2zWkr_D-dc2wpJjXphoLLImk2AuxpdjVqDuVpCcDoAnm4gL39EMOkR0yIQ2_8EpnMeDtpMs8fUUTgs9H-bykaS1PSn5p_KrDf75ySBcT2u3i45UZNILMP4Lg5TaBQ8ANfMLcpDt-Vs6QQq3aP__qba7GGggPduZkgPTrVKH9pwgPtYG2Pg8Ywldd1AX0R-D4dz5n4FTxqT7yl1xP9tHfZb8Jw.jpg)
**软件工程学科的奠基人之一、NASA 阿波罗计划软件团队负责人 Margaret Hamilton 于 9 月 30 日逝世，享年 90 岁。** 她在 MIT 仪器实验室领导阿波罗计划的软件工程团队，一生发表论文超过 130 篇，推动"软件工程"成为一门独立学科。

* 阿波罗 11 号登月舱"鹰"即将降落月面时，机载计算机因硬件开关故障触发 1202 过载警报；Hamilton 团队设计的优先级驱动软件能自动关闭非必要的后台任务、优先保障任务关键流程，休斯顿因此信任这套系统并批准继续降落，两名宇航员最终首次踏上月球。
* 她被视为"software engineering"一词的提出者之一，相关表述源自一次刊登于绝版教科书《Fluency With Information Technology》的访谈，博主 Dave DeGraw 找到完整访谈全文并以合理使用原则存档发布。
* 文末附有计算机历史博物馆的口述历史资料及多篇阿波罗制导计算机相关文章链接，适合对计算史与容错系统设计感兴趣的读者延伸阅读。

### [手腕骨折亲测：iOS 27 听写终于支持文本编辑命令，macOS 仍未跟进](https://mjtsai.com/blog/2026/10/08/what-a-broken-wrist-taught-me-about-ios-27-dictation-and-macos-voice-control/)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-08 23:27:09
![](https://cdn4.telesco.pe/file/q4JhZivcK-47DCPlxSvHbgAuAZljj5FeFgKZAuoBNa_jX6ryN38QMKNUTPUh3t6WXHvY1sxtncxh90pxxk_PjOZBUzULbv6Qsc0gSGNKSgEgi-jdylldAfjf4phRS2zWkr_D-dc2wpJjXphoLLImk2AuxpdjVqDuVpCcDoAnm4gL39EMOkR0yIQ2_8EpnMeDtpMs8fUUTgs9H-bykaS1PSn5p_KrDf75ySBcT2u3i45UZNILMP4Lg5TaBQ8ANfMLcpDt-Vs6QQq3aP__qba7GGggPduZkgPTrVKH9pwgPtYG2Pg8Ywldd1AX0R-D4dz5n4FTxqT7yl1xP9tHfZb8Jw.jpg)
**Adam Engst 借手腕骨折期间的亲身体验指出，iOS 27 终于将部分"语音控制"（Voice Control）的文本编辑能力下放到普通听写功能，但 macOS 27 Golden Gate 并未同步跟进。**

* iOS 27 听写新增命令：可用 "Capitalize …" / "Lowercase …" 调整单词大小写，用 "Replace A with B" 纠正听错或说错的内容，还支持 "Select …" 和 "Undo that"；其余大部分语音控制命令在听写模式下仍不可用。
* 长期开启语音控制的问题在于持续监听、容易在不希望输入时插入文本，且听写准确率有时略逊一筹，因此这批改进让普通听写更可独当一面。
* 遗憾的是 macOS 27 Golden Gate 的听写功能没有任何文本编辑命令，跨平台体验不一致。
* 有读者反馈 iOS 27 在多语言听写场景反而退步：iOS 26 能记住不同联系人和应用的语言偏好，iOS 27 不再记忆，每次都需手动切换语言。
