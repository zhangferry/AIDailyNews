---
title: "iOS Daily News #2024-02-28"
date: "2024-02-28 09:19:08"
author: 摸鱼仔
description: "🍎 苹果更新内部“未发布产品”文件，传闻新 iPad 和 Mac 即将发布
🌟Word 自动恢复功能，让您的工作永不丢失
⚡️安克充电配件大促，磁吸充电宝仅售 35 美元！
💡第三方库的使用许可与设置包确认
🔥 bpftop：简化 eBPF 性能优化
🌟 DotSlash：让可执行文件部署更简单
💡Mistral AI 推出可与主要参与者竞争的大型语言模型
💡 边缘计算和视频分析检测实时废物污染
🌟 TTS Arena：在野外对文本转语音模型进行基准测试
💡 深度学习优化仓库交通拥堵
🚀Alamofire：一个强大的网络请求库
🚀 YOLOv9：学习您想要学习的内容"
tags: 
- '软件开发'
- '边缘计算'
- '充电宝'
- '网络请求'
- '文本转语音'
- '二进制文件分发'
- '视频分析'
- '开源工具'
- '计算机视觉'
- '人工智能'
- '微软 Word'
- '苹果'
- '工具链分发'
- '平台兼容性'
- '目标检测'
- '废物管理'
- 'eBPF'
- '代码共享'
- '性能优化'
- '深度学习'
- '仓库管理'

---

> * 🍎 苹果更新内部“未发布产品”文件，传闻新 iPad 和 Mac 即将发布
> * 🌟Word 自动恢复功能，让您的工作永不丢失
> * ⚡️安克充电配件大促，磁吸充电宝仅售 35 美元！
> * 💡第三方库的使用许可与设置包确认
> * 🔥 bpftop：简化 eBPF 性能优化
> * 🌟 DotSlash：让可执行文件部署更简单
> * 💡Mistral AI 推出可与主要参与者竞争的大型语言模型
> * 💡 边缘计算和视频分析检测实时废物污染
> * 🌟 TTS Arena：在野外对文本转语音模型进行基准测试
> * 💡 深度学习优化仓库交通拥堵
> * 🚀Alamofire：一个强大的网络请求库
> * 🚀 YOLOv9：学习您想要学习的内容

## Apple News

### [🍎 苹果更新内部“未发布产品”文件，传闻新 iPad 和 Mac 即将发布](https://www.macrumors.com/2024/02/27/apple-updates-unreleased-products-document/)

来源：MacRumors: Mac News and Rumors - All Stories

发布时间：2024-02-27 23:52:14

苹果更新了有关“未宣布或未发布产品”的内部支持文件，传闻苹果计划在 3 月底发布新的 iPad 和 Mac，但尚不清楚两者是否直接相关。文件告知苹果支持顾问如何回应客户有关未宣布产品和服务或已宣布但尚未发布产品的潜在问题。文件已于今日“重新构建和优化”，但我们不知道进行了哪些具体更改。

### [🌟Word 自动恢复功能，让您的工作永不丢失](https://osxdaily.com/2024/02/26/how-to-recover-unsaved-word-documents-on-mac-with-autorecovery/)

来源：OS X Daily

发布时间：2024-02-27 00:08:43

微软 Word 具有自动恢复功能，可以自动保存您的工作进度。您可以通过启用自动恢复功能来确保您的工作不会丢失。

### [⚡️安克充电配件大促，磁吸充电宝仅售 35 美元！](https://www.engadget.com/ankers-5000mah-magsafe-power-bank-is-on-sale-for-35-right-now-155349545.html?src=rss)

来源：Engadget is a web magazine with obsessive daily coverage of everything new in gadgets and consumer electronics

发布时间：2024-02-27 23:54:02

安克磁吸充电宝 622 现价 35 美元，支持 MagSafe 标准，可快速为 iPhone 充电，但充电速度较慢，仅支持 7.5W 功率。安克 525 充电站现价 40 美元，具有两个 USB-C 端口、两个 USB-A 端口和三个交流电源插座，可同时为多个设备充电。安克 621 Lightning 版移动电源现价 20 美元，具有可折叠插头，可直接连接到旧款 iPhone 底部，提供 12W 紧急充电。

## iOS Blog

### [💡第三方库的使用许可与设置包确认](https://www.avanderlee.com/workflow/third-party-libraries-acknowledgments-swift-packages/)

来源：SwiftLee

发布时间：2024-02-27 18:05:22

文章主要介绍了第三方库的使用许可，以及如何使用设置包来确认第三方库的使用。

## Tech News

