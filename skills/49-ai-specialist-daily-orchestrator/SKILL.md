---
name: ai-specialist-daily-orchestrator
description: Orquestra o fluxo diário de trabalho de um AI Specialist entre discovery, análise, decisão, implementação e validação.
---

# AI Specialist Daily Orchestrator

## Objetivo
Escolher a próxima skill correta conforme a tarefa.

## Routing
### Novo sistema
repository-learning-plan -> application-onboarding-orchestrator

### Novo requisito
technical-discovery-interviewer -> requirement-to-ai-solution -> architecture-decision-record-writer

### POC
ai-poc-designer -> experiment-designer -> llm-evaluation-designer

### Mudança em código
change-impact-analyzer -> implementation-planner -> code-generation-guardrail -> pull-request-reviewer

### Incidente
production-debugger -> incident-postmortem

### Reunião
meeting-context-preparer -> stakeholder-technical-translator

### Ticket
ticket-context-builder -> change-impact-analyzer

### Iniciativa de IA
ai-business-value-analyzer -> ai-system-discovery -> ai-production-readiness

## Regra final
Sempre terminar com:
- decisão tomada;
- evidências;
- riscos;
- próximos passos;
- lacunas de conhecimento.

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

### Protocolo

1. Reescreva o pedido como resultado observável.
2. Classifique urgência, risco, dependências e artefatos disponíveis.
3. Escolha uma skill primária e somente os complementos que respondem desconhecidos concretos.
4. Defina o artefato esperado e o critério de conclusão antes de iniciar.
5. Após cada etapa, descarte rotas que já não agregam informação e transfira o contexto restante.

### Regras de segurança

- Pedido ambíguo que muda a solução: produzir perguntas de decisão antes de implementar.
- Falta de evidência: declarar desconhecido e propor investigação mínima.
- Ação destrutiva, produção ou dado sensível: exigir autorização e validação proporcional antes da execução.
- Mudança irreversível: registrar migração, rollout, rollback e condição de abortar.

### Pacote de handoff

Toda transição deve carregar: pedido original, escopo, artefatos consultados, conclusões, evidências, riscos, desconhecidos, decisões tomadas e próxima pergunta a responder.
