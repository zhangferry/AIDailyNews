---
title: "Daily News #2026-09-15"
date: "2026-09-15 08:00:00"
description: >
  刘震云对话马毅：人想不到的作品，AI 模仿不了 FreeCORE：社区驱动的 TrueNAS CORE 分支，坚守 FreeBSD 生态的存储系统生命线 Exploring map_directory in Bazel 9
tags:
- "开源治理"
- "创造力"
- "OpenZFS"
- "FreeBSD"
- "教育"
- "存储系统"
- "AI"
- "构建系统"
- "map_directory"
- "TrueNAS"
- "规则开发"
- "人文思考"
- "Bazel"
- "新质生产力"
- "动态依赖"

---

> - 刘震云对话马毅：人想不到的作品，AI 模仿不了
> - FreeCORE：社区驱动的 TrueNAS CORE 分支，坚守 FreeBSD 生态的存储系统生命线
> - Exploring map_directory in Bazel 9

## 📥 Tech News

### [刘震云对话马毅：人想不到的作品，AI 模仿不了](https://www.bestblogs.dev/article/00f31d8e54?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item)

来源：BestBlogs.dev - 精选文章

发布时间：2026-09-13 10:15:00
![](https://image.jido.dev/20260527130453_c4b7ab1.jpeg)
**背景/问题**：2026 外滩大会上，作家刘震云与香港大学教授马毅围绕 AI 对创造、教育和人际关系的冲击展开对话，回应大众对“AI 是否会取代人类”的普遍焦虑。

**核心观点/方案**：刘震云以自身为例指出，AI 可以复制他的声音和口型，却写不出他尚未想到的作品——AI 擅长处理过去与现在的共性知识，但缺乏个性化创造；马毅从教育视角补充，AI 时代的真正挑战是帮助学生找到个人价值与社会共性之间的平衡，用 AI 放大个人能力而非被其取代。深层次的情感交流（如朋友间的谈心、请客吃饭）同样是 AI 无法替代的领域。

**结论/价值**：两人均视 AI 为新质生产力而非洪水猛兽，核心命题是重新定义人在 AI 时代的角色与关系。对话生动、观点通俗，适合关注 AI 人文面向与教育变革的读者；但整体属思想漫谈，缺乏严谨论证与技术细节支撑。

### [FreeCORE：社区驱动的 TrueNAS CORE 分支，坚守 FreeBSD 生态的存储系统生命线](https://www.infoq.cn/article/TDav5ojS854dZKyfJmhI)

来源：InfoQ 推荐

发布时间：2026-09-13 16:00:00
![](https://static001.infoq.cn/resource/image/79/09/792f5243a3de1789529bdea79519a209.jpg)
**背景/问题**：TrueNAS CORE 长期是开源存储领域的公认标准，但维护方 iXsystems 将工程资源全面转向基于 Debian Linux 的 TrueNAS SCALE，坚守 FreeBSD 生态的存量用户面临架构被弃用的困境。

**核心观点/方案**：社区衍生项目 FreeCORE 将 TrueNAS CORE 13.3 基线就地升级至 FreeBSD 15.0，恢复了上游已标记废弃的 Jails 容器、原生插件与 bhyve 虚拟化生态。文章同时剖析了 Jails 相比 LXC/Docker 更强的内核级隔离边界、OpenZFS 原生加密缺乏上游维护者的隐患，以及围绕上游移除构建脚本引发的开源治理争议。

**结论/价值**：FreeCORE 为 FreeBSD 忠实用户提供了关键生命线，但目前仅由一名维护者主导并大量依赖 AI 编码代理开发，长期可持续性存疑。适合存储管理员、NAS 运维者和关注开源治理的读者参考，但用于企业关键任务环境需谨慎评估单点维护风险。

## 💾 Daily Dev

### [Exploring map_directory in Bazel 9](https://adincebic.com/2026/09/13/exploring-mapdirectory-in-bazel.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-09-14 00:12:36
![](https://cdn4.telesco.pe/file/Mh8yQsfAiYQ8GzOymw7UgBVYTbTcxSbajp2XXd5SSljsvp3H8sIChEUaDX5PXKYWL-jbbQzRUuwysaITlQ0Nm9OFyP-rkpmwTgvl1OAKwY2fBH0iHSJ_R9OCPHxSQjgRwaT0q3_iceMuzvr4OoC1fZfMXfRQgI_9A7S_DCvx7J7c_3PWILAfSpVzYkD_jzl431bWFe5dA-0n4D0pAfp27v78DdWQY4cQ7Bus0gAB5zJdhumSzMcD7WL16C09KdtT3DF8s15DYlNq5ULtrpN3rBkwOA_Li6JMAWOMwbBtAOoVezF5rnphtej0wALaHq4Y_odeHYPob6PVsh8_t9icbA.jpg)
**背景/问题**：Bazel 的核心设计哲学是显式声明、在分析阶段提前注册所有 action，这是增量构建与可复现性的根基。但当需要根据生成目录的实际内容决定后续 action（例如对目录中每个文件执行独立操作）时，传统 API 无法支持，开发者只能依赖各种 hack 绕过限制。

**核心观点/方案**：文章介绍 Bazel 9 新引入的 map_directory API：调用时传入 input_directories、output_directories 与 tools，并将自定义函数作为 implementation。该函数不在常规分析阶段运行，而是推迟到执行阶段——当目录内容已知后，Bazel 调用它遍历子文件并为每个文件注册独立 action。文中以「生成若干文件后逐个复制」为例，给出完整可运行的规则代码，演示了每个 action 仅依赖自身输入文件与工具的细粒度依赖关系。

**结论/价值**：map_directory 为 Bazel 构建引入了受控的动态性，使此前需要相当多创造性 hack 的场景变成原生能力，尽管功能仍较为受限。适合编写自定义 Bazel 规则、维护复杂构建管线的工程师阅读；示例偏简单，实际落地建议结合官方文档与 GitHub 上关于动态依赖的讨论进一步探索。
