# Python JIT project was asked to pause development

- Score: 140 | [HN](https://news.ycombinator.com/item?id=48425982) | Link: https://discuss.python.org/t/an-announcement-from-the-steering-council-regarding-the-jit-project/107638

### TL;DR

Python’s Steering Council asked that no new JIT features, optimizations, or performance work land on CPython’s main branch until a Standards Track PEP wins approval; bug and security fixes may continue. The PEP must define maintenance, compatibility, measurable targets, architecture stability, and relationships with third-party JITs. Without acceptance within six months, code would leave main, though council members described the deadline as flexible. HN debate split between necessary governance for a complex runtime subsystem and fears that the freeze, broad requirements, and fork-based work will dissipate contributors and momentum.

### Comment pulse

- Scope → Critics called multi-strategy infrastructure and broad requirements a poison pill — counterpoint: supporters say permanence demands evaluating options and sustainable ownership.
- Freeze semantics → Some rejected the title because only new main-branch work stops; developers replied that forks create merge friction and exclude volunteers.
- Threshold → Commenters disagreed whether recent gains justify JIT complexity, exposing an unresolved question: what speedup, memory cost, and platform reach merit permanence.

### LLM perspective

- **View:** A feature can outperform its baseline yet remain unready for permanence when ownership and ecosystem costs lack agreement.
- **Impact:** Redistributors and tooling authors could gain explicit guarantees; rejection would move JIT evolution outside CPython.
- **Watch next:** Working-group formation, draft timing, community participation, acceptance criteria, and whether the council grants an extension.
