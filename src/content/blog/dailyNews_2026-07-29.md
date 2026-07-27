---
title: "Daily News #2026-07-29"
date: "2026-07-29 08:00:00"
description: >
  不是模型变慢了，是任务变大了 - 肘子的 Swift 周报 #146 使用 AI Agent 安全清理 Xcode 磁盘空间 Agent 开始“自我进化”：会出题、会反思，还会自己长出新技能 下一代搜索智能体评测基准！美团开源LoHoSearch，用知识图谱校准AI能力认知 让AI离开温室，走向动态世界：MineExplorer揭示顶级多模态大模型被忽视的能力断层 GitLab 将碳足迹意识融入 CI/CD，以衡量软件交付的环境成本 AI如何拓展职场人员的工作边界 Cognizant与Anthropic深化合作：推动Claude大模型的企业级落地 SwiftUI中调整Glass按钮形状的技巧
tags:
- "可持续发展"
- "CI_CD"
- "SwiftUI"
- "Anthropic"
- "AI Agent"
- "具身智能"
- "评测基准"
- "职场"
- "绿色软件工程"
- "磁盘清理"
- "并发编程"
- "AI编程"
- "GitLab"
- "DevOps"
- "ChatGPT"
- "企业服务"
- "知识图谱"
- "UI设计"
- "AI大模型"
- "Swift"
- "技术架构"
- "强化学习"
- "自我进化"
- "搜索智能体"
- "Claude"
- "AI落地"
- "多模态大模型"
- "iOS开发"
- "生产力"
- "大模型"
- "开放世界"
- "Xcode"
- "AI"

---

> - 不是模型变慢了，是任务变大了 - 肘子的 Swift 周报 #146
> - 使用 AI Agent 安全清理 Xcode 磁盘空间
> - Agent 开始“自我进化”：会出题、会反思，还会自己长出新技能
> - 下一代搜索智能体评测基准！美团开源LoHoSearch，用知识图谱校准AI能力认知
> - 让AI离开温室，走向动态世界：MineExplorer揭示顶级多模态大模型被忽视的能力断层
> - GitLab 将碳足迹意识融入 CI/CD，以衡量软件交付的环境成本
> - AI如何拓展职场人员的工作边界
> - Cognizant与Anthropic深化合作：推动Claude大模型的企业级落地
> - SwiftUI中调整Glass按钮形状的技巧

## 🍎 iOS Blog

