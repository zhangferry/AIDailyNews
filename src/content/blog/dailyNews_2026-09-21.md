---
title: "Daily News #2026-09-21"
date: "2026-09-21 08:00:00"
description: >
  智谱 ZCode 偷传代码风波追踪：Agent 的数据行为谁来审计？ AI 写代码飞快，为何交付没有变快？小红书 Muse 的 Agentic 架构实践 Solaris 早已淡出视野，它的“转门”却还藏在 Go、WebKit 和 Rust 里 Stats：macOS 菜单栏系统监控开源工具
tags:
- "Solaris"
- "系统监控"
- "Go"
- "数据隐私"
- "架构设计"
- "Rust"
- "AI安全"
- "Agent"
- "操作系统"
- "工程实践"
- "安全审计"
- "效率工具"
- "AI Agent"
- "Agent编排"
- "并发编程"
- "AI编程"
- "macOS"
- "逆向分析"
- "开源工具"

---

> - 智谱 ZCode 偷传代码风波追踪：Agent 的数据行为谁来审计？
> - AI 写代码飞快，为何交付没有变快？小红书 Muse 的 Agentic 架构实践
> - Solaris 早已淡出视野，它的“转门”却还藏在 Go、WebKit 和 Rust 里
> - Stats：macOS 菜单栏系统监控开源工具

## 📥 Tech News

