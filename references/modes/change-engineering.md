# Change Engineering Modes

## impact

Given a requirement, bug or improvement, map affected code, use cases, APIs, data, events, caches, consumers, authorization, observability, tests, flags, rollout and migration risk.

## debt

Prioritize technical debt by operational impact, frequency, security risk, delivery impact, maintenance cost, effort and future dependencies. Classify as Do Now, Schedule, Monitor or Ignore for Now.

## risk

List unknowns first, classify risks, identify dependencies and perform high-value, low-cost investigations before implementation. Define stop conditions.

## tests

Evaluate unit, integration, contract, component, end-to-end, performance and resilience coverage. Recommend the smallest tests that prove the changed behavior and prevent regressions.

## implementation

Produce an incremental plan with components, data/API/event changes, tests, observability, security, rollout, rollback and ordered steps. Do not edit until the plan is approved.

## guardrails

Before code generation or editing, verify scope, existing conventions, compatibility, error handling, sensitive data, tests and unintended changes.

## review

Review a diff in this order: correctness, security, regressions, concurrency and transactions, contracts, tests, observability, architecture and readability. Report blocking and important findings with file and line.

For every mode, distinguish recommendation from decision and cite evidence. Follow `references/operating-contract.md`.
