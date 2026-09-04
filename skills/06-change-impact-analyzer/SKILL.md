---
name: change-impact-analyzer
description: Avalia impacto técnico e funcional antes de alterar uma aplicação desconhecida.
---

# Change Impact Analyzer

## Objetivo
Reduzir risco de regressão antes de uma implementação.

## Inputs
Uma mudança desejada, ticket, bug ou requisito.

## Workflow
1. Identifique entrypoints afetados.
2. Identifique casos de uso afetados.
3. Identifique entidades e tabelas.
4. Identifique contratos.
5. Identifique consumidores downstream.
6. Identifique eventos.
7. Identifique cache.
8. Identifique autenticação/autorização.
9. Identifique observabilidade.
10. Identifique testes existentes.
11. Identifique feature flags e rollouts.
12. Identifique risco de migração de dados.

## Saída
### Impact Map
- código;
- banco;
- API;
- eventos;
- infraestrutura;
- segurança;
- observabilidade;
- testes.

### Risk Matrix
Probabilidade x impacto.

### Recommended Change Strategy
Preferir mudanças incrementais e reversíveis.
