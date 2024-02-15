---
title: "iOS Daily News #5 (2024-02-16)"
date: "2024-02-16 00:05:11"
author: 摸鱼仔
description: "🌟 XcodeGen：告别 Xcode 项目文件，拥抱自动化！
🌟 Black：不妥协的Python代码格式化工具
🌟 Vapor：Swift 的 HTTP Web 框架
✨ Ibis：用于数据整理的轻量级通用接口"
tags: 
- '数据整理'
- 'Web 框架'
- '项目生成'
- 'Swift'
- '代码格式化'
- 'Xcode'
- 'Python'

---

> * 🌟 XcodeGen：告别 Xcode 项目文件，拥抱自动化！
> * 🌟 Black：不妥协的Python代码格式化工具
> * 🌟 Vapor：Swift 的 HTTP Web 框架
> * ✨ Ibis：用于数据整理的轻量级通用接口

## Daily News## Daily Code
### [🌟 XcodeGen：告别 Xcode 项目文件，拥抱自动化！](https://github.com/yonaskolb/XcodeGen)
 
XcodeGen 是一款用 Swift 编写的命令行工具，它使用文件夹结构和项目规范生成 Xcode 项目。项目规范是一个 YAML 或 JSON 文件，用于定义目标、配置、方案、自定义构建设置和许多其他选项。所有源目录都会自动解析并适当引用，同时保留文件夹结构。在许多地方都使用了明智的默认值，因此您只需自定义所需内容即可。还可以使用更高级的功能定义非常复杂项目。

- ✅ 按需生成项目，并将 `.xcodeproj` 从 git 中移除，这意味着 **不再有合并冲突**！
- ✅ Xcode 中的分组和文件始终 **与** 磁盘上的目录同步
- ✅ **配置** 项目非常容易，且具有可读性和 git 友好性
- ✅ 轻松 **复制和粘贴** 文件和目录，而无需在 Xcode 中编辑任何内容
- ✅ 使用 **构建设置组** 在多个目标之间共享构建设置
- ✅ 自动为 **不同环境**（如测试和生产）生成方案
- ✅ 轻松 **创建新项目**，具有复杂的设置，按需创建，而无需使用 Xcode
- ✅ 在任何地方生成，包括 **CI**
- ✅ 分发规范到多个文件，以便于 **共享** 和覆盖
- ✅ 轻松创建 **多平台** 框架
- ✅ 集成 **Carthage** 框架，无需任何工作
- ✅ 导出 **依赖关系图**，以便在 [Graphviz](https://www.graphviz.org) 中查看

### [🌟 Black：不妥协的Python代码格式化工具](https://github.com/psf/black)
 
Black是一款Python代码格式化工具，它以不妥协的风格对代码进行格式化，帮助开发者节省时间和精力，专注于更重要的内容。Black的格式化风格符合PEP 8规范，并提供了一致的代码格式，简化了代码审查流程。它还具有强大的测试套件和自动格式化功能，确保代码格式的准确性和一致性。Black已成功应用于众多知名开源项目和组织中，包括pytest、Django、SQLAlchemy和Facebook。

### [🌟 Vapor：Swift 的 HTTP Web 框架](https://github.com/vapor/vapor)
 
Vapor 是一个用于 Swift 的 HTTP Web 框架。它为您的下一个网站、API 或云项目提供了一个极具表现力且易于使用的基础。

### [✨ Ibis：用于数据整理的轻量级通用接口](https://github.com/ibis-project/ibis)
 
Ibis是一个Python库，它为数据整理提供了一个轻量级的通用接口。它帮助Python用户探索和转换任何规模的数据，无论存储在哪里。Ibis有三个主要组成部分：
1. Python的数据框API。
2. 与20多个查询引擎的接口。
3. 延迟执行。
Ibis使用延迟执行，因此代码的执行被推送到查询引擎。用户可以以其后端的速度执行，而不是其本地计算机的速度。
