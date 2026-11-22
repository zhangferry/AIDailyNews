---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  曝黎曼猜想被证明，Claude 与 Anthropic 数学家合作立大功 华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机 亚马逊云科技推出 TorchNeuron，可直接在 AWS Trainium 上运行 PyTorch 模型，无需任何修改
tags:
- "机器学习"
- "Lean"
- "AWS"
- "AI芯片"
- "鸿蒙"
- "华为"
- "AI 手机"
- "Claude"
- "黎曼猜想"
- "AI Agent"
- "Trainium"
- "评测"
- "AI"
- "数学"
- "PyTorch"

---

> - 曝黎曼猜想被证明，Claude 与 Anthropic 数学家合作立大功
> - 华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机
> - 亚马逊云科技推出 TorchNeuron，可直接在 AWS Trainium 上运行 PyTorch 模型，无需任何修改

## 📥 Tech News

### [曝黎曼猜想被证明，Claude 与 Anthropic 数学家合作立大功](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作找到黎曼猜想的证明，并进一步证明了广义黎曼猜想，证明首次以 Lean 形式化语言公开，引发数学界对 AI 前沿研究能力的广泛关注。**

* 黎曼猜想是悬置 167 年的千禧年难题，Alpöge 借助 Claude 探索迭代 theta 提升构造证明路径，AI 在处理高阶自守形式理论等复杂推导时展现出超越人类研究者的速度，甚至在研究后期超过 Alpöge 本人
* 证明以 Lean 形式化语言写成机器可检查的代码公开，既能由计算机验证推导的正确性，也代表了 AI 辅助数学研究的前沿方法
* Claude 此前在数论领域已有发现雅可比猜想反例、Hadamard 矩阵等成果，AI 正从辅助计算工具转变为能主动探索研究路线、提出原创成果的研究合作者
* 若证明最终被验证，数学家角色可能从「发现者」转向「解释者」与「应用者」，数学研究范式与智能水平评估标准都将被重塑

### [华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机](https://www.bestblogs.dev/article/27f1e1f7f5?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-21 12:00:00
![](https://media.bestblogs.dev/20261113050053_35a08f3.jpeg)
**华为子品牌 OSTA 星芒推出首款以 AI 为核心设计的鸿蒙手机 O1 Pro，以「小艺 AI 屏」为默认桌面，将手机主要交互方式从手动操作转向指令式 AI 代理。**

* 硬件采用 16:9.5 阔直屏、麒麟 9030S 处理器和 7000mAh 大电池，主界面压缩传统图标入口，聚焦键盘、麦克风、附件按钮「新三大金刚键」
* 实测可通过自然语言指令完成 B 站内容聚合、购物比价、外卖点单、微信消息收发等复杂任务，实现「不进 app 完成日常工作」；相较鸿蒙 6.1 版本，小艺的识别、理解和代理操作速度实现质的飞跃，成为 AI 功能「吃灰」与「日用」的分水岭
* 小艺基于盘古大模型并融合 DeepSeek 等前沿模型实现能力协同
* 星芒以「Come as you are」定位面向纯 AI 时代，是华为对下一个十年人机交互方式的探索工程；硬件成熟度略逊于主力产品线，但被视为目前唯一直面大众市场的 AI 手机

### [亚马逊云科技推出 TorchNeuron，可直接在 AWS Trainium 上运行 PyTorch 模型，无需任何修改](https://www.infoq.cn/article/XhtWUmaolJECUhPX2jzY)

来源：InfoQ 推荐

发布时间：2026-11-22 10:00:00
![](https://static001.infoq.cn/resource/image/a0/0d/a0b70de959696be3ebc674582469d70d.png)
**亚马逊云科技在 2026 年 PyTorch 北美大会上推出 TorchNeuron 原生 PyTorch 后端，开发者几乎无需修改代码即可在 AWS Trainium AI 芯片上运行现有 PyTorch 模型，显著降低迁移门槛。**

* 迁移成本极低：通过 torch.accelerator 自动设备检测，仅需将 `.to('cuda')` 改为 `.to('neuron')`，无需重写和重新验证模型；还可支持训练与推理工作负载共享硬件容量，非高峰时段灵活调度资源
* 原生支持分布式训练与 PyTorch 并行 API（DDP、FSDP2、DTensor），并通过 Neuron 内核接口（NKI）支持自定义算子，可获得比 Adaptive Eager 和 torch.compile 更精细的性能控制
* 团队已对 10 万个最受欢迎模型和 800 多种机器学习架构完成验证；Cartesia 已将其用于语音 AI 推理，利伯脑发育研究所正探索药物靶点识别与药物发现应用
* 该发布紧随谷歌 TorchTPU 之后，AI 芯片竞争焦点正从硬件本身转向规模化易用性；业界评论指出，真正的考验在于生产环境的性能、每 token 成本与总拥有成本
