---
title: "Daily News #2026-11-20"
date: "2026-11-20 08:00:00"
description: >
  美团 LongCat-2.5 正式开源：从看见，到抵达 美团正式发布 LongCat-2.5：面向智能体任务的原生多模态模型 从“能写代码”到“能交付”：腾讯轻量云 LoopForge 云端 Loop 实践 淘宝闪购本体平台：让人与 AI Agent 共用一份实时可信的业务知识 动线 Agent：AI 驱动的全链路用户转化引导 Inside the Codex sandbox：Codex 本地执行的安全隔离机制 OpenAI 前沿 AI 风险管理：从训练到部署 Apple 更新应用、内购与订阅的税费及价格政策
tags:
- "安全隔离"
- "多模态"
- "大模型"
- "对齐"
- "用户增长"
- "App Store"
- "AI Agent"
- "跨平台"
- "Codex"
- "AI Coding"
- "工程实践"
- "MoE"
- "系统设计"
- "系统架构"
- "SOP"
- "软件交付"
- "订阅"
- "大语言模型"
- "沙箱"
- "量化"
- "Agent"
- "税务合规"
- "智能体"
- "推理优化"
- "知识图谱"
- "OpenAI"
- "强化学习"
- "AI安全"
- "国产算力"
- "电商"
- "iOS 开发"
- "风险治理"
- "开源模型"
- "MCP"
- "部署"
- "内购"
- "数据治理"

---

> - 美团 LongCat-2.5 正式开源：从看见，到抵达
> - 美团正式发布 LongCat-2.5：面向智能体任务的原生多模态模型
> - 从“能写代码”到“能交付”：腾讯轻量云 LoopForge 云端 Loop 实践
> - 淘宝闪购本体平台：让人与 AI Agent 共用一份实时可信的业务知识
> - 动线 Agent：AI 驱动的全链路用户转化引导
> - Inside the Codex sandbox：Codex 本地执行的安全隔离机制
> - OpenAI 前沿 AI 风险管理：从训练到部署
> - Apple 更新应用、内购与订阅的税费及价格政策

## 📥 Tech News

### [美团 LongCat-2.5 正式开源：从看见，到抵达](https://tech.meituan.com/2026/11/10/Meituan-LongCat-2.5-Open-Source.html)

来源：美团 · 技术团队

