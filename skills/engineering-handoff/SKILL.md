---
name: engineering-handoff
description: Produce an evidence-based handoff for discovery, design, implementation or incident work with decisions, checks and next actions.
---

# Engineering handoff

Use when closing or transferring a technical task.

Deliver:
- Scope and outcome; repository and commit references.
- Verified facts versus assumptions and unresolved questions.
- Changed files or read-only findings with source references.
- Commands executed, test outcomes, failures and limitations.
- Architecture/security/operations impact, rollout and rollback if applicable.
- Risks, owner decisions, next actions and PR link if created.

Never claim a test passed unless it was executed and returned success. Never include secrets, PII or confidential source in public reports. Follow `references/operating-contract.md`.
