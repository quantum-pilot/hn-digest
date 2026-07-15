# The Tower Keeps Rising

- Score: 310 | [HN](https://news.ycombinator.com/item?id=48909785) | Link: https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/

### TL;DR
Ronacher argues that AI coding agents change the limiting factor in software: not individual productivity but shared understanding. Historically, the “language” of a system—its concepts, invariants, and ownership—was maintained through friction: reading code, reviews, arguments, and coordination. Agents remove this friction, enabling endless local changes without humans ever syncing on a common architectural model. Unlike Babel, construction doesn’t halt when mutual understanding collapses; the tower keeps rising, but becomes something humans can no longer reason about together.

---

### Comment pulse
- AI boosts local productivity but degrades global parsimony → agents happily duplicate concepts and abstractions, inflating complexity beyond what any human architect would tolerate.  
- Lisp Curse analogy → tools that make solo work easy reduce pressure to standardize and collaborate; AI risks turning every codebase into private DSLs and vibes.  
- Some see rising complexity as civilizational inevitability → others argue AI-as-plaster over bad foundations yields fragile systems and erodes human engineering skill.

---

### LLM perspective
- View: Agents should maintain and evolve explicit shared models (patterns, ownership maps, invariants) as a first-class artifact, not just emit code.  
- Impact: Tech leads, infra teams, and safety reviewers must treat architecture coherence and explainability as monitored, budgeted resources.  
- Watch next: Benchmarks for long-horizon refactors, tools that diff “system concepts” over time, and org policies requiring agent-authored design summaries.
