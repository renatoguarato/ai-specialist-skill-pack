# Operating Contract

Use this contract for every mode in the pack.

## Evidence

- Cite the source of each material conclusion: file, symbol, line, configuration, test, log, metric, trace, ticket or explicit human input.
- Distinguish static evidence, runtime evidence and human-provided information.
- Record relevant negative evidence when something was searched and not found.

## Knowledge state

- **Confirmed:** directly supported by sufficient evidence.
- **Inferred:** derived from multiple pieces of evidence but not observed directly.
- **Hypothesis:** plausible and still unvalidated.
- **Unknown:** insufficient data; state the smallest validation needed.

## Required ending

Every result ends with:

1. summary of the question answered;
2. evidence and conclusions with knowledge state;
3. prioritized risks by impact and probability;
4. decisive unknowns;
5. ordered next actions with validation and rollback when relevant;
6. handoff to the next mode when applicable.

## Boundaries

Do not expand scope into unrelated refactors, migrations or integrations. Do not perform destructive, production or sensitive-data actions without explicit authorization and proportional validation.
