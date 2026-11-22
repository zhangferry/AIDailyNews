---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  Anthropic 数学家宣布与 Claude 合作证明黎曼猜想，以 Lean 形式化语言公开 Pinterest 联合英特尔将开源性能分析推向互联网级规模
tags:
- "黎曼猜想"
- "开源"
- "gProfiler"
- "Lean 形式化验证"
- "云原生"
- "Claude"
- "AI"
- "可观测性"
- "性能分析"
- "数学"

---

> - Anthropic 数学家宣布与 Claude 合作证明黎曼猜想，以 Lean 形式化语言公开
> - Pinterest 联合英特尔将开源性能分析推向互联网级规模

## 📥 Tech News

### [Anthropic 数学家宣布与 Claude 合作证明黎曼猜想，以 Lean 形式化语言公开](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作找到黎曼猜想及广义黎曼猜想的证明，并首次以 Lean 形式化语言公开，引发数学界对 AI 参与前沿数学研究的强烈关注。**

* 黎曼猜想是悬置 167 年的千禧年难题，此次证明以机器可检查的 Lean 代码形式公开，既能由计算机验证推导正确性，也代表了 AI 辅助数学研究的前沿方法。
* Alpöge 借助 Claude 探索迭代 theta 提升构造证明路径，称 AI 在高阶自守形式等复杂推导上速度惊人，研究后期甚至超过本人，标志着 AI 从辅助工具向研究合作者转变。
* 此前 Claude 已在数论领域产出雅可比猜想反例、Hadamard 矩阵等成果，AI 能力正从解题走向原创发现，智能评估标准也随之从解题速度转向创造性发现。
* 若最终确认，数学家角色可能从“发现者”转向“解释者”与“应用者”；同时人类仍需理解证明方法，并评估其能否推动其他领域发展。

### [Pinterest 联合英特尔将开源性能分析推向互联网级规模](https://www.infoq.cn/article/fs4IuBTjwIwR1xUgdjqt)

来源：InfoQ 推荐

发布时间：2026-11-22 11:00:00
![](https://static001.infoq.cn/resource/image/98/45/983966ab1295ed5f5b70ba7aedd52245.png)
**Pinterest 与英特尔合作扩展开源持续性能分析工具 gProfiler，为数十万实例规模的生产集群提供跨语言、跨硬件层的统一性能可见性，并将新能力全部回馈开源社区。**

* Pinterest 支撑 6.4 亿月活用户，服务横跨 Java、Python、C++、Go、Node.js，此前 perf、async-profiler、py-spy 等工具产出的数据碎片化、难以跨机器关联；gProfiler 作为编排层整合系统级与各运行时分析器，对主机全部进程生成统一火焰图，无需修改应用代码。
* 新增能力包括动态远程分析（代理休眠时 CPU 占用低于 1%、内存约 100MB）、集成 Intel PerfSpect 的硬件遥测（缓存行为、内存带宽、CPU 停顿）、PMC 火焰图及挂钟时间分析，后者可将线程等待 IO、锁或远程调用的耗时可视化，弥补 CPU 分析的盲区。
* 架构上采集与分析分离：数据存 S3、经 SQS 异步索引、入 ClickHouse 支撑查询，React 前端支持跨主机、服务与时间段的火焰图对比。
* 与 Parca、Grafana Pyroscope 等 eBPF 方案相比，其差异化在多运行时编排与硬件级分析能力；相较 VTune 更适配云原生集群而非单机性能工程。
