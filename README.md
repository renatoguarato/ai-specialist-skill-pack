# AI Specialist Skill Pack

Versão atual: **4.0.0**

Pacote de skills para acelerar onboarding, entendimento, investigação e evolução de aplicações desconhecidas.

## Objetivo

O pacote foi desenhado para um AI Specialist que entra em um contexto com múltiplas aplicações, baixo conhecimento inicial e necessidade de ganhar autonomia rapidamente.

Ele separa o trabalho em quatro estágios:

1. **Descoberta**
   - codebase-inventory
   - architecture-mapper
   - domain-model-discovery
   - database-model-explorer
   - aws-infrastructure-mapper

2. **Compreensão de comportamento**
   - request-flow-tracer
   - api-contract-analyzer
   - dependency-risk-auditor

3. **Mudança segura**
   - change-impact-analyzer
   - implementation-planner
   - test-strategy-analyzer
   - security-boundary-reviewer

4. **Operação e aprendizado contínuo**
   - production-debugger
   - observability-reviewer
   - knowledge-capture
   - technical-question-generator

A skill `application-onboarding-orchestrator` funciona como porta de entrada.

## Fluxo recomendado para uma aplicação nova

```text
application-onboarding-orchestrator
            |
            v
      codebase-inventory
            |
     +------+------+
     |             |
     v             v
architecture   domain-model
  mapper        discovery
     |             |
     +------+------+
            |
            v
    request-flow-tracer
            |
    +-------+-------+
    |               |
    v               v
api-contract    database-model
 analyzer        explorer
    |               |
    +-------+-------+
            |
            v
 aws-infrastructure-mapper
            |
            v
 dependency-risk-auditor
            |
            v
      knowledge-capture
```

## Uso diário

### Entender um sistema
> Use application-onboarding-orchestrator para me explicar esta aplicação. Comece pelo inventário e separe fatos de hipóteses.

### Entender um fluxo
> Use request-flow-tracer para rastrear o fluxo de criação de pagamento desde o endpoint até banco e eventos.

### Antes de alterar código
> Use change-impact-analyzer para avaliar o impacto deste requisito antes de sugerir implementação.

### Implementar
> Use implementation-planner e gere um plano incremental com testes, observabilidade, rollout e rollback.

### Incidente
> Use production-debugger. Não assuma causa raiz; monte hipóteses ordenadas por evidência.

## Estrutura

Cada skill fica em:

```text
skills/<skill-name>/SKILL.md
```

O formato foi mantido simples e portátil para ser adaptado a agentes de código e ferramentas que suportam skills/instructions por diretório.

## Contrato v4

Todas as skills permanecem utilizáveis isoladamente e agora seguem um contrato operacional comum: escopo explícito, evidências rastreáveis, estado de conhecimento, riscos priorizados, desconhecidos decisivos, próximas ações, critérios de parada e handoff. As referências em `references/` aprofundam taxonomias reutilizáveis sem serem necessárias para o carregamento básico da skill.

Para validar o pacote sem instalar dependências externas:

```bash
python3 scripts/validate_skill_pack.py
```

Os cenários em `evals/representative-scenarios.md` cobrem onboarding, fluxos, mudanças, incidentes, RAG, agentes, seleção de modelos, POCs, PRs e reuniões.

## Princípios do pacote

- Evidência antes de inferência.
- Código antes de documentação desatualizada.
- Separar fato, hipótese e desconhecido.
- Entender fluxo antes de alterar.
- Avaliar impacto antes de implementar.
- Observabilidade, segurança e testes fazem parte da mudança.
- Documentar conhecimento validado ao final.

## Camada AI Systems

O pacote também inclui skills especializadas para aplicações baseadas em IA generativa:

- ai-system-discovery
- llm-call-tracer
- prompt-analyzer
- rag-pipeline-analyzer
- retrieval-quality-analyzer
- agent-workflow-mapper
- tool-calling-analyzer
- llm-evaluation-designer
- hallucination-analyzer
- token-cost-analyzer
- model-selection-advisor
- context-window-analyzer
- guardrail-reviewer
- ai-observability-reviewer
- bedrock-architecture-analyzer
- ai-production-readiness

### Fluxo recomendado para uma aplicação com IA

```text
application-onboarding-orchestrator
          |
          v
   ai-system-discovery
          |
   +------+------+----------------+
   |             |                |
   v             v                v
 RAG          Agents            LLM Calls
   |             |                |
   v             v                v
retrieval     tool-calling     prompt-analyzer
 quality        analyzer       context-window
   |             |                |
   +------+------+----------------+
          |
          v
 llm-evaluation-designer
          |
          v
 ai-observability-reviewer
          |
          v
 guardrail-reviewer
          |
          v
 ai-production-readiness
```

## Camada Daily Work

A terceira camada cobre o trabalho diário do AI Specialist:

- requirement-to-ai-solution
- technical-discovery-interviewer
- architecture-decision-record-writer
- ai-poc-designer
- experiment-designer
- stakeholder-technical-translator
- ai-business-value-analyzer
- technical-debt-prioritizer
- incident-postmortem
- pull-request-reviewer
- code-generation-guardrail
- technical-documentation-generator
- meeting-context-preparer
- ticket-context-builder
- repository-learning-plan
- risk-based-work-planner
- ai-specialist-daily-orchestrator

### Fluxo operacional

```text
                      AI SPECIALIST OS

        +----------------+----------------+----------------+
        |                |                |
        v                v                v
 Application         AI Systems       Daily Work
 Engineering
        |                |                |
 architecture       RAG / Agents      Discovery
 APIs               LLM / Evals       Decisions
 AWS                Guardrails        POCs
 Data               Cost / Obs        PR Review
 Security                            Docs / Meetings
```

Use `ai-specialist-daily-orchestrator` como porta de entrada para tarefas do dia a dia.
