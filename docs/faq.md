# FAQ

> 状态：规划中，持续补充。

## 基础

**Q: dsh 和 Claude Code / Codex 什么区别？**
A: dsh 是 DeepSeek AI 开源的 Agent 框架，核心是「一切皆插件」——模型、工具、沙箱、UI、连 agent loop 本身都可替换。适合深度定制与生态扩展；开箱即用选 Claude Code。

**Q: dsh 现在能用于生产吗？**
A: 当前为开发者预览版（本手册基线 0.1.1-rc.2），可能有破坏性变更，生产使用需谨慎评估。

## 安装与启动

**Q: `'pnpm' is not recognized` 怎么办？**
A: `npm i -g pnpm`。dsh 的 plugin 命令是 pnpm 转发器，必须先有 pnpm。

**Q: 端口 3080 被占用？**
A: `netstat -ano | findstr 3080` 找到 PID 后结束进程，或改用其他端口。

## 插件

**Q: 装插件安全吗？**
A: 装插件 = 运行第三方代码。dsh-market 本身可信（白名单源、无遥测），但**它安装的每个第三方插件都要先审源码**，用不持有密钥的测试 profile 试装。

**Q: 插件装不上 / 404？**
A: 依赖版本用 `^0.1.0-rc.6` 线；检查 pnpm 版本与网络。

## 学术场景

**Q: dsh 能读中文文献吗？**
A: 可以，配合 cnki-* 技能（检索/详情/下载/期刊收录）与 agent-reach（多平台调研）。

**Q: Stata 怎么和 dsh 配合？**
A: 用 stata-research-kit 工作流：do-file 规范、日志、表格、复现包，详见第 03 章。
