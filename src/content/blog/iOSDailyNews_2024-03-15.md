---
title: "iOS Daily News #2024-03-15"
date: "2024-03-15 21:50:22"
author: 摸鱼仔
description: "Apple Adjusts DMA Plan to Offer Direct Downloading of Apps From the Web
🎉iPad优惠来袭！9代iPad直降100美元，最低249.99美元入手
💥 macOS 14.4 更新后，部分 Mac 用户的 USB 集线器和外接显示器无法使用
🌟 SwiftUI 惰性容器使用技巧与注意事项
🎉 公开测试版：为企业托管用户自备身份提供商
🎉欧盟通过人工智能法案，褒贬不一
🎨 Lottie：iOS动画库
🚀 全栈 FastAPI 模板"
tags: 
- 'iOS'
- 'macOS'
- '身份验证'
- 'SwiftUI'
- 'FastAPI'
- '人工智能'
- 'Apple'
- '动画'

---

> - Apple Adjusts DMA Plan to Offer Direct Downloading of Apps From the Web
> - 🎉iPad优惠来袭！9代iPad直降100美元，最低249.99美元入手
> - 💥 macOS 14.4 更新后，部分 Mac 用户的 USB 集线器和外接显示器无法使用
> - 🌟 SwiftUI 惰性容器使用技巧与注意事项
> - 🎉 公开测试版：为企业托管用户自备身份提供商
> - 🎉欧盟通过人工智能法案，褒贬不一
> - 🎨 Lottie：iOS动画库
> - 🚀 全栈 FastAPI 模板

## Apple News

### [Apple Adjusts DMA Plan to Offer Direct Downloading of Apps From the Web](https://daringfireball.net/2024/03/apple_adjusts_dma_plan)

来源：Hacker News - Newest: "apple"

发布时间：2024-03-14 21:04:24

Apple has announced changes to its compliance plan for the Digital Markets Act (DMA), including the option for authorized developers to distribute their iOS apps directly from their own websites. This move comes after pressure from the European Commission (EC) to open up iOS to additional methods of software distribution. However, the direct download option will only be available to developers who have an app with over 1 million annual installations in the EU, which may limit its impact on smaller developers.

### [🎉iPad优惠来袭！9代iPad直降100美元，最低249.99美元入手](https://www.macrumors.com/2024/03/14/apples-9th-gen-ipad-100-off/)

来源：MacRumors: Mac News and Rumors - All Stories

发布时间：2024-03-14 22:58:56

苹果9代iPad迎来大幅优惠，64GB Wi-Fi版仅售249.99美元，256GB Wi-Fi版也降至379美元，是入手iPad的好时机。

### [💥 macOS 14.4 更新后，部分 Mac 用户的 USB 集线器和外接显示器无法使用](https://osxdaily.com/2024/03/13/usb-hub-external-monitors-not-working-after-macos-sonoma-14-4-update-for-some-mac-users/)

来源：OS X Daily

发布时间：2024-03-14 07:13:17

一些 Mac 用户发现，在更新到 macOS Sonoma 14.4 后，USB-C 集线器和外接显示器无法正常工作。此问题还会影响连接到 USB 集线器的任何设备，包括键盘、鼠标、外接显示器、SD 卡读卡器和相机。

## iOS Blog

### [🌟 SwiftUI 惰性容器使用技巧与注意事项](https://fatbobman.com/zh/posts/tips-and-considerations-for-using-lazy-containers-in-swiftui/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-03-14 08:12:00

在 SwiftUI 中使用惰性容器时，需要注意一些技巧和注意事项，以优化性能和内存使用。本文介绍了自定义遵循 RandomAccessCollection 的实现、实现无限数据加载、谨慎使用 id 修饰器、SwiftUI 仅保留 ForEach 子视图最顶层的状态以及针对特定类型的状态，SwiftUI 释放内存资源不够积极等内容，帮助开发者更好地掌握这些技巧，优化 SwiftUI 应用。

## Tech News

### [🎉 公开测试版：为企业托管用户自备身份提供商](https://github.blog/changelog/2024-03-13-public-beta-bring-your-own-identity-provider-to-enterprise-managed-users)

来源：Changelogs Archive - The GitHub Blog

发布时间：2024-03-14 03:57:02

GitHub 博客宣布了“自备身份提供商”功能的公开测试版，该功能允许企业为其托管用户使用自己的身份提供商。此功能为企业提供了更大的灵活性，使他们能够使用现有的身份管理系统来管理 GitHub 访问，从而简化了用户管理并提高了安全性。

### [🎉欧盟通过人工智能法案，褒贬不一](https://www.artificialintelligence-news.com/2024/03/13/eu-approves-controversial-ai-act-mixed-reactions/)

来源：AI News

发布时间：2024-03-14 00:39:55

欧盟议会通过了人工智能法案，这是第一个规范人工智能系统使用的监管框架。该法案以 523 票赞成、46 票反对和 49 票弃权的压倒性多数通过。意大利议员布兰多·贝尼菲称“这是历史性的一天”。

## Daily Code

### [🎨 Lottie：iOS动画库](https://github.com/airbnb/lottie-ios)

来源：Trending Swift repositories on GitHub today · GitHub

发布时间：2024-03-15 21:36:25

Lottie是一个跨平台库，用于iOS、macOS、tvOS、visionOS、Android和Web，它使用最少的代码实时渲染基于矢量的动画和艺术。Lottie加载并渲染以bodymovin JSON格式导出的动画和矢量。Bodymovin JSON可以通过bodymovin从After Effects创建和导出，通过Lottie Sketch Export从Sketch创建，以及从Haiku创建。设计师可以创建和发布精美的动画，而无需工程师费力地手动重新创建它们。由于动画是由JSON支持的，因此它们的大小非常小，但复杂性却很大！动画可以播放、调整大小、循环、加速、减速、反转，甚至可以交互式地擦除。Lottie还可以只播放或循环动画的一部分，可能性是无穷的！动画甚至可以在运行时以各种方式更改！更改颜色、位置或任何关键帧值！

### [🚀 全栈 FastAPI 模板](https://github.com/tiangolo/full-stack-fastapi-template)

来源：Trending repositories on GitHub today · GitHub

发布时间：2024-03-15 19:44:49

本模板提供了全栈 FastAPI 应用程序的完整设置，包括后端 API、前端、数据库、Docker Compose、CI/CD 等。它易于使用，只需克隆并运行即可。还支持使用 Copier 生成新项目，并提供详细的文档和示例。
