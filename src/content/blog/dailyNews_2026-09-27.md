---
title: "Daily News #2026-09-27"
date: "2026-09-27 08:00:00"
description: >
  htmx 4.0 发布：改用 Fetch API 重写，内置 DOM Morphing Swap，并明确属性继承规则 Claude 开放插件开发者门户：支持提交、审核跟踪与使用分析
tags:
- "超媒体"
- "Anthropic"
- "Claude"
- "AI"
- "JavaScript"
- "前端"
- "Web开发"
- "MCP"
- "插件开发"
- "htmx"

---

> - htmx 4.0 发布：改用 Fetch API 重写，内置 DOM Morphing Swap，并明确属性继承规则
> - Claude 开放插件开发者门户：支持提交、审核跟踪与使用分析

## 📥 Tech News

### [htmx 4.0 发布：改用 Fetch API 重写，内置 DOM Morphing Swap，并明确属性继承规则](https://www.infoq.cn/article/kJ4EkjPLVTh9iT5yyXkM)

来源：InfoQ 推荐

发布时间：2026-09-25 14:18:00
![](https://static001.infoq.cn/resource/image/5b/be/5b619fb6d122a708398376777d562ebe.jpg)
**htmx 发布 4.0.0 主版本，传输层由 XMLHttpRequest 全面改写为 fetch() API，并引入内置 Morphing Swap 与显式属性继承机制，是继 2.0 后首个主版本更新。**

* fetch 重写支持原生流式传输，脚本体积约 14KB；基于 idiomorph 的 Morphing Swap 在更新 DOM 时保留输入框焦点等状态；新增 hx-partial 标签，让单个响应可更新多个目标元素，替代原有带外交换的繁琐写法。
* 升级最大风险在属性继承改为显式机制：只有加 :inherited 后缀的属性才会传给子元素，原先靠 hx-headers 传递 CSRF Token 的代码会静默失效并被服务器以 403 拒绝。此外事件名统一为 htmx:phase:action 格式（如 htmx:afterRequest 改为 htmx:after:request），hx-disable 更名为 hx-ignore，新增 60 秒请求超时，历史记录改为重新拉取页面而非 localStorage 快照。
* 社区反应分化：HN 讨论帖超 700 赞，开发者称赞 Go + SQLite + htmx 技术栈及 Claude 等 AI 助手对其的良好支持；也有 .NET/Angular 开发者认为它混淆表现层与业务逻辑，团队准备迁回 React。
* 兼容性保障较完善：4.0 通过 npm 的 next 标签发布，未锁版本的 CDN 用户不受强制升级，2.x 继续维护且无终止时间；官方提供 upgrade-check 命令行工具排查继承、重命名等兼容问题，并附带面向 LLM 辅助升级的 Skills 文件。

## 🤖 AI Coding

### [Claude 开放插件开发者门户：支持提交、审核跟踪与使用分析](https://claude.com/blog/build-plugins-for-claude)

来源：Claude Blog

发布时间：2026-09-25 08:00:00
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab6a76f77cf7911a03be1bd_d852ff4a.png)
**Anthropic 上线 Claude 插件开发者门户，开发者现可向 Claude 目录提交插件、跟踪审核进度，并在上线后查看使用分析数据；插件已成为第三方扩展 Claude 的主要方式。**

* 插件可封装 MCP 连接器、Agent Skills 或两者组合。提交路径有两种：单一 MCP 连接器（指向远程 MCP 服务器），或插件包（将 MCP 服务器与 Skills 组合托管在 GitHub 后提交仓库）；在 Claude Code 中，插件还可包含 LSP、命令、Hooks 和 Agents
* 门户在提交时即自动校验并进行安全扫描，开发者可查看审核状态、扫描结果与修改建议，获批后自行决定发布时机；目前门户面向付费 Claude 计划的开发者开放
* 插件上线后提供使用分析，包括按产品界面和版本统计的安装量，以及列表浏览量、带来曝光的搜索词等发现侧数据，便于优化功能与_listing_
* Claude 已支持采用无状态核心的 MCP 2.0 规范，并提供两项扩展增强插件体验：MCP Apps（在聊天中嵌入交互式 UI）与 Enterprise Managed Auth（面向企业用户的零触 OAuth）
* 未来数周内，统一的发现体验将覆盖 Claude 与 Claude Code；现有 Skills、连接器或插件无需任何改动，后续开发者可将连接器列表升级为插件
