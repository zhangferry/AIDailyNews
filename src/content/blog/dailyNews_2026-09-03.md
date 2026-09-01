---
title: "Daily News #2026-09-03"
date: "2026-09-03 08:00:00"
description: >
  亚马逊开源内部 Agent 工作台 Kiro Crew：补齐长周期任务的工程控制层 How AI-native companies turn workflows into operating capability Healthcare organizations can now connect EHR and additional industry data to ChatGPT 使用 Foundation Models 构建多模态输入的 AI 功能 吴汉坤：AI 时代，演员第一个丢饭碗？
tags:
- "企业工作流"
- "AI"
- "ChatGPT"
- "AIGC"
- "Kiro"
- "开源"
- "Foundation Models"
- "AWS"
- "数字表演"
- "工程实践"
- "自动化"
- "OpenAI"
- "多模态"
- "EHR"
- "iOS"
- "播客"
- "AI Agents"
- "医疗数据集成"
- "影视创作"
- "Swift"
- "AI Agent"
- "医疗健康"
- "企业级AI"

---

> - 亚马逊开源内部 Agent 工作台 Kiro Crew：补齐长周期任务的工程控制层
> - How AI-native companies turn workflows into operating capability
> - Healthcare organizations can now connect EHR and additional industry data to ChatGPT
> - 使用 Foundation Models 构建多模态输入的 AI 功能
> - 吴汉坤：AI 时代，演员第一个丢饭碗？

## 📥 Tech News

### [亚马逊开源内部 Agent 工作台 Kiro Crew：补齐长周期任务的工程控制层](https://www.infoq.cn/article/Um4rVTweSFXAiwdGLFVB)

来源：InfoQ 推荐

