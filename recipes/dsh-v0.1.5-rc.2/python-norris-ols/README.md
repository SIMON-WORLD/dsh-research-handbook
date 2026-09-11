# Golden recipe: NIST Norris ozone calibration with OLS

Recipe ID: `dsh-v0.1.5-rc.2/python-norris-ols`

This is the first immutable golden recipe in the cookbook. It is deliberately small: one public NIST dataset, one linear model, Python standard library only, and a deterministic verifier against NIST certified values.

## Research question

Given NIST's ozone-monitor calibration observations, fit the linear model

```text
y = beta0 + beta1 * x + error
```

where:

- `x` is NIST's ozone concentration measurement;
- `y` is the customer's ozone concentration measurement.

The goal is not to discover a novel scientific result. The goal is to demonstrate a reproducible research path whose numerical result can be checked independently of model prose.

## Provenance

Source: NIST/ITL Statistical Reference Datasets (StRD), dataset **Norris**.

- Dataset page: <https://www.itl.nist.gov/div898/strd/lls/data/Norris.shtml>
- Original ASCII file: <https://www.itl.nist.gov/div898/strd/lls/data/LINKS/DATA/Norris.dat>
- Certified values: <https://www.itl.nist.gov/div898/strd/lls/data/LINKS/v-Norris.shtml>
- Reference recorded by NIST: Norris, J., NIST, *Calibration of Ozone Monitors*.

`data/norris.csv` is a local 36-observation snapshot transcribed from the NIST ASCII data file so that acceptance requires no network access.

Pinned data SHA-256:

```text
2600bb421b6d0a954dd3ce221501303973434f4ce90ff2fc14bea7739a61d7d7
```

`verify.py` checks this hash before accepting the analysis result.

## DSH pin

```text
tag:    dsh-v0.1.5-rc.2
commit: fb2c4b9e698e30edb738bca4cf0618587db7d203
```

This recipe does not silently move with upstream `master`.

## Dependencies

Runtime analysis dependency: **Python standard library only**.

No pandas, numpy, scipy, notebook server, database, API, plugin, or network access is required for the deterministic baseline.

## Deterministic baseline

From this directory:

```bash
python analyze.py
python verify.py
```

`analyze.py` writes `result.json`. `verify.py` then checks:

| Statistic | NIST certified value |
|---|---:|
| observations | `36` |
| intercept | `-0.262323073774029` |
| slope | `1.00211681802045` |
| residual standard deviation | `0.884796396144373` |
| R-squared | `0.999993745883712` |

Floating-point statistics use an absolute tolerance of `1e-12`.

Acceptance is binary:

```text
PASS + exit 0  => accepted
FAIL + exit 1  => rejected
```

## Pinned DSH headless contract

Start from this recipe directory so the DSH workspace boundary is the recipe itself:

```bash
npx -y @deepseek-ai/dsh@0.1.5-rc.2 --profile headless \
  "Use only local files in this workspace. Run python analyze.py, then python verify.py. Do not edit data/norris.csv, expected.json, or verify.py. The task succeeds only if verify.py exits 0. Report result.json and the verifier status."
```

The model's final prose is **not** the oracle. `verify.py` is.

This exact pinned DSH headless contract was verified on 2026-09-11 in a GitHub-hosted Ubuntu 24.04.5 runner: DSH exited `0`, the three protected oracle/fixture files retained identical pre/post SHA-256 values, and an independent post-DSH `python verify.py` returned `PASS` / exit `0`. Durable evidence is recorded in [Issue #3](https://github.com/SIMON-WORLD/dsh-research-handbook/issues/3) and [Actions run 34607136510](https://github.com/SIMON-WORLD/dsh-research-handbook/actions/runs/34607136510); the current-tested scope is summarized in [`docs/current-tested.md`](../../../docs/current-tested.md).

## Files

```text
data/norris.csv   local NIST data snapshot
analyze.py        stdlib OLS reference analysis
expected.json     NIST certified values + tolerances + data hash
verify.py         deterministic acceptance checker
result.json       generated artifact; intentionally not committed
```

## What this recipe does not prove

Passing this recipe does not establish that DSH is production-safe, that every Python research workflow is reproducible, or that later DSH releases are compatible. It proves only this pinned numerical contract on an environment where the verifier has been run.
