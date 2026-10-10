---
name: ai-evaluation
description: Evaluate RAG and agent behavior with reproducible datasets, retrieval and generation metrics, tool safety, latency and cost.
---

# AI evaluation

Use for LLM/RAG/agent quality, regressions, prompt and model comparisons.

1. Define task, dataset provenance, baseline, slice coverage, acceptance thresholds and budget.
2. Assess retrieval (Recall@K, Precision@K, MRR where labeled), groundedness, relevance, answer correctness, tool-call validity and safety.
3. Separate deterministic tests from judge-model scores; calibrate judge agreement and review failure examples.
4. Capture model, prompt, dataset, embedding and index versions; log latency, tokens, cost and tracing IDs with sensitive fields redacted.
5. Produce a reproducible evaluation plan, metric table, failure taxonomy, confidence limits and go/no-go recommendation.

Do not send proprietary documents or PII to unapproved model providers. Follow `references/operating-contract.md`.
