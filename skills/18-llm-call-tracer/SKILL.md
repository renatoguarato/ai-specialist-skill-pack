---
name: llm-call-tracer
description: Traça uma chamada de LLM ponta a ponta, incluindo contexto, prompt, modelo, ferramentas, tokens, resposta e pós-processamento.
---

# LLM Call Tracer

## Objetivo
Explicar exatamente o que acontece em uma interação com um modelo.

## Rastreie
1. Evento de entrada.
2. Dados do usuário.
3. Contexto recuperado.
4. Prompt do sistema.
5. Prompt do usuário.
6. Prompt final.
7. Modelo/provedor.
8. Parâmetros:
   - temperature;
   - top_p;
   - max_tokens;
   - stop;
   - response format.
9. Ferramentas disponibilizadas.
10. Tool calls executadas.
11. Pós-processamento.
12. Validação de saída.
13. Persistência.
14. Métricas e tracing.

## Saída
### Invocation Path
### Prompt Composition
### Model Configuration
### Tools
### Token Flow
### Failure Paths
### Data Exposure Risks
### Improvement Opportunities
