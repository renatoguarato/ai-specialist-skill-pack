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

## Contrato operacional v4

### Princípios de execução

- Comece pela pergunta e pelo escopo autorizado; não investigue tudo por padrão.
- Prefira evidência direta no código, configuração, contrato, telemetria ou declaração explícita do usuário.
- Registre fonte, arquivo/símbolo/linha ou artefato e diferencie observação estática, runtime e informação humana.
- Separe **Confirmado**, **Inferido**, **Hipótese** e **Desconhecido**; ausência de evidência não confirma ausência do comportamento.
- Não invente valores, contratos, owners, SLAs, preços ou capacidades de provedores.
- Priorize investigações de alto valor e baixo custo; preserve reversibilidade e não faça ações destrutivas sem autorização.

### Método mínimo

1. Reformule a pergunta em uma frase e declare inclusões/exclusões.
2. Colete os artefatos mais próximos do comportamento; só amplie a busca quando uma dependência concreta exigir.
3. Construa uma cadeia de evidências antes de concluir.
4. Diferencie fato observado, inferência e hipótese; indique a validação mínima para cada hipótese.
5. Priorize achados por impacto, probabilidade, detectabilidade e reversibilidade.
6. Finalize com ações ordenadas, critérios de conclusão e handoff quando outra skill for necessária.

## Saída v4

Use a estrutura específica existente nesta skill e acrescente sempre:

### Resumo da resposta
- pergunta respondida;
- escopo e data da análise;
- conclusão principal.

### Evidências e conclusões
| Afirmação | Fonte | Tipo | Estado | Confiança |
|---|---|---|---|---|

### Riscos priorizados
| Risco | Impacto | Probabilidade | Detectabilidade | Severidade | Mitigação |
|---|---|---|---|---|---|

### Desconhecidos decisivos
Liste somente lacunas que podem alterar a conclusão ou a implementação.

### Próximas ações
Para cada ação: objetivo, pré-condição, resultado esperado, validação e rollback quando houver mudança.

### Handoff
Informe a próxima skill, o contexto que deve ser transferido e o artefato produzido. Se não houver handoff, declare 'Nenhum'.

## Critérios de parada

Pare quando a pergunta estiver respondida com evidência suficiente, quando a investigação exigir acesso não disponível ou quando o próximo passo tiver risco maior que o valor de continuar. Nesse caso, declare o bloqueio e o menor dado necessário para prosseguir.

### Referências operacionais

- [Contrato de skills](../../references/skill-contract.md)
- [Evidência e risco](../../references/evidence-and-risk.md)


### Controles de orquestração

- Classifique primeiro a intenção, urgência, risco, artefatos disponíveis e resultado esperado.
- Escolha o menor conjunto de skills; execute em paralelo apenas investigações independentes.
- Antes de encadear, confirme que a saída da skill anterior é pré-condição real para a próxima.
- Preserve o contexto de handoff e não repita etapas sem nova evidência.
- Em caso de risco crítico, bloqueio de acesso ou ambiguidade que muda a solução, pare e explicite a decisão necessária.
- Termine com decisão, evidências, riscos, lacunas e próximo passo executável.

### Matriz de roteamento

Consulte [roteamento e handoffs](../../references/routing-and-handoffs.md).

## Roteamento v4

Antes de acionar qualquer skill, classifique:

| Intenção | Primeiro passo | Complementos condicionais | Saída de entrada |
|---|---|---|---|
| Entender aplicação | `codebase-inventory` | arquitetura, domínio, dados, infraestrutura | mapa factual do repositório |
| Entender fluxo | `request-flow-tracer` | API, banco, dependências, observabilidade | entrada, transformações e efeitos |
| Alterar comportamento | `change-impact-analyzer` | testes, plano, segurança, PR | mapa de impacto e riscos |
| Incidente | `production-debugger` | observabilidade, dependências, postmortem | hipóteses testáveis e mitigação |
| Sistema de IA | `ai-system-discovery` | RAG, agentes, avaliação, segurança, custo | inventário do caminho de IA |

Não acione análise de produção sem janela temporal/sintoma; não acione model selection sem workload e critérios; não acione implementação sem escopo, impacto e critério de aceite. Quando houver artefatos independentes, execute as investigações em paralelo e consolide uma única síntese.
