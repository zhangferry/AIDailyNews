---
title: "Daily News #2026-09-22"
date: "2026-09-22 08:00:00"
description: >
  智谱 ZCode「偷传代码」风波升级：企业发函追责，AI 编程工具的安全边界在哪里？ YC 最新判断：Harness 比模型更重要 Matt Pocock：AI 时代软件基本功更重要 在 Bazel 中用 Tree Artifacts 代替 ZIP 文件
tags:
- "AI 工程"
- "上下文工程"
- "LLM"
- "智谱"
- "AI 编程"
- "Agent Harness"
- "构建优化"
- "隐私"
- "AI Agent"
- "iOS"
- "远程执行"
- "数据安全"
- "构建系统"
- "Harness"
- "TypeScript"
- "架构"
- "软件工程"
- "AI编程"
- "Bazel"

---

> - 智谱 ZCode「偷传代码」风波升级：企业发函追责，AI 编程工具的安全边界在哪里？
> - YC 最新判断：Harness 比模型更重要
> - Matt Pocock：AI 时代软件基本功更重要
> - 在 Bazel 中用 Tree Artifacts 代替 ZIP 文件

## 📥 Tech News

### [智谱 ZCode「偷传代码」风波升级：企业发函追责，AI 编程工具的安全边界在哪里？](https://www.infoq.cn/article/huOiZyyH32MpRwTFkoNe)

来源：InfoQ 推荐

发布时间：2026-09-20 19:46:24
![](https://static001.infoq.cn/resource/image/86/f0/86e2c45e7ca284cf11a6c18fa1ceb3f0.jpg)
**智谱 ZCode「静默上传代码」风波从开发者技术质疑升级为企业正式追责：太原承明科技发函指控 ZCode 未经充分告知和授权上传其商业秘密，要求 10 月 10 日前书面答复，并保留索赔、投诉及诉讼权利。**

* 开发者 ferstar 从本地 ~/.zcode 目录发现 313MB 加密快照：客户端将整个工作区打包为 tar.gz，用 AES-256-CTR 加密、RSA 公钥封装密钥后上传阿里云 OSS，因体积过大连续失败 564 次。
* 快照中 86.6% 内容来自 .git 目录（含 LFS 缓存、对象库与 reflog），源代码仅占约 13.4%，远超检查点恢复与 Repo Wiki 的功能所需；「体验优化」「仓库快照索引」两个开关均无法关闭上传链路。
* 智谱已致歉并称数据「用完即销毁」，3.14.0 版本移除了云端上传链路；但影响范围、历史数据是否彻底删除及数据是否跨境等问题仍无法独立验证。
* 文章进一步指出，AI 编程工具的安全边界取决于模型之外的 Agent Harness，需审查外围软件的额外数据操作及 MCP、插件、云存储等供应链风险，并与 Grok Build、Cursor 的类似争议和索引机制做了对比。

### [YC 最新判断：Harness 比模型更重要](https://www.bestblogs.dev/article/683d44b352?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-20 19:00:00
![](https://image.jido.dev/20260603135251_1257b89.jpeg)
**YC 最新判断指出，AI 竞争的胜负手正从模型能力转向 Harness（模型运行框架）：模型决定能力上限，Harness 决定能否触达上限。**

* ARC-AGI-3 测试显示，同一模型在不同 Harness 下得分相差可达 35.9 个百分点
* 通过信息分层设计（信息分布在上下文、REPL 编程环境和外部存储），非硬编码方案可为 Agent 提供连续状态保持，支撑长周期复杂任务
* OpenJarvis 实验证明，系统层优化能让本地小模型显著追回与云端大模型的性能差距，且运行成本极低
* 企业场景下 Harness 重心转向规模化运维与权限管控，如 YC 内部 QM 系统负责 Agent 状态集中管理，防范信息泄露风险
* Harness 与模型的边界正在融合，优化路径从提示词工程演进至 Harness 代码优化，再借助 Agent 运行产生的经验数据反哺模型权重，形成闭环

### [Matt Pocock：AI 时代软件基本功更重要](https://www.bestblogs.dev/podcast/14ae62014?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-20 16:50:27
![](https://image.jido.dev/20260605145427_78cff8f.png)
**TypeScript 教育者 Matt Pocock 认为 AI 已吃掉战术性编程，工程师价值转向战略层与 Agent 运行环境设计，而经典软件工程概念恰是引导 Agent 的最佳语言。**

* Grill Me skill 逼人类显性化隐藏的技术决策——写一个简单 API 端点被追问 35 个问题，涵盖认证、限流、边界等
* 上下文并非越大越好，顶尖模型表现较好的区间约在前 15 万 token；Ralph Loops 每轮只做最小改动后清空上下文，靠文件系统保留状态，让 Agent 留在聪明区
* Wayfinder 用地图、里程碑与战争迷雾把复杂项目拆成多会话工单（最多 50-100 张），并已迁移到课程规划等非技术场景
* 示踪弹开发、垂直切片、深度模块等经典术语深植于模型训练数据，在提示词中作为引导词可直接改变 Agent 行为
* 警告 Agent 加速软件熵增：TDD 对 Agent 的价值在于反馈回路而非同义反复测试，代码库应按每次从零读取的 Agent 特点优化

## 💾 Daily Dev

### [在 Bazel 中用 Tree Artifacts 代替 ZIP 文件](https://adincebic.com/2026/09/20/tree-artifacts-over-zip-files.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-21 00:17:29
![](https://cdn4.telesco.pe/file/HXTFmfOVjovuMzo_LbuGJOBScgiPngOCq4TtKY4GP6AOwxTBlyKiiMIGbdXZNPdWsTJjk5S5wiJj3nylTVjO2XcDbKzryhp6kOMhB8V6BrRBoEtGXUiP1dLRr_sCbMuPbC66WcU4xIXl8ykc0cDpZ4QcKH9ehXoBm_xuYmhECdW-cihuqLN83JoTg45KBYL-XpkLLXnqn_FF2n8sLtALfsoIrQypYPkybg0Iq_ekjDlxKKV1hh90bKgE2x8M0JrZr9mh-qii7r2eCedwIr3ca9QMUWBBoHbItefHqYGpfK0Y6bJFamf-tXqlawNCKO8xRpk5BLWT2kcLt2fuOo2KdA.jpg)
**文章主张在编写 Bazel 规则时，用 tree artifact（目录输出）替代 ZIP 等归档文件作为构建产物，以减少打包开销并提升远程缓存效率。**

* ZIP 压缩耗时且成本高，下游动作每次使用都需重新解压，带来额外的 CPU、磁盘 I/O 和临时文件；且归档是不透明的二进制大块，难以被缓存系统高效处理。
* Tree artifact 仍作为单一声明输出参与依赖与动作缓存，但其内部各文件存放在内容寻址存储中，远程缓存与远程执行可对这些文件去重，避免反复存储和传输一整个大归档。
* 对 Apple 平台尤为实用：签名、校验、安装等工具天然操作 .app bundle 目录，中间构建步骤保持目录形态可省去大量压缩/解压，明显加快 rules_xcodeproj 本地开发时的编辑-构建-运行循环；仅在真正需要归档的边界（如产出最终 .ipa）才打包。
* 实现上通过 ctx.actions.declare_directory() 声明，用法与 declare_file 类似；限制是 Bazel 在分析阶段无法获知目录内容，不能把其中文件变成常规声明输出，较新的 map_directory 可对目录内容展开操作，但尚不成熟、使用不广。
