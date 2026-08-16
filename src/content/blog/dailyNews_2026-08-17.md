---
title: "Daily News #2026-08-17"
date: "2026-08-17 08:00:00"
description: >
  一份数据，多种用途：Spotify 用 RAP 打通分析与在线服务 SwiftUI concentricCornerRadii（iOS 27）：GeometryProxy 同心圆角完全指南 SwiftUI 点击失效的诡异案例：双向 ScrollView 导致按钮失灵
tags:
- "数据湖"
- "iOS 27"
- "Spotify"
- "Parquet"
- "iOS开发"
- "UI设计"
- "存储架构"
- "调试"
- "SwiftUI"
- "点查询"
- "API"
- "GeometryReader"
- "hit-testing"
- "ScrollView"

---

> - 一份数据，多种用途：Spotify 用 RAP 打通分析与在线服务
> - SwiftUI concentricCornerRadii（iOS 27）：GeometryProxy 同心圆角完全指南
> - SwiftUI 点击失效的诡异案例：双向 ScrollView 导致按钮失灵

## 📥 Tech News

### [一份数据，多种用途：Spotify 用 RAP 打通分析与在线服务](https://www.infoq.cn/article/iRjDa2ayZ9KLUtWylQZl)

来源：InfoQ 推荐

发布时间：2026-08-16 10:00:00
![](https://static001.infoq.cn/resource/image/23/ec/23da3c9f783068d47a23e05491b0d8ec.png)
**背景/问题**：现代数据湖已成为分析与 AI 工作负载的中央存储，但 Trino、BigQuery 等引擎面向扫描优化，基于键的单条记录检索效率极低；Spotify 在 Bigtable 存有 PB 级在线数据、数据湖存有 EB 级数据，向服务库大规模复制数据的成本日益失控。

**核心观点/方案**：RAP 在 Parquet 之上增加外部索引层，将查询键直接映射到文件及行位置，查询先经索引解析再发起定向范围读取；索引构建器随 Iceberg 表写入生成仅追加片段，无需修改不可变文件。配合按键排序、记录聚簇、交错值列、覆盖索引及免重写文件的二级索引等布局优化，部分点查询仅需一次 KB 级范围读取即可完成。

**结论/价值**：一套数据同时支撑分析、ML 流水线与低延迟在线服务，消除重复存储系统，是开放湖格式向操作型负载延伸的代表性实践，与 Google 的 Iceberg 湖仓路线形成互补。适合数据平台与存储架构师深入研究，落地时需评估索引维护成本与存储布局改造代价。

## 💾 Daily Dev

### [SwiftUI concentricCornerRadii（iOS 27）：GeometryProxy 同心圆角完全指南](https://www.sagarunagar.com/blog/swiftui-concentriccornerradii-ios-27/)

来源：iOS Development News - Telegram Channel

发布时间：2026-08-16 15:12:27
![](https://cdn4.telesco.pe/file/WdJtB8su9gQhPi6vCTvsCkr1s1Umq_-eUkP79FnwjREkRr28bNI99v0GKu4oWX--pXN3k2Un0v7LFMUoUGForopRXPAbknQLOjLvvCQbKwTDgS6nXEWqjrsMnqkkh3ppews0j5xzIWMD1fXx7ZOxfAZiDJdWKWqPaJtYW71PnOde1aSxW_v0HN2fBADLlbnkb6WN17KjrPsQ2M5SnkDnlq46ca5g79nwetwuWI3IZcqySpuUiVskQYK0SUpPutUPAK2KubzsRTnlErmRS85s0R5-gRgDfAcrbZVjaq5-K0Tc1OFm357KcCzgQ3FD0s_-PIEFj6XeiB01NO4wscxEYA.jpg)
**背景/问题**：在 iOS 27 之前，想让自定义绘制的视图（如 Canvas、Path）与外层容器的圆角视觉对齐，只能靠硬编码圆角半径、嵌套 RoundedRectangle 或 ContainerRelativeShape 近似实现；一旦容器圆角、内边距或设备布局变化，硬编码值立即失效，且无法直接拿到计算结果复用。

**核心观点/方案**：iOS 27 为 GeometryProxy 新增 concentricCornerRadii 属性和 concentricCornerRadii(in:) 方法，直接暴露 SwiftUI 基于容器形状（需配合 containerShape 声明）计算出的同心圆角半径。文章讲清了几何原理（内圆角 ≈ 容器圆角减去内角到容器角的距离，如 48-12=36pt）、属性与方法的分工——方法接受本地坐标系 CGRect，可对子区域分别查询——并给出与 Canvas、Path、动画配合的完整代码示例；返回值为可选的 RectangleCornerRadii，四个角半径可各不相同。

**结论/价值**：这是面向全新 API 的系统性教程，代码可直接落地，适合从事自定义绘制与组件开发的 SwiftUI 工程师升级适配时精读。局限在于 API 过新，社区踩坑经验尚少，边界行为（如返回 nil 的具体场景）需读者自行验证。

### [SwiftUI 点击失效的诡异案例：双向 ScrollView 导致按钮失灵](https://damian.fyi/swift/2026/08/16/curious-case-of-missing-click.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-08-16 16:47:12
![](https://cdn4.telesco.pe/file/qSl5qGCjYgNei83HSCtK7ETY48MQQ5tQJmiK7pgh7tcDngXznkaDA0q0FKrRapi-L8K072B3x6wt8nuo-_bqFy6ouN2TVbraGK3Pg6AmC0WN2Jl4TyFag0pttdDznVO0LKJysa_kHPq8RUJ45PQzt113CZXnMvHZ2oLlMEWCpprp3BtSbSJky7Uf8IBkJN3x8rDaIP-DJWlbeNRwPPG3gLhAZ3T0E7OaUBvO8FjlktUVcC8i_u76PMoZcADtDTXyW4M8xeIsKpcab1nz3yGc0wJG8Xyx38MuGno3nIOlkBisUswYhbrbEs-DeAb2Fptco0dSjoqFF3hXaZWrjb5vkQ.jpg)
**背景/问题**：作者在开发 Ploze 应用的日历视图时，遇到 SwiftUI 中 Button 点击几次后突然失效的诡异问题——点击单元格后回调不再触发，滚动一下视图又能恢复，但几次点击后再度失灵，逐行注释代码排查也找不到原因。

**核心观点/方案**：将 LazyVStack 换成普通 VStack 可让问题消失，但牺牲了懒加载性能，并非正解；最终发现真正的触发点是 ScrollView 的双向滚动轴——把 ScrollView([.horizontal, .vertical]) 改为仅 [.vertical] 后问题彻底解决，且由于已用 GeometryReader 动态计算单元格尺寸，水平滚动本就不再需要。

**结论/价值**：这是一个典型的“症状消除但根因不明”的实战调试记录，StackOverflow 上有类似问题同样缺乏解释。对遇到 SwiftUI 点击失效的开发者有直接参考价值，可快速尝试该 workaround；但文章未剖析横向滚动与 hit-testing 失效的底层机制，方案通用性有待验证。适合中高级 SwiftUI 开发者作为排错线索收藏。
