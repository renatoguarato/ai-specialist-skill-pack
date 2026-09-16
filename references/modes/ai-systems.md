# AI Systems Modes

## discovery

Map model calls, prompts, context, retrieval, agents, tools, memory, evaluation, safety, cost and observability.

## llm

Trace input, prompt assembly, model/provider, parameters, tools, tokens, latency, response parsing, post-processing, retries and fallbacks.

## prompt

Review clarity, hierarchy, conflicts, injection resistance, output constraints, context use, cost and predictability.

## rag

Trace ingestion, chunking, embeddings, indexing, retrieval, ranking, context assembly, generation, citations and failure modes.

## retrieval

Design or evaluate retrieval datasets and metrics such as recall, precision, ranking quality, groundedness and error categories.

## agents

Map planner, state, memory, loops, handoffs, termination and failure recovery.

## tools

Review tool schemas, authorization, validation, side effects, idempotency, least privilege and auditability.

## evals

Define task dataset, baseline, quality metrics, safety metrics, regression thresholds and decision criteria.

## hallucination

Trace whether unsupported output originates in retrieval, context, prompt, model behavior or post-processing.

## cost

Measure tokens, requests, latency, cache use and provider cost. Recommend optimizations with measurable trade-offs.

## context

Analyze context composition, truncation, noise, instruction loss and token budget.

## model

Compare models only against a named workload and explicit quality, latency, cost, context and tool-use criteria. Include deterministic alternatives.

## guardrails

Review input, output, tool, data and policy controls, including bypasses and failure handling.

## bedrock

Map Bedrock models, Knowledge Bases, Agents, Guardrails, IAM, observability and integration boundaries from evidence.

## readiness

Assess quality, safety, reliability, observability, cost, access control, rollout, rollback and operational ownership before production.

Follow `references/operating-contract.md`. Use only the modes relevant to the AI architecture under review.
