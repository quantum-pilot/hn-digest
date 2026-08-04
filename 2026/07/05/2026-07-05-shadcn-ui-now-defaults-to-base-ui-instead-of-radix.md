# Shadcn/UI now defaults to Base UI instead of Radix

- Score: 271 | [HN](https://news.ycombinator.com/item?id=48791328) | Link: https://ui.shadcn.com/docs/changelog

### TL;DR

New shadcn/ui projects, creation flows, and documentation now default to Base UI, reflecting a 2:1 user preference and Base UI’s reported 6 million weekly downloads at version 1.6. Radix remains supported, receives parallel updates, and requires no migration; noninteractive setups expecting it should pass `-b radix`. Optional migrations use an agent skill instead of a codemod, moving customized components incrementally, typechecking builds, writing per-component reports, and committing separately. HN debated whether vendored components justify bespoke upgrades, whether LLM skills should complement deterministic codemods, and whether headless libraries overproduce `div`-heavy markup.

### Comment pulse

- Vendoring split developers → selective component upgrades preserve customizations — counterpoint: package users prefer centralized version bumps and established libraries such as Mantine.
- Agent migrations intrigued readers → models can interpret modified code — counterpoint: deterministic codemods, linters, and human-readable guides remain safer for hard rules.
- Semantic HTML remained a concern → Base UI often renders generic containers where native elements might reduce markup and improve platform behavior.

### LLM perspective

- **View:** Default selection follows demonstrated adoption while avoiding a forced ecosystem migration, a notably conservative change-management choice.
- **Impact:** Maintainers are formalizing migration knowledge as executable agent context, potentially changing how copy-owned component ecosystems evolve.
- **Watch next:** Base-only components, accessibility regressions, migration-skill failure rates, token cost, semantic markup improvements, and long-term parity commitments.
