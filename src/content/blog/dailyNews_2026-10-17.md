---
title: "Daily News #2026-10-17"
date: "2026-10-17 08:00:00"
description: >
  SLM 生成式高并发推理引擎：延迟约束下的有效吞吐优化 MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践 阶跃星辰开放 Step 5 Preview 权重：长程 Agent 的竞争，延伸到上下文管理与训练系统 侏罗纪不飞鸟类化石“杨源”被发现，挑战鸟类演化传统认知 他建立了中国的“脑银行”，利息是征服人脑疾病 Teaching students to think and learn through questions Anthropic 向 METR 开放“类员工权限”，建立三级独立评估体系 对Dyna创始人Lindon的3小时访谈：机器人世界的迷雾、分歧与抉择
tags:
- "科研基础设施"
- "机器人"
- "科学传播"
- "模型评估"
- "Agent"
- "具身智能"
- "鸟类演化"
- "创业"
- "大模型"
- "METR"
- "OpenAI"
- "Dyna Robotics"
- "搜索推荐"
- "推荐系统"
- "EdTech"
- "长上下文"
- "高性能计算"
- "AOTInductor"
- "人脑库"
- "科学发现"
- "脑科学"
- "Anthropic"
- "MoE"
- "Nature"
- "开源权重"
- "AI 教育"
- "神经退行性疾病"
- "侏罗纪"
- "Scaling Law"
- "AI治理"
- "古生物学"
- "精排"
- "SLM"
- "推理优化"
- "AI安全"
- "KDD"
- "基座大模型"
- "Study Mode"
- "访谈"
- "产品动态"

---

> - SLM 生成式高并发推理引擎：延迟约束下的有效吞吐优化
> - MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践
> - 阶跃星辰开放 Step 5 Preview 权重：长程 Agent 的竞争，延伸到上下文管理与训练系统
> - 侏罗纪不飞鸟类化石“杨源”被发现，挑战鸟类演化传统认知
> - 他建立了中国的“脑银行”，利息是征服人脑疾病
> - Teaching students to think and learn through questions
> - Anthropic 向 METR 开放“类员工权限”，建立三级独立评估体系
> - 对Dyna创始人Lindon的3小时访谈：机器人世界的迷雾、分歧与抉择

## 📥 Tech News

### [SLM 生成式高并发推理引擎：延迟约束下的有效吞吐优化](https://tech.meituan.com/2026/10/15/Small-Language-Model-in-meituan.html)

来源：美团 · 技术团队

