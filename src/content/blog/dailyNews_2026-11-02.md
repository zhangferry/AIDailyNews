---
title: "Daily News #2026-11-02"
date: "2026-11-02 08:00:00"
description: >
  在低端 Android 手机浏览器里离线跑 Python 和 SQL：Efiwe 离线优先编程教育平台的工程实践 Apple Intelligence 确认即将登陆中国大陆，合作模型为阿里巴巴千问（Qwen）
tags:
- "Apple Intelligence"
- "离线优先"
- "千问"
- "前端架构"
- "Apple"
- "编程教育"
- "PWA"
- "阿里巴巴"
- "WebAssembly"
- "AI"

---

> - 在低端 Android 手机浏览器里离线跑 Python 和 SQL：Efiwe 离线优先编程教育平台的工程实践
> - Apple Intelligence 确认即将登陆中国大陆，合作模型为阿里巴巴千问（Qwen）

## 📥 Tech News

### [在低端 Android 手机浏览器里离线跑 Python 和 SQL：Efiwe 离线优先编程教育平台的工程实践](https://www.infoq.cn/article/HHgKMMKa8BNZYQuMFSMS)

来源：InfoQ 推荐

发布时间：2026-10-31 20:43:05
![](https://static001.infoq.cn/resource/image/25/04/25015ae7cff901afccf5a933f31fef04.png)
**Efiwe 是面向低端 Android 手机的离线优先编程教育平台，Python 与 SQL 通过 WebAssembly 在浏览器本地执行、无需服务器，已覆盖 160 个国家超 2.2 万名学习者，文章系统复盘了其中的工程坑与解法。**

* 放弃原生应用选择 PWA：免 APK 下载流量、Service Worker 即时生效更新、一套 Web 运行时跑通 Pyodide 与 sql.js；运行时只在 Worker 中按需初始化，学生代码报错被当作正常数据而非系统异常。
* 从 localStorage 迁移至 IndexedDB：前者约 5MB 配额且同步阻塞主线程；迁移采用双重读取过渡期，读旧、写新分别独立捕获异常，避免缓存损坏或磁盘写满拖垮页面。
* 最深刻的故障教训：启动流程中 await 缓存写入，在存储已满的设备上会静默中断渲染导致白屏；修复为发起后不等待、显式捕获异常，并用 navigator.storage.estimate() 预检查、主动降级离线能力。
* AI 反馈采用两级机制：云端模型设 4 秒超时，端侧确定性分析无条件先执行兜底，并按距离正确答案的远近切换提示粒度；多人共用设备场景要求本地存储按用户档案做命名空间隔离，支持 20 个档案一键切换。
* 尚未解决：弱设备 Wasm 冷启动慢、端侧模型质量是离线反馈上限、浏览器存储配额机制不透明。对面向弱网弱设备用户的产品普遍适用。

### [Apple Intelligence 确认即将登陆中国大陆，合作模型为阿里巴巴千问（Qwen）](https://t.me/AppleNuts/2567)

来源： Apple Nuts - Telegram Channel

发布时间：2026-10-31 12:52:43
![](https://cdn5.telesco.pe/file/Lcd-0AxB9rGoZeCvKv4WqgGzEtn2oSFn0JTQ_yRNUUNfMwF70RTANRodnjKg-Lmp4vlhqnEjRwYvEEbjqIESTG5k0RS6w8G4bXprHMCXMn2xYpQSFAcWXHRFqEIBdvvqFjryCHH1fp-Lb-QtSf2h0dBa89SemQVaf-ng0z5mmJ9f2qPcmxhmNI0BKHcjlXmmkuHLCOg8Tali12UPGvA5KJjddQxTJaaHniK9SMCZvAnC8XLNI9lXCVDXqlne9catu3Sy1qhXbcZKSowigMqGNEJ_JoDc0Eyl7XoWe9LKuBTJhZ3jP5t4RnWTxu-bgzzA3nZt1XD1yt2QEgjUFcM4Hw.jpg)
**苹果确认 Apple Intelligence 即将登陆中国大陆市场，本地化合作的大模型为阿里巴巴千问。**

* 苹果已在中国大陆官网上线 Apple Intelligence 介绍页面，作为该消息的官方信息来源，证实了此前流传的合作传闻
* 这意味着国行 Apple 设备用户即将获得苹果的 AI 功能套件支持，阿里千问将承担本地化模型能力
* 原文属于简短新闻速讯，未披露具体上线时间、支持机型范围、可用功能清单及数据合规安排等细节，感兴趣的读者可持续关注苹果官网页面更新
