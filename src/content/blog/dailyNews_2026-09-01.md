---
title: "Daily News #2026-09-01"
date: "2026-09-01 08:00:00"
description: >
  如何减少多个 Git Worktree 下 Bazel 的磁盘占用
tags:
- "Git Worktrees"
- "工程效率"
- "bb-clientd"
- "Bazel"
- "构建缓存"

---

> - 如何减少多个 Git Worktree 下 Bazel 的磁盘占用

## 💾 Daily Dev

### [如何减少多个 Git Worktree 下 Bazel 的磁盘占用](https://adincebic.com/2026/08/30/how-to-reduce-bazel-disk.html)

来源：iOS Development News - Telegram Channel

发布时间：2026-08-31 01:02:32
![](https://cdn4.telesco.pe/file/hk7ycUKZO3HRQPUCfWi6iJ-5jVkNzAsVAAsURIKT9n6QDavUaKgrLfOaRjlANiATPNnMZjCoWTmjNIJuUGfOENQO-ik6MYhTDGiihFxOBVuOTE2MEDvO3dyjT41HcjDafYyCg8EGjNUs4C1Dd4sClP0WE1F1Hk-xE39Ruf3f8jLYhgmwsNm5bNUZXBwsz6MWXf9hxBqvpaEDWW8c3gMmd842ohJilSdbF77qSenziMhtH_1G4KMQPjCX7LGVhjkg-2ewCdNMgd2issnjPN03qEqX8gEzj6L59sBsnx5d1bpFhlntqC9mLXm2xZLMSDl-ewQPoA-_5RmIkKV1weBBBw.jpg)
**背景/问题**：随着编码智能体的普及，越来越多工程师开始使用 Git worktree 并行工作，这意味着同时存在多个 Bazel output base。大型项目的 Bazel 缓存本就体积惊人，多个输出基各自维护独立副本后，磁盘空间问题被进一步放大，手动删除和垃圾回收只能治标。

**核心观点/方案**：文章推荐用 bb-clientd 守护进程解决。它可作为 Bazel 的本地远程缓存与代理，并实现了 Bazel 7.2 引入的 Output Service 协议，通过虚拟文件系统（Linux 用 FUSE、macOS 用 NFSv4）接管输出树，文件只在被实际访问时才惰性物化。配合内容寻址缓存，多个 output base 可共享同一份内容而非重复存储。文中给出可直接使用的 .bazelrc 配置片段，并提醒使用 rules_swift 且非 Xcode 工具链时需启用 swift.module_map_home_is_cwd 特性，以适配虚拟化输出树下的头文件路径。

**结论/价值**：该方案能为多 worktree 用户节省数 GB 磁盘空间，且社区讨论很少，属于被低估的实践。适合大型 monorepo 的 Bazel 重度用户和受磁盘空间困扰的 iOS/后端工程师参考，局限在于依赖实验性的 Output Service 协议，配置有一定门槛。
