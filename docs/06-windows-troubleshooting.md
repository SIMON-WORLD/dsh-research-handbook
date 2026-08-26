# Windows 排坑实录

> 状态：规划中。dsh 生态公认第一痛点就是 Windows（中文路径 / koffi / 端口 / 子进程），本机正是 Windows，逐条实测后补全。

## 已实测的坑

| # | 现象 | 根因 | 解法 | 状态 |
|---|---|---|---|---|
| 1 | `'pnpm' is not recognized` | dsh plugin 是 pnpm 转发器，PATH 无 pnpm | `npm i -g pnpm` | ✅ 已实测（2026-08-26） |
| 2 | `dsh plugin --profile web --help` 报缺 `--profile` | 帮助信息要求完整参数 | 写全 `--profile web --help` | ✅ 已实测 |
| 3 | 沙箱内 gh/curl/npm 直连失败 | 网络/子进程限制 | node 直连 GitHub API 绕过 | ✅ 已实测 |

## 待补（社区高频，尚未本机复现）

- 中文路径导致插件构建失败（15+ 帖同根因）；
- koffi 原生模块安装问题；
- 3080 端口被占用；
- 长任务崩溃（建议全局安装绕 npx + 降推理档）。

## 社区参考

- [deepseek-ai/deepseek-harness discussions](https://github.com/deepseek-ai/deepseek-harness/discussions)（Windows 相关帖）
- [dsh-handbook 第 12 章：已知不足与边界](https://github.com/Electricitysheep/dsh-handbook)

---

[上一章：学术向精选插件](05-plugins.md) · [下一章：缓存与成本调优](07-cost-tuning.md)
