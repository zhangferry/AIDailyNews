---
title: "Daily News #2026-10-13"
date: "2026-10-13 08:00:00"
description: >
  Uber 在 Kubernetes 平台上将扩容意图与执行操作解耦 AI 无限，人生有限｜对谈 KK、山音：一线 AI 创作者 Fine-Grained Swift Warning Control with Bazel Features
tags:
- "架构"
- "AIGC"
- "rules_swift"
- "Kubernetes"
- "Bazel"
- "视频生成"
- "编译警告"
- "构建系统"
- "分布式系统"
- "AI"
- "Uber"
- "高可用"
- "Swift"
- "影视创作"
- "创意工作流"

---

> - Uber 在 Kubernetes 平台上将扩容意图与执行操作解耦
> - AI 无限，人生有限｜对谈 KK、山音：一线 AI 创作者
> - Fine-Grained Swift Warning Control with Bazel Features

## 📥 Tech News

### [Uber 在 Kubernetes 平台上将扩容意图与执行操作解耦](https://www.infoq.cn/article/2SNgaiHoK808v22dl5SJ)

来源：InfoQ 推荐

发布时间：2026-10-11 15:00:00
![](https://static001.infoq.cn/resource/image/a3/c2/a338c8fb086ba1659f7316c4f3efb9c2.jpg)
**Uber 通过自定义资源 ServiceScale 和服务扩缩容控制器（SSC），将多个编排器的扩缩容意图与实际执行解耦，在无需预留闲置容量的前提下支持区域故障转移，稳态资源配比从 2 倍降至 1.3 倍，节省超 100 万 CPU 核。**

* 背景规模：Uber 平台 Up 管理跨数据中心与云厂商的 100 多个集群、约 4000 个服务、300 万核 CPU，每天启动 150 万个 Pod；双活区域故障转移时需缩容低优先级工作负载、扩容高优先级工作负载，因此引入了新的扩缩容意图来源。
* 核心设计：团队未将故障转移逻辑塞进处于关键路径的部署控制器 UDC，而是引入 ServiceScale CRD 和 SSC，让各编排器独立表达意愿，由 SSC 调和为 Kubernetes 对象；意图直接物化在 K8s 中，无需外部数据库或独立控制平面，故障排查与状态恢复更简单。
* 生产经验一：Informer 缓存过期导致状态误判，团队实现"读己所写"一致性防护——更新下游资源时打上资源版本注解，上报状态前校验缓存已读到该版本。Kubernetes v1.36 也引入了类似缓解机制，并正在推动 controller-runtime 全面支持该语义。
* 生产经验二：UDC 与 SSC 并发写同一资源导致 ReplicaSet 元数据与规范漂移、滚动更新卡住，团队通过全集群可观测检测不一致并构建自动修复程序。
* 整个方案历时一年上线，采用预发布环境、金丝雀发布和基于 KubeKind 的集成测试模拟控制器竞态，支持原生 Deployment 与 OpenKruise CloneSet，全程无客户可感知中断。

### [AI 无限，人生有限｜对谈 KK、山音：一线 AI 创作者](https://www.bestblogs.dev/article/e5bb8efe1e?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-10-11 09:58:00
![](https://image.jido.dev/20251127045458_5f2addf4)
**一线 AI 导演 KK 与山音在对谈中指出，AI 正在颠覆传统影视生产链路，导演的核心能力正从工业调度转向审美判断与拍板决策。**

* AI 将生成与剪辑一体化，创作从庞大团队协作回归到以剪辑台为核心的工作流，从 Image-to-Video 到 Reference-to-Video 的范式演进大幅降低资产复用与协作门槛，显著缩短制作周期；
* 工业分工褪去后，导演失去推卸责任的借口，必须精通光影、构图、节奏等底层技术，核心竞争力浓缩为面对海量生成内容时的审美批判与决策力；
* 技术无限与人生有限构成新矛盾：制作周期的极度压缩加速消耗创作者的生活积累，而触动人心的内核仍需亲眼所见、亲身所感的真实体验；
* 两位创作者认为技术平权打破了西方工业流水线垄断，处于混沌期的 AI 影视让全球创作者站上同一起跑线，东方创作者迎来参与定义下一代视听语言的历史性契机。

## 💾 Daily Dev

### [Fine-Grained Swift Warning Control with Bazel Features](https://adincebic.com/2026/10/11/finegrained-swift-warning-control-with.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-10-11 23:57:28
![](https://cdn4.telesco.pe/file/dZ8kpQ-G6eGhcqcoT5WUwdFsojiPmrGrF_NCImmrdZfUm48KTSnXOQ1g5-0az_Lv0IKn6YFZWC5T3ptO2Y-5zzUrDBi1fW-Rxl1y5dVpkDQda0KfbZQgE9PcsKcmNrcG1T7iryWMBptdTB7HJc1ttRL4gaLVb7KDI8Fvwu4rzN-PzA4qfBrGynMNZu8hvDieg7N5pW5MTBDHOL5OxF60el5ttRw0EEKc9J7oCT3SiKuWuNrUrhL5l0JVhTQADxth41puf86R1-gpAPmdsZhGW4_ggeJnMaiardI23Gh69yy89HFrgFdahd155ISMoKZ27ucJHGpsmL5UIBQB5FwN2Q.jpg)
**rules_swift 4.2.0 引入基于 Bazel features 机制的 Swift 警告控制方案，可将特定诊断组的警告升级为编译错误，并支持从全局到单个目标的精细化配置。**

* Swift 早在 SE-0443 中就支持按诊断组控制警告，但传统做法需在 swift_library 的 copts 传参、写入 .bazelrc 或借助宏批量应用，存在误伤外部仓库、增加维护复杂度、难以对特定目标退出等缺陷。
* 新方案使用极简：`bazel build //... --features=swift.werror.DeprecatedDeclaration` 即可将 DeprecatedDeclaration 诊断组的所有警告作为错误上报。
* 配置粒度灵活：命令行或 .bazelrc 全局生效，REPO.bazel 限定当前 Bazel 仓库，features 属性则可精确到单个 target。
* 借助 Bazel 的 feature 否定机制，在目标的 features 中加 `-` 前缀（如 `"-swift.werror.DeprecatedDeclaration"`）即可让遗留代码库保持警告级别，而项目其余部分仍按错误处理。

适合使用 Bazel 构建 Swift 项目的工程团队用于统一警告治理。
