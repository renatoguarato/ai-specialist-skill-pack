# Cenários representativos de validação

Execute cada cenário com os artefatos mínimos indicados e verifique se a saída contém evidências, estado de conhecimento, riscos, desconhecidos, ações e handoff quando necessário.

| Cenário | Skill principal | Resultado esperado |
|---|---|---|
| Repositório novo com API e worker | `repository-discovery` / `inventory` | mapa factual de stack, entradas, módulos, delivery e lacunas |
| Criação de pagamento | `repository-discovery` / `flow` | fluxo feliz, falhas, transação, efeitos colaterais e observabilidade |
| Alteração de campo em evento público | `change-engineering` / `impact` | consumidores, compatibilidade, migração, rollout e rollback |
| Latência elevada após deploy | `production-reliability` / `debug` | hipóteses ordenadas por evidência e mitigação segura |
| Chat RAG multi-tenant | `rag-pipeline-analyzer` + `guardrail-reviewer` | caminho causal, grounding, isolamento e abuso |
| Agente com ferramenta de escrita | `tool-calling-analyzer` | permissões, confirmação, idempotência, auditoria e contenção |
| Comparação de modelos | `model-selection-advisor` | matriz baseada no workload e indicação de verificação atual |
| POC de classificação assistida | `ai-poc-designer` + `llm-evaluation-designer` | baseline, dataset, métricas, limiar e regra GO/NO-GO |
| PR com migração de banco | `change-engineering` / `review` | achados priorizados, concorrência, rollback e testes ausentes |
| Reunião sobre arquitetura desconhecida | `meeting-context-preparer` | fatos, decisões, perguntas de alto valor e resultado desejado |
