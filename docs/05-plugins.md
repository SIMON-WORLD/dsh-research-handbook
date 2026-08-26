# 学术向精选插件

> 状态：规划中。以下基于生态调研初筛，**待逐个实测后标注「已实测」**。

## 插件安装前置

```bash
npm i -g pnpm                        # 前置依赖
dsh plugin --profile web add dshmarket   # 可视化插件市场
dsh plugin --profile test add <pkg>      # 先在测试 profile 试装
```

## 初筛名单（从 awesome-dsh-plugin 21 大类中挑学术相关）

| 类别 | 候选插件 | 用途 | 状态 |
|---|---|---|---|
| 上下文管理 | dsh-context | 上下文洞察 / 压缩 | 待实测 |
| 视觉 | modlens | 给纯文本 Agent 加视觉（看图） | 待实测 |
| 记忆 | 记忆类插件（77+ 候选） | 跨会话记忆 | 待实测 |
| 跨会话引用 | dsh-cue-plugin | cue 引用 | 待实测 |
| 会话管理 | dph-taskboard | 侧边栏任务板 | 待实测 |
| 工作流 | dsh-agent-teams | Agent 团队 | 待实测 |

## 安全红线（务必先读）

装插件 = 运行第三方代码。**先审源码**：README、package.json、cordis.patch.yml、src/。用不持有密钥的测试 profile 试装。

---

[上一章：论文图表](04-figures-maps.md) · [下一章：Windows 排坑实录](06-windows-troubleshooting.md)
