---
name: codebase-inventory
description: Faz inventário estrutural de um repositório desconhecido e identifica stack, entrypoints, módulos, dependências, build, testes e pontos críticos.
---

# Codebase Inventory

## Objetivo
Criar uma visão inicial factual do repositório antes de interpretar arquitetura ou domínio.

## Workflow
1. Liste diretórios até profundidade suficiente para identificar módulos.
2. Localize:
   - arquivos de build;
   - manifests;
   - Dockerfiles;
   - CI/CD;
   - IaC;
   - configurações;
   - testes;
   - documentação.
3. Identifique linguagem, frameworks e versões.
4. Identifique entrypoints.
5. Identifique módulos internos.
6. Identifique dependências externas relevantes.
7. Localize código de integração:
   - HTTP;
   - banco;
   - filas;
   - eventos;
   - caches;
   - serviços cloud.
8. Localize mecanismos transversais:
   - autenticação;
   - autorização;
   - logs;
   - métricas;
   - tracing;
   - feature flags;
   - retry;
   - circuit breaker.
9. Não faça afirmações arquiteturais sem evidência.

## Saída
### Stack
### Entry Points
### Modules
### External Dependencies
### Persistence
### Messaging
### Cross-cutting Concerns
### Tests
### Delivery Pipeline
### Questions / Unknowns
