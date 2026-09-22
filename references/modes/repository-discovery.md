# Repository Discovery Modes

Use the smallest mode that answers the question.

## inventory

Map directories, manifests, build files, CI/CD, Dockerfiles, IaC, tests, entrypoints, frameworks, external dependencies and cross-cutting concerns. Cite paths and versions; do not infer architecture from folder names alone.

## architecture

Trace runtime boundaries, modules, dependency direction, integration points, persistence and asynchronous processing. Distinguish logical architecture from deployment topology.

## domain

Identify entities, states, business rules, invariants, bounded contexts and domain events from code and behavior. Separate technical naming from confirmed business meaning.

## flow

Trace a named user or system flow from input through transformations, validation, authorization, persistence, events, integrations, retries, failures and response.

## contracts

Analyze REST, GraphQL, messaging and event contracts, including validation, errors, idempotency, compatibility and versioning.

## data

Map entities, migrations, queries, repositories, indexes, transactions, retention and sensitive data. Call out migration and consistency risks.

## infrastructure

Map AWS or other deployment infrastructure only from IaC and configuration. Identify ownership boundaries, permissions, networking, scaling, delivery and runtime dependencies.

## dependencies

Assess internal and external dependencies for criticality, coupling, version risk, resilience, timeout, retry and failure blast radius.

## knowledge

Turn validated findings into concise documentation with sources, confidence, risks and unresolved questions.

## learning

Create a progressive repository-learning path for 1, 3, 5 and 10 days, ordered by value and risk reduction.

## onboarding

Produce a structured onboarding map covering application boundaries, entrypoints, key flows, external dependencies, persistence, events, authentication and authorization, observability, deployment, ownership, known risks, domain glossary, open questions and a prioritized study plan. Cite evidence and mark unavailable items as unknowns.

For `inventory`, `architecture`, `domain`, `flow`, `contracts`, `data`, `infrastructure` and `onboarding`, output an application map. For all modes, follow `references/operating-contract.md`.
