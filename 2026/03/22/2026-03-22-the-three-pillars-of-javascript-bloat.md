# The three pillars of JavaScript bloat

- Score: 441 | [HN](https://news.ycombinator.com/item?id=47473718) | Link: https://43081j.com/2026/03/three-pillars-of-javascript-bloat

### TL;DR

James Garbutt identifies three sources of JavaScript dependency bloat: compatibility machinery for obsolete engines and unusual realms, an “atomic” package culture that publishes trivial snippets separately, and ponyfills retained long after native support became universal. These choices multiply downloads, resolution work, duplicate versions, maintenance obligations, and supply-chain exposure for needs most projects do not share. He recommends questioning every package, removing unused dependencies with Knip, inspecting trees with npmgraph, and using e18e’s replacement data and migrations to prefer modern built-ins or leaner alternatives.

### Comment pulse

- Several developers report dependency-light projects staying stable and audit-friendly, though vanilla implementations can take longer and contain more application code.
- Critics call the three pillars marginal beside feature accumulation — counterpoint: micro-packages uniquely magnify metadata, update, and compromise costs.
- Legacy and unusual browsers remain real for some users, complicating any universal cutoff.

### LLM perspective

- **View:** Compatibility should be an explicit product requirement, not an inherited default buried deep in transitive dependencies.
- **Impact:** Modernizing dependency policy can turn periodic cleanup into a routine release-engineering discipline.
- **Watch next:** Environment-aware tooling that proves a native replacement matches each project’s actual runtime floor.
