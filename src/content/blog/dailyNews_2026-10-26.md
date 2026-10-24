---
title: "Daily News #2026-10-26"
date: "2026-10-26 08:00:00"
description: >
  被拆掉的 NSHostingView 还会再建一次 View AI 助理争夺战：Instinct、Muse 与 Grok Bot 的入口之争、信任困境与盈利难题 何时应使用 Liquid Clustering？湖仓布局策略基准测试 实测 Kimi K3.1 Pro：3 万亿参数、100 万上下文，国产开源旗舰再攀性能天花板 Apple 为 iPhone Duo 发布特殊 iOS 27.2 RC 版本，修复数据迁移问题
tags:
- "湖仓一体"
- "iOS"
- "调试"
- "AppKit"
- "性能优化"
- "OTA"
- "生命周期"
- "macOS"
- "模型评测"
- "Apple"
- "数据布局"
- "Delta Lake"
- "大语言模型"
- "固件"
- "商业模式"
- "iPhone Duo"
- "产品分析"
- "科技行业分析"
- "SwiftUI"
- "人工智能"
- "AI Agent"
- "Liquid Clustering"
- "开源模型"
- "Kimi"

---

> - 被拆掉的 NSHostingView 还会再建一次 View
> - AI 助理争夺战：Instinct、Muse 与 Grok Bot 的入口之争、信任困境与盈利难题
> - 何时应使用 Liquid Clustering？湖仓布局策略基准测试
> - 实测 Kimi K3.1 Pro：3 万亿参数、100 万上下文，国产开源旗舰再攀性能天花板
> - Apple 为 iPhone Duo 发布特殊 iOS 27.2 RC 版本，修复数据迁移问题

## 🍎 iOS Blog

### [被拆掉的 NSHostingView 还会再建一次 View](https://onevcat.com/2026/10/nested-hosting-view/)

来源：OneV's Den

发布时间：2026-10-24 14:00:00

**onevcat 记录了 Prowl 中的一个诡异 bug：切换到 Canvas 视图时，进入前选中的 tab 对应的卡片一片空白，其他卡片均正常，切回 Default 或 Shelf 视图后该终端又完全可用，内部 agent 仍在正常工作。**

* 排查中发现一个反直觉的行为：SwiftUI 会在一个 view 已经被 dismantle 之后，再次调用其 makeNSView，这正是问题的根源，属于 SwiftUI 与 AppKit 混用时的生命周期问题
* Prowl 中每个终端 pane 背后是一个长寿的 GhosttySurfaceView（NSView），持有 Ghostty 的 surface 与背后的 shell 进程，用户在不同视图间切换时该 view 会被复用或重建
* 最终修复只需几行代码，但定位过程比预想曲折，作者完整记录了排查思路与中间的困惑
* 对从事 SwiftUI 与 AppKit 互操作（NSHostingView、NSViewRepresentable）的 macOS 开发者有较高参考价值

## 📥 Tech News

