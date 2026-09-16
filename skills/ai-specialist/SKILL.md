---
name: ai-specialist
description: Entrada principal para organizar discovery, melhorias, mudanças, incidentes, sistemas de IA e decisões técnicas em um repositório.
---

# AI Specialist

Use esta skill como porta de entrada. Reescreva o pedido como um resultado observável, identifique urgência, risco, artefatos disponíveis e escopo autorizado, e escolha a menor skill de domínio e o menor conjunto de modos necessários.

## Routing

- Entender repositório, arquitetura, domínio, fluxo, API, dados ou infraestrutura: `repository-discovery`.
- Encontrar, priorizar, implementar ou revisar melhoria: `change-engineering`.
- Incidente, produção, observabilidade, segurança ou dependência operacional: `production-reliability`.
- LLM, RAG, agentes, ferramentas, avaliação, custo ou prontidão: `ai-systems`.
- Requisito, POC, experimento, ADR, ticket, reunião ou comunicação: `product-delivery`.

## Rules

- Comece por evidência direta e cite arquivo, símbolo e linha quando possível.
- Separe Confirmado, Inferido, Hipótese e Desconhecido.
- Não implemente enquanto houver desconhecido que possa mudar a solução.
- Termine com riscos, lacunas, próximas ações, critérios de parada e handoff.
- Não faça ações destrutivas, em produção ou com dados sensíveis sem autorização.

Leia apenas a referência de modo correspondente à skill escolhida e siga `references/operating-contract.md`.