发布时间：2026-10-15 15:11:43
![](https://p0.meituan.net/meituantechblog/449102302ea0d472417c6fff369dd63882001.png)
**美团针对搜索推荐场景的极低延迟约束，重新设计了 SLM 推理引擎，在平均端到端时延低于 20ms 的约束下实现 Prefill-Only 有效 MFU 67%，吞吐较 SGLang 提升 10 倍。**

* 核心洞察：搜推场景属于"有界生成负载"（decode 次数有确定上界），SGLang/vLLM 为无界生成设计的调度与优化策略在此场景下均为负向优化。
* 架构设计：以静态 DAG 组织完整业务请求作为执行边界，用 PyTorch AOTInductor 离线编译 GPU 计算节点，C++ Runtime 负责调度，消除 Python 对请求和 Token 的调度开销。
* 关键优化：Packed Prefill 处理变长样本避免 padding 浪费、请求内 shared-prefix K/V 共享（跨请求 prefix cache 因命中率低而不维护）、固定 Beam Search 编译为单节点、选择性 FP8 矩阵计算。
* 性能数据：约 0.6B Prefill-Only 模型达到约 100 request QPS（1500 sample/s），Beam Search 模型达 300/120 request QPS，P99 约 70ms。
* 该框架已在美团搜索意图分流、相关性判断、生成式召回等场景取得实验显著性，支撑业务在成本可控下全量推送。

### [MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践](https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html)

来源：美团 · 技术团队

发布时间：2026-10-15 15:11:43
![](https://p0.meituan.net/meituantechblog/5dcc2af83b5b9da04717c9fcff76b69a1943722.png)
**美团在 MTGR 基础上推出统一推荐基座大模型 MTFM，首次实现外卖多个主要业务的统一精排模型，各业务订单量提升 2.06%~6.68%，推理成本降低 24%，论文被 KDD 2026 收录。**

* 针对规模可扩展性、场景可延展性、架构高效性三大挑战，采用异构 Tokenizer（H-Token/R-Token/T-Token）与动态掩码机制，实现多场景特征免显式对齐。
* 引入混合注意力架构（Target:Full=3:1，共 16 层）与 Target Token Scale-Up，样本吞吐达全 Full Attention 架构的 2.9 倍，在参数量与序列长度上验证了稳健 Scaling 能力。
* 训练侧借鉴 LLM 实践：深度感知初始化（按层深缩放标准差）+ Muon 优化器，随机重复实验的 AUC 波动从 0.4pp 降至 0.1pp。
* 工程优化扎实：FA Mask Kernel 重构（前向加速 128%）、GLN 融合算子（带宽利用率 30%→60%）、Muon 批量正交化（端到端吞吐 +19%）、特征精简删减近 500 个且 GAUC 无损。
* 采用 User-Level 统一样本范式，多业务共享长序列 Attention 计算，跨场景信息迁移使小流量业务显著提升 0.60~0.93pp。

### [阶跃星辰开放 Step 5 Preview 权重：长程 Agent 的竞争，延伸到上下文管理与训练系统](https://www.infoq.cn/article/EwqsJX6f03ODRac6Kk4c)

来源：InfoQ 推荐

发布时间：2026-10-15 20:09:59
![](https://static001.infoq.cn/resource/image/5f/55/5f6c7069786e603e264c0d3f093d2d55.jpg)
**阶跃星辰正式开放Step 5 Preview权重（BF16与FP8版本），这是600B总参数/27B激活的稀疏MoE模型，支持100万token上下文，面向软件工程、专业知识工作和金融等长程Agent任务，已在OpenRouter Token用量日榜和周榜位列全球第二。**

* 架构采用92层Transformer，以3:1比例交替配置门控滑动窗口注意力与稀疏全局注意力；Sparse GQA将相邻8个token合并为索引块，使索引与top-k选择开销降至原来的八分之一
* 训练侧构建了百万级可验证环境，显式控制Agent合成数据的难度与多样性，并检查模型是否利用评测漏洞获取奖励
* 上下文压缩被纳入端到端策略训练：Agent在上下文预算接近耗尽时将工作整理为可恢复状态再继续执行
* 部署支持vLLM、SGLang及Transformers，提供兼容OpenAI接口的API服务

文章提醒需区分局部优化与整体收益：索引开销下降不等于推理流程提速八倍；600B总参数的专家权重仍需部署系统管理，不能等同于27B稠密模型的部署门槛。长上下文容量与长任务可靠性之间，仍需通过跨多轮压缩的任务完成情况做工程验证。

### [侏罗纪不飞鸟类化石“杨源”被发现，挑战鸟类演化传统认知](https://www.bestblogs.dev/article/82bf3890aa?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-15 13:24:00
![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6l6x0G2huoMz5XoT5ecEr7xoQN0W0OeffFLlrvjRCpFQ/0)
**中国科学院古脊椎所与福建地科院在福建政和发现一具侏罗纪新鸟类化石，命名为“杨源”，研究表明它是不具备飞行能力的地栖食肉鸟类，相关成果发表于《自然》杂志。**

* 化石形态特征独特：短小的前肢、强壮的后肢，以及与恐爪龙类相似的特化第二趾，表明其适应陆地奔跑与捕食，而非飞行。
* 演化地位关键：杨源是已知最原始的鸟类之一，介于始祖鸟与后来的中生代鸟类之间，填补了鸟类演化历程中的时空空白。
* 核心突破：作为已知最早的不具备飞行能力的鸟类，它打破了“飞行选择压力主导早期鸟类演化”的单向假说，证明鸟类身体结构的演化并非沿“优化飞行”单一路径线性前进。
* 该发现表明鸟类在起源之初就已探索多种非飞行生态位，重塑了对侏罗纪鸟类生态多样性的理解。

### [他建立了中国的“脑银行”，利息是征服人脑疾病](https://www.bestblogs.dev/article/9e04aa579d?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-15 12:48:00
![](https://image.jido.dev/20260527052055_60638a4.jpeg)
**浙江大学脑科学与脑医学学院院长段树民院士于 2012 年牵头建立中国最早的脑库之一——浙江大学医学院中国人脑库，通过收集和研究人脑组织，推动攻克阿尔茨海默病、帕金森病等神经精神类疾病。**

* 建库动因：国外脑样本无法完全反映中国人脑的结构与疾病特征，且进口审批复杂；同时动物模型难以准确模拟抑郁症、自闭症等人类疾病，人脑组织是验证疾病机制和药物有效性的关键。
* 已有成果：脑库纳入国家科技资源共享服务平台，累计收到 750 例捐献，并完成了人脑海马图谱绘制等工作。
* 现实困境：健康大脑对照样本严重不足，脑组织跨省收集困难、全国标准化尚未实现，制约研究深度与资源利用效率。
* 未来方向：呼吁建设更多脑库并提升公众捐献认知；脑组织不能用于移植、只能用于科研，捐献也被视为一种保存个人遗产的方式。

### [Teaching students to think and learn through questions](https://openai.com/index/teaching-students-to-think-and-learn-through-questions)

来源：OpenAI News

发布时间：2026-10-15 21:00:00

**OpenAI 借教师节发布面向教育者的更新：AI for Educators 课程新增巴西葡萄牙语版本，同时介绍 Study Mode 如何帮助教师支持学生的主动式、分步学习。**

* AI for Educators 的巴西葡萄牙语版本，使巴西教师能以本地语言了解如何将 AI 融入教学场景；
* Study Mode 主打通过提问引导学生思考和学习，教师可借助该模式让学生循序渐进地完成学习过程，而非直接获取答案；
* 该内容属于产品宣传与功能介绍性质，未涉及技术实现细节，信息量有限；
* 适合关注 AI 教育应用与教育科技产品动态的读者快速了解。

## 🤖 AI Coding

### [Anthropic 向 METR 开放“类员工权限”，建立三级独立评估体系](https://www.anthropic.com/news/an-update-on-independent-evaluators)

来源：Anthropic News

发布时间：2026-10-15 08:00:00
![](https://www-cdn.anthropic.com/images/4zrzovbb/website/c2af6aeedb4995d202c7543f3d59c6bbbd5352f1-2000x1125.jpg)
**Anthropic 宣布已向非营利评估机构 METR 的团队提供“类员工权限”，用于独立评估其前沿模型与安全实践，并同步建立三级评估者访问体系。**

* METR 六名员工已入驻，获得公司硬件、办公场地及与内部风险评估团队大致相当的内部工具权限；Anthropic 无权否决其发布结论，仅可在客户数据、律师特权信息、模型架构等预定义类别内要求删减，METR 可公开评价删减是否合理。
* 评估者须满足四项标准：前沿模型评估专业能力（如识别 alignment faking）、独立性（不持有被评公司股权、无财务或运营依赖）、足够的访问权限、发布自由；Anthropic 以银行驻场监管检查员作类比。
* 三级访问体系：一级为范围受限且发布需批准的调查（SecureBio 现处于该层级，正在审查八月风险报告的化生武器章节）；二级可自主发布但仍可被要求删减特定信息；三级即 METR 式的类员工权限，未来希望有多家评估者进入该层级。
* 此举延续上月承诺并呼应白宫超级智能协议；公司同时与 Accenture、Faculty 推进红队测试、对齐评估与防护测试合作，并呼吁所有前沿 AI 公司自愿采取类似做法。

## 📻 Podcast

### [对Dyna创始人Lindon的3小时访谈：机器人世界的迷雾、分歧与抉择](https://www.xiaoyuzhoufm.com/episode/6acf81f0195d838e2af1e281)

来源：张小珺Jùn｜商业访谈录

发布时间：2026-10-15 08:00:00
![](https://image.xyzcdn.net/Fte6xuZ2YUty60D_vPm3lb72mQpp.png)
**本期播客是对Dyna Robotics创始人兼CEO Lindon Gao的3小时深度访谈，探讨机器人行业的路线分歧与创业者的自我修行，Dyna选择了与Physical Intelligence"纯大脑研究"截然不同的"Product-research"路线。**

* Dyna以具体工作流为最小单元，从真实任务出发反向驱动模型预训练，而非从通用智能出发探索机器人大脑；这是Lindon的第四次创业
* 全球机器人行业远未到达收敛时刻，这场长跑看不见终点，创业者需要在尚未绘制完成的地图上找方向、做关键决策
* Lindon分享心境转变：过去要求自己做"不能犯错的CEO"，后来意识到对犯错的恐惧反而导致许多错误决策，直到去年底才渡过这段难关
* 访谈还涉及《沉思录》与王阳明心学对创业修心的启发，以及对机器人开放地图、中国市场等话题的讨论
