# 快速上手

本页只保留当前产品所需的最小入口。**先看 [`current-tested.md`](current-tested.md)**，不要默认继承章节中的旧命令仍适用于最新 DSH。

## 1. 选择一个 pinned recipe

第一条 golden recipe 固定在：

- DSH tag：`dsh-v0.1.5-rc.2`
- upstream commit：`fb2c4b9e698e30edb738bca4cf0618587db7d203`
- recipe：[`recipes/dsh-v0.1.5-rc.2/python-norris-ols/`](../recipes/dsh-v0.1.5-rc.2/python-norris-ols/README.md)

versioned recipe 的目标是复现一个已知契约，而不是追随 `master`。

## 2. DSH 官方入口

Upstream 当前文档给出的 Web 启动形式是：

```bash
npx @deepseek-ai/dsh web
```

当前 CLI 也支持 headless profile：

```bash
dsh --profile headless "任务"
```

为了复现本仓库 recipe，应把 npm 包版本钉死，而不是隐式使用最新版本：

```bash
npx -y @deepseek-ai/dsh@0.1.5-rc.2 web
```

模型配置、workspace 选择和权限提示以 upstream 当前文档为准。

## 3. 先跑 deterministic baseline

不依赖 DSH，也不需要网络：

```bash
cd recipes/dsh-v0.1.5-rc.2/python-norris-ols
python analyze.py
python verify.py
```

只有 `verify.py` 返回 0，才算该统计流程通过。

## 4. 再跑 DSH contract

进入同一 recipe 目录后，按 recipe README 中的 pinned headless invocation 执行。DSH 的任务只负责在明确边界内执行工作流；最终成功判据仍由 `verify.py` 决定。

## 5. 安全边界

DSH 仍是 developer-preview 软件。它可以执行模型生成的命令、加载插件并访问被授予的文件、进程、网络和凭据。优先使用最小权限与可丢弃环境；第三方插件不属于本仓库默认路径。

---

下一步：[当前实测矩阵](current-tested.md) · [Golden recipe](../recipes/dsh-v0.1.5-rc.2/python-norris-ols/README.md)
