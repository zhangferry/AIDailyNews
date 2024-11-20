---
title: "Daily News #2024-11-20"
date: "2024-11-20 23:19:50"
description: "在 SwiftData 和 Core Data 中如何优雅地使用事务
苹果的清理工具：照片编辑的新标准
Writing Tools v5版本发布，增强功能与修复
AI如何赋能Meta个性化广告推荐
Hoarder应用评测：便捷的AI标签管理工具
智能交互创新赛：OPPO引领AI技术新趋势
Forta防火墙：AI驱动的网络安全解决方案
深入解析哔哩哔哩客服坐席调度系统演进
Xcode编译时间基准测试工具
数据工程师手册：一站式学习资源
macOS系统监控工具Stats
从创业到被收购：MAIA ACTIVE创始人Lisa的精彩故事"
tags: 
- "应用"
- "技术"
- "调度策略"
- "事务处理"
- "系统监控"
- "客服系统"
- "Core Data"
- "图像处理"
- "SwiftData"
- "广告技术"
- "网络安全"
- "开发工具"
- "数据工程"
- "创业故事"
- "工具更新"
- "赛事"

---

> - 在 SwiftData 和 Core Data 中如何优雅地使用事务
> - 苹果的清理工具：照片编辑的新标准
> - Writing Tools v5版本发布，增强功能与修复
> - AI如何赋能Meta个性化广告推荐
> - Hoarder应用评测：便捷的AI标签管理工具
> - 智能交互创新赛：OPPO引领AI技术新趋势
> - Forta防火墙：AI驱动的网络安全解决方案
> - 深入解析哔哩哔哩客服坐席调度系统演进
> - Xcode编译时间基准测试工具
> - 数据工程师手册：一站式学习资源
> - macOS系统监控工具Stats
> - 从创业到被收购：MAIA ACTIVE创始人Lisa的精彩故事

## 🍎 iOS Blog

### [在 SwiftData 和 Core Data 中如何优雅地使用事务](https://fatbobman.com/zh/posts/using-transactions-instead-of-save-in-swiftdata-and-core-data/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-11-20 22:00:00

本文探讨了在 SwiftData 和 Core Data 中使用事务来提升数据持久化操作的安全性和性能。事务作为一个不可分割的逻辑单元，可以有效防止数据操作中的不一致性。Core Data 隐式处理事务，而 SwiftData 则引入了明确的 transaction 方法。通过实例，作者强调了将多个操作打包到单一事务中可以提高性能，并确保数据一致性。还提到在使用 @ModelActor 的并发模式下，可以构建更高效的事务处理架构。最后，提醒开发者在使用事务时需适度，避免过大的事务影响性能。

### [苹果的清理工具：照片编辑的新标准](https://sixcolors.com/post/2024/11/how-does-clean-up-measure-up/)

来源：Six Colors

发布时间：2024-11-20 00:24:50

在这篇文章中，作者回顾了苹果的清理工具及其在照片编辑中的作用。初步尝试显示，该工具对使用者的摄影后期处理是极有帮助的，尤其是在图像修饰方面，能够有效提升照片的整体质量。文章强调了清理工具的实用性及其在日常编辑中的重要性，值得摄影爱好者和专业人士深入了解。

## 📥 Tech News

### [Writing Tools v5版本发布，增强功能与修复](https://github.com/theJayTea/WritingTools/releases/tag/v5)

来源：Hacker News - Newest: "apple"

发布时间：2024-11-20 20:50:32

Writing Tools v5版本发布，新增弹出式UI和Markdown渲染功能，修复了Gemini相关问题，并增强了在MS Word中的兼容性。用户需删除旧版本后下载新版本。已知问题包括默认热键的使用不畅，建议更改热键设置以解决问题。

### [AI如何赋能Meta个性化广告推荐](https://engineering.fb.com/2024/11/19/data-infrastructure/sequence-learning-personalized-ads-recommendations/)

来源：Engineering at Meta

发布时间：2024-11-20 01:00:43

在Meta的应用生态中，AI在建立用户与广告商之间的连接方面发挥着关键作用。Meta的广告推荐引擎基于深度学习推荐模型（DLRMs），通过结合数千个人工设计的信号，实现了个性化广告的传递。这种方法不仅提高了广告的相关性，也进一步推动了广告效果的提升，展示了序列学习在个性化推荐中的重要性。

### [Hoarder应用评测：便捷的AI标签管理工具](https://www.v2ex.com/t/1091339)

