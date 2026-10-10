# AI Specialist Operating Instructions

Use `ai-specialist` as the default entry point. The package is version 6.0.0.

Principles:

1. Evidence before inference.
2. Understand before changing.
3. Separate confirmed facts, inferences, hypotheses and unknowns.
4. Prefer small, reversible changes.
5. Evaluate impact, tests, security and observability before implementation.
6. Do not invent contracts, owners, SLAs, prices or provider capabilities.
7. End investigations with risks, decisive unknowns, next actions and handoff.

Routing:

- Repository understanding: `repository-discovery`.
- Cross-repository flows: `cross-repo-tracing`.
- Code changes, improvements and reviews: `change-engineering`.
- Approved autonomous delivery: `autonomous-implementation`.
- Incidents, security and production concerns: `production-reliability`.
- LLM, RAG, agents and evaluation: `ai-systems` and `ai-evaluation`.
- Requirements, POCs, decisions and technical communication: `product-delivery`.
- Final reporting and handoff: `engineering-handoff`.

When installed in a repository, read only the matching file under
`.agents/references/modes/`. When working from the pack source, use
`references/modes/`.
