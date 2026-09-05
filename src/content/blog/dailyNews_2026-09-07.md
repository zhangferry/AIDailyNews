---
title: "Daily News #2026-09-07"
date: "2026-09-07 08:00:00"
description: >
  RTX 4060 跑 35B 模型，每秒 39 Token？伯克利、MIT 联手开源 FreeToken
tags:
- "异构计算"
- "LLM推理"
- "MoE"
- "开源"
- "边缘计算"

---

> - RTX 4060 跑 35B 模型，每秒 39 Token？伯克利、MIT 联手开源 FreeToken

## 📥 Tech News

### [RTX 4060 跑 35B 模型，每秒 39 Token？伯克利、MIT 联手开源 FreeToken](https://www.infoq.cn/article/tij5T0vJ1Yk0s7Uov7SE)

来源：InfoQ 推荐

发布时间：2026-09-05 17:00:00
![](https://static001.infoq.cn/resource/image/c3/a0/c3f17d739d6f8a7c8a76946350dabba0.jpg)
**背景/问题**：稀疏 MoE 模型虽每个 Token 只激活少量参数，但解码仍需在数千亿未激活权重间路由。数据中心可依赖 NVLink 掩盖传输开销，而消费级硬件的 PCIe 带宽（16～64 GB/s）与主机内存延迟构成严重瓶颈，现有边缘运行时采用静态专家卸载，缓存未命中时 GPU 完全停顿。

**核心观点/方案**：FreeToken 用名为 q* 的动态协同调度取代僵化卸载：缓存未命中时不让 GPU 停转，而是依据实时互连吞吐量在 CPU 核心与 GPU 张量核心间分配 Token 计算；配合快速权重格式与整层双缓冲使权重传输与计算完全重叠；弹性内存管理器动态调整 KV 缓存与常驻专家槽位的显存分配；语义锚点检查点机制在智能体频繁改写上下文时复用中间注意力状态，避免全量重算。

**结论/价值**：8GB 显存的 RTX 4060 笔记本可运行 Qwen3.6-35B 达 39 token/s，解码比 Ollama/llama.cpp 快 3～4 倍，预填充快 6～30 倍。对追求本地推理自主权、摆脱 API 锁定、降低智能体迭代成本的开发者极具吸引力；但社区对 q* 闭式解在真实 CPU 调度延迟与内存争用下的有效性、以及与手工调优 llama.cpp 基线对比的公平性仍有争论，落地效果需自行验证。
