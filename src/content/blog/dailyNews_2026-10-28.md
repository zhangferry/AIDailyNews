---
title: "Daily News #2026-10-28"
date: "2026-10-28 08:00:00"
description: >
  别再让计算等着搬权重了！KTransformers 让 CPU 直接参与 MoE 微调计算 TypeSafe AI发布Jev：一种只返回类型化概率而非文本的决策模型 Apple 发布全新 14 寸 M6 芯片 MacBook Pro Apple 发布全新 iMac（M6 芯片）
tags:
- "MoE"
- "新品发布"
- "M6"
- "系统优化"
- "概率决策"
- "MacBook Pro"
- "模型推理"
- "硬件"
- "Apple"
- "API"
- "大模型"
- "AI"
- "模型微调"
- "iMac"
- "LLM"

---

> - 别再让计算等着搬权重了！KTransformers 让 CPU 直接参与 MoE 微调计算
> - TypeSafe AI发布Jev：一种只返回类型化概率而非文本的决策模型
> - Apple 发布全新 14 寸 M6 芯片 MacBook Pro
> - Apple 发布全新 iMac（M6 芯片）

## 📥 Tech News

### [别再让计算等着搬权重了！KTransformers 让 CPU 直接参与 MoE 微调计算](https://www.bestblogs.dev/article/456f1fed7b?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-27 00:00:00
![](https://media.bestblogs.dev/20260801222332_04b96cd.jpeg)
**清华 MADSys 实验室、趋境科技与 LlamaFactory 团队联合推出 KTransformers-FineTune (KT-FT)，打破传统“卸载范式”，提出 CPU/GPU 协同计算：CPU 利用 AVX-512/AMX 指令集就地完成 MoE 专家计算，GPU 专注 Attention，在千亿参数模型上实现比卸载基线快 2.5–21.2 倍的 LoRA 微调吞吐。**

* MoE 稀疏负载下“用计算掩盖搬运”失效：理论带宽下传输 1B BF16 参数需 62.5ms，而 RTX 5090 计算仅 2.8ms，传输是计算的 22 倍；ZeRO-Offload 有 94% 单步时间耗在通信同步。
* 系统优化是落地关键：语义感知布局引擎按张量用途预分配内存、后台原地转换布局并与 GPU 计算重叠；动态线程调度器以细粒度任务队列加工作窃取平衡冷热专家负载。同分工下 PyTorch 直译仅 12.1 tokens/s，KT-FT 达 166.8 tokens/s。
* LoRA Expert (LE) 系统-算法协同设计利用剩余显存增设常驻 GPU 的共享适配路径，缓解路由倾斜导致的冷门专家更新不足，缩短 Time-to-Quality。
* 已集成至 LlamaFactory 支持一键微调，在 DeepSeek-V3.1-671B、Qwen3.5-397B、Qwen3-235B 等模型及单/多卡、Intel AMX/AMD AVX-512 平台完成验证。

### [TypeSafe AI发布Jev：一种只返回类型化概率而非文本的决策模型](https://www.infoq.cn/article/3o7gwgKJt2SbH8AhdpkU)

来源：InfoQ 推荐

发布时间：2026-10-27 15:22:00
![](https://static001.infoq.cn/resource/image/db/ef/dbe30d9a2a9c850b5380fyy0133719ef.jpg)
**前 OpenAI 研究员、RLHF 联合发明人 Diogo Almeida 创立的 TypeSafe AI 发布首款模型 Jev：不生成文本，而是返回带类型的概率化决策（Choice、Score、Noul 布尔概率），调用方可按置信度阈值直接执行动作。**

* 定价：输入 0.042 美元/百万 Token、输出免费，32k 上下文，端到端延迟 70-500ms，采用“校准决策强化学习”方法训练
* 生态接纳迅速：Vercel 上线次日接入，24 小时覆盖近 13% 付费团队（为 GPT-5.6 系列的两倍），Netlify、LangChain 及多个第三方客户端跟进
* 实测反馈：安全分类器比所替代的 LLM 快 5-18 倍；社区统计速度提升中位数 7 倍、成本节省中位数 30 倍，明显低于官方宣称
* 争议点：HN 用户指出它虽不输出无效类型，但仍可能输出“完全错误的合法值”；Flask 作者 Armin Ronacher 认为该设计把幻觉判断责任转嫁给用户
* 已知缺陷：计数、算术和日期比较不可靠，官方建议数学运算保留在代码中完成，并固定具体版本号以避免别名漂移

### [Apple 发布全新 14 寸 M6 芯片 MacBook Pro](https://t.me/AppleNuts/2561)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-27 22:02:57
![](https://cdn5.telesco.pe/file/XpaK5ritD5lgF8YhO_Ck9z349w4PWM8Om_sQC5vHJRkIc9fF0TIQtWSLcNShDI_L6AHEwidU4QbH0e3Oa7UzvlKD8x9jKbMFBOeToGPRRSpx0MBT8Vd6s2t4hCNitUUyhvyGPq3sx1QTd3P3qQetPZhKEtItO7rqfE1WqNtgx2P4Wsr-C3xHczp2Cs2e_SOzb4t3t0wtT6xNkEpWXtLmxynibaJwOKVWHpD9y1JeIwhqESTPezzLF7TpL98UVFsAryFkfRBfkjqyYzTWUiCiBzm_Du7nOZ5WDsHWt8dKkYOVPsQN8-qlYffTb6U9dL0sZsXyHxkPswrr7ZwnVdhbUg.jpg)
**Apple 发布搭载 M6 芯片的全新 14 寸 MacBook Pro，售价 ￥15,999 起，11 月 6 日正式发售。**

* 核心配置：搭载满血版 M6 处理器，存储从 1TB SSD 起步
* 连接规格：支持 Wi-Fi 7 与蓝牙 6，网络与外设连接均采用当前最新标准
* 销售安排：10 月 29 日凌晨 1 点 10 分开启预购，11 月 6 日正式发售
* 官方新闻稿已同步发布，属于典型的新品发布资讯，暂未披露性能跑分或架构层面的技术细节

### [Apple 发布全新 iMac（M6 芯片）](https://t.me/AppleNuts/2560)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-27 21:21:10
![](https://cdn5.telesco.pe/file/XzIKjTRohxWDcHzWkl0jUi2lKzzC4YucqJsTy4k59OpEhELM1XZeIeDQ0UqgFHDOv5j3BxSamRqtc7KLapW63Zw-fasW5IlxDaiX1YfnwRQTd9M8jkiO9tUBmnmeMfILGaleQZ8d0Yz4BB2YKgZviNWsnuh_urVqW7SC2LP9B821UWrFBnT_KtzNGu92Vqr_6GGlRmKsK161EwYxfOVt9GfKTjfVV8OGFQgQJGsZJMzIfpg978fYxJKJ6bDsTbkAlRqa5HR5DrRVpcUHppgiQrvhId0volIwIo0Gbh2gekwI_gTM8j0ZG6DsMYiptcg4Kteq8uoXojnoIiqlAQHiNg.jpg)
**Apple 发布搭载 M6 芯片的全新 iMac，售价 ￥12,499 起，与新款 MacBook Pro 同日开启预购并同步发售。**

* 核心配置：搭载 M6 芯片，支持 Wi-Fi 7 与蓝牙 6，无线连接规格与同期发布的 MacBook Pro 保持一致
* 网络选项：可选配 2.5 千兆以太网接口，满足对有线网络速度有更高要求的办公场景
* 销售安排：10 月 29 日凌晨 1 点 10 分开启预购，每位顾客限购 6 台，11 月 6 日正式发售
* 官方新闻稿已同步公布，属于常规新品资讯，未涉及更多技术细节
