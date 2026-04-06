# Eight years of wanting, three months of building with AI

- Score: 573 | [HN](https://news.ycombinator.com/item?id=47648828) | Link: https://lalitm.com/post/building-syntaqlite-ai/

### TL;DR
An engineer spent eight years wanting serious SQLite devtools and finally shipped them—syntaqlite—after ~250 side‑project hours, largely by pairing tightly with AI coding agents. First, a “vibe‑coded” Claude-driven prototype proved feasibility but produced unmaintainable spaghetti he threw away. The successful Rust rewrite came from flipping the relationship: human owns architecture, taste, and review; AI handles boilerplate, refactors, research, and tedious rule generation. AI massively expanded project scope (tests, bindings, editors, docs) but worsened design procrastination, addiction loops, and loss of codebase understanding when over‑delegated.

---

### Comment pulse
- AI as accelerator, not replacement → Vibe-coded prototypes plus human-guided rewrites match many engineers’ experience; the real gain is 2–50% uplift on boring work.  
- Tests stay hard → AI inflates test counts yet misses behavior; people lean on specs, BDD, equivalence partitioning, or TLA+ to regain confidence.  
- Two usage modes → “All-knowing oracle” vs IDE assistant; commenters see the oracle path as a dead-end for sustainable systems and careers.

---

### LLM perspective
- View: This story models effective AI use: prototype → discard → design-first rewrite with aggressive refactoring, oracles, and strong test harnesses.  
- Impact: Makes ambitious infra and tooling projects feasible for solo devs; teams must adapt review, design, and testing habits, not abandon them.  
- Watch next: Tooling that tracks design history, enforces architectural constraints, and explores input spaces could push AI beyond local codegen into safer systems work.
