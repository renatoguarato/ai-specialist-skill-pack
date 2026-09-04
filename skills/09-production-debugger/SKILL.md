---
name: production-debugger
description: Investiga incidentes de produção de forma orientada a evidências, correlacionando sintomas, logs, métricas, traces, deploys e dependências.
---

# Production Debugger

## Objetivo
Produzir hipóteses testáveis, não palpites.

## Workflow
1. Defina sintoma e janela temporal.
2. Determine blast radius.
3. Verifique mudanças recentes.
4. Correlacione:
   - logs;
   - métricas;
   - traces;
   - erros;
   - latência;
   - saturação;
   - filas;
   - banco;
   - serviços downstream.
5. Diferencie causa, efeito e ruído.
6. Monte hipóteses ordenadas por evidência.
7. Proponha formas seguras de validar.
8. Priorize mitigação antes da correção estrutural quando necessário.

## Saída
### Incident Summary
### Timeline
### Evidence
### Hypotheses
| Hipótese | Evidência a favor | Evidência contra | Como validar |

### Mitigation
### Root Cause Candidate
### Permanent Fix
