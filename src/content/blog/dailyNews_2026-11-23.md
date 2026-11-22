---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作完成 Lean 形式化证明 Pinterest 联合英特尔将开源性能分析推向互联网级规模 华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机
tags:
- "AI"
- "开源"
- "大语言模型"
- "gProfiler"
- "性能分析"
- "可观测性"
- "云原生"
- "鸿蒙"
- "华为"
- "数学"
- "Lean"
- "产品评测"
- "AI 手机"
- "AI Agent"
- "Claude"

---

> - 曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作完成 Lean 形式化证明
> - Pinterest 联合英特尔将开源性能分析推向互联网级规模
> - 华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机

## 📥 Tech News

### [曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作完成 Lean 形式化证明](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作找到黎曼猜想的证明，并进一步证明了广义黎曼猜想，证明以 Lean 形式化语言公开，标志着 AI 从辅助工具向前沿数学研究合作者的角色转变。**

* 黎曼猜想是悬置 167 年的千禧年难题，本次证明首次以 Lean 形式化语言的机器可检查代码形式公开，既保证推导可被计算机验证，也体现了 AI 辅助数学研究的前沿方法论。
* Alpöge 通过 Claude 探索迭代 theta 提升构造证明路径，并指出 Claude 在处理高阶自守形式理论等复杂推导时速度超越人类研究者，甚至在研究后期超过他本人。
* Claude 此前已在数论领域取得雅可比猜想反例、Hadamard 矩阵发现等进展，AI 的数学能力正从解题验证走向原创性发现。
* 若证明最终通过验证，数学家的工作模式可能从「发现者」转向「解释者」与「应用者」，AI 正在重塑数学研究范式与智能水平的衡量标准。

### [Pinterest 联合英特尔将开源性能分析推向互联网级规模](https://www.infoq.cn/article/fs4IuBTjwIwR1xUgdjqt)

来源：InfoQ 推荐

发布时间：2026-11-22 11:00:00
![](https://static001.infoq.cn/resource/image/98/45/983966ab1295ed5f5b70ba7aedd52245.png)
**Pinterest 联合英特尔扩展开源持续性能分析工具 gProfiler，新增动态分析、硬件遥测、挂钟时间分析与 PMC 火焰图等能力，将性能分析打造为互联网级生产集群的常态化可观测能力。**

* Pinterest 运维数十万实例、支撑 6.4 亿月活，业务横跨 Java、Python、C++、Go 等多语言，此前 perf、async-profiler、py-spy 等工具产出的数据碎片化，难以跨语言、跨机器关联分析
* gProfiler 定位为编排层，自动发现进程并合并各运行时分析器结果为统一火焰图，无需修改应用代码；代理休眠时 CPU 占用低于 1%、内存约 100 MB，支持远程触发分析与参数热调整
* 集成 Intel PerfSpect 采集缓存行为、内存带宽、CPU 停顿等硬件信息，PMC 火焰图可将函数与缓存未命中、分支预测错误关联；挂钟时间分析用于定位 CPU 不高但响应缓慢的 IO、锁等待问题
* 数据链路采用 S3 存储、SQS 异步索引、ClickHouse 分析查询；相比 Parca、Pyroscope、Datadog 等竞品，差异化在系统级多运行时编排与硬件层分析，相比 VTune 更适配云原生集群场景

### [华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机](https://www.bestblogs.dev/article/27f1e1f7f5?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-21 12:00:00
![](https://media.bestblogs.dev/20261113050053_35a08f3.jpeg)
**华为子品牌 OSTA 星芒推出首款以 AI 为核心设计的鸿蒙手机 O1 Pro，以「小艺 AI 屏」取代传统桌面，尝试将手机交互方式从手动操作转变为指令式 AI 代理。**

* 硬件方面采用 16:9.5 阔直屏、麒麟 9030S 处理器与 7000mAh 大电池，硬件成熟度略逊于华为主力产品线。
* 「小艺 AI 屏」压缩传统图标入口，聚焦键盘、麦克风、附件按钮三大交互键，用户可通过自然语言指令完成 B 站内容聚合、购物比价、外卖点单、微信消息收发等任务，实现「不进 app 完成日常工作」的场景。
* 小艺基于盘古大模型并融合 DeepSeek 等前沿模型，相较鸿蒙 6.1 版本在识别、理解和代理操作速度上实现质的飞跃，接近人类手动操作水平。
* 星芒定位为面向「纯 AI 时代」的新生品牌，是华为对下一个十年人机交互方式的探索，适合关注 AI 硬件生态与人机交互演进的读者。
