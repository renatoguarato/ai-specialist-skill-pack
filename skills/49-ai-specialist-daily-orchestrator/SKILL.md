---
name: ai-specialist-daily-orchestrator
description: Orquestra o fluxo diário de trabalho de um AI Specialist entre discovery, análise, decisão, implementação e validação.
---

# AI Specialist Daily Orchestrator

## Objetivo
Escolher a próxima skill correta conforme a tarefa.

## Routing
### Novo sistema
repository-learning-plan -> application-onboarding-orchestrator

### Novo requisito
technical-discovery-interviewer -> requirement-to-ai-solution -> architecture-decision-record-writer

### POC
ai-poc-designer -> experiment-designer -> llm-evaluation-designer

### Mudança em código
change-impact-analyzer -> implementation-planner -> code-generation-guardrail -> pull-request-reviewer

### Incidente
production-debugger -> incident-postmortem

### Reunião
meeting-context-preparer -> stakeholder-technical-translator

### Ticket
ticket-context-builder -> change-impact-analyzer

### Iniciativa de IA
ai-business-value-analyzer -> ai-system-discovery -> ai-production-readiness

## Regra final
Sempre terminar com:
- decisão tomada;
- evidências;
- riscos;
- próximos passos;
- lacunas de conhecimento.
