---
name: cross-repo-tracing
description: Trace a request or event across multiple repositories and services, with evidence-backed contracts, ownership, auth, telemetry and failure paths.
---

# Cross-repository tracing

Use this skill for end-to-end user journeys spanning BFF, agent runtime, data stores, queues or external tools.

1. Identify repository names, checked-out refs/SHAs, entrypoint and request or event identifier.
2. Trace inbound route, authentication and authorization, transformation, service calls, messaging, agent/tool execution, persistence, response and errors.
3. Verify each edge using caller and callee implementations, tests, schemas or published contracts. Mark unverified edges as hypotheses.
4. Map trace propagation, idempotency, retries, timeouts, cost attribution and PII boundaries where relevant.
5. Produce a Mermaid sequence diagram, evidence matrix (repo:path:line), failure modes, gaps and prioritized follow-ups.

Default to read-only. Do not access live production or secrets. Apply `references/operating-contract.md`.