发布时间：2026-11-18 13:49:03
![](https://p0.meituan.net/meituantechblog/8a3b4550cd7f5892dee9ff468bc6adfe159324.png)
**美团以 MIT 协议正式开源 LongCat-2.5，模型总参数 1.6 万亿、每 token 激活约 480 亿、支持 100 万上下文，允许自由商用部署与二次训练，无需额外授权。**

* 长程智能体能力来自训练链路整体扩展：加入长程轨迹与真实 Agent 失败轨迹转化的训练任务，采用 partial rollout 异步强化学习并按通过率动态调整过采样率，通过任务环境断网、清除 git 历史和 LLM judge 监督抑制 reward hacking。
* 原生多模态设计将视觉信号表示为多层级离散 token（残差向量量化逐级补足细节），视觉与文本共享同一主干参数，可离线预计算视觉 token，支撑 Visual Coding、3D 与专业办公场景的端到端交付。
* 推理侧采用 W4A4 方案，将专家权重与激活同时量化至 4bit 并用原生 INT4 矩阵乘单元执行，基于 FlatQuant 可学习等价变换，已评测下游任务表现与量化前相当。
* 国产算力适配上，在单卡显存不足 80GB 的加速器上通过双重分片 FSDP、混合词表并行、MoonEP 动态专家复制等策略完成万亿参数 MoE 的长序列训练，长序列 SFT 单卡吞吐较 DDP 基线提升 86%，为社区复现提供可参考的基础设施路径。

### [美团正式发布 LongCat-2.5：面向智能体任务的原生多模态模型](https://tech.meituan.com/2026/11/02/Meituan-LongCat-2.5.html)

来源：美团 · 技术团队

发布时间：2026-11-18 13:49:03
![](https://s3.meituan.net/static-prod01/com.sankuai.friday.longcat.next2p/assets/chat-image-D95MTdam.png)
**美团正式发布 LongCat-2.5，总参数 1.6 万亿、每 token 激活 480 亿、支持 100 万上下文的原生多模态模型，官方选取 GPT-5.5、GPT-5.6-Sol、Claude-Opus-4.8 和 Claude-Opus-5 作为对比基准。**

* 视觉表征采用残差向量量化（RVQ）将原生分辨率特征转为多层级离散 token，可离线预计算并缓存，视觉与文本 embedding 在共享语义空间中融合，简化长序列训练的负载均衡。
* Agentic RL 链路涵盖自动化数据合成与环境构建（F2P/P2P 校验）、partial rollout 异步训练（对跨 checkpoint 旧轨迹做梯度校正）、reward hacking 约束及跨任务跨 scaffold 混合训练。
* 多专家在线教学（MOPD）通过全词表 KL 散度将各领域能力蒸馏入主线模型，教师回复按固定长度切分控制分布偏移，配合 Tree Attention 单次前反向完成同组样本训练。
* 基础设施重点包括国产超节点并行策略（双重分片 FSDP、MoonEP 动态专家复制，长序列 SFT 吞吐提升 86%）、训推逐 token logprob bitwise 一致方案（扩展 TP 与 DCP 支持）以及 PD 分离的长上下文 rollout 优化。
* W4A4 量化推理相对 W8A8 基线，prefill 与 decode 吞吐分别提升 43.3% 和 42.77%，GMM 算子平均 1.73 倍加速。

### [从“能写代码”到“能交付”：腾讯轻量云 LoopForge 云端 Loop 实践](https://www.infoq.cn/article/Ae5uw6m9wC2gj5QUCC36)

来源：InfoQ 推荐

发布时间：2026-11-18 18:59:07
![](https://static001.infoq.cn/resource/image/48/17/48e5d4b98db8b264ec29e98b08050e17.jpg)
**腾讯轻量云专家江露分享 LoopForge 云端 Loop 实践，指出 AI Coding 的核心挑战已从“代码写得快不快”转向“结果能否被团队信任、接手并合入”，且多数失败最终应归因于工程机制而非模型能力。**

* 团队将研发共识写成可执行 SOP：用 DAG 定义节点依赖，程序负责状态流转、检查与交接，Agent 在节点内完成分析实现；步骤明确、可命令判断的交给脚本，需要理解判断的交给 Agent，关键取舍与最终责任保留给人。
* 验证环节强调“独立预期 + 可复现的运行事实”：评审与测试角色同实现分离并使用独立上下文，建立五道质量门禁，代码变更后旧检查报告必须失效。
* 能力进一步延伸至生产运维：从日志、K8s、慢 SQL 巡检发现异常，经聚类去重建单后衔接修复、验证与人工确认合入，Agent 准备证据、人做判断。
* 江露建议初引入 Coding Agent 的团队从高频、验收标准清晰的任务小范围试跑，“先把人放在正确的位置，而不是急着把人拿掉”。

### [淘宝闪购本体平台：让人与 AI Agent 共用一份实时可信的业务知识](https://www.bestblogs.dev/article/331e15e7ff?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-18 18:29:00
![](https://image.jido.dev/20260527050038_b20a9a1.jpeg)
**淘宝闪购本体平台通过三层元模型与治理链路，将业务对象、关系、术语、方法论等组织为可版本化的知识定义，解决人与 AI Agent 获取一致业务口径的核心问题。**

* 平台构建实体层、关系层、策略层三层元模型：实体层定义业务对象、语义数据集与指标，关系层统一边的定义方式，策略层涵盖术语、视角、事件、决策、方法论等七类，确保业务知识结构化可追溯。
* 治理链路通过版本化管理、审批流程和变更留痕，保证每份定义有明确责任人和生效时间，兑现“单一生效版本、每次变更留痕、读模型可重建、范围可限定”四大核心承诺。
* 架构经历三代演进：从读写分离到跨引擎拼装，再到实时多模，实现离线到实时的知识同步；平台定位为知识定义服务，只提供定义不承担计算，责任边界清晰。
* 场景子图快照机制圈定查询范围，防止 Agent 获取范围外的错误答案；文末给出判断知识“机器可读性”的三个追问及四条避坑指南，对构建企业级知识平台的团队有较高参考价值。

### [动线 Agent：AI 驱动的全链路用户转化引导](https://www.bestblogs.dev/article/bd4ba3ed69?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-18 16:37:00
![](https://image.jido.dev/20251127045404_f9729af6)
**淘特 App 构建动线 Agent 系统，由 LLM 驱动并受确定性规则约束，通过三个差异化智能体覆盖用户“进端→在端→离端”全链路转化时机，峰值增量 GMV 占比超大盘 5%，token 成本降低 60% 以上。**

* TensorLiftAgent 负责进端时机：基于多维用户特征张量分解生成网格人群差异化权益策略，后台天级寻优、入端毫秒命中，兼顾策略效果与响应速度。
* PeiAgent 负责在端时机：端云协同实时计算个性化购物热情指数（PEI），端上算分免除网络往返，200ms 内感知热情衰减并触发基于行为序列的 AI 干预。
* DeepFlowAgent 负责离端未购时机：异步执行长链 CoT 深度归因推理，拆分为召回判断、选品定价、文案生成三轮链式推理，分别控制不同错误代价并多渠道召回。
* 系统在数百亿 token/日的规模下通过架构设计将成本降低 60% 以上，为电商团队用 LLM 做精细化用户经营提供了含完整落地数据的实践参考。

### [Inside the Codex sandbox：Codex 本地执行的安全隔离机制](https://openai.com/index/inside-the-codex-sandbox)

来源：OpenAI News

发布时间：2026-11-18 16:00:00

**OpenAI 公开 Codex 沙箱机制的实现细节，说明其如何在用户本地机器上执行命令，同时严格遵循用户设定的文件系统与网络访问限制。**

* 沙箱方案覆盖 macOS、Linux 和 Windows 三大平台
* 核心设计目标是在赋予 AI 编码代理执行能力的同时，防止其越权访问文件系统与网络
* 对正在构建本地 AI 代理隔离方案、关注代理安全边界的开发者具有直接参考价值

### [OpenAI 前沿 AI 风险管理：从训练到部署](https://openai.com/index/managing-frontier-ai-risk)

来源：OpenAI News

发布时间：2026-11-18 14:00:00

**OpenAI 阐述其前沿 AI 风险管理体系，覆盖从模型训练到实际部署的完整链路。**

* 具体手段包括模型对齐、沙箱隔离、阻断式防护措施以及部署后的持续监控
* 属于官方安全治理框架的系统性说明，展示了风控如何嵌入训练与部署各环节
* 适合关注 AI 安全、合规与安全工程实践的读者，可作为了解 OpenAI 风控思路的一手资料

### [Apple 更新应用、内购与订阅的税费及价格政策](https://developer.apple.com/news/?id=4o5ie73a)

来源：Latest News - Apple Developer

发布时间：2026-11-18 08:00:25
![](https://developer.apple.com/news/images/og/app-store-og.png)
**Apple 宣布调整 App Store 应用、内购与订阅的税务与价格政策，涉及多个国家/地区新增税费，并将于 2026 年 12 月 3 日更新部分 storefront 价格。**

* 税务更新：博茨瓦纳新增 14% 增值税、卢旺达新增 18% 增值税，喀麦隆与科特迪瓦各新增 3% 的重大经济存在（SEP）税；Apple 将在博茨瓦纳和卢旺达代收代缴相关税费，付费应用协议附件 B 相应更新。
* 新增 "SaaS（软件即服务）" 税务属性，适用于 App Store 软件、软件培训材料、交友、推广等税务类别，开发者可在 App Store Connect 的价格与销售范围中更新选择。
* 自 2027 年 1 月 1 日起，SaaS、App Store 软件、培训材料、交友及推广类应用在美国加州需缴纳销售与使用税；美国 storefront 价格不含税展示，开发者收益不变，但用户含税总价可能上升。
* 价格更新：若未将博茨瓦纳、哥伦比亚、埃及、卢旺达、土耳其设为基础 storefront，这些地区价格将统一调整；自动续期订阅价格及手动管理价格的 storefront 不受影响。

该通知面向在多国销售数字商品与服务的开发者，建议尽快在 App Store Connect 中核查即将生效的价格变动与税务类别设置。
