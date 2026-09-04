---
name: request-flow-tracer
description: Traça ponta a ponta um fluxo funcional desde a entrada até banco, eventos, integrações e resposta.
---

# Request Flow Tracer

## Objetivo
Responder perguntas como:
- "O que acontece quando este endpoint é chamado?"
- "De onde vem este valor?"
- "Onde esta regra é aplicada?"
- "Qual serviço publica este evento?"

## Workflow
1. Identifique o ponto de entrada.
2. Siga chamadas internas.
3. Registre transformações de dados.
4. Registre regras executadas.
5. Registre chamadas externas.
6. Registre operações de persistência.
7. Registre eventos publicados/consumidos.
8. Registre comportamento de erro, retry e fallback.
9. Identifique contexto de transação.
10. Relacione logs, métricas e trace IDs quando existirem.

## Saída
### Flow
Use passos numerados.

### Sequence Diagram
Gere Mermaid `sequenceDiagram`.

### Side Effects
### Failure Paths
### Observability
### Hotspots
