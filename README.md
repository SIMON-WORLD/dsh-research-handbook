# dsh-research-handbook

> **Versioned Research Reproducibility Cookbook for DeepSeek Harness (DSH)** —— 面向 Python / R / Stata 科研工作流，用版本钉死、可本地验收的 recipe 记录“什么在什么版本上真的跑得通”。

本仓库已经从“广覆盖的 DSH 学术手册”调整为 **可复现科研 cookbook**。核心产物不是概念性章节，而是可审计的 versioned recipe：固定 DSH 版本、输入数据、执行步骤、预期产物与 deterministic acceptance check。

> ⚠️ DeepSeek Harness 官方仍将 DSH 标记为 **developer preview**，并明确提示会有 compatibility-breaking changes。不要把本仓库的 recipe 当作生产安全保证；运行 DSH 前应阅读 upstream `SAFETY.md`，并采用最小权限、可丢弃环境与明确的文件/凭据边界。

## 当前已验证

当前验证快照见 [`docs/current-tested.md`](docs/current-tested.md)。

第一条 golden recipe：

- [`dsh-v0.1.5-rc.2 / Python / NIST Norris OLS`](recipes/dsh-v0.1.5-rc.2/python-norris-ols/README.md)
  - 公开 NIST StRD 数据；
  - Python 标准库，无第三方 Python 包；
  - 本地离线分析；
  - 用 NIST certified values 做 deterministic verifier。

## 维护模型

- **Immutable versioned recipes**：recipe 以 DSH release/tag 为版本边界。历史 recipe 不因 upstream 新版本而“静默升级”；除事实性勘误外保持不可变。
- **Small current-tested matrix**：只记录实际执行过的组合，不把“看起来应该能跑”写成已验证。
- **Official primitives first**：优先使用 DSH 官方 CLI、profiles、内置工具与官方文档。
- **Third-party provenance required**：第三方插件或外部 agent 工具只有在单独完成 provenance、安全边界和版本核验后才能进入推荐路径。
- **Acceptance over prose**：模型文字不是成功判据。recipe 必须有机器可判定的验收步骤。

## 快速入口

- [快速上手](docs/00-quickstart.md)
- [当前实测矩阵](docs/current-tested.md)
- [一页速查](docs/cheatsheet.md)
- [Golden recipe: NIST Norris OLS](recipes/dsh-v0.1.5-rc.2/python-norris-ols/README.md)

## 继承内容状态

`docs/01-academic-workflow.md` 至 `docs/07-cost-tuning.md`、`docs/faq.md` 等内容来自项目早期 handbook 阶段，其中多处仍是规划稿、候选生态信息或基于 `dsh 0.1.1-rc.2` 的旧快照。

**除非某一条内容被 `docs/current-tested.md` 或某个 versioned recipe 明确列为已验证，否则不要把这些继承章节视为当前 DSH 的可执行契约。**

这些旧内容暂时保留作为素材库，本轮不会一次性重写；后续只在有明确 recipe/vertical mission 时逐步迁移、核验或淘汰。

## GitHub Pages

<https://simon-world.github.io/dsh-research-handbook/>

## 贡献原则

欢迎 Issue / PR。新增 recipe 应提供：版本 pin、数据/输入 provenance、最小依赖、可重复执行步骤、machine-readable output 和 deterministic acceptance check。

现有贡献说明仍包含早期 handbook 约定，后续会在独立 bounded mission 中更新；在此之前，以本 README 与 [`docs/current-tested.md`](docs/current-tested.md) 的产品/验证边界为准。

## 许可证

- 文档与教程文本：[CC BY 4.0](LICENSE)
- 示例代码：按文件内说明；新增 recipe 应明确来源与许可/引用要求。

## 上游

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness documentation](https://deepseek-harness.github.io/deepseek-harness/)
