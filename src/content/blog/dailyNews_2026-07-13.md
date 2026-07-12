---
title: "Daily News #2026-07-13"
date: "2026-07-13 08:00:00"
description: >
  万字复盘：从模型到可用 Agent，WorkBuddy 的 Harness 工程是怎么做的？ 面向 Qwen 系列模型线性注意力的高性能优化实践 Bazel 模块扩展协同工作：深入理解 override_repo
tags:
- "大模型应用"
- "系统架构"
- "AI Infra"
- "大模型"
- "Bzlmod"
- "构建工具"
- "AI Agent"
- "Android开发"
- "算子优化"
- "依赖管理"
- "Bazel"
- "Harness工程"
- "线性注意力"
- "Qwen"
- "上下文工程"

---

> - 万字复盘：从模型到可用 Agent，WorkBuddy 的 Harness 工程是怎么做的？
> - 面向 Qwen 系列模型线性注意力的高性能优化实践
> - Bazel 模块扩展协同工作：深入理解 override_repo

## 📥 Tech News

### [万字复盘：从模型到可用 Agent，WorkBuddy 的 Harness 工程是怎么做的？](https://www.bestblogs.dev/article/5044bf45a4?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-12 14:30:00
![](https://image.jido.dev/20251127045419_08d80bcb)
**背景/问题**：大语言模型本身本质上是“无状态函数”，仅依靠其强大的推理能力无法保证 Agent（智能体）在实际业务场景中稳定、可靠地完成任务。如何解决工具接入、上下文爆炸、记忆混淆等工程难题，是 Agent 从“能执行”走向“可落地”的痛点。

**核心观点/方案**：文章指出“模型决定上限，上下文和 Harness 决定下限”。WorkBuddy 通过精细的 Context Engineering（上下文工程）和记忆管理来保障 Agent 表现。上下文工程追求信息的相关、准确与及时，通过写入、选择、检索、压缩、隔离五个动作精准控制模型输入；记忆系统严格区分边界，将事实记忆注入上下文，而将程序性记忆沉淀为可版本化、可审计的 Skill。此外，通过意图识别与工具的渐进式加载策略，避免一次性铺开所有能力，同时理清了工具、MCP、Skill、Plugin 的协作层次。

**结论/价值**：本文是一份极具深度与实战价值的 Agent 工程拆解指南，系统论述了外部工程机制如何弥补大模型自身的不可靠性。非常适合 AI 产品经理、架构师及大模型应用开发者阅读，为构建企业级、高可用的 AI Agent 提供了清晰的设计范式和落地参考。

### [面向 Qwen 系列模型线性注意力的高性能优化实践](https://www.infoq.cn/article/wg5h3JBMvs5ZkoP0azha)

来源：InfoQ 推荐

发布时间：2026-07-12 10:00:00
![](https://static001.infoq.cn/resource/image/83/2d/8322af560fa2df672498789473f10a2d.jpg)
**背景/问题**：随着 Qwen 等大模型引入混合注意力结构，其线性注意力层 GDN（Gated Delta Network）在训练与推理中的计算开销日益显著。现有实现面临两大痛点：一是多步算子频繁读写 HBM 导致严重的访存瓶颈；二是状态递推的串行性限制了算子并行度，在长序列或张量并行（TP）等场景下 GPU 利用率低下。

**核心观点/方案**：阿里 Qwen 团队提出了基于 TileLang 的高性能算子库 FlashQLA。该方案将前向与反向流程各拆分为融合算子，通过数据复用降低访存开销，并利用 warp-specialization 实现计算重叠。同时，基于门控衰减特性实现自动化卡内序列并行，动态调节并行粒度；针对指数衰减特性的注意力头，采用轻量级预热替代昂贵的修正矩阵计算，大幅降低开销。

**结论/价值**：在 Hopper 显卡上，FlashQLA 相比现有方案实现了显著的前反向加速，有效提升了模型的预训练与端侧推理效率。本文适合 AI 基础设施工程师与底层性能优化专家阅读，提供了极具参考价值的算子级融合与并行设计思路。需注意本文属于大会演讲预告，部分系统底层实现细节有待后续深度拆解。

## 💾 Daily Dev

### [Bazel 模块扩展协同工作：深入理解 override_repo](https://adincebic.com/2026/07/12/making-bazel-module-extensions-work.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-07-12 21:02:54
![](https://cdn4.telesco.pe/file/HQnrbEGDm61Ov0vIuMK0NAvAmIu4elfEy9ZFqQyA_yvmsWlBiJbaft-7gFWuU9Rp74s9HrmNknzaIB7YzzQWMcGezh0X6UespoIb85UOgcD16uBkTYlYnpbf4uG0AZOVWx9NtMwVs2UGDXButeUd03a5CHyJKW_p8kDNmnwN7fGx317IVXl-880zs_G8xZkFV_F_MVHV5bn_WRS12As72uyCgZPbhUlw4NfEqOwdT6x3joVSRJWPo_m3RgLI5Gx74wilzulhepSa5aGxyv_U4ptTcsr9a_2Zx-2XlnUaBidIYBzRVZfXVda3a1bGOEJG4IC-cCFrs1m6Pxz6xPmf0w.jpg)
**背景/问题**：随着 Bazel 6 逐渐被淘汰，Bzlmod（Bazel 模块）在生态系统中被广泛采用。但在集成不同的规则集（如设置密封的 Android 工具链）时，多个模块扩展可能会生成同名或冲突的代码库，导致迁移过程和配置变得复杂。

**核心观点/方案**：文章介绍了 Bazel 7.4.0 引入的 `override_repo` 功能。该功能允许根模块使用位置参数或关键字参数，将模块扩展自动生成的代码库替换为根模块中已可见的同名代码库。例如，利用该特性，可以让 `rules_android` 直接引用由 `hermetic_android_toolchains` 下载的密封 SDK，避免重复配置。

**结论/价值**：`override_repo` 虽然是一个微小的 API 特性，但能有效避免引入冗余的同名代码库，显著简化不同模块扩展之间的集成与迁移工作。对于重度依赖 Bazel 进行复杂项目构建和依赖管理的基础架构工程师或高级开发者来说，是一个非常实用的进阶技巧。
