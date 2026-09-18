# PROJECT_CONTROL

> Project-local durable control for `SIMON-WORLD/dsh-research-handbook`.
>
> This file was materialized from existing durable GitHub truth. It does **not** create a new product roadmap, approve Recipe 002, replace the owner decision gate, or grant any conversation Parent/mutation authority merely because the file exists.

## Stable adoption locator

```text
mode = scoped_identity
container.kind = github_repo
container.pointer = https://github.com/SIMON-WORLD/dsh-research-handbook
identity = PROJECT_CONTROL.md

locatorKey = scoped_identity:github_repo:https://github.com/SIMON-WORLD/dsh-research-handbook#PROJECT_CONTROL.md
```

This is a mature-project `MATERIALIZE_CONTROL` adoption. It is **not** `NEW_GENESIS`.

## Canonical control record

```json
{
  "schemaVersion": 1,
  "projectKey": "dsh-research-handbook",
  "controlId": "DSH-PROJECT-CONTROL",
  "revision": "CTRL-0001",
  "freshness": "current",
  "writerState": "clear",
  "parentBinding": {
    "status": "UNBOUND",
    "provenance": "materialized from existing GitHub durable truth under Human Principal bounded adoption authorization; no durable Parent designation was observed"
  },
  "lifecycle": "STRATEGY_REVIEW",
  "activeMissionRef": {
    "kind": "github_issue",
    "pointer": "https://github.com/SIMON-WORLD/dsh-research-handbook/issues/5",
    "displayRef": "#5 · STRATEGY_REVIEW"
  },
  "pointers": [
    {
      "kind": "github_repo_baseline",
      "pointer": "https://github.com/SIMON-WORLD/dsh-research-handbook/commit/2d6a81112276f7596555700bd4e0cba6931489de"
    },
    {
      "kind": "product_baseline",
      "pointer": "https://github.com/SIMON-WORLD/dsh-research-handbook/blob/2d6a81112276f7596555700bd4e0cba6931489de/README.md"
    },
    {
      "kind": "strategy_gate",
      "pointer": "https://github.com/SIMON-WORLD/dsh-research-handbook/issues/5"
    },
    {
      "kind": "shared_kernel_observation",
      "pointer": "https://github.com/SIMON-WORLD/chatgpt-codex-orchestrator/commit/7a8500102b590f7a94df7fc5aa25ed866e8d400c"
    }
  ]
}
```

## Preserved project truth

- Current product baseline: **Versioned Research Reproducibility Cookbook for DeepSeek Harness (DSH)**, with immutable versioned recipes, a small current-tested matrix, official primitives first, provenance requirements, and deterministic acceptance over prose.
- Current active strategy gate: GitHub Issue #5, `STRATEGY_REVIEW`.
- **Do not implement Recipe 002 until the owner approves a direction based on Issue #5.**
- The four completed review lenses on Issue #5 are evidence for the owner decision; this control materialization does not choose a direction for the owner.
- Legacy handbook material is not current executable truth unless `docs/current-tested.md` or a versioned recipe explicitly verifies it.

## Authority and recovery boundary

- Project Instructions, Project membership, conversation title, memory, transcript, provider/tool access, and readability of this file do not grant Parent or mutation authority.
- Because no durable DSH Parent designation was observed during materialization, `parentBinding.status` is intentionally `UNBOUND`. A destination-specific Human Principal designation/takeover contract is required before a conversation acts as ongoing Parent.
- Capability does not grant authority. Runtime capabilities must be rediscovered on each fresh/replacement bootstrap.
- GitHub current `main`, current Issue #5, and other live repository evidence remain implementation/project truth. This file is the stable project-local control surface that points to that truth; it is not a substitute for live readback.
- No central project registry, watcher, scheduler, multi-Parent hierarchy, or orchestrator-owned downstream supervisor is introduced.

## Recovery order

```text
orchestrator current shared kernel
-> DSH stable repository root
-> this project-local durable control
-> current conversation role/authority
-> active mission (#5) OR next safe action
-> fresh runtime capability discovery
-> route/act or fail closed
```

Until a destination-specific Parent role is valid, the safe state is read-only recovery of Issue #5 and its evidence. Any product-direction decision remains owner-gated.
