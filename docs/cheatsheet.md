# dsh 一页速查卡（Cheatsheet）

> 面向学术科研场景。打印 / 收藏，日常用 dsh 不用翻书。
> 基线：Windows 11 / dsh 0.1.1-rc.2 / Node.js 24.x / pnpm 11.24.0（2026-08-26 实测）

## 安装与启动

```bash
npx -y @deepseek-ai/dsh --version      # 免安装运行，先看版本
npm i -g pnpm                          # dsh plugin 依赖 pnpm（必需前置）
npx @deepseek-ai/dsh web               # Web UI → http://127.0.0.1:3080
dsh --profile headless "任务"          # 一次性任务（脚本 / CI 友好）
dsh --dump-config                      # 查看合成后的完整配置
```

## 推理档位（性能关键：工具链任务 90% 时间在思考）

| 档位 | 用途 | 备注 |
|---|---|---|
| `off` | 关闭思考 / 最快 | DeepSeek 官方适配器档位 |
| `high` | 日常默认 | 官方适配器默认 |
| `max` | 复杂推理 / 长链规划 | 官方适配器支持 |

```yaml
# ~/.dsh/settings.yaml
agent-default-model:
  model: deepseek-v4-flash     # 或 deepseek-v4-pro
  reasoningEffort: high        # off / high / max
```

## 核心命令

| 命令 | 用途 |
|---|---|
| `dsh web` | Web UI |
| `dsh --profile headless "任务"` | 一次性任务 |
| `dsh --dump-config` | 看合成配置 |
| `dsh plugin --profile <n> add <pkg>` | 装插件（需 pnpm） |
| `dsh plugin --profile <n> --help` | 插件命令帮助 |

## 插件（装插件 = 运行第三方代码，先审源码）

```bash
dsh plugin --profile web add dshmarket   # 可视化插件市场
dsh plugin --profile test add <pkg>      # 先在测试 profile 试装
```

安全红线：不审源码不装 / 密钥 profile 不试陌生插件 / 不放行未知构建脚本 / Git 源固定 commit。

## 学术科研三连（本手册主场景）

```bash
# 1) 文献调研（CNKI / 多平台）→ 用 agent-reach / cnki-* 技能
# 2) Stata 可复现 → 用 stata-research-kit 工作流（do-file + log + 表格）
# 3) 论文图表 → pydeck 地图 / officecli 文档 / framework-figure-studio-pro
```

## 提示词黄金法则（学术场景）

1. **写验收标准**：`"运行验证通过，输出 p-value 表"` > `"分析数据"`；
2. **给上下文**：数据文件路径、变量含义、目标期刊风格；
3. **一次一个任务**：小闭环比巨型任务可靠（可复现性更高）。

## 缓存省钱（实测命中可到 97%）

- 长任务保持会话延续，别频繁新建会话；
- prompt 前缀保持稳定，别老改配置；
- 看 Web UI 底部「缓存命中 %」指标。

## 排障速查（Windows）

| 现象 | 解法 |
|---|---|
| 端口占用 | `netstat -ano \| findstr 3080` → kill |
| 模型无响应 | 查 settings.yaml + API key |
| `'pnpm' is not recognized` | `npm i -g pnpm`（dsh plugin 前置） |
| 插件装不上 404 | 依赖用 `^0.1.0-rc.6` 线 |
| 长任务崩 | 全局安装（绕 npx）+ 降推理档 |
| 中文路径报错 | 项目目录避免非 ASCII 路径 |

## 术语速记

`profile` 形态 · `bundle` 插件组 · `host/client 半` 服务端/界面 · `扩展点` 官方钩子 · `waterfall` 请求链 · `compaction` 上下文压缩 · `headless` 一次性 CLI · `locations` 产物路径 · `dsh.bundle` 插件清单声明

---

完整章节见 [dsh-research-handbook](https://github.com/SIMON-WORLD/dsh-research-handbook) 各 docs/ 章节。
