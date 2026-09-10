# Current-tested matrix

本页只记录**实际核验过**的事实。它是一个小型验证矩阵，不是对所有 DSH 平台/模型/操作系统的兼容性承诺。

Snapshot date: **2026-09-10**

| DSH pin | Upstream commit | Verification environment | Verified here | Live DSH execution |
|---|---|---|---|---|
| `dsh-v0.1.5-rc.2` | `fb2c4b9e698e30edb738bca4cf0618587db7d203` | Linux x86_64; Python 3.13.5 | NIST Norris local data snapshot; stdlib OLS; certified-value verifier; negative mismatch test | **Not verified in this mission environment.** A pinned `npx -y @deepseek-ai/dsh@0.1.5-rc.2 --version` attempt did not complete before the execution environment timed out, so no DSH runtime pass is claimed. |

## Upstream truth used for this snapshot

- Latest pinned recipe release: `dsh-v0.1.5-rc.2`.
- The tag resolves to commit `fb2c4b9e698e30edb738bca4cf0618587db7d203`.
- Upstream documents `dsh --profile headless "job"` as a supported CLI entry mode.
- Upstream root documentation continues to label DeepSeek Harness as **developer preview** with compatibility-breaking changes expected.
- Upstream `SAFETY.md` states that DSH has not undergone a security audit and must not be treated as secure or production-ready.

## Local deterministic verification evidence

Executed in this mission environment:

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

## Maintenance rule

Add a new row when a new DSH release/environment is actually exercised. Do not overwrite historical recipe pins to make them appear current. Factual errata may be corrected with an explicit note.
