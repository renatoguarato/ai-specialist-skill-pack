# Devin CLI integration (v6)

This pack is installed as a Devin CLI plugin, without copying company source into this public repository.

## Setup

```bash
git clone https://github.com/renatoguarato/ai-specialist-skill-pack.git
cd ai-specialist-skill-pack
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
devin plugins install .
devin plugins list
```

Run `devin` from an authorized project checkout. Start with a read-only task and confirm that the installed skills appear in the CLI. If your CLI version does not support a plugin manifest field or skill path, consult `devin plugins --help` and adapt the installation; do not assume a successful load from file placement alone.

## Daily workflows

**Onboarding:** `Use repository-discovery/onboarding; read-only; document entrypoints, data flow, contracts, deployment, tests and unknowns with file:line evidence.`

**Cross-repo tracing:** `Use cross-repo-tracing to follow one user request across BFF and agent services. Record commit refs, correlation IDs and confirmed edges; distinguish missing edges.`

**Architecture:** `Use change-engineering/impact to propose an ADR and migration stages. No edits before approval.`

**Implementation:** `Use autonomous-implementation with approved scope, branch, acceptance tests and rollback. Never merge automatically.`

**AI quality:** `Use ai-evaluation to assess RAG retrieval, groundedness, tool safety, latency and cost using representative authorized datasets.`

**Handoff:** `Use engineering-handoff to produce decisions, evidence, test results, residual risks and next actions.`

## Permissions and data handling

1. Start with read-only Git permissions and sandboxed local tooling.
2. Allow branch writes and PR creation only for approved implementation tasks.
3. Keep production, credentials, private MCP connections, and destructive operations outside autonomous permission scope.
4. Store organization-specific context in an approved internal location, not in this public plugin.
5. If using subagents, delegate independent bounded questions; require each to report evidence and uncertainties. Subagents are orchestration roles, not automatically registered executables.

## Multi-repository investigation

Check out authorized repositories side-by-side, or make them accessible through approved connectors. Do not copy code between repositories. Identify each repository's HEAD SHA and version assumptions. A call edge is confirmed only with evidence from both sides or a shared contract.

## Compatibility

The existing `install.py` remains supported for non-Devin agents. Devin plugin installation and the legacy per-repository installer are separate workflows. The manifest version is kept in sync with `manifest.json`.
