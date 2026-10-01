# Solving Factorio Quality

- Score: 272 | [HN](https://news.ycombinator.com/item?id=49887343) | Link: https://exyr.org/2026/solving-factorio-quality/

### TL;DR

Factorio’s Quality system makes crafting and recycling probabilistic across five tiers, creating loops that resist ordinary resource accounting. The author models quality changes, filtering, crafting, recycling, and asteroid reprocessing as transition matrices, then solves long-run equilibrium with linear equations rather than approximating an infinite series. Examples quantify the large yield gap between destructive washing and upcycling, plus machine requirements and bottlenecks. The work culminates in an exact-rational TypeScript web calculator for planning quality-production systems.

### Comment pulse

- Linear solvers fit upcycling well → commenters independently built similar tools and praised the matrix formulation’s clarity.
- Small speed bonuses can improve practical throughput → expensive legendary machines, rather than raw inputs, often become the binding constraint.
- Some examples are version-sensitive → commenters note Factorio 2.1 removes quality from asteroid reprocessors, eliminating the described space casino.

### LLM perspective

- View: Equilibrium modeling turns repeated randomness into deterministic planning quantities without simulating every item journey.
- Impact: Players can size machines and compare strategies before committing scarce modules, space, and materials.
- Watch next: Update the calculator for Factorio 2.1 and test predicted throughput against measured factories.
