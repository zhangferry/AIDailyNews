---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作完成，证明以 Lean 形式化公开 华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机 亚马逊云科技推出 TorchNeuron：无需修改代码即可在 AWS Trainium 上运行 PyTorch 模型
tags:
- "形式化验证"
- "AI手机"
- "小艺"
- "机器学习"
- "PyTorch"
- "华为"
- "Claude"
- "Trainium"
- "AWS"
- "AI 芯片"
- "AI"
- "黎曼猜想"
- "人机交互"
- "鸿蒙"
- "数学"

---

> - 曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作完成，证明以 Lean 形式化公开
> - 华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机
> - 亚马逊云科技推出 TorchNeuron：无需修改代码即可在 AWS Trainium 上运行 PyTorch 模型

## 📥 Tech News

### [曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作完成，证明以 Lean 形式化公开](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作找到黎曼猜想的证明，并进一步证明了广义黎曼猜想，证明以 Lean 形式化语言公开，被视为 AI 参与前沿数学研究的标志性事件。**

* 黎曼猜想是悬置 167 年的千禧年难题，Alpöge 称通过与 Claude 探索迭代 theta 提升构造出证明路径，AI 在复杂推导和技术细节上的速度甚至超过了研究者本人。
* 证明首次以 Lean 形式化语言写成机器可检查的代码形式公开，既能由计算机验证推导正确性，也代表了 AI 辅助数学研究的前沿方法。
* 此前 Claude 已在数论领域取得雅可比猜想反例、Hadamard 矩阵发现等成果，标志着 AI 从辅助计算工具向主动探索研究路线的合作者转变，其能力评估标准正从解题速度转向创造性发现。
* 若最终验证成功，数学家角色可能从“发现者”转向“解释者”与“应用者”，数学研究范式将被重塑；当然该结论目前仍属宣布阶段，尚待数学界完成验证确认。

### [华为 OSTA 星芒 O1 Pro 评测：一台真正为 AI 而生的鸿蒙手机](https://www.bestblogs.dev/article/27f1e1f7f5?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-21 12:00:00
![](https://media.bestblogs.dev/20261113050053_35a08f3.jpeg)
**华为子品牌 OSTA 星芒推出首款以 AI 为核心设计的鸿蒙手机 O1 Pro，通过「小艺 AI 屏」将手机交互从手动操作转向指令式 AI 代理，尝试实现“不进 app 完成所有日常工作”的体验。**

* 硬件上采用 16:9.5 阔直屏、麒麟 9030S 处理器和 7000mAh 超大电池；主界面压缩传统图标入口，聚焦键盘、麦克风、附件按钮组成的“新三大金刚键”。
* 实测中小艺可完成 B 站内容聚合、购物比价、外卖点单、微信消息收发等复杂任务，其能力基于盘古大模型并融合 DeepSeek 等前沿模型协同。
* 相比鸿蒙 6.1 版本，小艺在识别、理解和代理操作速度上实现质的飞跃，被视为 AI 功能从“吃灰”到“日用”的关键分水岭。
* 星芒定位为面向“纯 AI 时代”的新生品牌，本质上是华为对下一个十年人机交互方式的探索工程；其硬件成熟度略逊于主力产品线，但在 AI 体验上展现了突破性尝试。

### [亚马逊云科技推出 TorchNeuron：无需修改代码即可在 AWS Trainium 上运行 PyTorch 模型](https://www.infoq.cn/article/XhtWUmaolJECUhPX2jzY)

来源：InfoQ 推荐

发布时间：2026-11-22 10:00:00
![](https://static001.infoq.cn/resource/image/a0/0d/a0b70de959696be3ebc674582469d70d.png)
**亚马逊云科技在 2026 年 PyTorch 北美大会推出 TorchNeuron 原生 PyTorch 后端，开发者几乎无需修改代码即可在 AWS Trainium 芯片上运行现有模型，迁移时仅需将 .to('cuda') 替换为 .to('neuron')，无需重写和重新验证模型。**

* 原生支持分布式训练与 PyTorch 并行 API（DDP、FSDP2、DTensor 等），通过 torch_neuronx.Stream/Event 支持 Torch 流与事件；还可借助 Neuron 内核接口（NKI）编写自定义运算符，获得比 Adaptive Eager 与 torch.compile 更精细的性能控制
* 开发团队对 10 万个最受欢迎模型和 800 多种机器学习架构进行了验证；Cartesia 已将其用于语音 AI 推理，利伯脑发育研究所用于药物靶点识别与药物发现
* 支持训练与推理工作负载共享硬件容量，非高峰时段可将资源从推理重新分配至训练
* 业界评论指出，真正考验在于生产环境的性能、每 token 成本与总拥有成本；该发布紧随谷歌 TorchTPU 之后，显示 AI 芯片竞争正从硬件本身转向规模化应用的易用性