发布时间：2026-09-01 19:57:24
![](https://static001.infoq.cn/resource/image/3e/a6/3e8049d108e6c6cf5a81a3efe68f46a6.jpg)
**背景/问题**：当开发者将代码迁移、故障排查等任务委派给多个 Agent 长时间运行时，瓶颈从“模型会不会写代码”转向 Agent 能否跨会话保留记忆、无人值守时安全执行、过程可审计且可人工接管。

**核心观点/方案**：亚马逊将内部业余项目 Kiro Crew（原 MeshClaw，半年内被近 4 万内部构建者采用）以 Apache 2.0 开源。它定位为长期存在的 Agent 工作空间：延续 Kiro 的规范驱动开发思路，在写代码前澄清需求歧义（如逻辑删除还是物理删除）；提供跨会话语义记忆、可复用技能沉淀、定时任务/Webhook 触发与失败重试；通过“问题雷达”追踪仓库 issue，支持 Slack 等消息工具操作。文章同时强调记忆治理（来源审计、编辑删除、限定作用域）与长期运行边界——受上下文窗口限制，长任务应拆为带检查点的状态化步骤，而非让模型无限循环。

**结论/价值**：Agent 竞争正从“一次生成多少代码”转向状态管理、成本预算、失败恢复等工程控制层，对企业落地 Agent 工作台有较高参考价值；需注意开源的是 Kiro Crew 而非完整 Kiro 产品，且长期记忆的治理成本不可低估。

### [How AI-native companies turn workflows into operating capability](https://openai.com/index/ai-native-company-workflows)

来源：OpenAI News

发布时间：2026-09-02 01:00:00

**背景/问题**：如何将日常工作流沉淀为可持续的运营能力，是企业在 AI 落地过程中普遍面临的挑战，AI 原生公司的实践路径成为行业关注焦点。

**核心观点/方案**：OpenAI 以 Basis、Clay、Exa Labs 三家 AI 原生公司为例，展示 AI Agent 在客户入驻、账户管理和开发者集成等业务场景中的实际应用，供企业管理者参考借鉴。

**结论/价值**：抓取内容仅为文章导语，缺乏具体技术架构、实施路径与量化效果，信息密度较低。适合快速了解企业级 AI Agent 应用方向的管理者与产品负责人，如需深度参考仍需阅读原文全文。

### [Healthcare organizations can now connect EHR and additional industry data to ChatGPT](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources)

来源：OpenAI News

发布时间：2026-09-01 20:00:00

**背景/问题**：医疗行业长期存在数据割裂问题，临床医生需在电子健康记录（EHR）、医学研究等多源系统间频繁切换，影响诊疗与决策效率。

**核心观点/方案**：OpenAI 宣布 ChatGPT 现可连接受信任的医疗数据源，包括 EHR 系统，帮助临床医生安全地获取患者上下文、医学研究等信息。

**结论/价值**：EHR 与大模型的集成是医疗 AI 落地的重要信号，但抓取内容仅为官方公告摘要，未涉及数据安全机制、合规细节与具体实现方式。适合医疗信息化从业者跟踪动向，实际落地评估需依赖后续技术文档与隐私合规审查。

## 💾 Daily Dev

### [使用 Foundation Models 构建多模态输入的 AI 功能](https://swiftwithmajid.com/2026/09/01/building-ai-features-using-foundation-models-multimodal-input/)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-02 00:42:23
![](https://cdn4.telesco.pe/file/iMLWVybxIwoeAIEe9ciw1xv3AN3mq9jJ9VP90oa26BDOTRwrgM_9sk-cThNabRMJp92lpLfuwringITjL6NmCQJCQeigxj7BcmZhS7CXH5yAIqK49H5xpiTZsAyt9gQ-4mP-9YmwGgjPLsEF9-IB_5pap7TPohnzSjFYabRlv-FjWD1WybNZx1x5n5L36WZHWBo1BdtO4s6xjeh-3XPLoCZqCwOkSOUtTpdtPESgAgI9x5RK_tEuousZTzjzjMffjf9bGEH3r0CmAqY_LWUDG_oD-CYkDFagCJcavU6wMVEVC37uQ5HOa0gmCnlfc2VGMgCLobJ3r8LayyOgtC8Jcw.jpg)
**背景/问题**：Apple 在 Foundation Models 框架中新增了开发者期待已久的多模态输入能力，端侧 AI 交互不再局限于纯文本，可以直接让模型理解图片等文件内容。

**核心观点/方案**：文章以一个"餐盘扫描"应用为例演示完整实现路径：先用 @Generable 宏定义结构化输出类型 PlateClassification（含餐品标题及糖分、蛋白质、纤维、饱和脂肪等布尔属性），再通过 LanguageModelSession 的 respond 新重载，配合类似 SwiftUI ViewBuilder 的 PromptBuilder 结果构建器，将文本指令与 Attachment 附件组合成提示词。Attachment 支持 URL、像素缓冲、CGImage、CIImage 等多种实例化方式，且可附加任意文件而非仅限图片。

**结论/价值**：多模态输入显著提升了 Foundation Models 构建真实功能的实用性，开发者无需再用文字向模型描述世界，直接交付图像即可完成推理。适合正在为 iOS 应用集成端侧 AI 的 Swift 开发者作为上手教程；局限在于示例较简单，未涉及识别精度、错误处理与性能等生产环境问题。

## 📻 Podcast

### [吴汉坤：AI 时代，演员第一个丢饭碗？](https://www.xiaoyuzhoufm.com/episode/6a959a88f03e74ee6b02d5bf)

来源：三五环

发布时间：2026-09-01 20:00:00
![](https://image.xyzcdn.net/Fu4ClHDng2TBItAcMVhPEmc3EQSy.png)
**背景/问题**：AI 视频生成技术正快速重塑影视行业，从业者普遍面临"演员是否第一个被 AI 取代"的焦虑。本期播客邀请兼具演员与 AI 创业者双重身份的吴汉坤，从跨界一线视角探讨技术变革下表演艺术的价值与创作者的应对之道。

**核心观点/方案**：吴汉坤结合独立完成《粉丝悖论》《人口异常》等 AI 短片的全流程经验（分镜、生图、视频生成、剪辑，使用 Kling 2.0 等工具），指出 AI 生成内容往往过于规律化，难以模拟喜剧等对毫秒级节奏要求极高的表演；真人演员的微表情、情绪停顿与设计性"破绽"恰是引发观众共鸣的关键。表演作为生命体验的表达涉及"自主意识"，是 AI 短期无法替代的核心。他主张通过亲身实践认知 AI 能力边界，AI 是消解焦虑的工具而非来源；技术平权降低创作门槛后，核心竞争力回归创作者的想象力与表达欲，不必盲目追逐每个新模型。

**结论/价值**：适合影视从业者、AIGC 创作者及关注 AI 冲击创意产业的听众，提供了稀缺的"演员+技术"双重视角。局限在于访谈形式偏经验分享，缺乏系统性方法论支撑，观点多为主观判断，读者需结合自身领域审慎参考。
