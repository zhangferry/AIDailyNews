---
title: "Daily News #2026-11-24"
date: "2026-11-24 08:00:00"
description: >
  Perplexity and Intelligence：OpenAI 提议以困惑度作为衡量 AI 进展与安全的行业通用指标 Pinterest 联合英特尔将开源性能分析推向互联网级规模
tags:
- "基础设施"
- "可观测性"
- "预训练"
- "开源"
- "AI"
- "eBPF"
- "OpenAI"
- "性能分析"
- "AI安全"
- "困惑度"

---

> - Perplexity and Intelligence：OpenAI 提议以困惑度作为衡量 AI 进展与安全的行业通用指标
> - Pinterest 联合英特尔将开源性能分析推向互联网级规模

## 📥 Tech News

### [Perplexity and Intelligence：OpenAI 提议以困惑度作为衡量 AI 进展与安全的行业通用指标](https://openai.com/index/perplexity-and-intelligence)

来源：OpenAI News

发布时间：2026-11-22 08:00:00
![](https://images.ctfassets.net/kftzwdyauwt9/3q9FXuH69IDGjPgpzj2Ayv/95477fdeea31ffb7eae01ec1c191b1f0/research-acceleration-the-jagged-frontier-of-rsi-cover.png)
**OpenAI 首席科学家 Jakub Pachocki 发文，主张将困惑度（交叉熵损失）确立为跨实验室衡量 AI 智能进展的通用指标，首次公开 OpenAI 内部预训练困惑度数据，并呼吁行业据此建立共享安全标准与开发红线。**

* 核心论点：现代 AI 本质是在大规模语料上训练压缩器/预测器，新能力随困惑度下降而涌现——GPT-3.5（约 0.99）支撑 ChatGPT 流畅对话，GPT-4（约 0.91）催生思维链推理与现代推理模型，损失低于 0.8 后在网络安全与数学领域出现变革性能力，预计 0.68-0.7 区间将涌现目前无法预知的新能力。
* 困惑度约 0.76 的模型已在数学开放问题上接连产出突破性成果，作者据此推测 AI 参与预训练算法研究最早可能在 2027 年引发根本性进展的"雪崩"，而对齐与监控研究的加速恐难跟上。
* 治理提议：各前沿实验室共同设定基于困惑度等指标的开发上限，在监控能力（如 CoT 监控的继任者）达成具体里程碑前承诺不越线，并配套透明度标准与红队测试规范。
* 该指标的局限：各实验室数据集与数据配比不同导致难以横向比较、与具体任务表现脱节、无法反映思维链等预训练之外的进展、数据固有熵的下界未知——越接近下界，困惑度的微小下降对应的智能跃迁越大。

### [Pinterest 联合英特尔将开源性能分析推向互联网级规模](https://www.infoq.cn/article/fs4IuBTjwIwR1xUgdjqt)

来源：InfoQ 推荐

发布时间：2026-11-22 11:00:00
![](https://static001.infoq.cn/resource/image/98/45/983966ab1295ed5f5b70ba7aedd52245.png)
**Pinterest 联合英特尔扩展开源持续性能分析工具 gProfiler，为支撑 6.4 亿月活、数十万实例的生产集群提供性能可见性，并将新能力回馈开源社区。**

* 新增能力包括动态分析、硬件层遥测、挂钟时间分析与 PMC 火焰图：PMC 可将函数与缓存未命中、分支预测错误等硬件事件关联；挂钟分析则能定位 CPU 占用不高但响应缓慢时的 IO、锁与远程调用等待。
* gProfiler 定位为编排层，自动发现进程、启动分析器并合并堆栈生成跨 JVM、本地库与内核的统一火焰图，无需修改应用代码；代理平时休眠，CPU 占用低于 1%、内存约 100 MB，可通过心跳远程触发并动态调整分析频率、时长与所用的分析器，把性能分析变成一种运维能力。
* 架构上采集与分析分离：数据存 S3、经 SQS 异步索引、写入 ClickHouse 供查询，React 前端支持跨主机、服务与时间段的火焰图对比。
* 与 Parca、Grafana Pyroscope、Datadog 等竞品相比，差异化在于系统级多运行时编排、开源可扩展，以及通过 Intel PerfSpect 获得的硬件级分析能力。适合大规模生产集群的性能工程与可观测性团队参考。
