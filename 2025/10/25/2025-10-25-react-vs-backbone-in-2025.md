# React vs. Backbone in 2025

- Score: 271 | [HN](https://news.ycombinator.com/item?id=45702558) | Link: https://backbonenotbad.hyperclay.com/

- TL;DR
  - The author compares equivalent Backbone (2010) and React (2025) apps to argue we’ve traded explicit, traceable verbosity for abstraction-induced gotchas (keys, controlled inputs, effects, stale closures) without clear net simplicity—especially for small apps. HN counters that React meaningfully improved composition, unidirectional data flow, and efficient updates, plus enables SSR and lazy-loading; complexity is mostly about state propagation. Many agree it’s tradeoffs and incentives (ecosystem, hiring). Alternatives like lit-html exist; pick tools per project, not dogma.

- Comment pulse
  - React fixed hard Backbone pain: composition, one-way state, efficient updates, SSR/lazy-loading → fewer ad-hoc patterns, better defaults, easier large app hygiene.
  - Simplicity vs. abstraction: Backbone’s explicitness aids debugging; React introduces keys/effects/closure gotchas — counterpoint: those tradeoffs yield a “pit of success” for state propagation.
  - Tooling choice: Use React everywhere to avoid rewrites; others prefer smaller stacks or lit-html → optimize for team skills, hiring, and project scope.

- LLM perspective
  - View: Favor explicit state/dataflow and predictable lifecycles; abstractions should surface identity hazards early with actionable errors.
  - Impact: Small/medium apps could shift to lighter libs (Preact, Solid, lit-html) without losing composition or SSR options.
  - Watch next: React Forget and Signals-based approaches; measurable reduction in effect/identity bugs; DX studies comparing debugging time across stacks.
