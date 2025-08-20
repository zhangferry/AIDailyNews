---
title: "Daily News #2025-08-20"
date: "2025-08-20 23:22:04"
description: "吴翼：从OpenAI到AReaL的AI之旅
Rust 1.90.0：x86_64-apple-darwin目标降级至Tier 2
推荐七款AI写论文工具，助力学术研究
RAG：AI知识获取的核心新模型
网易有道发布会：教育AI新产品全景解读
AI时代的用户体验设计新准则
iOS 26 UIKit 更新亮点概览
Technicolor 全栈Swift技术架构解析"
tags: 
- "人工智能"
- "RAG"
- "UIKit"
- "iOS开发"
- "AI"
- "Swift"
- "设计原则"
- "编程语言"
- "Rust"
- "全栈开发"
- "创业"
- "知识增强"
- "写作工具"
- "用户体验"
- "教育"

---

> - 吴翼：从OpenAI到AReaL的AI之旅
> - Rust 1.90.0：x86_64-apple-darwin目标降级至Tier 2
> - 推荐七款AI写论文工具，助力学术研究
> - RAG：AI知识获取的核心新模型
> - 网易有道发布会：教育AI新产品全景解读
> - AI时代的用户体验设计新准则
> - iOS 26 UIKit 更新亮点概览
> - Technicolor 全栈Swift技术架构解析

## 📥 Tech News

### [吴翼：从OpenAI到AReaL的AI之旅](https://www.infoq.cn/article/VlLeHW4JApCJVxUIsf3w)

来源：InfoQ 推荐

发布时间：2025-08-20 17:57:27

此文聚焦吴翼博士的职业历程与思考，他从加州大学伯克利分校到OpenAI，历经多次重要项目，参与AI前沿研究的过程中，他反思了AI团队的“自下而上”文化如何激发创新。离开OpenAI后，他致力于AReaL开源项目，推动强化学习的应用，为未来的AI人才培养和技术创新铺平了道路。

### [Rust 1.90.0：x86_64-apple-darwin目标降级至Tier 2](https://blog.rust-lang.org/2025/08/19/demoting-x86-64-apple-darwin-to-tier-2-with-host-tools/)

来源：Hacker News - Newest: "apple"

发布时间：2025-08-20 00:01:53

在Rust 1.90.0版本中，x86_64-apple-darwin目标将降级为Tier 2。尽管编译器和标准库仍会分发，但未来将不再保证其自动测试的运行。这一变更反映了Rust项目对苹果支持的调整，尤因苹果逐步放弃x86_64架构。此举可能导致该目标在未来累积更多缺陷。

### [推荐七款AI写论文工具，助力学术研究](https://www.v2ex.com/t/1153816)

来源：V2EX-最新主题

发布时间：2025-08-20 23:01:23

总结了七款实用的AI写论文工具，包括AI论文及时雨和Consensus等，帮助用户简化论文写作流程。这些工具不仅能自动生成文献综述，还能提高改稿效率、降低查重率，为学术写作提供了有效支持。适用于不同论文需求的研究者，极大提高了写作效率。

### [RAG：AI知识获取的核心新模型](https://www.woshipm.com/ai/6257932.html)

来源：热门文章 - 日榜 - 人人都是产品经理

发布时间：2025-08-20 16:30:14

本文深入探讨了检索增强生成（RAG）技术。它不仅阐述了RAG如何结合传统信息检索与大型语言模型，解决知识时效性和获取问题，还阐释了RAG如何提升AI系统的可靠性和可信度。通过设定外部知识库，RAG可以克服LLM的知识停滞和内容幻觉，提高信息输出的准确性与实时性。此外，文章强调RAG在未来AI应用中的重要性，值得关注其进化趋势。

### [网易有道发布会：教育AI新产品全景解读](https://www.infoq.cn/article/yVIa68gtCRZtZ3Ay1RHF)

来源：InfoQ 推荐

发布时间：2025-08-20 20:45:10

网易有道发布会展示了包括AI答疑笔Space X和多模态翻译平台等多款基于教育大模型的AI新品，CEO周枫介绍教育AI能力分级标准L1-L5，强调个性化课堂的实现。尤其是Space X通过智能拼图技术而升级，提升了学生答疑体验。新版本网易有道词典和音视频翻译平台亦在发布中亮相，标志着教育AI技术的多维进化，有望推动教与学的智能化转型。

### [AI时代的用户体验设计新准则](https://www.woshipm.com/ai/6257922.html)

来源：热门文章 - 日榜 - 人人都是产品经理

发布时间：2025-08-20 14:56:32

本文总结了AI驱动的用户体验（UX）设计11条新准则，强调设计师需适应AI带来的变革。设计不再仅是界面美观，而应更注重智能行为、透明度以及用户与AI的协作关系。强调设计应具有未来视野，将透明度与控制权结合，以创造更信任的用户体验，从而引领UI/UX设计的转变，适应新一轮的数字化挑战。

## 💾 Daily Dev

### [iOS 26 UIKit 更新亮点概览](https://sebvidal.com/blog/whats-new-in-uikit-26/)

来源：iOS Development News - Telegram Channel

发布时间：2025-08-20 21:03:01

随着WWDC 25的结束，UIKit在iOS 26中进行了多项重要更新。新增UIAction、背景扩展视图UIBackgroundExtensionView及UIBarButtonItem的新属性，使得应用界面设计更加灵活且美观。此外，UIKit开始逐渐去中心化UIApplicationDelegate，向更现代的UISceneDelegate和UIWindowSceneDelegate过渡。同时， UIKit也为HDR颜色提供了新的构建方法，增强了对色彩的支持。这些更新加强了UIKit的全面性能，开发者可根据新特性优化用户体验。

### [Technicolor 全栈Swift技术架构解析](https://twocentstudios.com/2025/08/04/full-stack-swift-technicolor-technical-architecture/)

来源：iOS Development News - Telegram Channel

发布时间：2025-08-20 21:03:00

在这篇文章中，作者探讨了自己的全栈Swift项目Technicolor的架构演变。Technicolor从Ruby on Rails迁移到Swift Vapor，经过十年的迭代，现已成为一款支持iOS及macOS的社交网络应用。文章详细描述了前端及后端架构，包括API层的设计及相应的Codable模型。此外，作者分享了使用Xcode统一开发的经验，以及如何在服务器中管理认证和数据模型，探讨了外部依赖、测试及部署等一系列挑战，为全栈开发者提供了宝贵的经验教训。
