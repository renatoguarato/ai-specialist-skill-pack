---
name: application-onboarding-orchestrator
description: Orquestra o entendimento de uma aplicação desconhecida, escolhendo e sequenciando as demais skills deste pacote.
---

# Application Onboarding Orchestrator

## Objetivo
Transformar uma solicitação ampla como "me explique esta aplicação" em uma investigação técnica estruturada, progressiva e verificável.

## Quando usar
- Primeiro contato com um repositório.
- Entrada em um novo produto ou domínio.
- Antes de realizar mudanças relevantes em uma aplicação desconhecida.
- Quando houver dúvidas sobre qual skill especializada usar.

## Inputs esperados
- Repositório ou diretório da aplicação.
- Pergunta do usuário.
- Opcional: documentação, diagramas, tickets, logs, dashboards, IaC, contratos de API.

## Estratégia
1. Identifique a intenção:
   - compreender arquitetura;
   - compreender domínio;
   - localizar fluxo;
   - investigar incidente;
   - estimar impacto;
   - implementar mudança;
   - revisar segurança;
   - analisar infraestrutura;
   - melhorar testes.
2. Execute primeiro `codebase-inventory`.
3. Se houver domínio desconhecido, execute `domain-model-discovery`.
4. Se houver APIs, execute `api-contract-analyzer`.
5. Se houver cloud/IaC, execute `aws-infrastructure-mapper`.
6. Para fluxos específicos, use `request-flow-tracer`.
7. Para mudanças, use `change-impact-analyzer`.
8. Para incidentes, use `production-debugger`.
9. Para observabilidade, use `observability-reviewer`.
10. Para segurança, use `security-boundary-reviewer`.
11. Para implementação, use `implementation-planner`.
12. Sempre conclua com:
   - fatos confirmados;
   - hipóteses;
   - lacunas;
   - riscos;
   - próximos passos.

## Saída obrigatória
### Executive Summary
Resumo de 5 a 10 linhas.

### Application Map
- responsabilidade;
- entradas;
- saídas;
- dependências;
- persistência;
- mensageria;
- integrações;
- infraestrutura.

### Confidence
Classifique cada conclusão como:
- Confirmado;
- Provável;
- Hipótese.

### Next Investigation
Liste no máximo 5 investigações de maior valor.

## AI Systems Branch
Se a aplicação utilizar IA generativa:
1. Execute `ai-system-discovery`.
2. Para chamadas de modelo, use `llm-call-tracer`.
3. Para prompts, use `prompt-analyzer`.
4. Para RAG, use `rag-pipeline-analyzer` e `retrieval-quality-analyzer`.
5. Para agentes, use `agent-workflow-mapper` e `tool-calling-analyzer`.
6. Para qualidade, use `llm-evaluation-designer`.
7. Para respostas incorretas, use `hallucination-analyzer`.
8. Para custo, use `token-cost-analyzer`.
9. Para contexto, use `context-window-analyzer`.
10. Para segurança, use `guardrail-reviewer`.
11. Para observabilidade, use `ai-observability-reviewer`.
12. Em AWS Bedrock, use `bedrock-architecture-analyzer`.
13. Antes de produção, use `ai-production-readiness`.
