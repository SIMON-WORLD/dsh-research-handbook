# dsh-research-handbook

> **DeepSeek Harness × 学术科研中文手册** —— 用 dsh 做可复现的学术研究：文献调研、Stata 实证、论文图表、精选插件与 Windows 排坑。

中文 · [English](README.en.md)（规划中）

DeepSeek Harness（`dsh`）是 DeepSeek AI 开源的 Agent 框架，核心哲学是 **「一切皆插件」**（Everything is a Plugin）。本手册聚焦一个垂直场景：**学术科研**——从文献调研到 Stata 可复现实证，再到论文图表与投稿，每一步都用 dsh 跑通，并给出可复制、可验证的命令与工作流。

> ⚠️ dsh 当前为开发者预览版（本手册实测基线 `0.1.1-rc.2`），API 可能变动；请以官方仓库 [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) 为准。

## 快速开始

```bash
npx @deepseek-ai/dsh web      # Web UI → http://127.0.0.1:3080
dsh --profile headless "任务"  # 一次性任务（脚本/CI 友好）
```

## 目录

- [快速上手（五分钟）](docs/00-quickstart.md)
- [学术研究工作流总览](docs/01-academic-workflow.md)
- [文献调研：CNKI 与多平台检索](docs/02-literature-review.md)
- [Stata 可复现实证](docs/03-stata-reproducible.md)
- [论文图表：地图 / 文档 / 框架图](docs/04-figures-maps.md)
- [学术向精选插件](docs/05-plugins.md)
- [Windows 排坑实录](docs/06-windows-troubleshooting.md)
- [缓存与成本调优](docs/07-cost-tuning.md)
- [一页速查卡](docs/cheatsheet.md)
- [常见问题 FAQ](docs/faq.md)

## 在线阅读

GitHub Pages：<https://simon-world.github.io/dsh-research-handbook/>（随 main 自动构建）

## 内容准则

- **实测优先**：每章命令均在本机 Windows + dsh 0.1.1-rc.2 环境验证；
- **可复现**：脚本与配置可复制运行，注明验证时间与版本；
- **中文优先**：面向中文科研用户，术语保留英文原文。

## 贡献

欢迎 Issue / PR。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

- 文档与教程文本：[CC BY 4.0](LICENSE)
- 示例代码：MIT（见各文件头部说明）

## 致谢与参考

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) — 官方仓库
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) — dsh 通用白皮书（本手册的生态参照）
- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) — 插件精选列表
