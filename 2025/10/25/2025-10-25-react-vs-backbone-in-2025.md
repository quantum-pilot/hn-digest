# React vs. Backbone in 2025

- Score: 271 | [HN](https://news.ycombinator.com/item?id=45702558) | Link: https://backbonenotbad.hyperclay.com/

### TL;DR

A small side-by-side app leads the author to argue that React has changed frontend complexity more than reduced it. Backbone exposes event handlers and DOM mutations directly; React reads declaratively but introduces keys, controlled inputs, effects, identity stabilization, stale closures and reconciliation behavior that developers must learn. The author asks whether this abstraction cost suits ordinary applications. Commenters counter that the example omits the problems React addressed: composition, unidirectional state flow, efficient updates and large-scale lifecycle management. The comparison therefore illuminates tradeoffs but cannot establish fifteen years of stagnation.

### Comment pulse

- Former Backbone users recall cascading state changes and manual component lifecycles becoming painful well below thousand-component scale.
- Others agree popularity and hiring ecosystems can entrench frameworks beyond their technical fit for a specific project.

### LLM perspective

- View: React replaces explicit coordination with declarative invariants; neither model eliminates complexity, but they locate it differently.
- Impact: Small apps may pay abstraction overhead, while evolving applications benefit from standardized composition and state propagation.
- Watch next: Choose using expected state complexity and maintenance context, not toy line counts or framework prestige.
