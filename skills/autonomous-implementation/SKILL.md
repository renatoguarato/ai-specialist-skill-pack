---
name: autonomous-implementation
description: Deliver an approved, bounded engineering change through plan, isolated branch, tests, review and PR handoff.
---

# Autonomous implementation

Use only after the user explicitly approves an implementation scope.

1. Confirm acceptance criteria, impacted contracts, dependencies, rollout and rollback.
2. Establish a branch and baseline checks; inspect repository instructions and existing patterns.
3. Implement the smallest reversible change. Avoid unrelated formatting and dependency upgrades.
4. Run targeted and broader tests, lint, type checks and relevant security checks; record exact commands and results.
5. Review diff for compatibility, secrets, data handling, migrations and observability.
6. Prepare PR with rationale, changed paths, test evidence, risks and manual verification steps.

Never merge or deploy without separate approval. Stop on missing permissions, destructive migrations, ambiguous requirements or sensitive data exposure. Follow `references/operating-contract.md`.
