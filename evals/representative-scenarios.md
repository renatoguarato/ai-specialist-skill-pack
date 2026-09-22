# Cenários representativos de validação

Execute cada cenário com os artefatos mínimos indicados e verifique se a saída contém evidências, estado de conhecimento, riscos, desconhecidos, ações e handoff quando necessário.

| Cenário | Skill principal | Resultado esperado |
|---|---|---|
| Repositório novo com API e worker | `repository-discovery` / `inventory` | mapa factual de stack, entradas, módulos, delivery e lacunas |
| Onboarding de um sistema desconhecido | `repository-discovery` / `onboarding` | mapa da aplicação, riscos, owners, glossário, lacunas e plano de estudo |
| Criação de pagamento | `repository-discovery` / `flow` | fluxo feliz, falhas, transação, efeitos colaterais e observabilidade |
| Alteração de campo em evento público | `change-engineering` / `impact` | consumidores, compatibilidade, migração, rollout e rollback |
| Design de uma nova capacidade | `product-delivery` / `system-design` | requisitos, NFRs, limites, dados, resiliência, segurança, observabilidade e trade-offs |
| Latência elevada após deploy | `production-reliability` / `debug` | hipóteses ordenadas por evidência e mitigação segura |
| Saturação de serviço sob carga | `production-reliability` / `capacity` | gargalos, headroom, limites, backpressure e validação segura |
| Chat RAG multi-tenant | `ai-systems` / `rag` + `ai-systems` / `guardrails` | caminho causal, grounding, isolamento e abuso |
| Agente com ferramenta de escrita | `ai-systems` / `tools` | autorização, confirmação, idempotência, auditoria e contenção |
| Comparação de modelos | `ai-systems` / `model` | matriz baseada no workload e indicação de verificação atual |
| POC de classificação assistida | `product-delivery` / `poc` + `ai-systems` / `evals` | baseline, dataset, métricas, limiar e regra GO/NO-GO |
| PR com migração de banco | `change-engineering` / `review` | achados priorizados, concorrência, rollback e testes ausentes |
| Reunião sobre arquitetura desconhecida | `product-delivery` / `meeting` | fatos, decisões, perguntas de alto valor e resultado desejado |
