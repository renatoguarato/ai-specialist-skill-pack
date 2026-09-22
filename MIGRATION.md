# Migração da v4 para a v5

A v5 reduz as 50 skills da v4 para seis skills públicas. Os nomes antigos continuam documentados nesta tabela, mas não são mais instalados.

| Skill v4 | Skill v5 | Modo |
|---|---|---|
| `application-onboarding-orchestrator` | `repository-discovery` | `onboarding` |
| `ai-specialist-daily-orchestrator` | `ai-specialist` | roteamento |
| `codebase-inventory` | `repository-discovery` | `inventory` |
| `architecture-mapper` | `repository-discovery` | `architecture` |
| `domain-model-discovery` | `repository-discovery` | `domain` |
| `request-flow-tracer` | `repository-discovery` | `flow` |
| `api-contract-analyzer` | `repository-discovery` | `contracts` |
| `database-model-explorer` | `repository-discovery` | `data` |
| `aws-infrastructure-mapper` | `repository-discovery` | `infrastructure` |
| `dependency-risk-auditor` | `repository-discovery` ou `production-reliability` | `dependencies` |
| `knowledge-capture` | `repository-discovery` | `knowledge` |
| `technical-question-generator` | `repository-discovery` | `learning` |
| `change-impact-analyzer` | `change-engineering` | `impact` |
| `technical-debt-prioritizer` | `change-engineering` | `debt` |
| `risk-based-work-planner` | `change-engineering` | `risk` |
| `test-strategy-analyzer` | `change-engineering` | `tests` |
| `implementation-planner` | `change-engineering` | `implementation` |
| `code-generation-guardrail` | `change-engineering` | `guardrails` |
| `pull-request-reviewer` | `change-engineering` | `review` |
| `production-debugger` | `production-reliability` | `debug` |
| `observability-reviewer` | `production-reliability` | `observability` |
| `security-boundary-reviewer` | `production-reliability` | `security` |
| `incident-postmortem` | `production-reliability` | `postmortem` |
| `ai-system-discovery` | `ai-systems` | `discovery` |
| `llm-call-tracer` | `ai-systems` | `llm` |
| `prompt-analyzer` | `ai-systems` | `prompt` |
| `rag-pipeline-analyzer` | `ai-systems` | `rag` |
| `retrieval-quality-analyzer` | `ai-systems` | `retrieval` |
| `agent-workflow-mapper` | `ai-systems` | `agents` |
| `tool-calling-analyzer` | `ai-systems` | `tools` |
| `llm-evaluation-designer` | `ai-systems` | `evals` |
| `hallucination-analyzer` | `ai-systems` | `hallucination` |
| `token-cost-analyzer` | `ai-systems` | `cost` |
| `context-window-analyzer` | `ai-systems` | `context` |
| `model-selection-advisor` | `ai-systems` | `model` |
| `guardrail-reviewer` | `ai-systems` | `guardrails` |
| `ai-observability-reviewer` | `ai-systems` | `readiness` ou `observability` |
| `bedrock-architecture-analyzer` | `ai-systems` | `bedrock` |
| `ai-production-readiness` | `ai-systems` | `readiness` |
| `requirement-to-ai-solution` | `product-delivery` | `requirements` |
| `technical-discovery-interviewer` | `product-delivery` | `interview` |
| `architecture-decision-record-writer` | `product-delivery` | `adr` |
| `ai-poc-designer` | `product-delivery` | `poc` |
| `experiment-designer` | `product-delivery` | `experiment` |
| `stakeholder-technical-translator` | `product-delivery` | `translation` |
| `ai-business-value-analyzer` | `product-delivery` | `business-value` |
| `technical-documentation-generator` | `product-delivery` | `documentation` |
| `meeting-context-preparer` | `product-delivery` | `meeting` |
| `ticket-context-builder` | `product-delivery` | `ticket` |

## Comando

Para uma instalação v4 registrada pelo instalador:

```bash
python3 install.py migrate /caminho/do/projeto
```

A migração remove somente arquivos v4 que não foram modificados localmente, instala o perfil v5 escolhido e atualiza o bloco controlado do `AGENTS.md`. Arquivos modificados são preservados e reportados.
