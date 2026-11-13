---
title: "Daily News #2026-11-14"
date: "2026-11-14 08:00:00"
description: >
  FileWrapper(directoryWithFileWrappers:).write(…) erroneously deletes existing folders & files Google 联合 Meta 推出 TorchTPU：PyTorch 原生支持 TPU Amplitude 借助 OpenAI 模型将产品改进交付周期缩短至 1-2 天
tags:
- "深度学习"
- "开源"
- "OpenAI"
- "客户案例"
- "Swift"
- "macOS"
- "AI Agent"
- "FileWrapper"
- "Foundation"
- "效率提升"
- "Bug"
- "TPU"
- "产品研发"
- "AI 基础设施"
- "PyTorch"

---

> - FileWrapper(directoryWithFileWrappers:).write(…) erroneously deletes existing folders & files
> - Google 联合 Meta 推出 TorchTPU：PyTorch 原生支持 TPU
> - Amplitude 借助 OpenAI 模型将产品改进交付周期缩短至 1-2 天

## 🍎 iOS Blog

### [FileWrapper(directoryWithFileWrappers:).write(…) erroneously deletes existing folders & files](https://wadetregaskis.com/filewrapperdirectorywithfilewrappers-write-erroneously-deletes-existing-folders-files/)

来源：Wade Tregaskis

发布时间：2026-11-13 02:58:23

**开发者 Wade Tregaskis 发现 Apple Foundation 框架中 FileWrapper(directoryWithFileWrappers:) 的 write(...) 方法存在危险缺陷：当写入操作失败时，它会连带删除目标位置已存在的文件夹和文件。**

* 预期行为应为二者之一：要么完成写入并覆盖已有内容，要么失败但完整保留原有数据；实际情况却是写入失败的同时原有文件被删除，不存在任何合理场景能解释这一行为。
* 作者尚未深入调试该 Bug 的根本原因，文章目前仅记录了这一现象。
* 对 macOS/iOS 开发者的启示：在使用 FileWrapper 进行目录写入前应警惕数据丢失风险，重要数据务必先行备份，避免依赖该 API 的失败回滚行为。

## 📥 Tech News

### [Google 联合 Meta 推出 TorchTPU：PyTorch 原生支持 TPU](https://www.infoq.cn/article/Fikt82HLToqb6ZANB2xj)

来源：InfoQ 推荐

发布时间：2026-11-12 15:00:00
![](https://static001.infoq.cn/resource/image/d2/66/d26cc0b823699480b6130d7340617b66.jpg)
**Google 与 Meta 合作推出开源项目 TorchTPU，为 TPU 提供原生 PyTorch 后端，现有工作负载仅需少量代码修改（替换设备名与分布式后端）即可迁移，解决了 PyTorch/XLA 侵入式修改、编译延迟高、不支持即时执行等长期痛点。**

* 支持 Strict、Debug 和 DeferAndFuse 三种执行模式，其中 DeferAndFuse 混合模式比 Strict Eager 快 50% 以上，同时降低 HBM 峰值内存占用。
* 通过集成流水线在 v5e 起的多代 TPU 上以即时和编译两种模式验证了约 5000 个 Hugging Face 模型、覆盖 500 多种架构。
* 性能方面，300 亿参数模型在单枚 TPUv7 上推理吞吐达每秒 25,700 Token（序列长度 5120）；Qwen3 MoE 235B 训练可扩展至 8,192 枚芯片。
* 项目仍处早期，路线图包括动态形状、算子覆盖、强化学习和量化；社区普遍认为此举早该发生，将显著利好 PyTorch 生态与 TPU 硬件的结合。

### [Amplitude 借助 OpenAI 模型将产品改进交付周期缩短至 1-2 天](https://openai.com/business/customer-stories/amplitude)

来源：OpenAI News

发布时间：2026-11-13 04:00:00

**产品分析公司 Amplitude 基于 OpenAI 模型构建了主动式产品代理 Wave，将产品改进的交付周期压缩至 1-2 天。**

* Wave 覆盖完整的产品研发闭环：识别应该构建什么功能、借助编码代理帮助团队交付变更、并自动衡量变更的实际影响
* 该案例展示了 AI 代理从单纯编码辅助扩展到「洞察—开发—度量」全流程整合的趋势
* 此为 OpenAI 官方客户案例，营销属性较强，未披露具体技术架构与实现细节，实际效果数据有待独立验证
