---
title: "Daily News #2026-10-06"
date: "2026-10-06 08:00:00"
description: >
  一些关于开发的杂谈话题 - 代码审核 Agent 的记忆不在对话里：把企业数仓沉淀为可治理的共享语义记忆｜QCon上海 使用 tag_class 配置 Bazel 模块扩展
tags:
- "tag_class"
- "记忆系统"
- "工业智能"
- "Starlark"
- "Agent Coding"
- "软件开发"
- "Bazel"
- "代码审核"
- "Bzlmod"
- "观点杂谈"
- "数据治理"
- "构建工具"
- "语义记忆"
- "AI"
- "AI Agent"

---

> - 一些关于开发的杂谈话题 - 代码审核
> - Agent 的记忆不在对话里：把企业数仓沉淀为可治理的共享语义记忆｜QCon上海
> - 使用 tag_class 配置 Bazel 模块扩展

## 🍎 iOS Blog

### [一些关于开发的杂谈话题 - 代码审核](https://onevcat.com/2026/10/agent-review/)

来源：OneV's Den

发布时间：2026-10-05 00:00:00

**资深开发者回顾三年前对 AI 编程的预测，指出以 Opus 4.5 和 GPT-5.2-Codex 为代表的 agent coding 能力飞跃，已让"AI 主驾、人类副驾"的图景以远超预期的速度成为现实，软件开发的工作性质已彻底改变，代码审核成为愈发核心的话题。**

* 三年前 Kite、Tabnine 与早期 Copilot 时代的判断大多应验：让 AI 依据测试完成实现、人类必须花大量时间 review 并真正理解 AI 产出的代码等观点如今已成现实
* 原预估业界至少需要五年才能把人类从编程任务中解放出来，但去年底以来的 agent coding 新时代明显加速了这一进程
* 三年前后的软件开发已不是同一个工种，开发者此前被认为重要的技能正在发生转移，如何审核与维护 AI 生成的代码成为新的关键能力

## 📥 Tech News

### [Agent 的记忆不在对话里：把企业数仓沉淀为可治理的共享语义记忆｜QCon上海](https://www.infoq.cn/article/M4mgbKf4RDv5AKTwQvFH)

来源：InfoQ 推荐

发布时间：2026-10-04 10:00:00
![](https://static001.infoq.cn/resource/image/0e/92/0ebc3716538efee4dea8a82a5d9d2992.jpg)
**卡奥斯工业智能首席科学家余锦泽将在 QCon 上海分享：工业多智能体真正缺的记忆不是主流框架关注的"用户说过什么"，而是藏在数仓、代码与文档中的企业数据语义；且写错的记忆比遗忘更危险——实测只注入一半语义时，回答正确率反而低于完全不注入。**

* 写入侧坚持"大模型只提议、真实数据裁决"：须通过取值重叠度、父键唯一性、时间轴校验等判据方可入库，记忆按数据验证、人工断言、缺口三级置信分层，人工断言永不冒充数据验证（约束写进接口签名而非规章）。
* 冲突消解三招：时间轴校验排除巧合性重合、双源融合（代码中 JOIN 证据优先于命名推断）、对抗评审多数否决打回重抽。
* 使用侧按问句锚定对象、只注入命中子图并挂载指标口径；实体未在记忆中命中即明确拒答，答案同屏给出口径卡保证可追溯；配套"消费方审计"防止记忆存而不用。
* 经验沉淀固化为代码而非文档：时序假象固化为采样窗口判据，建模规范做成可插拔提示词组件后，对比实验显示候选大幅收敛、已验证占比上升。
* 核心结论是"企业语义记忆是需要治理的资产"——写入有裁决、冲突有消解、经验能沉淀、错误可撤销；演讲同时坦承覆盖率代价、写治理吞吐受限、阈值需跨行业重标定等边界与取舍。

## 💾 Daily Dev

### [使用 tag_class 配置 Bazel 模块扩展](https://adincebic.com/2026/10/04/configuring-bazel-module-extensions-with.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-05 00:27:41
![](https://cdn4.telesco.pe/file/PRWXCKr24xNYcJL4_wcj50eGUWgzYeMlevIT0arjlvU2yM5Xd_FuEF0hah3CzLaM4AH5jiZDKXLBPGXaPOQ2DF9RH9f1JLDTNtOqbLpALYgdjH4KlfQV-WUzlyXnEnUrG1kHqkAjHjNWZCxxIL2E-sYrUoJ5n5vETYOu3C3x9NaiqLS4AV4peMYUpxVrhy_FULW6BDwuQ6a3CwTNlAvuMcUAWMcI8BBOKDbQ4jhDjhDoz6U6HmGAotmDc5oR6P2sTA-NiOP6v5_FUcyztMx6lgBaUdZdxBr80Lv5Xu982MN2BChdWyMG71Opxztm048EPErsZXNtPkwg9bufVhX70Q.jpg)
**文章讲解如何在 Bazel 模块扩展（module extension）中使用 tag_class API 定义标签属性，使用户能在 MODULE.bazel 中向扩展传递 URL、SHA-256 等配置值。**

* 模块扩展本身不像 repository rule 或普通规则那样直接支持属性，而是通过 tag_class 暴露属性；单个扩展可以定义多个 tag class。
* 扩展评估时通过 module_ctx.modules 遍历所有使用该扩展的模块，再经 module.tags.binary 读取各模块的标签，将 name、url、sha256 等值转发给 repository rule，由其执行下载并生成导出文件的 BUILD.bazel。
* 文章以“下载二进制”为例给出完整链路：MODULE.bazel 中 binary_download.binary(...) 写入标签 → tag_class 定义属性 → module extension 调用 repository rule → 下载的二进制文件，最后通过 use_repo 引入生成的仓库。
* 内容属于入门级简化讲解，作者自述官方文档已有较好覆盖，适合刚开始接触 Bzlmod 机制的开发者快速理解标签配置的工作方式。