来源：V2EX-最新主题

发布时间：2024-11-20 23:09:59

Hoarder这款应用致力于支持AI进行自动打标签和全文搜索，具备离线存档和截图功能，近期更新丰富，逐渐替代其他工具。作者还分享了部署在NAS上的经验，适合对信息存档与管理有需求的用户，提升了工作效率。

### [智能交互创新赛：OPPO引领AI技术新趋势](http://www.geekpark.net/news/343294)

来源：极客公园

发布时间：2024-11-20 11:32:09

2024年中国高校计算机大赛智能交互创新赛在浙江大学举行，OPPO深度参与，为参赛团队提供技术平台支持与专业指导，助力他们在智能交互领域的创新。哈尔滨工大和四川大学分别带来了基于OPPO平台的AI智能背诵助手及心理测评系统，展现了技术的应用潜力。此次赛事推动了高校生的创新实践，OPPO借此平台进一步布局智能体技术，为未来AI生态的发展做出贡献。

### [Forta防火墙：AI驱动的网络安全解决方案](https://decohack.com/producthunt-daily-2024-11-20/)

来源：Decohack

发布时间：2024-11-20 15:17:09

Forta防火墙采用先进的人工智能检测模型，能够无缝对接各种协议与扩展方案，预计有效防止超过99%的黑客攻击。此外，平台还推出了固定收藏功能，用户可以将最多5个重要对话保留在边栏，随时查看；并支持将对话分类到自定义文件夹中，提升视图的整洁性和组织性。

### [深入解析哔哩哔哩客服坐席调度系统演进](https://mp.weixin.qq.com/s/60adp5UQw4VxYM4Qm6gRfw)

来源：值得一读技术博客

发布时间：2024-11-20 00:00:00

本文详细探讨了哔哩哔哩的客服坐席调度系统，包括在线客服和工单客服的调度策略。随着客户需求的增长，系统通过均衡分配、熟客优先、虚拟排队等策略，改进了服务效率与客户满意度。同时，文章分析了调度过程中的挑战与应对措施，为今后优化提供了思路。

## 💾 Daily Code

### [Xcode编译时间基准测试工具](https://github.com/devMEremenko/XcodeBenchmark)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-11-20 23:17:51

XcodeBenchmark是一个面向iOS/macOS开发的性能比较工具，旨在帮助开发者评估不同配置Mac设备在Xcode中的编译时间。此工具具有大规模代码库，包含76个流行的CocoaPods库，适用于Xcode 15及以上版本。提供了各款Mac设备在不同Xcode版本的编译时间数据，便于开发者在性能与成本之间做出明智的决策。

### [数据工程师手册：一站式学习资源](https://github.com/DataExpert-io/data-engineer-handbook)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-11-20 23:17:54

《数据工程师手册》是一个集合了多种资源的平台，旨在帮助新手和有经验的数据工程师深入学习。推荐的学习路径、项目以及免费训练营视频为入门提供了便利。此外，书籍、社区及个人社交媒体的链接也为学习者提供多元化的支持。手册中列出了超过25本数据工程必读书籍和多达10个优质社区，涵盖了数据道德、产品管理、广告评估等方方面面，同时也包括多个有影响力的播客和资讯源，非常适合希望进入数据工程领域的人士。

### [macOS系统监控工具Stats](https://github.com/exelban/stats)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-11-20 23:17:51

Stats是一款实用的macOS菜单栏监控应用，支持监控CPU、GPU、内存、磁盘、网络使用情况及电池电量，还提供风扇控制和传感器信息等功能。用户可以通过手动安装或Homebrew轻松获取。该应用优化了能源消耗，并支持多国语言，使其更易于全球用户使用。

## 📻 Podcast

### [从创业到被收购：MAIA ACTIVE创始人Lisa的精彩故事](https://www.xiaoyuzhoufm.com/episode/673c82828d1233fb0d6abc65)

来源：温柔一刀

发布时间：2024-11-20 07:00:00

本期播客邀请了MAIA ACTIVE创始人Lisa，探讨她的创业经历及被国内运动巨头收购的背后故事。Lisa从顶尖设计学院毕业，成为高定品牌设计师后选择辞职创业，期间经历了品牌初期的挣扎与不被理解。她透露，尽管公司被收购光鲜，但背后是创业中的艰难时刻，以及与抑郁和焦虑的斗争。这期内容为听众提供了关于品牌建设和创业压力的深刻见解，并引发了对未来探索自我和帮助他人的思考。
