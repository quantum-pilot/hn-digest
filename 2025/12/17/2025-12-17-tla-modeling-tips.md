# TLA+ Modeling Tips

- Score: 109 | [HN](https://news.ycombinator.com/item?id=46299389) | Link: http://muratbuffalo.blogspot.com/2025/12/tla-modeling-tips.html

### TL;DR

Demirbas gives concrete advice for making TLA+ useful on real distributed systems: start from a tiny, abstract core and add detail only when omission demonstrably breaks correctness; specify *what* must hold instead of mirroring implementation control flow; avoid illegal global knowledge and overly coarse atomic steps; think in guarded commands rather than procedures; and systematically add TypeOK, safety, and liveness properties. Treat passing model checks with suspicion (inject bugs to test specs) and worry about TLC performance last. HN commenters discuss cultural resistance to TLA+, the steep learning curve, refinement as a practical technique, and how to invent good invariants for systems like collaborative editors.

---

### Comment pulse

- TLA+ is powerful but culturally hard to adopt → teams resist, refinement is underused, model checking gives instance-level proofs; hardware reality caps “perfect” correctness — counterpoint: steep learning curve and tooling still deter teams.

- Extra practice tips → separate machine vs environment, clarify assumptions, over-comment, use helpers, ASSUME/model values/constants, and understand semantic gaps between TLA+ and specific model checkers.

- Choosing properties is harder than modeling → examples for collaborative editing include eventual consistency, durability, causal consistency, per-user order, security, and conflict-resolution consistency.

---

### LLM perspective

- View: This post is a pragmatic checklist for treating TLA+ as a design tool, not a mathematical trophy or code simulator.

- Impact: Most relevant for teams building consensus, storage, and collaboration protocols that routinely ship subtle concurrency bugs.

- Watch next: LLM-assisted spec drafting, richer IDEs (e.g., Spectacle-like tools), and CI pipelines that routinely model-check critical flows.
