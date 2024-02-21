---
title: "iOS Daily News #2024-02-21"
date: "2024-02-21 09:36:39"
author: 摸鱼仔
description: "🌟 MLX Swift：Apple 芯片上的机器学习研究框架
Swift 扩展：如何和何时使用它们
🌟 Byte Pair Encoding（BPE）算法详解
📱 手机进水别用大米！苹果官方给出正确处理方法
🌟macOS Sonoma 提供 134 张令人惊叹的动态壁纸
🎉 iPhone 16 Pro 新配色曝光：沙漠黄和水泥灰
🚨 安洵信息内幕曝光：欺骗、低质产品、渗透海外"
tags: 
- '网络安全'
- 'Swift'
- '机器学习'
- '手机进水'
- '苹果官方建议'
- '标记化'
- '壁纸'
- 'iPhone'
- '欺诈'
- '苹果'
- '自然语言处理'
- '编程'
- 'macOS'

---

> * 🌟 MLX Swift：Apple 芯片上的机器学习研究框架
> * Swift 扩展：如何和何时使用它们
> * 🌟 Byte Pair Encoding（BPE）算法详解
> * 📱 手机进水别用大米！苹果官方给出正确处理方法
> * 🌟macOS Sonoma 提供 134 张令人惊叹的动态壁纸
> * 🎉 iPhone 16 Pro 新配色曝光：沙漠黄和水泥灰
> * 🚨 安洵信息内幕曝光：欺骗、低质产品、渗透海外

## Daily News

### [📱 手机进水别用大米！苹果官方给出正确处理方法](https://www.macworld.com/article/2239742/iphone-liquid-damage-dry-rice.html)

来源：Macworld

发布时间：2024-02-20 22:15:09

手机进水后，很多人会使用大米来吸干水分，但研究表明大米并不能加快手机干燥速度，反而可能使逻辑板进一步损坏。苹果官方建议，手机进水后应采取以下步骤：1. 将手机连接器朝下轻拍，去除多余液体，放置在干燥通风处。2. 30 分钟后尝试使用闪电或 USB-C 数据线充电或连接配件。3. 如果再次出现液体检测警报，则表示连接器或数据线插针下仍有液体，继续放置在干燥通风处，最长可达一天。4. 如果手机已干燥但仍无法充电，请拔下数据线和适配器，然后再重新连接。

### [🌟macOS Sonoma 提供 134 张令人惊叹的动态壁纸](https://osxdaily.com/2024/02/19/how-to-use-134-new-aerial-wallpapers-in-macos-sonoma/)

来源：OS X Daily

发布时间：2024-02-20 00:02:15

macOS Sonoma 提供了 134 张令人惊叹的新壁纸，可用于美化您的 Mac 桌面背景。大量新壁纸以主题分类，包括风景、城市景观、水下和太空中的地球。更棒的是，这些壁纸不仅是静态的，它们都是动态壁纸，这意味着它们会短暂地移动。

### [🎉 iPhone 16 Pro 新配色曝光：沙漠黄和水泥灰](https://www.macworld.com/article/2241884/iphone-16-pro-colors-desert-yellow-cement-gray.html)

来源：Macworld

发布时间：2024-02-20 21:34:33

苹果每年都会通过关注外观变化来掩饰其新机型中相对较小的升级——即以前无法用于区分最新手机与其前代产品的颜色饰面。iPhone 13 Pro 推出了新的绿色和浅蓝色，14 Pro增加了紫色，15 Pro 去年获得了全新的钛合金饰面。
距离苹果发布 2024 年的 iPhone 更新还有六个多月的时间，但我们刚刚获得了有关今年晚些时候发布的 iPhone 16 Pro 和 16 Pro Max 将提供的全新颜色的第一个线索。据 Twitter 爆料者 Majin Bu 透露，更昂贵的机型“可能”采用沙漠黄和水泥灰——尽管他强调这些信息不应被视为 100% 准确。
如果这两款产品都没有特别吸引力，爆料者澄清说沙漠黄（或沙漠钛）“类似于 iPhone 14 Pro 的金色，但更深更重”，而水泥灰（或钛灰色）是“类似于 iPhone 6 上使用的深空灰色”。

## Daily Blog

### [🌟 MLX Swift：Apple 芯片上的机器学习研究框架](https://swift.org/blog/mlx-swift/)

来源：Swift.org

发布时间：2024-02-20 18:00:00

MLX Swift是一个机器学习研究框架，它将Python语言的易用性和高级语法与C++语言的速度相结合。它具有硬件加速、自动微分和神经网络训练等功能。MLX Swift使研究人员能够轻松地在Apple芯片上进行实验，并提供了一个友好的机器学习框架，可以在不同的平台和设备上进行实验。

### [Swift 扩展：如何和何时使用它们](https://www.avanderlee.com/swift/extensions/)

来源：SwiftLee

发布时间：2024-02-20 21:59:52

Swift 扩展允许您使用新功
能扩展现有的类、结构、
枚举或协议。无论是由您
定义的自定类
型还是某个
frameworks 内的现有类
型，扩展都可以
创
建自定访问器并增强您使
用的类
型。所谓的追溯建
模允许您扩展… ->

这篇文章《Swift 扩展：如何和何时使
用它们》首发于



## Daily Code

### [🌟 Byte Pair Encoding（BPE）算法详解](https://github.com/karpathy/minbpe)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-02-21 06:40:14

Byte Pair Encoding（BPE）算法是一种流行的无监督多任务学习算法，用于训练大型语言模型（LLM）的标记器。该算法将文本编码为字节对，并通过合并最常见的字节对来创建新的标记。这可以减少标记器的词汇量，同时保持其表示文本的能力。minbpe是一个Python库，它提供了两个标记器：BasicTokenizer和RegexTokenizer。BasicTokenizer直接在文本上运行BPE算法，而RegexTokenizer在标记化之前使用正则表达式模式将输入文本按类别拆分。minbpe还允许用户训练自己的标记器，并支持特殊标记。

### [🚨 安洵信息内幕曝光：欺骗、低质产品、渗透海外](https://github.com/I-S00N/I-S00N)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-02-21 06:40:14

上海安洵信息科技有限公司是一家声称提供网络安全服务的公司，但其真实性受到质疑。该公司被指控欺骗国家安全机关，员工抱怨工作环境恶劣，财务状况存在问题。安洵还被指控提供低质量的产品，渗透海外政府部门。
