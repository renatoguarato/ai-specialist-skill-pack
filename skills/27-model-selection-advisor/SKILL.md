---
name: model-selection-advisor
description: Compara modelos para um caso de uso considerando qualidade, custo, latência, contexto, ferramentas e requisitos operacionais.
---

# Model Selection Advisor

## Critérios
- task type;
- reasoning;
- structured output;
- tool use;
- context size;
- latency;
- cost;
- availability;
- region;
- compliance;
- multimodality.

## Saída
### Workload Profile
### Required Capabilities
### Candidate Models
### Trade-off Matrix
### Recommended Primary Model
### Recommended Fallback
### Evaluation Needed

Não selecione modelo apenas por benchmark genérico.

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


### Controles especialistas de sistemas de IA

- Trace a cadeia causal: entrada → dados/contexto → prompt → modelo → ferramentas → pós-processamento → persistência/telemetria.
- Redija exemplos e logs com dados sensíveis redigidos; verifique isolamento de tenant e autorização antes de recuperar contexto.
- Separe qualidade do modelo, recuperação, grounding, sucesso da tarefa, segurança, latência e custo.
- Toda avaliação deve declarar dataset, baseline, métrica, limiar, casos adversariais e regra GO/NO-GO.
- Trate preço, quota, disponibilidade, ID de modelo, limite de contexto e comportamento de provedor como dados voláteis que exigem verificação atual.
- Para ferramentas e agentes, analise permissões efetivas, efeitos colaterais, idempotência, confirmação, auditoria, loops, retries e condição de término.

### Referência de IA

Consulte [qualidade e segurança de IA](../../references/ai-quality-safety.md) quando a análise envolver LLM, RAG, agente, ferramenta, Bedrock ou avaliação.
