---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  Claude 助力证明黎曼猜想：Anthropic 数学家以 Lean 形式化公开证明 Pinterest 联合英特尔将开源性能分析推向互联网级规模
tags:
- "DevOps"
- "黎曼猜想"
- "形式化验证"
- "gProfiler"
- "可观测性"
- "AI for Science"
- "开源"
- "Claude"
- "性能分析"
- "Lean"

---

> - Claude 助力证明黎曼猜想：Anthropic 数学家以 Lean 形式化公开证明
> - Pinterest 联合英特尔将开源性能分析推向互联网级规模

## 📥 Tech News

### [Claude 助力证明黎曼猜想：Anthropic 数学家以 Lean 形式化公开证明](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作，找到了悬置 167 年的黎曼猜想证明，并进一步证明了广义黎曼猜想，证明首次以 Lean 形式化语言、以机器可检查代码的形式公开，被视为 AI 参与前沿数学研究的突破性事件。**

* 证明过程中，Alpöge 借助 Claude 探索迭代 theta 提升构造，AI 在高阶自守形式等复杂推导和技术细节上的推演速度超越了人类研究者，甚至在研究后期超过 Alpöge 本人；
* Claude 此前已在数论领域产出雅可比猜想反例、Hadamard 矩阵等成果，AI 的数学能力正从解题与验证转向主动探索研究路线并提出原创成果，智能评估标准也随之从解题速度转向创造性发现；
* 若证明最终通过社区验证，数论将获得坚实的理论基础，广义黎曼猜想的证明还会进一步扩展其适用范围；
* 文章同时指出，此事将促使数学界重新思考研究范式：当重大成果越来越多由 AI 首先提出，人类需更长时间理解其逻辑，数学家的角色或从“发现者”转向“解释者”与“应用者”。

### [Pinterest 联合英特尔将开源性能分析推向互联网级规模](https://www.infoq.cn/article/fs4IuBTjwIwR1xUgdjqt)

来源：InfoQ 推荐

发布时间：2026-11-22 11:00:00
![](https://static001.infoq.cn/resource/image/98/45/983966ab1295ed5f5b70ba7aedd52245.png)
**Pinterest 联合英特尔扩展开源持续性能分析工具 gProfiler，为其支撑 6.4 亿月活用户的数十万实例集群提供跨语言、跨机器的生产级性能可见性，并将新能力全部回馈开源社区。**

* gProfiler 定位为编排层，将系统级 perf 数据与运行时专用工具（Java 的 async-profiler、基于 eBPF 的 Python 分析等）整合为单机全部进程的统一火焰图，全程无需修改应用代码
* 新增硬件层遥测（集成 Intel PerfSpect）、PMC 火焰图和挂钟时间分析，可将函数与缓存未命中、分支预测错误等硬件事件关联，并可视化 IO、锁等待导致的响应缓慢
* 代理平时休眠（CPU 低于 1%、内存约 100MB），支持按服务/主机/集群远程动态触发分析，无需 shell 权限；数据经 S3 存储、SQS 异步索引后进入 ClickHouse 供查询
* 双方针对生产环境解决了代理资源消耗、磁盘占用、TB 级数据摄入等稳定性问题；与 Parca、Grafana Pyroscope、Datadog 相比，其差异化在于多运行时编排与硬件级分析能力
