---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  刚刚，曝黎曼猜想被证明，Claude 立大功 Pinterest 联合英特尔将开源性能分析推向互联网级规模
tags:
- "AI"
- "开源"
- "基础设施"
- "可观测性"
- "性能分析"
- "数学"
- "黎曼猜想"
- "Claude"
- "云原生"
- "Lean"

---

> - 刚刚，曝黎曼猜想被证明，Claude 立大功
> - Pinterest 联合英特尔将开源性能分析推向互联网级规模

## 📥 Tech News

### [刚刚，曝黎曼猜想被证明，Claude 立大功](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作找到黎曼猜想的证明，并进一步证明了广义黎曼猜想，证明首次以 Lean 形式化语言公开，被视为 AI 参与前沿数学研究的突破性事件。**

* 黎曼猜想是悬置 167 年的千禧年难题，此次证明以 Lean 形式化语言写成机器可检查的代码，计算机可直接验证推导正确性，这是此类成果首次采用形式化方法公开
* Alpöge 通过 Claude 探索迭代 theta 提升构造证明路径，AI 在高阶自守形式理论等复杂推导上展现出超越人类的速度，研究后期甚至超过 Alpöge 本人
* Claude 此前已在数论领域发现雅可比猜想反例与 Hadamard 矩阵，正从辅助计算工具转变为主动探索研究路线的合作者，AI 能力的评估标准也随之从解题速度转向创造性发现
* 若验证成功，数学家角色可能从“发现者”转向“解释者”与“应用者”，数学研究范式与人类研究者的定位面临重新定义

### [Pinterest 联合英特尔将开源性能分析推向互联网级规模](https://www.infoq.cn/article/fs4IuBTjwIwR1xUgdjqt)

来源：InfoQ 推荐

发布时间：2026-11-22 11:00:00
![](https://static001.infoq.cn/resource/image/98/45/983966ab1295ed5f5b70ba7aedd52245.png)
**Pinterest 联合英特尔扩展开源持续性能分析工具 gProfiler，为数十万实例规模的生产集群提供跨语言、跨机器的统一性能可见性，并将全部新能力回馈开源社区。**

* Pinterest 运维数十万实例、支撑 6.4 亿月活，服务横跨 Java、Python、C++、Go、Node.js；此前使用 perf、async-profiler、py-spy 等工具产生的数据碎片化，难以跨语言、跨机器关联分析
* 新增能力包括动态远程分析、基于 Intel PerfSpect 的硬件层遥测（缓存行为、内存带宽、CPU 停顿）、将函数与缓存未命中和分支预测错误关联的 PMC 火焰图，以及可视化 IO、锁、远程调用等待的挂钟时间分析
* 架构上采集与分析分离：代理平时休眠（CPU 占用低于 1%、内存约 100MB），自动发现进程并合并堆栈生成统一火焰图，无需修改应用代码；数据存于 S3，经 SQS 异步索引、ClickHouse 支撑分析查询，React 前端支持跨主机、服务和时间段比较
* 相比 Parca、Grafana Pyroscope 及 Datadog 等竞品，gProfiler 定位为现有分析工具的编排层而非替代品，差异化在多运行时整合、开源可扩展及硬件级分析能力
