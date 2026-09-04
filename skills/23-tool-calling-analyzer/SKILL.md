---
name: tool-calling-analyzer
description: Analisa definição, uso, autorização e riscos de ferramentas expostas a modelos e agentes.
---

# Tool Calling Analyzer

## Analise
Para cada tool:
- descrição;
- schema;
- argumentos;
- validação;
- permissões;
- efeitos colaterais;
- idempotência;
- retry;
- timeout;
- auditoria;
- rollback.

## Riscos
- tool injection;
- privilege escalation;
- broad permissions;
- destructive actions;
- ambiguous schemas;
- missing validation;
- retries não idempotentes.

## Saída
| Tool | Purpose | Side Effect | Permission | Risk |

### High Risk Tools
### Schema Problems
### Permission Problems
### Recommended Controls
