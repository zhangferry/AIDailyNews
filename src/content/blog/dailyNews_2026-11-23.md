---
title: "Daily News #2026-11-23"
date: "2026-11-23 08:00:00"
description: >
  曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作，首次以 Lean 形式化语言公开证明 亚马逊云科技推出 TorchNeuron，可直接在 AWS Trainium 上运行 PyTorch 模型，无需任何修改 华为 OSTA 星芒 O1 Pro 评测：以「小艺 AI 屏」为核心的指令式 AI 代理手机
tags:
- "黎曼猜想"
- "鸿蒙"
- "AI 手机"
- "数学"
- "人机交互"
- "Trainium"
- "Lean"
- "Claude"
- "AI基础设施"
- "AWS"
- "PyTorch"
- "深度学习"
- "AI"
- "小艺"
- "华为"

---

> - 曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作，首次以 Lean 形式化语言公开证明
> - 亚马逊云科技推出 TorchNeuron，可直接在 AWS Trainium 上运行 PyTorch 模型，无需任何修改
> - 华为 OSTA 星芒 O1 Pro 评测：以「小艺 AI 屏」为核心的指令式 AI 代理手机

## 📥 Tech News

### [曝黎曼猜想被证明：Anthropic 数学家与 Claude 合作，首次以 Lean 形式化语言公开证明](https://www.bestblogs.dev/article/e04c586efc?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-22 03:29:22
![](https://media.bestblogs.dev/20261121114301_lark2pad-1795215065663-7.jpg)
**Anthropic 数学家 Levent Alpöge 宣布与 Claude 合作找到黎曼猜想及广义黎曼猜想的证明，并首次以 Lean 形式化语言公开，引发数学界对 AI 前沿数学研究能力的广泛关注。**

* 黎曼猜想是悬置 167 年的千禧年难题，Alpöge 借助 Claude 探索迭代 theta 提升构造证明路径；证明以机器可检查的代码形式呈现，可通过计算机验证推导正确性
* Claude 在高阶自换形式理论等复杂推导上速度超越人类研究者，甚至在研究后期超过 Alpöge 本人，标志着 AI 从辅助工具向研究合作者转变
* Claude 此前已在数论领域取得雅可比猜想反例、Hadamard 矩阵发现等成果，其能力正从解题走向原创性发现，智能评估标准或从解题速度转向创造性发现能力
* 若最终验证成功，数学家角色可能从“发现者”转向“解释者”与“应用者”；证明方法能否推动其他领域发展仍有待人类深入研究

### [亚马逊云科技推出 TorchNeuron，可直接在 AWS Trainium 上运行 PyTorch 模型，无需任何修改](https://www.infoq.cn/article/XhtWUmaolJECUhPX2jzY)

来源：InfoQ 推荐

发布时间：2026-11-22 10:00:00
![](https://static001.infoq.cn/resource/image/a0/0d/a0b70de959696be3ebc674582469d70d.png)
**亚马逊云科技在 2026 年 PyTorch 北美大会上推出 TorchNeuron 原生 PyTorch 后端，开发者几乎无需修改代码即可在 AWS Trainium AI 芯片上运行现有 PyTorch 模型，大幅降低自研芯片的迁移门槛。**

* 迁移成本极低：借助 torch.accelerator 自动设备检测，只需将 .to('cuda') 替换为 .to('neuron')，无需重写和重新验证模型；原生支持 DDP、FSDP2、DTensor 等分布式训练并行 API
* 兼容性保障充分：开发团队对 10 万个最受欢迎模型和 800 多种机器学习架构进行了验证；开发者还可通过 Neuron 内核接口（NKI）编写自定义算子，获得比即时执行和 torch.compile 更精细的性能控制
* 支持训练与推理共享硬件容量，非高峰时段可在两类任务间灵活调配资源；Cartesia 已将其用于语音 AI 推理，利伯脑发育研究所在探索药物靶点识别应用
* 业界评论指出，真正的考验在于生产环境的性能、每 token 成本与总拥有成本，降低迁移门槛只是竞争的第一步；此举紧随谷歌推出 TorchTPU 之后，反映 AI 芯片厂商的竞争焦点正从芯片本身转向规模化易用性

### [华为 OSTA 星芒 O1 Pro 评测：以「小艺 AI 屏」为核心的指令式 AI 代理手机](https://www.bestblogs.dev/article/27f1e1f7f5?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-11-21 12:00:00
![](https://media.bestblogs.dev/20261113050053_35a08f3.jpeg)
**华为子品牌 OSTA 星芒发布首款旗舰 O1 Pro，以「小艺 AI 屏」作为默认桌面，将人机交互从手动操作转变为指令式 AI 代理，是目前市面上少有的真正以 AI 为核心设计的鸿蒙手机。**

* 硬件配置包括 16:9.5 阔直屏、麒麟 9030S 处理器和 7000mAh 大电池，硬件成熟度略逊于华为主力产品线
* 「小艺 AI 屏」压缩传统图标入口，以键盘、麦克风、附件按钮“新三大金刚键”为核心交互，用户可通过自然语言完成 B 站内容聚合、购物比价、外卖点单、微信消息收发等任务，实现“不进 app 完成日常工作”
* 相较鸿蒙 6.1 版本，小艺在识别、理解和代理操作速度上实现质的飞跃，成为 AI 功能“吃灰”与“日用”的分水岭，背后基于盘古大模型并融合 DeepSeek 等前沿模型能力
* 星芒以「Come as you are」为定位，承载华为对“下一个十年人机交互方式”的探索，意在打造面向纯 AI 时代的新品牌形象
