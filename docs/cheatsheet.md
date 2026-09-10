# dsh-research-handbook 一页速查

> 这是 **versioned reproducibility cookbook** 的速查页，不是“最新 DSH 全功能手册”。实际通过状态以 [`current-tested.md`](current-tested.md) 为准。

## 当前 recipe pin

```text
DSH tag:    dsh-v0.1.5-rc.2
Commit:     fb2c4b9e698e30edb738bca4cf0618587db7d203
Golden:     recipes/dsh-v0.1.5-rc.2/python-norris-ols/
```

## 官方 CLI 入口

```bash
npx @deepseek-ai/dsh web
dsh --profile headless "任务"
dsh --dump-config
dsh plugin --profile <name> <pnpm args>
```

复现 recipe 时显式 pin npm 版本：

```bash
npx -y @deepseek-ai/dsh@0.1.5-rc.2 web
```

## Golden recipe 本地验收

```bash
cd recipes/dsh-v0.1.5-rc.2/python-norris-ols
python analyze.py
python verify.py
```

成功判据：`verify.py` 输出 `PASS` 且退出码为 `0`。

## DSH headless 契约

在 recipe 目录运行：

```bash
npx -y @deepseek-ai/dsh@0.1.5-rc.2 --profile headless \
  "Use only local files in this workspace. Run python analyze.py, then python verify.py. Do not edit data/norris.csv, expected.json, or verify.py. The task succeeds only if verify.py exits 0. Report result.json and the verifier status."
```

## DeepSeek adapter reasoningEffort

当前 upstream DeepSeek adapter 文档列出的取值为：

```text
off | low | high | max
```

不要把旧 cheatsheet 中的性能/成本百分比或特定推荐档位当作已验证事实。

## 安全与生态

- DSH 是 developer preview；compatibility-breaking changes 是官方明确预期。
- 最小权限运行，敏感凭据与不可信数据隔离。
- official DSH primitives first。
- 第三方插件：未单独 provenance-check，不进入 recipe 默认依赖。

## 旧章节

早期 `docs/01-*` 至 `docs/07-*` 与 FAQ 含规划稿和 `0.1.1-rc.2` 时期内容。除非 current-tested matrix 或某条 versioned recipe 明确覆盖，否则一律按 **legacy / unverified** 处理。
