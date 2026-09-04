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


### Controles especialistas de aplicações

- Mapeie símbolo, chamada, dado transformado, persistência, evento e dependência; não trate nomes de pastas como arquitetura.
- Separe fluxo feliz, falhas, retries, timeouts, transação, concorrência e efeitos assíncronos.
- Para mudanças, identifique consumidores, compatibilidade, migração, rollout, observabilidade e rollback antes de sugerir código.
- Para produção, priorize mitigação reversível e correlacione janela temporal, deploy, blast radius e sinais de telemetria.
- Para segurança, explicite trust boundaries, ativo protegido, pré-condição de exploração e evidência; não declare vulnerabilidade apenas por padrão textual.
