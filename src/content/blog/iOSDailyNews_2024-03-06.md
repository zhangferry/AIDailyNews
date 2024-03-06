---
title: "iOS Daily News #2024-03-06"
date: "2024-03-06 09:32:03"
author: 摸鱼仔
description: "🎉 苹果发布 Xcode 15.3，支持 iOS 17.4 提交
🌟Apple Watch Ultra 2再创新低，仅663.99美元
💻 新款 MacBook Air 搭载 M3 芯片，支持连接两个外部显示器
💰 iPad 优惠来袭：多款机型限时折扣
🤔 探索 AR 眼镜控制智能家居的可能性
🎉 Swift 5.10 发布，全面数据隔离！
🌟Anthropic最新AI模型超越竞争对手，创行业先河
🌟 ConTextual：多模态模型如何同时推理文本和图像中的文本？
🌟 NectarGPT: 强大的中文生成式 AI
🌟 Shen 语言：一种面向人工智能的编程语言
🗣️ WhisperKit：将 OpenAI 的 Whisper 集成到 CoreML 中，实现高效的本地语音识别"
tags: 
- '语音识别'
- 'Swift'
- '中文生成式 AI'
- 'AR'
- '编程语言'
- '优惠'
- 'iOS'
- 'Apple Watch Ultra 2'
- 'MacBook Air'
- 'AI模型'
- '多模态模型'

---

> - 🎉 苹果发布 Xcode 15.3，支持 iOS 17.4 提交
> - 🌟Apple Watch Ultra 2再创新低，仅663.99美元
> - 💻 新款 MacBook Air 搭载 M3 芯片，支持连接两个外部显示器
> - 💰 iPad 优惠来袭：多款机型限时折扣
> - 🤔 探索 AR 眼镜控制智能家居的可能性
> - 🎉 Swift 5.10 发布，全面数据隔离！
> - 🌟Anthropic最新AI模型超越竞争对手，创行业先河
> - 🌟 ConTextual：多模态模型如何同时推理文本和图像中的文本？
> - 🌟 NectarGPT: 强大的中文生成式 AI
> - 🌟 Shen 语言：一种面向人工智能的编程语言
> - 🗣️ WhisperKit：将 OpenAI 的 Whisper 集成到 CoreML 中，实现高效的本地语音识别

## Apple News

### [🎉 苹果发布 Xcode 15.3，支持 iOS 17.4 提交](https://developer.apple.com/news/?id=7tt9f8cu)

来源：Latest News - Apple Developer

发布时间：2024-03-05 23:56:58

苹果发布 Xcode 15.3，支持 iOS 17.4、iPadOS 17.4、macOS 14.4、tvOS 17.4、visionOS 1.1 和 watchOS 10.4 的应用和游戏提交。开发者现在可以提交在欧盟提供替代支付选项的应用，并衡量其应用累积的首次年度安装量。

### [🌟Apple Watch Ultra 2再创新低，仅663.99美元](https://www.macrumors.com/2024/03/05/apple-watch-ultra-2-new-low/)

来源：MacRumors: Mac News and Rumors - All Stories

发布时间：2024-03-05 22:44:20

亚马逊现推出Apple Watch Ultra 2限时促销，仅售663.99美元，创历史新低。此次促销仅适用于中号靛蓝高山表带。亚马逊预计在周五免费送达，Prime会员可在周四收到。该价格比之前的历史最低价低近60美元，也低于近期第一代Apple Watch Ultra的许多促销价格。

### [💻 新款 MacBook Air 搭载 M3 芯片，支持连接两个外部显示器](https://osxdaily.com/2024/03/04/apple-launches-new-macbook-air-with-m3-chip-support-for-2-external-displays/)

来源：OS X Daily

发布时间：2024-03-05 02:57:38

苹果发布了 MacBook Air 系列电脑的新更新，为这款流行的 Mac 笔记本电脑带来了强大的 M3 芯片以及一些其他新功能。据苹果宣布产品的新闻稿称，新款 M3 MacBook Air 比 M1 机型快 60%，并且最高可达...

### [💰 iPad 优惠来袭：多款机型限时折扣](https://www.theverge.com/21280354/best-ipad-deals-apple)

来源：The Verge -  Apple Posts

