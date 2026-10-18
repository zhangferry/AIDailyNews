---
title: "Daily News #2026-10-20"
date: "2026-10-20 08:00:00"
description: >
  Meta 联手苹果推出全美最强开源模型，编码基测输给智谱、Kimi BazelCon 2026：参会笔记与观察
tags:
- "本地部署"
- "开源模型"
- "MoE"
- "Meta"
- "开发工具"
- "大模型"
- "Bazel"
- "Rust"
- "iOS"
- "构建系统"

---

> - Meta 联手苹果推出全美最强开源模型，编码基测输给智谱、Kimi
> - BazelCon 2026：参会笔记与观察

## 📥 Tech News

### [Meta 联手苹果推出全美最强开源模型，编码基测输给智谱、Kimi](https://www.infoq.cn/article/EuYOPRUBAeBgBGBu5ktk)

来源：InfoQ 推荐

发布时间：2026-10-18 23:01:32
![](https://static001.infoq.cn/resource/image/6a/c5/6ac620300bf7c754e3643785e65bccc5.png)
**Meta 开放 Muse Spark Open 模型权重，定位为美国能力最强的开放权重模型，可在两台 M5 Ultra Mac Studio 上本地运行，但 Terminal-Bench 2.1 与 DeepSWE 1.1 编程测试得分低于智谱 GLM 5.3 max 和 Kimi K3 max。**

* 模型采用稀疏 MoE 架构，总参数 8160 亿、每 token 激活约 420 亿，支持 104.8 万 token 上下文，可接收文本、图片、音频、视频输入，输出为文本
* 桌面部署是 MoE（降低激活计算）、NVFP4 量化（权重从 BF16 的约 1.65TB 压缩至 537GB）与多机分布式（Thunderbolt RDMA）共同作用的结果；四台 Mac Studio 推理速度超 36 token/s
* Muse Model License 含商业条款：提供模型即服务且年收入超 2000 万美元的企业需通知 Meta 并签订单独书面协议（内部使用、研究等场景除外）
* 集成 SGLang 的 Helion 定制算子在 NVIDIA/AMD GPU 上实现最高 3.95 倍算子级加速，但端到端收益有限（AMD MI350 约 3%）
* 社区评价不一：有人质疑基准成绩针对榜单优化，也有用户称 Muse 系列实际使用表现出色

## 💾 Daily Dev

### [BazelCon 2026：参会笔记与观察](https://adincebic.com/2026/10/18/bazelcon-my-notes-and-observations.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-18 22:57:38
![](https://cdn4.telesco.pe/file/Sg3WYxt0WaB8XvFOH3ordWiXbSyKXP6tAB59spDh1cvZHz4YrVqAJ89NpKgG1MG8HM6r3oQlkKu8wr2V4o5DhqIpYYlp3ZTAXSbwPwOiVZ7jAEg3tFcH12N-y0HsTaPJkWb1o6dbKJEvR5L9Q8lABp5S9Gzs6GEirh8MDPY_UBpGIOJJpvHvkOEQKNy2T2gv2bAy9Xgl3_pU26MRC-6MlqYv96cHS2oq69_NskC_OxAIbCuKGecaVOuhiGO-kf1QovmNLxQQ-dVSkaf13CXAyovqdJ5TNIF2RXMP31xxoQkSjPQkG7mzq0sPooTImKS-lBZ6Ysnrh6aHfLAf8IZZZg.jpg)
**这篇参会笔记梳理了 BazelCon 2026 的核心观察：Bazel 10 将继续把语言特定功能从核心迁至 Starlark 扩展并带来多项性能改进，其中部分优化正由 AI 加速推进。**

* AI 已成为日常基础工具，会场共识是"让 agent 去读文档"而非亲自阅读；IDE 地位下降，rules_xcodeproj 在部分大型组织中的使用减少，转向 VS Code 等轻量方案，IDE 的下一机会在代码审查集成与代码导航。
* Project Skymetal 计划用 Rust 等原生代码逐步替换 Bazel 的 Java 实现，通过 JNI 桥接、逐组件迁移，早期结果乐观；Skycache 尝试远程缓存日益昂贵的分析状态，Google 已在内部试验早期实现。
* Hermetic LLVM 提供完全密闭的 C/C++ 工具链备受关注；rules_rs 凭借快速 Cargo 依赖解析与密闭性获得认可；Aspect 正为 macOS 开发可插拔的自定义沙箱方案，以缩小与 Linux 的性能差距。
* Apple BOF 聚焦静态链接导致测试磁盘占用过高、Linux 发起构建 + macOS 远程执行的混合 RBE 架构，以及 rules_swift 的 Swift 显式模块支持；EngFlow 的 any2bazel 通过确定性对比原构建系统输出，引导 AI agent 完成正确迁移。
