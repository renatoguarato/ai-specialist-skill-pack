---
name: technical-documentation-generator
description: Gera documentação técnica a partir de código e evidências, separando fato, inferência e lacuna.
---

# Technical Documentation Generator

## Tipos
- README;
- architecture overview;
- runbook;
- API guide;
- onboarding guide;
- troubleshooting;
- deployment guide.

## Regra
Nunca documente hipótese como fato.

## Saída
### Confirmed
### Inferred
### Unknown

Adapte a estrutura ao tipo de documento solicitado.

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


### Controles especialistas de decisão e execução

- Converta intenção em resultado observável, baseline, critérios de aceite e limites de escopo.
- Compare alternativas determinísticas e de IA antes de recomendar complexidade adicional.
- Diferencie decisão, recomendação, sugestão e pergunta pendente; registre trade-offs e custo de atraso.
- Todo plano de mudança deve indicar sequência, dependências, testes, observabilidade, rollout, rollback e condição de abortar.
- Ações devem ser pequenas, verificáveis e atribuíveis; não use 'melhorar' sem definir como medir.

### Referência de handoff

Consulte [roteamento e handoffs](../../references/routing-and-handoffs.md) para encadear discovery, decisão, implementação e validação.
