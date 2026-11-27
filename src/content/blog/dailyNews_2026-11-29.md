---
title: "Daily News #2026-11-29"
date: "2026-11-29 08:00:00"
description: >
  Octop Memory：把 Agent 记忆拆成五个可配置环节，让 Agent 记得住、查得准、改得对
tags:
- "LLM"
- "记忆系统"
- "开源"
- "Agent"
- "RAG"

---

> - Octop Memory：把 Agent 记忆拆成五个可配置环节，让 Agent 记得住、查得准、改得对

## 📥 Tech News

### [Octop Memory：把 Agent 记忆拆成五个可配置环节，让 Agent 记得住、查得准、改得对](https://www.infoq.cn/article/DUG6LEgK9Vi4sGy6QYTW)

来源：InfoQ 推荐

发布时间：2026-11-27 17:25:02
![](https://static001.infoq.cn/resource/image/f8/d0/f8e0e4459b714d10090e5280fcac71d0.png)
**开源多智能体框架 Octop 推出可配置的记忆系统 Octop Memory，将记忆拆解为写入、提炼、晋升审批、召回、存储五个可独立编排的环节，目标是让 Agent 沉淀出可溯源、可治理的“工作直觉”。**

文章首先指出仅有 RAG 不够的核心症结：检索到的片段难以区分是用户要求、助手建议还是工具结果，结论无法回到原始对话核对，适用条件易在整理时丢失。为此 Octop Memory 设计了完整闭环：

* 写入提供被动留存证据与 Agent 主动保存双路径，可按场景单独或组合启用
* 后台提炼的候选须经过价值评估、证据核验、冲突检查等晋升治理，或由人工审核台确认后生效；旧记忆被替代时保留完整审计轨迹而非静默抹除
* 召回区分宿主被动预取与 Agent 主动查证，支持混合策略，并可设置 token 软预算与耗时上限
* 存储底座支持 SQLite/PostgreSQL、命名空间隔离、生命周期清理与跨库迁移

架构上库只提供原子能力、由宿主决定产品策略。文章还给出个人助理、研发助手、强推理模型搭档三类差异化配置示例，并规划在 2.0 中原生支持 MCP、推进多 Agent 记忆协同共享。适合构建长期协作型 Agent 的开发者参考。
