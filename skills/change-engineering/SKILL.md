---
name: change-engineering
description: Encontra, prioriza, planeja, implementa e revisa melhorias e mudanças de código com baixo risco.
---

# Change Engineering

Escolha um modo: `impact`, `debt`, `risk`, `tests`, `implementation`, `guardrails` ou `review`.

Para qualquer mudança relevante, siga `impact` → `tests`/`risk` → `implementation` → `guardrails` → `review`. Prefira passos pequenos, compatíveis e reversíveis. Não introduza framework, migração ou refatoração fora do escopo sem decisão explícita.

Saída mínima: problema e evidência, estado do conhecimento, impacto, riscos, critérios de aceite, próximos passos, validação e rollback. Para o workflow do modo, leia `references/modes/change-engineering.md`; para o contrato, leia `references/operating-contract.md`.