### [🔥 bpftop：简化 eBPF 性能优化](https://netflixtechblog.com/announcing-bpftop-streamlining-ebpf-performance-optimization-6a727c1ae2e5?source=rss----2615bd06b42e---4)

来源：Netflix TechBlog - Medium

发布时间：2024-02-27 12:08:37

bpftop 是一款命令行工具，用于优化和监控 eBPF 程序的性能。它可以显示每个程序的平均执行时间、每秒事件数和估计的总 CPU 使用率。bpftop 使用 BPF_ENABLE_STATS 系统调用命令来启用全局 eBPF 运行时统计信息收集，并每秒收集这些统计信息，计算每个 eBPF 程序在该样本期间的平均运行时间、每秒事件数和估计的 CPU 利用率。bpftop 使用 Rust 编写，利用了 libbpf-rs 和 ratatui 箱子。

### [🌟 DotSlash：让可执行文件部署更简单](https://engineering.fb.com/2024/02/26/developer-tools/dotslash-meta-tech-podcast/)

来源：Engineering at Meta

发布时间：2024-02-27 03:46:58

DotSlash 是 Meta 推出的开源工具，它简化了二进制文件和工具链在开发者之间的分发。开发者无需将大型平台特定可执行文件提交到存储库，而是可以将源代码存储在存储库中，并使用 DotSlash 在构建时生成可执行文件。这使得开发人员可以更轻松地协作和共享代码，而无需担心平台兼容性问题。

### [💡Mistral AI 推出可与主要参与者竞争的大型语言模型](https://www.artificialintelligence-news.com/2024/02/27/mistral-ai-unveils-llm-rivalling-major-players/)

来源：AI News

发布时间：2024-02-27 20:59:49

法国初创公司 Mistral AI 推出了一个名为 Mistral Large 的大型语言模型 (LLM)，声称可以与市场上几大顶级人工智能系统相媲美。Mistral AI 表示，Mistral Large 在语言理解测试中击败了除 OpenAI 最近推出的 GPT-4 之外的所有主要 LLM。它在其他任务中也表现出色，例如文本摘要、机器翻译和问答。

### [💡 边缘计算和视频分析检测实时废物污染](https://developer.nvidia.com/blog/detecting-real-time-waste-contamination-using-edge-computing-and-video-analytics/)

来源：NVIDIA Technical Blog

发布时间：2024-02-27 08:22:56

文章介绍了一种利用边缘计算和视频分析来检测垃圾收集卡车中的塑料袋污染的解决方案。该解决方案使用 NVIDIA Metropolis 应用程序框架，包括 NVIDIA Jetson、NVIDIA TAO 工具包和 NVIDIA DeepStream SDK。文章还讨论了为什么必须改变废物管理做法，以及边缘计算解决方案如何帮助解决废物污染问题。

### [🌟 TTS Arena：在野外对文本转语音模型进行基准测试](https://huggingface.co/blog/arena-tts)

来源：Hugging Face - Blog

发布时间：2024-02-27 08:00:00

TTS Arena 是一个比较文本转语音（TTS）模型的工具，它允许用户轻松地比较两个不同的 TTS 模型，并投票选出他们认为最好的模型。该工具旨在通过收集社区的排名来对模型进行排名，并使模型比较和选择对每个人都触手可及。

### [💡 深度学习优化仓库交通拥堵](https://news.mit.edu/2024/new-ai-model-could-streamline-operations-robotic-warehouse-0227)

来源：MIT News - Machine learning

发布时间：2024-02-27 13:00:00

深度学习技术将一个难以解决的问题分解成更小的块，从而确定仓库中减少交通拥堵的最佳区域。

## Daily Code

### [🚀Alamofire：一个强大的网络请求库](https://github.com/Alamofire/Alamofire)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-02-28 09:17:51

Alamofire是一个网络请求库，它支持多种网络请求方式，如GET、POST、PUT、DELETE等，并且支持多种数据格式，如JSON、XML、HTML等。它还支持多种认证方式，如Basic认证、Digest认证、OAuth认证等。

### [🚀 YOLOv9：学习您想要学习的内容](https://github.com/WongKinYiu/yolov9)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2024-02-28 06:11:37

YOLOv9，一种新的目标检测算法，通过可编程梯度信息学习您想要学习的内容。YOLOv9 在 MS COCO 数据集上表现出色，在测试集上获得了 55.6% 的 AP，在 AP50 上获得了 72.8%，在 AP75 上获得了 60.6%。YOLOv9 具有较小的模型尺寸和较低的 FLOP，使其非常适合部署在移动设备和嵌入式系统上。
