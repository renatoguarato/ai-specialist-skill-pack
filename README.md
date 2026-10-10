# AI Specialist Skill Pack

Versão atual: **6.0.0**

Pack de skills para entender repositórios, encontrar e implementar melhorias, operar sistemas, analisar IA e tomar decisões técnicas.

## Devin CLI (instalação recomendada)

Este repositório inclui o plugin `.devin-plugin/plugin.json`, instruções em `AGENTS.md`, skills especializadas e papéis de subagentes em `agents/`.

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
devin plugins install .
devin plugins list
```

Leia [DEVIN_CLI.md](DEVIN_CLI.md) para fluxos de onboarding, tracing entre repositórios, implementação aprovada, avaliação de IA e handoff. A pasta `agents/` contém instruções de papéis, não subagentes automaticamente registrados. O plugin deve ser validado em uma instalação real do Devin CLI.

## Instalação rápida (legado / outros agentes)

O instalador usa apenas Python 3 e instala o perfil `standard` com cinco skills:

```bash
python3 /caminho/ai-specialist-skill-pack/install.py /caminho/do/projeto
```

Perfis opcionais:

```bash
python3 /caminho/ai-specialist-skill-pack/install.py /caminho/do/projeto --profile ai
python3 /caminho/ai-specialist-skill-pack/install.py /caminho/do/projeto --profile delivery
python3 /caminho/ai-specialist-skill-pack/install.py /caminho/do/projeto --profile full
```

| Perfil | Skills adicionadas |
|---|---|
| `standard` | entrada, discovery, mudanças e confiabilidade |
| `ai` | standard + análise de sistemas de IA, tracing multi-repo e avaliações |
| `delivery` | standard + requisitos, delivery e implementação |
| `full` | todas as dez skills públicas |

O instalador cria `.agents/skills`, adiciona um bloco controlado ao `AGENTS.md` e registra a instalação em `.ai-specialist-pack/pack.lock.json`.

## Primeiro uso

Abra uma nova sessão do agente no projeto e use:

```text
Use ai-specialist para descobrir melhorias neste repositório.
Comece com repository-discovery no modo inventory.
Depois priorize os achados com change-engineering no modo debt.
Não altere arquivos ainda; cite arquivo, símbolo e linha.
```

Para usar um modo diretamente:

```text
Use change-engineering no modo impact para esta melhoria: [descreva a melhoria].
```

## Fluxos recomendados

### Descobrir melhorias

```text
Use repository-discovery no modo inventory para mapear áreas frágeis,
duplicadas, pouco testadas, acopladas ou difíceis de manter.
Não proponha refatorações cosméticas.
```

```text
Use change-engineering no modo debt para priorizar os achados por impacto,
frequência, risco, esforço e custo de atraso. Retorne no máximo cinco itens.
```

### Implementar uma melhoria

```text
Use change-engineering no modo impact para validar este achado:
[achado e evidências]
```

```text
Use change-engineering no modo tests e implementation.
Defina testes, critérios de aceite, rollout, rollback e condição de parada.
Não edite código até o plano estar completo.
```

### Incidentes e IA

Use `production-reliability` para `debug`, `observability`, `security`, `dependencies`, `capacity` ou `postmortem`.

Use `ai-systems` para `discovery`, `llm`, `prompt`, `rag`, `retrieval`, `agents`, `tools`, `evals`, `hallucination`, `cost`, `context`, `model`, `guardrails`, `bedrock` ou `readiness`.

Use `product-delivery` para `requirements`, `interview`, `adr`, `system-design`, `poc`, `experiment`, `translation`, `business-value`, `documentation`, `meeting` ou `ticket`.

Use `repository-discovery / onboarding` para construir um mapa de entrada de um sistema desconhecido e `product-delivery / system-design` para transformar requisitos em uma arquitetura avaliável.

## Atualização e migração

Atualizações são explícitas:

```bash
python3 /caminho/ai-specialist-skill-pack/install.py update /caminho/do/projeto
python3 /caminho/ai-specialist-skill-pack/install.py validate /caminho/do/projeto
```

Instalações da versão 4 devem ser migradas explicitamente:

```bash
python3 /caminho/ai-specialist-skill-pack/install.py migrate /caminho/do/projeto
```

Antes de escrever, simule:

```bash
python3 /caminho/ai-specialist-skill-pack/install.py /caminho/do/projeto --dry-run
```

Conflitos exigem `--force`. A remoção preserva arquivos modificados localmente:

```bash
python3 /caminho/ai-specialist-skill-pack/install.py uninstall /caminho/do/projeto --yes
```

Consulte [`MIGRATION.md`](MIGRATION.md) para a conversão dos nomes da v4 para modos da v5.

## Estrutura

As dez skills públicas são pequenas portas de entrada. Checklists detalhados vivem em `references/modes/` e são lidos somente quando o modo correspondente é necessário. O contrato compartilhado está em `references/operating-contract.md`.

Validação do pack:

```bash
python3 scripts/validate_skill_pack.py
```