发布时间：2024-03-05 06:50:59

虽然最好的 iPad 优惠通常出现在黑色星期五、网络星期一和亚马逊 Prime 会员日等大型促销活动中，但许多假日季的优惠已经延续到了 2024 年。现在，你仍然可以享受许多机型的优惠，尤其是更实惠的 iPad。此外，据最新传闻，苹果将在本月推出新的 iPad Pro 和 iPad Air 机型，届时价格可能会进一步下降。

### [🤔 探索 AR 眼镜控制智能家居的可能性](https://news.ycombinator.com/item?id=39601354)

来源：Hacker News - Newest: "vision pro"

发布时间：2024-03-05 17:57:37

文章讨论了在 AR 眼镜上开发一款应用程序的可行性，该应用程序允许用户通过工作流或“任务”控制应用程序和智能设备。尽管 Vision Pro AR 眼镜尚未正式发布，但文章作者已经构建了一个专门的应用程序，允许用户控制灯光、警报、音乐播放列表和特斯拉汽车。作者正在寻求反馈，以了解在当前 AR 眼镜的限制下，是否有用户或企业对此类应用程序有需求。

## iOS Blog

### [🎉 Swift 5.10 发布，全面数据隔离！](https://swift.org/blog/swift-5.10-released/)

来源：Swift.org

发布时间：2024-03-05 22:00:00

Swift 5.10 发布，带来了全面数据隔离，解决了并发代码中数据竞争问题。还引入了新的 `nonisolated(unsafe)` 关键字，用于取消对存储属性和变量的 actor 隔离检查。Swift 6 将默认启用完全数据隔离，消除 Swift 中所有软件中的数据竞争。

## Tech News

### [🌟Anthropic最新AI模型超越竞争对手，创行业先河](https://www.artificialintelligence-news.com/2024/03/05/anthropic-latest-ai-model-beats-rivals-achieves-industry-first/)

来源：AI News

发布时间：2024-03-05 19:52:32

Anthropic的最新语言模型Claude 3在性能和能力上超越了ChatGPT和Google的Gemini等竞争对手，树立了新的行业标准。据Anthropic称，Claude 3不仅超越了其前辈，还在各种任务中达到了“接近人类”的熟练程度。

### [🌟 ConTextual：多模态模型如何同时推理文本和图像中的文本？](https://huggingface.co/blog/leaderboard-contextual)

来源：Hugging Face - Blog

发布时间：2024-03-05 08:00:00

ConTextual 是一个语境敏感的文本丰富视觉推理数据集，用于评估多模态模型。它包含 506 个具有挑战性的指令，涵盖 8 个真实世界的视觉场景，需要对图像中的文本和视觉线索进行语境敏感的联合推理。该数据集有助于开发细致的视觉语言对齐技术，并欢迎任何形式的合作。

### [🌟 NectarGPT: 强大的中文生成式 AI](https://www.nectargpt.net/)

来源：Hacker News - Newest: "agi"

发布时间：2024-03-05 07:03:25

NectarGPT 是一款强大的中文生成式 AI，它可以帮助你完成各种写作任务，包括撰写文章、生成代码、翻译语言等。它使用先进的深度学习技术，可以生成高质量、流畅自然的中文文本。如果你正在寻找一款中文生成式 AI，NectarGPT 是一个不错的选择。

### [🌟 Shen 语言：一种面向人工智能的编程语言](https://shenlanguage.org/)

来源：Hacker News - Newest: "programming"

发布时间：2024-03-05 20:30:22

Shen 是一种面向人工智能的编程语言，它提供了用于构建和训练机器学习模型的高级抽象。Shen 旨在使人工智能开发人员能够专注于解决问题，而不是底层实现细节。

## Daily Code

### [🗣️ WhisperKit：将 OpenAI 的 Whisper 集成到 CoreML 中，实现高效的本地语音识别](https://github.com/argmaxinc/WhisperKit)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-03-06 09:30:26

WhisperKit 是一个 Swift 软件包，它将 OpenAI 流行的 Whisper 语音识别模型与 Apple 的 CoreML 框架集成在一起，以便在 Apple 设备上进行高效的本地推理。

WhisperKit 可以通过 Swift 包管理器集成到你的 Swift 项目中。