### [不是模型变慢了，是任务变大了 - 肘子的 Swift 周报 #146](https://fatbobman.com/zh/weekly/issue-146/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2026-07-27 22:00:00
![](https://og.fatbobman.com/weekly/issue146.webp)
**背景/问题**：随着AI模型能力增强，开发者常发现交付结果等待时间变长；同时，在现代iOS开发中，开发者面临着传统回调API与Swift Concurrency融合困难、CI环境管理昂贵低效、以及跨设备UI布局难以自适应等诸多工程痛点。

**核心观点/方案**：针对AI效率问题，作者指出变慢的根本原因是任务粒度变大及Agent主动扩大分析范围，开发者正转向“更慢但更好地写代码”。针对开发痛点，本期周报推荐了多项前沿方案：利用Swift 6.2的Custom Executor将CoreBluetooth回调绑定至Actor以解决并发难题；通过合理分配CI任务和优化Flaky Test来提升GitHub Actions效能；借助onGeometryChange在SwiftUI中构建可变尺寸的非模态面板；此外还探讨了Xcode 27的编译优化及用Rust构建轻量Swift运行时的创新尝试。

**结论/价值**：文章精准洞察了AI协作模式从“问答式”向“交付式”演进的趋势，并为iOS开发者汇总了极具价值的技术实践。无论是想掌握现代并发、优化工程CI，还是探索SwiftUI布局，读者都能从中获得启发，特别适合中高级苹果生态开发者与技术架构师阅读。

### [使用 AI Agent 安全清理 Xcode 磁盘空间](https://www.avanderlee.com/ai-development/how-to-free-up-xcode-disk-space-safely-with-an-ai-agent/)

来源：SwiftLee

发布时间：2026-07-27 16:34:16
![](https://swiftlee-banners.herokuapp.com/imagegenerator.php?title=How+to+free+up+Xcode+disk+space+safely+with+an+AI+Agent)
**背景/问题**：在 iOS 开发过程中，Xcode 经常会不知不觉地占用大量 Mac 磁盘空间。尤其是在当前多 AI Agent 和多 Git worktree 并行开发的趋势下，旧版模拟器、派生数据以及各种临时文件成为了隐形的“磁盘杀手”，导致存储空间急剧萎缩。

**核心观点/方案**：针对这一痛点，文章探讨了如何利用 AI Agent 来安全且高效地清理这些无用文件。相比于过去仅依靠手动或单一 Mac 应用偶尔清理模拟器的做法，引入 AI Agent 可以更智能地统筹排查并管理 worktrees 和 derived data 文件夹，实现自动化的空间回收。

**结论/价值**：这篇文章为 iOS 开发者提供了一个结合前沿 AI 技术解决本地环境痛点的新思路。虽然具体实现细节受限于摘要内容未完全展开，但其方向对受困于本地存储不足、且希望提升开发工作流自动化程度的苹果生态开发者具有很好的启发与参考价值。

## 📥 Tech News

### [Agent 开始“自我进化”：会出题、会反思，还会自己长出新技能](https://www.bestblogs.dev/article/5d978f2ae1?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-07-27 17:27:00
![](https://image.jido.dev/20260527045543_19fddfe.jpeg)
**背景/问题**：当前大语言模型（LLM）面临知识静态化、上下文窗口受限以及容易重复犯错等痛点，过度依赖人工频繁调优和喂数据，限制了 AI Agent 的自主成长与泛化能力。

**核心观点/方案**：文章系统梳理了 Agent 从“被动执行”向“主动进化”转变的三大技术路线：1) 经验/Skill 存储型，通过外挂记忆库积累跨会话能力；2) 基于 RL 的训练型，利用强化学习将经验内化至模型权重；3) 0 数据自学型，通过 Agent 互考实现全闭环进化。文章特别指出，训练专门的“技能管理者（如 SkillOS）”比直接训练执行者更高效，且“技能总结”环节是当前被严重低估的技术突破口。

**结论/价值**：自进化 Agent 是突破现有 AI 能力瓶颈的关键趋势，能够大幅降低对昂贵人工干预的依赖。本文对前沿学术研究进行了极具深度的拆解与横向对比，不仅理清了技术脉络，还指出了未来的研究空白，极具前瞻性，非常适合 AI 架构师、算法工程师及资深技术决策者精读参考。

### [下一代搜索智能体评测基准！美团开源LoHoSearch，用知识图谱校准AI能力认知](https://tech.meituan.com/2026/07/24/LongCat-LoHoSearch.html)

来源：美团 · 技术团队

