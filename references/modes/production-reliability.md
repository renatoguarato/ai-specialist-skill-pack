# Production Reliability Modes

## debug

Require a symptom and time window. Correlate deploys, logs, metrics, traces, dependencies and blast radius. Rank testable hypotheses; do not declare root cause without evidence.

## observability

Review structured logs, levels, correlation IDs, PII, RED metrics, business metrics, dependency metrics, trace propagation, spans, SLOs and actionable alerts. Identify blind spots and minimum telemetry.

## security

Map trust boundaries, protected assets, authentication, authorization, secrets, encryption, PII, input validation, injection, SSRF, deserialization, uploads, rate limiting and sensitive logs. Do not call something a vulnerability without evidence and exploit preconditions.

## dependencies

Assess production dependency failure modes, timeouts, retries, circuit breakers, version exposure, ownership and fallback behavior.

## postmortem

Produce a blameless timeline, impact, detection, confirmed cause, contributing factors, uncertainty, corrective actions, owners, validation and prevention.

Prefer reversible mitigation before permanent correction. Follow `references/operating-contract.md`.