### [智谱 ZCode 偷传代码风波追踪：Agent 的数据行为谁来审计？](https://www.bestblogs.dev/article/9e731b7253?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-19 17:54:31
![](https://media.bestblogs.dev/20260919134949_2646a559-999b-4397-9737-66507e341f6e.jpeg)
**智谱 ZCode 被逆向发现后台将整个项目连同历史记录加密上传云端，事件暴露出现有 Agent 安全框架对厂商自身数据行为的结构性盲区，社区提出出口声明、本地外传日志与责任保险等务实约束路径。**

* 逆向分析显示：用户登录后约 4.2 万个文件被打包加密上传至阿里云（86.6% 为历史修改记录），解密私钥仅存于智谱一侧；界面两个相关开关均无法关闭上传，删除本地待发送文件后仍会自动重建重试。
* 智谱致歉称问题源于「代码库索引」默认开启，但回应与社区追问错位：本地索引技术上无需上云、触发时机在每次提问之前而非生成 Wiki 时、v3.12.2 更新日志中相关条目事后被删除。
* 分析认为上传包的粗放程度更像激进产品决策叠加工程偷懒而非系统性窃取，但厂商真正稀缺的三类训练数据（改动因果链、带结果标注的使用轨迹、真实项目）与上传内容高度吻合。
* OWASP、NIST 倡议、欧盟 AI 法案等规则均假设厂商站在用户一边、防的是外部攻击者，无法覆盖厂商自身外传通道；知情同意在结构上也无法解决风险承担者与授权者分离的问题。
* 现实走向大概率分层：大型企业通过采购合同加入数据条款与审计权，个人开发者消费版仍处于无人审计、无人负责的状态。

### [AI 写代码飞快，为何交付没有变快？小红书 Muse 的 Agentic 架构实践](https://www.bestblogs.dev/article/035d4a4609?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-19 13:30:00
![](https://image.jido.dev/20260527123921_5b85448.jpeg)
**小红书 AI Coding 总架构师郑鑫祺拆解 Muse 平台的完整实践：AI 生成代码快不等于交付快，瓶颈已从编码转移到上下文与协作链路，需通过 Agent Team 编排、程序化护航、企业知识工程与 Agent OS，把「会生成代码」的模型变成能交付、兜底和恢复的研发系统。**

* 模型控制架构从 Workflow、Pipeline 演进到 Agent Team，三者并存而非替代；多 Agent 仅在子任务独立、可并行、上下文可分离时才有收益，否则不如一条清晰的 Pipeline。
* 高可用依赖可验证的程序化护航而非 Prompt：Agent 生命周期设置 Hook，四类检查分布于请求前拦截、结果离场校验、工具参数校验、副作用前人工确认；写操作需带幂等键和副作用日志。
* 不要把对话记录当成运行状态：Transcript 只是审计材料，任务恢复需结构化保存目标、约束、计划版本、工具证据、审批记录与剩余预算。
* 企业知识应像 Research 一样被推理链组织，并通过「删除实验」量化价值——去掉某类上下文若成功率不降，说明它只是在消耗窗口和成本。
* 评测需分层（结果/轨迹/组件），成本按成功任务计算；权限可解释、状态可恢复、审计可追溯，往往比模型能力领先几个百分点更有价值。

### [Solaris 早已淡出视野，它的“转门”却还藏在 Go、WebKit 和 Rust 里](https://www.infoq.cn/article/GAhNItmT2o7kvEA1ovxt)

来源：InfoQ 推荐

发布时间：2026-09-19 13:00:00
![](https://static001.infoq.cn/resource/image/87/f5/87b9b38b30862f97f4caf9f7aff03ef5.jpg)
**Solaris 首创的转门同步机制通过将等待状态与锁结构分离，深刻影响了 Go、WebKit 和 Rust 的现代并发设计，成为高性能软件沿用至今的基础范式。**

* 转门机制旨在解决阻塞式互斥锁的两大难题：细粒度锁数量庞大导致锁内嵌管理数据的内存浪费，以及优先级反转引发的系统停滞。线程阻塞时将预分配的转门交给锁，通过以锁虚拟地址为键的全局哈希表建立映射，使无竞争锁保持一个字节到一个机器字的极小体积
* Go 运行时采用同样思路：goroutine 阻塞时通过 semtable 全局哈希表定位 semaRoot 桶，将 sudog 结构链接到等待树中，开销完全外置，支撑数百万 goroutine 的高效扩展
* WebKit 的 WTF::ParkingLot 将线程挂起机制与锁本体分离，Rust 的 parking_lot crate 则明确移植了这一设计，提供优于操作系统原语的性能与公平性
* 核心原则是将线程协调的繁重工作集中到共享外部数据结构；代价是高竞争时需付出全局哈希桶查找与总线同步的开销

## 💾 Daily Dev

### [Stats：macOS 菜单栏系统监控开源工具](https://github.com/exelban/stats)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-19 13:42:42
![](https://cdn4.telesco.pe/file/Gl8yj1Of65dSyrwStZBdaO0KlAvsK678rz4xrIPvVUCaJqd8axECZQRh_LwDgVVAHEGrtdNGnSqE3AWUzt6g1dRMVjY5zNgS6wGbVATie-ztwBvx6zpJxY_Lum4tY1NIqobTuWpLAvER6xUcQ0TxUgAehhB0cMp1d66hEqnQXpnBRmw1rJY__FKkYeTmEpu5j16YJbFnR8hGQqN5fN5oNxahPuTsynsR_9cV4VXG4SGs6f_w784z_NV4_YFCNeB65ndy3aGm_ZC-r_c3UgyY3JK_fiVw-SiQVNit4VM9KNHjIomzzSxGfge7fLs0l3Z50kRaQHlAocBrR1SeqZuRdw.jpg)
**Stats 是一款基于 MIT 协议开源的 macOS 菜单栏系统监控工具，支持 macOS 12 及以上稳定版本，可实时监控 CPU、GPU、内存、磁盘、网络、电池、传感器温度及蓝牙设备等状态。**

* 安装支持手动下载与 Homebrew 两种方式；卸载需运行应用附带脚本并授予管理员权限以移除 SMC 辅助程序及相关偏好数据。
* macOS 26 引入新的隐私控制，需在「系统设置 → 菜单栏」中手动允许 Stats 显示图标；桌面小组件因系统进程数据负载问题默认关闭通信，需在设置中手动开启。
* 能耗方面，Sensors 与 Bluetooth 是开销最大的模块，禁用后最多可降低约 50% 的 CPU 占用；风扇控制功能已进入遗留模式，不再接收更新。
* 隐私上不收集任何遥测数据，仅向自建的 api.mac-stats.com 与 GitHub API 发起更新检查和公网 IP 查询；项目为单人维护的「开源但不开放贡献」模式，未经 issue 讨论的 PR 通常不会被接受，翻译改进除外。
