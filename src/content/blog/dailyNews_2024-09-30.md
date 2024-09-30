---
title: "Daily News #2024-09-30"
date: "2024-09-30 21:34:11"
description: "深入探讨Swift Testing中的#expect宏
Xcode 拥有新竞争者，Swift 开发生态迎变革
使用Hummingbird构建代理服务器的简易指南
深入探讨Swift Package Index的演变与社区支持
K8s集群存储性能优化思考
Meta发布AR眼镜原型Orion，AR行业再迎重磅揭示
苹果在Epic诉讼中被指撒谎，法官拒绝延长提交期限
超值谷歌云服务大转让
AeroSpace：适用于macOS的现代平铺窗口管理器
LocalSend - 安全快捷的本地文件共享工具
Maccy：轻量级的macOS剪贴板管理器
Pake - 将网页轻松转化为桌面应用"
tags: 
- "科技"
- "Hummingbird"
- "法律"
- "桌面应用"
- "开源项目"
- "剪贴板管理"
- "性能优化"
- "K8s"
- "代理服务器"
- "开发者工具"
- "开发"
- "Rust开发"
- "窗口管理器"
- "测试"
- "AR眼镜"
- "技术开发"
- "文件共享"
- "云服务"
- "Swift"
- "行业动态"
- "开发工具"

---

> - 深入探讨Swift Testing中的#expect宏
> - Xcode 拥有新竞争者，Swift 开发生态迎变革
> - 使用Hummingbird构建代理服务器的简易指南
> - 深入探讨Swift Package Index的演变与社区支持
> - K8s集群存储性能优化思考
> - Meta发布AR眼镜原型Orion，AR行业再迎重磅揭示
> - 苹果在Epic诉讼中被指撒谎，法官拒绝延长提交期限
> - 超值谷歌云服务大转让
> - AeroSpace：适用于macOS的现代平铺窗口管理器
> - LocalSend - 安全快捷的本地文件共享工具
> - Maccy：轻量级的macOS剪贴板管理器
> - Pake - 将网页轻松转化为桌面应用

## 🍎 iOS Blog

### [深入探讨Swift Testing中的#expect宏](https://www.avanderlee.com/swift-testing/expect-macro/)

来源：SwiftLee

发布时间：2024-09-30 19:46:30

Swift Testing是苹果的Swift测试框架，介绍了多种宏，包括强大的#expect宏。与之前需要使用各种XCAssert变体相比，#expect宏帮助开发者更快捷地调试测试，提高测试的效率和准确性。文章深入探讨了这一功能，强调其在现代Swift开发中的重要性，鼓励开发者掌握这一工具以提升测试质量。

### [Xcode 拥有新竞争者，Swift 开发生态迎变革](https://fatbobman.com/zh/weekly/issue-051/)

来源：肘子的 Swift 记事本 ｜ Fatbobman's Blog

发布时间：2024-09-30 22:00:00

在 JetBrains 停更 AppCode 后，开发者忧虑 Xcode 的竞争和发展，但 Swift 生态正在变化。VSCode 和 Cursor 等工具为开发者提供了新选择，使得 Swift 开发不仅更加便利，也增强了用户体验。作者分享了在多个编辑器间切换的工作模式，强调多样化工具选择的重要性，从而促进了良性竞争，长远看将带来更多创新。此外，文章讨论了 Core Data 和 SwiftData 的技术细节，介绍了最新的通讯模式和 UI 效果等，不断推动 Swift 开发的进步与完善。

### [使用Hummingbird构建代理服务器的简易指南](https://swiftonserver.com/how-to-build-a-proxy-server-with-hummingbird/)

来源：Swift on server

发布时间：2024-09-30 16:00:00

本文详细介绍了如何使用Hummingbird框架轻松构建HTTP代理服务器。通过创建路由、RouterMiddleware或自定义HTTPResponder三种方式，用户可以拦截请求并将其转发到目标服务器。文中说明了修改请求的URL、方法与头信息，使用HTTPClient发送请求并返回响应的四个步骤。此外，Hummingbird设计支持数据流，可以高效传输数据，同时实施回压机制。选择适合自己需求的方案即可享受Hummingbird的强大功能。

### [深入探讨Swift Package Index的演变与社区支持](https://swifttoolkit.dev/posts/dc-dave-and-sven)

来源：SwiftToolkit.dev

发布时间：2024-09-30 08:00:00

Dev Conversations系列访谈中，Dave Verwer与Sven A. Schmidt深入探讨了Swift Package Index的建立与发展。两位开发者分享了其在工具、开发者体验及服务器端Swift的社区贡献，尤其强调了开源项目的复杂性与需求。访谈中披露了他们如何将原本的Ruby on Rails项目迁移至Swift框架Vapor，并深入讨论了Swift 6的严格并发性带来的挑战与机遇。两位也回顾了如何在社区支持与企业赞助下，持续改进与维护项目，让即便是大规模的开源网站也能顺利运营。

