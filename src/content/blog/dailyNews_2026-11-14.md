---
title: "Daily News #2026-11-14"
date: "2026-11-14 08:00:00"
description: >
  Google 发布 TorchTPU：PyTorch 原生跑上 TPU，少量代码修改即可迁移 维护 3.3 万字符的长 Prompt？让优化 Agent 迭代执行 Agent Amplitude 借助 OpenAI 将产品改进交付周期压缩至 1-2 天 OpenAI 投入 200 万美元支持 AI 与儿童安全研究
tags:
- "负责任 AI"
- "PyTorch"
- "LLM"
- "软件工程"
- "AI基础设施"
- "Google"
- "AI Agent"
- "Prompt 工程"
- "测试与质量"
- "自动化优化"
- "OpenAI"
- "产品开发"
- "儿童保护"
- "AI 安全"
- "深度学习"
- "TPU"
- "自动化"

---

> - Google 发布 TorchTPU：PyTorch 原生跑上 TPU，少量代码修改即可迁移
> - 维护 3.3 万字符的长 Prompt？让优化 Agent 迭代执行 Agent
> - Amplitude 借助 OpenAI 将产品改进交付周期压缩至 1-2 天
> - OpenAI 投入 200 万美元支持 AI 与儿童安全研究

## 📥 Tech News

### [Google 发布 TorchTPU：PyTorch 原生跑上 TPU，少量代码修改即可迁移](https://www.infoq.cn/article/Fikt82HLToqb6ZANB2xj)

来源：InfoQ 推荐

发布时间：2026-11-12 15:00:00
![](https://static001.infoq.cn/resource/image/d2/66/d26cc0b823699480b6130d7340617b66.jpg)
**Google 与 Meta 合作开源 TorchTPU 项目，为 TPU 提供原生 PyTorch 后端，现有工作负载只需少量代码修改即可运行，解决了 PyTorch/XLA 方案侵入式修改、编译延迟高、不支持即时执行等长期痛点。**

* 迁移成本低：将 cuda 设备替换为 tpu、nccl 分布式后端替换为 tpu_dist 即可；支持 Strict、Debug、DeferAndFuse 三种即时执行模式，其中混合模式 DeferAndFuse 比 Strict Eager 快 50% 以上并降低 HBM 峰值内存
* 兼容性经过约 5000 个 Hugging Face 模型、500 多种架构的集成流水线验证；300 亿参数模型在单枚 TPUv7 上推理吞吐达每秒 25700 Token
* 已完成 Qwen3 MoE 235B 从 1024 枚到 8192 枚 TPUv7 芯片的扩展训练实验
* 项目仍处早期阶段，路线图涵盖动态形状、编译性能、算子覆盖、强化学习和量化；开发者普遍认为此举早该发生，PyTorch 生态优势将进一步释放

### [维护 3.3 万字符的长 Prompt？让优化 Agent 迭代执行 Agent](https://www.bestblogs.dev/article/eac30685b5?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-12 09:09:00
![](https://image.jido.dev/20251127045410_4d44587a)
**文章分享如何利用 Google Research 开源的 harness² 框架构建自动迭代的优化 Agent，解决 3.3 万字符长 Prompt 难以人工维护的问题，在输入法联想场景中将问题识别 F1 从 82.78% 提升至 89.89%。**

* 方案将优化拆分为 INV（怎么工作）与 DOM（需要知道什么）两个独立 Agent，通过 Propose、Probe、Compose 三步实现 Prompt 自动化迭代合成
* 将准确率、召回率、F1 等量化指标连同分歧样本及模型判断依据完整传递给优化 Agent，使其精准定位根因而非依赖模型直觉修改
* 每轮迭代后复盘改动，把有证据支撑的经验写入经验库供后续任务检索复用，形成持续改进机制，避免每次从零开始
* 通过放宽常驻内容至 5 万字符、限定仅修改 Prompt 本体、增加校验防止对评测集样本直接记忆等手段控制长度并防止过拟合
* 在 611 条评测数据上单轮迭代（约 95 分钟）即带来 F1 提升 7.11 个百分点，对需要维护长 Prompt 的 LLM 应用团队有直接借鉴价值

### [Amplitude 借助 OpenAI 将产品改进交付周期压缩至 1-2 天](https://openai.com/index/amplitude)

来源：OpenAI News

发布时间：2026-11-13 04:00:00

**Amplitude 基于 OpenAI 模型构建了主动式产品代理 Wave，将产品改进的交付周期压缩至 1-2 天。**

* Wave 负责识别"应该构建什么"，辅助团队进行产品决策
* 通过编码代理帮助团队完成变更的开发与交付
* 交付后进一步衡量改进的实际业务影响，形成发现问题到验证效果的完整闭环
* 案例展示了 AI 代理在产品研发全流程中的端到端应用，适合关注 AI 辅助研发效率的工程与产品团队参考；内容偏客户案例宣传，未披露具体技术细节

### [OpenAI 投入 200 万美元支持 AI 与儿童安全研究](https://openai.com/index/children-first-declaration)

来源：OpenAI News

发布时间：2026-11-12 08:00:00

**OpenAI 宣布投入 200 万美元，用于支持 AI 与儿童安全方向的研究。**

* 相关工作将支持开发共享工具，用于衡量 AI 给未成年人带来的风险与机遇
* 此举属于 AI 安全与治理领域的企业投入，与行业和监管层面日益重视未成年人保护的趋势相呼应
* 适合关注 AI 政策、安全研究与负责任 AI 议题的读者跟进了解后续研究进展
