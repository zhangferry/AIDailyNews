---
title: "Daily News #2026-08-19"
date: "2026-08-19 08:00:00"
description: >
  Agent 的命门是上下文：关键不在少给，而在给对 Snowflake CoCo AI 成本优化指南：7 个关键方法
tags:
- "AI 成本治理"
- "SQL"
- "AI 编程"
- "多 Agent 工作流"
- "上下文工程"
- "云成本优化"
- "Snowflake"
- "Token 优化"
- "FinOps"
- "AI Agent"

---

> - Agent 的命门是上下文：关键不在少给，而在给对
> - Snowflake CoCo AI 成本优化指南：7 个关键方法

## 📥 Tech News

### [Agent 的命门是上下文：关键不在少给，而在给对](https://www.bestblogs.dev/article/4b235c023f?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-08-18 08:45:00
![](https://image.jido.dev/20251127045410_4d44587a)
**背景/问题**：多 Agent 工作流的 Token 成本居高不下。作者以一张 2480 万 Token、约 202 元的真实账单切入，质疑 CodeGraph（代码结构图谱）与 RTK（终端输出压缩）两个看似合理的"做减法"优化为何没能压低总成本。

**核心观点/方案**：提出"上下文信息密度 = 相关可执行信息 ÷ 进入窗口的全部上下文"的判断框架，主张省 Token 必须从局部输出、行动路径、整体结果三层评估。实验显示：CodeGraph 在符号查询任务可省 80%，但调用链与精确行号任务反增 95.8%~152.9%；RTK 压短终端字符 40% 却使总 Token 增 4.23%，还会过滤掉关键命中。有效做法是把上下文拆为 Handoff（交接纸条）与 Artifact（完整材料）分层，CodeGraph 只在前段付一次成本，RTK 按场景启用并配熔断回退，状态迁移交给脚本。最终每步 Token 从 10.68 万降至 6.70 万，Claude 下总量降 23.34%。

**结论/价值**：省 Token 的本质不是少给而是给对。文章实验设计严谨，含对照与重复实验及方差分析，结论反直觉且有数据支撑，适合构建多 Agent 系统与 AI 编程工具的工程师深度参考；局限在于结论基于自研 Devflow 工作流，迁移到其他架构时需重新验证。

### [Snowflake CoCo AI 成本优化指南：7 个关键方法](https://www.infoq.cn/article/pOfV96f9DHG9Cw1KQAZB)

来源：InfoQ 推荐

发布时间：2026-08-18 16:29:05
![](https://static001.infoq.cn/resource/image/5e/68/5e0d76ec9728090617596d6733b74c68.png)
**背景/问题**：Snowflake CoCo 能将自然语言转化为真实工作流，但 Agentic 会话按 token 消耗 credits，缺乏治理机制时成本极易失控，麦肯锡调研显示 93% 组织 AI 支出超预算。

**核心观点/方案**：文章给出 7 层递进的治理手段：用 ACCOUNT_USAGE 视图摸清成本基线；用 /cost-intelligence skill 以自然语言完成归因查询；按 surface 设置每日 credit 限额快速封顶单用户；per-user quotas 作为跨 AI 域的强制硬阻断；budgets 基于时序预测提供提前预警（低延迟模式成本放大 12 倍需谨慎）；RBAC 模型访问控制从源头导向低成本模型（旧 allowlist 参数 2026 年 11 月移除）；基于 alerts/tasks 的自动化 guardrails 检测并取消失控查询。

**结论/价值**：整套方法对应"可见性—优化—强制执行"三层框架，均可通过 SQL 或 Snowsight 管理，附大量可直接使用的代码。对部署企业级 AI 的平台团队极具操作价值，其治理思路也可迁移到其他云 AI 服务的 FinOps 实践中。
