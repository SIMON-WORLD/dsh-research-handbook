# 快速上手（五分钟）

> 本文所有命令在 Windows 11 + dsh 0.1.1-rc.2 + Node.js 24.13.0 实测通过（2026-08-26）。

## 1. 安装

```bash
# 需要 Node.js（推荐 22.19.x 或 24+）
npx -y @deepseek-ai/dsh --version     # 免安装验证版本
```

> 注意：若要用 `dsh plugin` 装插件，需要额外安装 pnpm：
> ```bash
> npm i -g pnpm
> ```

## 2. 启动 Web UI

```bash
npx @deepseek-ai/dsh web
# → http://127.0.0.1:3080
```

启动后：

1. **Settings → Models**：填入 DeepSeek API Key（或配置其他 Provider）；
2. **Choose workspace**：选择项目目录；
3. 开始第一个会话。

## 3. 第一次任务

发给 Agent：

> 总结这个仓库，列出主要包。

Agent 可以读/写工作区文件、运行命令、委托子任务、维护计划。

## 4. 双模式

| 模式 | 命令 | 用途 |
|---|---|---|
| Web UI | `dsh web` | 交互式对话 |
| Headless | `dsh --profile headless "任务"` | 脚本 / CI 一次性任务 |

## 5. 推理档位

`off`（最快）/ `high`（默认）/ `max`（最强）。学术任务建议：简单检索用 `high`，复杂实证分析用 `max`。

---

下一步：[学术研究工作流总览](01-academic-workflow.md)
