# Current-tested matrix

本页只记录**实际核验过**的事实。它是一个小型验证矩阵，不是对所有 DSH 平台/模型/操作系统的兼容性承诺。

Snapshot date: **2026-09-11**

| DSH pin | Upstream commit | Verification environment | Verified here | Live DSH execution |
|---|---|---|---|---|
| `dsh-v0.1.5-rc.2` | `fb2c4b9e698e30edb738bca4cf0618587db7d203` | Deterministic baseline: Linux x86_64, Python 3.13.5. Live DSH: GitHub-hosted Ubuntu 24.04.5, Linux `6.17.0-1022-azure` x86_64, Node `v22.19.0`, npm `10.9.3`, Python `3.13.15`. | NIST Norris local data snapshot; stdlib OLS; certified-value verifier; negative mismatch test; pinned DSH headless execution. | **Verified 2026-09-11 for recipe 001 only.** Real `@deepseek-ai/dsh@0.1.5-rc.2 --profile headless` completed with exit `0`; oracle files were unchanged; an independent post-DSH `python verify.py` passed. Evidence: [Issue #3](https://github.com/SIMON-WORLD/dsh-research-handbook/issues/3), [Actions run 34607136510](https://github.com/SIMON-WORLD/dsh-research-handbook/actions/runs/34607136510). |

## Upstream truth used for this snapshot

- Latest pinned recipe release: `dsh-v0.1.5-rc.2`.
- The tag resolves to commit `fb2c4b9e698e30edb738bca4cf0618587db7d203`.
- Upstream documents `dsh --profile headless "job"` as a supported CLI entry mode.
- Upstream root documentation continues to label DeepSeek Harness as **developer preview** with compatibility-breaking changes expected.
- Upstream `SAFETY.md` states that DSH has not undergone a security audit and must not be treated as secure or production-ready.

## Local deterministic verification evidence

Executed in the recipe-creation mission environment:

```text
Python 3.13.5
Linux 6.18.35 x86_64

python analyze.py
-> exit 0

python verify.py
-> PASS: NIST Norris certified values matched.
-> exit 0

python verify.py bad-result.json
-> FAIL
-> slope mismatch detected
-> exit 1
```

The deliberately corrupted result changed the fitted slope by `+0.01`; this demonstrates that the verifier rejects a known-bad artifact rather than merely checking file existence.

## Live DSH execution evidence

On 2026-09-11, GitHub Actions run `34607136510` exercised the exact pinned recipe 001 headless contract with a repository secret supplied only to the credential/runtime steps.

```text
@deepseek-ai/dsh resolved: 0.1.5-rc.2
DSH --version:              0.1.5-rc.2
DSH headless exit:          0
post-run python verify.py:  PASS / exit 0
```

Before and after the DSH session, SHA-256 values for `data/norris.csv`, `expected.json`, and `verify.py` were identical. This verification is intentionally narrow: it establishes the pinned Norris recipe contract on the recorded GitHub-hosted Linux environment, not general DSH compatibility or production safety.

## Maintenance rule

Add a new row when a new DSH release/environment is actually exercised. Do not overwrite historical recipe pins to make them appear current. Factual errata may be corrected with an explicit note.
