# Roteamento e handoffs

O roteador deve escolher o menor conjunto de skills que responde à intenção. Só encadeie uma skill quando a saída da anterior for uma entrada necessária para a próxima.

## Handoff

Transfira: pergunta original, escopo, evidências já coletadas, conclusões, desconhecidos, riscos, artefatos produzidos e decisão pendente. A skill seguinte deve reutilizar esse contexto e não repetir a investigação sem motivo.

## Ordem padrão

- Descoberta: inventário → arquitetura/domínio → fluxo/API/dados/infraestrutura → conhecimento capturado.
- Mudança: impacto → estratégia de testes → plano de implementação → execução protegida → revisão.
- IA: descoberta → análise especializada → avaliação → segurança/observabilidade → prontidão.
- Operação: diagnóstico → mitigação segura → causa provável → correção permanente → postmortem.