### [AI 助理争夺战：Instinct、Muse 与 Grok Bot 的入口之争、信任困境与盈利难题](https://www.bestblogs.dev/article/3d63b11351?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-24 10:49:00
![](https://image.jido.dev/20251127045520_f3caed2e)
**硅谷 101 深度解析 Instinct、Meta Muse、Grok Bot 三大 AI 助理产品的差异化切入路径，揭示 AI Agent 抢占用户任务执行入口的商业博弈，以及信任与盈利两大核心难题。**

* 三条路径分化明显：Instinct 以短信为零门槛入口、靠硬核用户裂变，但面临热度退潮与广告变现存疑；Meta Muse 借 WhatsApp/Instagram 社交分发优势，主打 Goals 长期委托与交易佣金模式；Grok Bot 创新多 Agent 协作界面，通过角色分工解决上下文污染、以状态动画降低人工监督成本
* 技术成熟度催化产品化：Harness 框架解决工具调用与重试编排，模型成本大幅下降（OpenAI Luna 仅为前沿模型 1/10），使长程持续运行的 Agent 在经济上成为可能
* 信任与平台冲突成核心障碍：Agent 易越权操作、隐私数据去向不透明，亚马逊已以安全为由封锁 Muse，根本矛盾在于 Agent "截胡"平台客户关系与广告收入
* 盈利模式尚未跑通：消费端烧钱补贴难以为继，企业端付费意愿强但数据合规成本高；专业化垂直 Agent 或成未来方向，长期信任的建立仍是决定胜负的关键

### [何时应使用 Liquid Clustering？湖仓布局策略基准测试](https://www.infoq.cn/article/lkefSu7SjjIHL1Fmk0Pv)

来源：InfoQ 推荐

发布时间：2026-10-24 10:00:00
![](https://static001.infoq.cn/resource/image/da/9f/daf11b674890e950bbd484f82a62f19f.jpg)
**一项基于 5000 万条合成记录、四种分析型工作负载的 Delta Lake 受控基准测试显示：Liquid Clustering 在点查询、时间范围聚合和大型聚合中延迟最低，应作为查询模式多变团队的默认选择；ZOrder 仅在过滤列与聚类键精确匹配的稳定多谓词负载中占优。**

* 两项反直觉发现：日期列作为 ZOrder 二级或三级键时，时间范围查询比简单日期分区慢 78%；多列精确过滤场景下，Liquid Clustering 比 ZOrder 慢约 5 倍、扫描数据量多出 10 倍。
* 结果由两个机制解释：文件剪枝效率与文件内局部性。ZOrder 和分区靠剪枝取胜，Liquid Clustering 凭希尔伯特曲线的局部性在查询不匹配或全表扫描时占优，点查询中甚至读更多字节反而更快。
* 实践决策：先自问热门查询是否总是按相同两三列筛选——是则对这些列做 ZOrder（高选择性列在前）；否则或查询模式会演变时选 Liquid Clustering，还可省去手动调度 OPTIMIZE 的运维成本。
* 局限：测试使用合成数据，未测量写入放大与布局维护开销，结论宜作方向性参考，不可逆的表设计决策前应用自身工作负载验证。

### [实测 Kimi K3.1 Pro：3 万亿参数、100 万上下文，国产开源旗舰再攀性能天花板](https://www.bestblogs.dev/article/e4059c1902?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-24 18:07:19
![](https://media.bestblogs.dev/20261024120900_lark2pad-1792807418768-26.jpg)
**月之暗面发布新一代旗舰模型 Kimi K3.1 Pro，凭借 3 万亿参数和 100 万上下文长度在多项基准中跻身全球前列，成为国产开源模型新的性能天花板。**

* 在 Artificial Analysis 智能指数中排名全球第四、开源第一；在 Office QA Pro v2 和 SpreadsheetBench 2 中超过 GPT-6 Astra 和 Opus 5.5，展现出强大的金融文档分析与电子表格操作能力
* 3D 创作与网页设计能力突出，可根据简单提示生成高质量 3D 动画和交互式网页，对材质、灯光、空间层次和动作节奏具有出色控制力
* 坚持"大而美"技术路线，不追求推理成本最小化，而是通过扩大参数规模与上下文长度提升复杂任务表现；同步推出高速版，并计划于 11 月 4 日前开放完整模型权重
* 在行业普遍追求更快更省的趋势下，该模型代表了对大模型能力上限的持续探索，使国产模型有机会参与全球顶尖竞争

### [Apple 为 iPhone Duo 发布特殊 iOS 27.2 RC 版本，修复数据迁移问题](https://t.me/AppleNuts/2556)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-24 06:58:48
![](https://cdn5.telesco.pe/file/DLfra1-QUB4DNALto2SQBd2t8_CALCeSoKZ8PrXDOJlCNefB6rIlSJwlIXkC38lcw4iAiYebQrSy0dgtLMYfZMtgbkvUgYOk6kFFilsHGSaG3FhWZ_skH9Hy5Sj9OSqL_Po8AzoliiJPCQ9BoInCg_zQPRFeMbLmVZSYFxcfmVThU9tQCa8mQOI8IyP0CLzNQ3XtKauZK6LToIl4AJONAhfVHEpm-wPoxOVXD98HzKqGQLRoF6d38kqpG0sa1EoOSndWqUlBnDt6_BHGFoTmVWOCAEhGAlgYGl1bg1-Cx7cuIiJT4EgaTgrF-23NzdkENpWQTvpNKrI_RjJyl_btfg.jpg)
**Apple 为 iPhone Duo 发布了特殊的 iOS 27.2 RC 版本（build 24B91016），目前无完整固件，仅能通过 OTA 更新。**

* build 号中的“1016”反映了苹果在 iPhone Duo 固件上的高频迭代，build 数字之大在苹果固件发布史上较为罕见。
* 该版本的核心目的是解决数据迁移问题：部分用户旧设备已尝鲜 iOS 27.2 RC，而 iPhone Duo 出厂固件为 iOS 27.1，版本不匹配导致无法完成数据传输。
* 已购入新机且旧设备运行 iOS 27.2 的用户无需担心，更新此版本后即可正常进行数据迁移。
* 更新至该版本后，iPhone Duo 将获得 Apple Pencil 支持。