## 📥 Tech News

### [K8s集群存储性能优化思考](https://www.v2ex.com/t/1077198)

来源：V2EX-最新主题

发布时间：2024-09-30 20:42:33

zhoudaiyu针对K8s集群的存储性能问题进行了深入探讨，介绍了虚拟化环境导致的api-server超时及iowait问题，并提出使用内存盘和fsync等工具以实现异步双写存储的创新思路。这为同处类似问题的技术人员提供了有价值的参考和解决方案。

### [Meta发布AR眼镜原型Orion，AR行业再迎重磅揭示](http://www.geekpark.net/news/341432)

来源：极客公园

发布时间：2024-09-30 14:29:19

Meta Connect大会上，Meta首次展示AR眼镜原型Orion，凭借传统眼镜形态与高性能融合，掀起行业热议。或将成为AR领域的'Apple Vision Pro'。直播中，雷鸟创新的李宏伟认为Orion虽炫酷却仍需时日，预计三年后方可问世。该产品结合MicroLED显示、光波导和AI等前沿技术，标志着新一代计算平台的到来。两家公司在AR技术上的探索，让外界对未来充满期待。雷鸟X3亦在今年量产，致力于突破市场，迎接AR眼镜的新时代。

### [苹果在Epic诉讼中被指撒谎，法官拒绝延长提交期限](https://9to5mac.com/2024/09/30/second-judge-implies-apple-lied-in-epic-lawsuit-denies-request/)

来源：Hacker News - Newest: "apple"

发布时间：2024-09-30 21:26:10

在苹果与Epic Games的诉讼中，第二位法官暗示苹果在法庭上撒谎，认为苹果对新App Store政策的解释并不可信。苹果曾声称并非出于经济动机，但法官质疑其论点，并要求苹果提交相关决策文件。苹果在截止日期前四天才声称需要更多时间，法官拒绝了这一请求，认为苹果早已知道文件量过大，显示出其不负责任的行为。

### [超值谷歌云服务大转让](https://www.v2ex.com/t/1077202)

来源：V2EX-最新主题

发布时间：2024-09-30 21:24:19

Jacobbb提供了一项极具吸引力的转让信息——2折转让100k美元的谷歌云使用权，包括GPU、储存、数据库等服务。此转让无需付款，且有额外技术支持及返点，吸引了需要大量算力的公司关注。这则信息对相关领域的企业具有高度吸引力。

## 💾 Daily Code

### [AeroSpace：适用于macOS的现代平铺窗口管理器](https://github.com/nikitabobko/AeroSpace)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-09-30 21:32:18

AeroSpace 是一款受 i3 启发的 macOS 平铺窗口管理器，现处于公测阶段。它允许快速切换工作区，并无须关闭系统完整性保护(SIP)。支持纯文本配置，强调键盘操作，且提供良好的多显示器支持。安装可通过 Homebrew，使用简单且安全，且其设计针对高级用户，避免 GUI 面板。AeroSpace 遇到重大变更时会谨慎处理，并致力于长期更新，且不依赖于苹果的 notarization 机制。

### [LocalSend - 安全快捷的本地文件共享工具](https://github.com/localsend/localsend)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-09-30 21:32:21

LocalSend 是一个跨平台的开源应用，允许用户在不需要互联网连接的情况下，通过本地网络安全地共享文件和消息。它使用 REST API 和 HTTPS 加密来实现设备间的通信，避免了对第三方服务器的依赖，大大提高了速度和可靠性。该应用支持多种操作系统，包括 Windows、macOS、Linux、Android 和 iOS。为了确保应用正常运行，用户可能需要配置防火墙，并禁用路由器的 AP 隔离功能。

### [Maccy：轻量级的macOS剪贴板管理器](https://github.com/p0deje/Maccy)

来源：Trending Swift repositories on GitHub this week · GitHub

发布时间：2024-09-30 21:32:18

Maccy 是一款高效的 macOS 剪贴板管理器，支持快速浏览和搜索剪贴板历史记录。此应用适用于 macOS Sonoma 及以上版本，强调键盘优先的操作方式，确保安全与隐私。用户通过快捷键或菜单栏快速访问历史内容，并可自定义剪贴板忽略规则，以保护敏感数据。Maccy 是开源软件，免费提供，适合寻找简单而强大的剪贴板工具的用户。

### [Pake - 将网页轻松转化为桌面应用](https://github.com/tw93/Pake)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2024-09-30 21:32:21

Pake 是一个基于 Rust 的工具，可以将任何网页转换为桌面应用程序。其包体积大约为 5MB，显著小于传统的 Electron 应用。Pake 支持 Mac、Windows 和 Linux 等多个平台，提供命令行打包和定制开发的功能，方便开发者进行应用的个性化修改。对于初学者，Pake 提供了多种常用包的示例，帮助用户更直观地体验软件功能。同时，文档中详尽介绍了如何配置环境及进行高级用法。
