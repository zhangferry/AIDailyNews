---
title: "Daily News #2026-07-20"
date: "2026-07-20 08:00:00"
description: >
  朱松纯两万字演讲：反思AI产业泡沫与“唯大模型论”，提出“为机器立心”的AGI架构 边端AI不只缺算力：安谋科技重做CPU、NPU、VPU与AI操作系统 A Note on Bazel’s config.exec()
tags:
- "NPU"
- "API设计"
- "CUV框架"
- "人工智能"
- "芯片架构"
- "VPU"
- "Bazel"
- "端侧AI"
- "构建工具"
- "代码规范"
- "AGI"
- "人机共生"
- "AIOS"
- "产业泡沫"

---

> - 朱松纯两万字演讲：反思AI产业泡沫与“唯大模型论”，提出“为机器立心”的AGI架构
> - 边端AI不只缺算力：安谋科技重做CPU、NPU、VPU与AI操作系统
> - A Note on Bazel’s config.exec()

## 📥 Tech News

### [朱松纯两万字演讲：反思AI产业泡沫与“唯大模型论”，提出“为机器立心”的AGI架构](https://www.bestblogs.dev/article/06ac8ab341?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-19 15:52:00
![](https://media.bestblogs.dev/20260719125010_8c61df1.jpeg)
**背景/问题**：当前全球 AI 产业陷入了对算力、数据和大模型的盲目崇拜与营销炒作中，引发了从“AI 四小龙”到“百模大战”等多轮泡沫。现存的以数据统计拟合为基础的大语言模型存在根本性的局限，无法产生内在的驱动力，更无法回答“智能体为什么要做这件事”的价值问题。

**核心观点/方案**：朱松纯教授提出构建通用人工智能（AGI）的五层架构，并首创 CUV（认知-能力-价值）数理框架。该方案主张“为机器立心”，强调智能体的行为应当由内在的价值系统驱动，而非单纯依赖外部数据的映射。通过“通通”智能体的实践验证，这种以价值驱动为核心的通用智能，在复杂场景的任务泛化与社会交互测试中，表现超越了 GPT-5 等主流大模型。

**结论/价值**：文章指出社会智能是 AGI 融入人类社会的最后一道屏障，呼吁在技术狂热中保持思想自主，构建中国自己的 AGI 战略与叙事体系。对于 AI 研究人员、架构师及科技战略决策者而言，这是一篇极具思想穿透力的必读佳作。它不仅打破了“唯大模型论”的局限，更为跨越当前 AI 发展瓶颈、探索下一代真正通用人工智能提供了坚实的理论基石与全新的工程范式。

### [边端AI不只缺算力：安谋科技重做CPU、NPU、VPU与AI操作系统](https://www.infoq.cn/article/iIoJ2qhXbXCH2ozGqCJ6)

来源：InfoQ 推荐

发布时间：2026-07-19 11:09:02
![](https://static001.infoq.cn/resource/image/57/8b/578377260282d7b5c65aece216bb438b.jpg)
**背景/问题**：随着大模型向边缘设备下沉，传统的“云端模型缩小化”思路遭遇瓶颈。端侧设备不仅面临严格的功耗、内存和散热限制，还需满足极高的实时响应要求，单纯的算力堆叠已无法解决复杂的异构计算需求。

**核心观点/方案**：安谋科技提出一套全栈边端 AI 基础设施方案：在 CPU 端引入 Helium 技术增强并行处理能力；NPU 端推出“周易”X3-Pro 架构，放弃单一峰值算力，转向兼顾算力、内存带宽和任务并发的统一架构；VPU 端引入任务感知编码，优化机器视觉的数据流转；同时牵头构建开源 AIOS 联盟，解决异构硬件间的模型路由、内存搬运（Zero Copy）和任务编排等系统级问题。

**结论/价值**：文章极具前瞻性地指出端侧 AI 竞争已从单卡算力比拼转向系统工程的协同效率。对于嵌入式开发者、AI 芯片架构师及边缘计算研究者而言，深入理解这种“软硬件深度协同”的系统性思路具有很高的启发价值。

## 💾 Daily Dev

### [A Note on Bazel’s config.exec()](https://adincebic.com/2026/07/19/a-note-on-bazels-configexec.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-07-19 23:27:33
![](https://cdn4.telesco.pe/file/D-9dyO10rKfOBa7scwd9e-xt6Xyyq1eTzJ3QobRAG2H4Jj4ZXI93wbXZS8MqheqXg5w_bAHEZlaCo9naXth4hsKmsV71_ViWZ7RHr1jXc9pPwoMoEGv-i9I8NstAO7VlPzGQy7vshLH9zRSzVI2gsbTqyZWAyAqo7a9K_dtEHSTDKsNlctkyIY1jtTvDlNLg-9KDbq6aoldMmPxDZX-781x7rRnXYLqnFfUVt0fkdWXHVfgdpdo5YfMiV3J-GMcSgxhUjiFDyJaS6h1yVZfoKe0EcchdukjToGrUVHCXs3NXfvDruZaxay8QRFDJDpyLRHOIJ8ImWNjb4oEvbnZBYg.jpg)
**背景/问题**：在使用 Bazel 构建系统编写自定义规则时，若需让规则在 exec（执行）配置下运行，传统做法是直接在规则定义中传入 `cfg = "exec"` 字符串。这种硬编码的字符串形式虽然能实现功能，但在代码的语义表达和后期维护上存在一定局限性。

**核心观点/方案**：作者建议开发者弃用这种特殊的字符串传参方式，转而使用更新的 transition 对象 API，即 `cfg = config.exec()`。该对象形式不仅提升了 API 的可读性和可发现性，让代码意图更加明确，更重要的是，它支持转换组合和传递 exec group 等高级特性，这是字符串形式无法做到的。

**结论/价值**：虽然这项改动属于代码风格层面的优化，并不会带来实质性的构建速度提升，但它极大增强了代码的规范性。对于重度依赖 Bazel 的工程团队或底层架构开发者而言，采纳这种更现代、更具扩展性的 API 调用方式具有显著的工程价值。