发布时间：2026-07-27 09:34:23
![](https://p0.meituan.net/meituantechblog/69e86f1a417ef555aed62d74c1152c53108351.png)
**背景/问题**：现有的搜索智能体评测基准（如BrowseComp）迅速饱和，人工出题存在已知实体和关系局限，难以系统性地构造高难度问题来真实区分模型的长程搜索能力。

**核心观点/方案**：美团提出基于知识图谱自动化构造的评测基准 LoHoSearch。该方案利用覆盖762万实体的维基百科知识图谱，从“搜索空间”和“结构复杂度”双维度精准控制题目难度，并配合自然语言转换与多重验证流程生成高质量题库。

**结论/价值**：测试表明当前最强模型GPT-5.5准确率仅为34.74%，且现有的上下文管理策略在此基准上的增益大幅缩水，暴露出大模型在长程搜索推理上的严重短板。该基准为下一代智能搜索和上下文管理技术提供了极具区分度和挑战性的试验场，适合大模型评估与Agent领域研究者深入研读。

### [让AI离开温室，走向动态世界：MineExplorer揭示顶级多模态大模型被忽视的能力断层](https://tech.meituan.com/2026/07/24/LongCat-MineExplorer.html)

来源：美团 · 技术团队

发布时间：2026-07-27 09:34:23
![](https://p1.meituan.net/meituantechblog/3415508a98cf053008ffb59af0ed592a421327.png)
**背景/问题**：当前多模态大模型在静态图像和视频理解上表现出色，但一旦置于实时变化、需要持续探索和长程规划的动态开放世界中，其真实能力因缺乏有效评估手段而难以准确衡量。

**核心观点/方案**：美团构建了首个面向开放世界长程任务的评测基准 MineExplorer。利用多智能体协作合成包含隐藏前置条件的多跳任务（1到4-hop），并主动剥离游戏专有知识以纯粹测试模型的“通用探索”能力，全面评估模型在感知、推理和行动三大维度的表现。

**结论/价值**：对18款顶级模型的测试揭示了一个被忽视的能力断层：模型感知能力强于推理能力，在多跳任务中成功率断崖式下跌。这为具身智能赛道提供了量化基线，明确指出将感知转化为长程规划策略是当前AI走向真实世界面临的最大阻碍，具有极高的行业参考价值。

### [GitLab 将碳足迹意识融入 CI/CD，以衡量软件交付的环境成本](https://www.infoq.cn/article/hJjOFog5ObigvYFod90j)

来源：InfoQ 推荐

发布时间：2026-07-27 17:14:00
![](https://static001.infoq.cn/resource/image/c7/97/c79357bffcecb086265108d34b5ca097.jpg)
**背景/问题**：在传统的 DevOps 实践中，软件交付流水线（CI/CD）的优化往往只聚焦于执行速度、系统可靠性和基础设施成本。然而，随着云计算资源消耗的剧增以及 AI 辅助开发带来的高频构建趋势，软件工程对环境造成的碳排放影响日益凸显，传统指标已无法全面反映工程实践的综合价值。

**核心观点/方案**：GitLab 提出了一种全新的“绿色 DevOps”理念，主张将碳足迹意识融入 CI/CD 管道。该方案并不直接测量硬件耗电量，而是通过结合管道执行时长、执行器利用率、计算资源规模及外部区域电网碳强度模型，来估算软件交付过程的碳排放量。文章强调，降低碳排放与提升工程效率是天然契合的：通过智能缓存、选择性测试和复用构建产物等手段优化冗余流水线，不仅能大幅降低云成本、加速交付，还能同步减少环境消耗。

**结论/价值**：该文章为软件工程引入了全新的可持续发展视角，具有很高的启发性和前瞻性。适合平台工程团队、DevOps 负责人及关注企业 ESG 指标的决策者阅读。它不仅是一项环保倡议，更证明了优秀的工程优化实践本身就是最经济、最绿色的策略。

### [AI如何拓展职场人员的工作边界](https://openai.com/index/how-ai-is-expanding-what-people-do-at-work)

来源：OpenAI News

发布时间：2026-07-27 11:30:00

**背景/问题**：随着人工智能技术的全面普及，职场的工作模式和职责边界正在发生深刻改变。企业和员工均面临如何有效利用生成式 AI 来提升个人能力、优化工作流程，以及如何适应新型人机协作关系的挑战。

**核心观点/方案**：OpenAI 发布的最新研究指出，以 ChatGPT 为代表的 AI 工具正在实质性地“扩展”员工的工作能力，而非单纯地替代人工。研究观察到，使用者正在打破传统的单一岗位限制，借助 AI 承担起跨越不同职能领域的多元化任务，这种趋势正在消解固有的职业壁垒，从而重塑现代职场的工作边界。

**结论/价值**：该资讯揭示了 AI 作为核心生产力放大器在职场转型中的关键作用。其观点适合企业管理者、HR 以及关注职业规划的职场人士阅读，有助于从宏观层面把握未来工作模式的演进方向。但由于原文仅为简短的新闻摘要，缺乏详细的数据样本和具体的行业落地细节，因此实操指导价值相对有限。

## 🤖 AI Coding

### [Cognizant与Anthropic深化合作：推动Claude大模型的企业级落地](https://www.anthropic.com/news/cognizant-anthropic)

来源：Anthropic News

发布时间：2026-07-27 08:00:00
![](https://cdn.sanity.io/images/4zrzovbb/website/6d4a0d28992ade92d6fa63646fd9c9d318245c6c-2400x1260.jpg)
**背景/问题**：随着AI技术飞速发展，大型企业在将AI能力转化为实际生产力时，面临着技术吸收能力不足、缺乏行业上下文以及工程化落地困难等痛点。企业需要的不仅是AI实验，而是能够在严格合规环境下稳定交付的AI应用。

**核心观点/方案**：高知特与 Anthropic 宣布扩大合作，将 Claude 大模型深度嵌入企业级业务中。高知特通过其 Flowsource 等工程平台将 Claude Code 融入软件开发流程，并培养了超3万名具备 Claude 认证的工程师。实际落地案例包括为制造、生物医药和保险等行业构建智能合同审查系统（缩短40%审查时间）和风险导航工具（每周节省8小时人工）。

**结论/价值**：文章展示了大型 IT 服务商如何作为“桥梁”，帮助传统企业跨越AI技术鸿沟。对于关注 AI 企业级落地、大模型商业化路径以及 IT 服务业转型的企业决策者和架构师具有较高参考价值。局限在于内容偏向商业公关宣传，缺乏底层架构细节和具体实施过程中的技术挑战。

## 💾 Daily Dev

### [SwiftUI中调整Glass按钮形状的技巧](https://livsycode.com/swiftui/changing-the-shape-of-glass-buttons-in-swiftui/)

来源：iOS Development News - Telegram Channel

发布时间：2026-07-27 23:37:23
![](https://cdn4.telesco.pe/file/R6ekK7zgsXPfMMdKY86GI1nVMVgoa88PPFGLT10iIiVIf_DqaH-2wckdZzR2jZEsSQctXNwfF2LQWx_gNgwlj3RHQsbS9hfl3SZp0QA4k3-zoJOr3i623qGcseIBWmbkOWfWk9rINUtuoH55vrPad-eLk5RW7LUg753hDg4ZRU90XiWvli-U2FiZRwsZEjaFjxmnu_xstuXTUKx-xKb_EFkhHOXGQxfZn9kId-KfSy7xW9tSX56XZ1t7R1eRDLaNR-kcoMU_Q9J6vF4HmZz_MyJ8RQFv4mr_KC2CLrZoA68bd97iQrXghoVcqPSilABig97uq2DuVZFKjRhbb_FnxA.jpg)
**背景/问题**：在 iOS 26 中，SwiftUI 引入了新的 Liquid Glass API 及 `.glass` 按钮样式。然而，默认情况下，纯图标的玻璃按钮通常呈现为胶囊形，这在处理如设置、主题切换等纯图标操作时显得不够自然，开发者往往需要将其修改为更符合直觉的圆形。

**核心观点/方案**：无需自定义按钮样式，可直接利用 SwiftUI 中现有的 `buttonBorderShape(_:)` 修饰符来更改系统样式的按钮外边框形状。通过将其设置为 `.circle`，开发者可以完美适配纯图标按钮。同时强调应使用 `buttonBorderShape` 而非 `clipShape`，因为前者会参与到系统按钮底板的构建逻辑中，保留材质、高光等系统特效，而后者只是粗暴地在渲染后裁切视图。

**结论/价值**：旧有的 SwiftUI API 在新视觉体系中依然发挥着重要作用。文章为 iOS 开发者提供了一种优雅且符合系统规范的 UI 调整方案，特别适合需要适配 iOS 26 新特性的移动端开发者阅读，能够帮助他们在不破坏系统按钮原生体验的前提下实现自定义外观。
