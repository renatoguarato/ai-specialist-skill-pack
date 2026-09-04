# Contrato operacional das skills

Este contrato é a referência comum da versão 4.0.0. Cada skill deve continuar funcionando quando somente sua `SKILL.md` for carregada; este arquivo concentra detalhes reutilizáveis.

## Evidência mínima

- Cite a origem da conclusão: arquivo e linha/símbolo, configuração, log, métrica, trace, contrato, ticket ou declaração explícita do usuário.
- Separe observação estática, evidência de runtime e informação fornecida por pessoas.
- Registre também evidência negativa relevante: algo procurado e não encontrado.
- Nunca converta convenção de framework em fato sobre o sistema sem confirmar no código/configuração.

## Estados de conhecimento

| Estado | Uso |
|---|---|
| Confirmado | Há evidência direta e suficiente. |
| Inferido | A conclusão resulta de múltiplas evidências, mas não foi observada diretamente. |
| Hipótese | Explicação plausível ainda não validada. |
| Desconhecido | Não há dados suficientes; indique como descobrir. |

## Saída mínima

Toda resposta deve terminar com:

1. resumo da pergunta respondida;
2. evidências e conclusões, com estado de conhecimento;
3. riscos priorizados por impacto e probabilidade;
4. desconhecidos que podem alterar a decisão;
5. ações seguintes ordenadas por valor e reversibilidade;
6. handoff para outra skill, quando aplicável.

## Controle de escopo

Não invente dados ausentes, não execute mudanças destrutivas sem autorização explícita e não amplie o pedido para refatorações, migrações ou integrações não necessárias. Quando a evidência for insuficiente para uma conclusão, pare a análise daquela conclusão e proponha a investigação mínima necessária.
