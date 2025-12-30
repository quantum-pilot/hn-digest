# You can't design software you don't work on

- Score: 227 | [HN](https://news.ycombinator.com/item?id=46418415) | Link: https://www.seangoedecke.com/you-cant-design-software-you-dont-work-on/

### TL;DR
The essay argues that meaningful software design for large, evolving systems can only be done by engineers actively working in the code, because real decisions hinge on local, messy constraints: existing APIs, data flow, deployment quirks, and half‑finished migrations. Generic design principles and “architect-only” planning mostly fail here; their proper role is guiding greenfield projects, standardizing tie‑break choices across teams, and steering company‑wide infrastructure bets. HN comments debate the value of consistency, the usefulness of architects, and how much generic theory still helps.

---

### Comment pulse
- Over-fragmented microservices hurt: too many services per team, many integrations, and basic issues (like timestamp formats) compound coordination and reliability problems.  
- Architects often just rubber‑stamp proposals; short engineer tenures limit deep system understanding, so real design tends to be local and constrained.  
- Generic theory gives vocabulary and mental models; critics of “consistency first” fear it ossifies bad patterns, defenders say uniformity boosts org throughput and cross‑team maintainability.

---

### LLM perspective
- View: Static “best practices” are weak without precise knowledge of concrete dependencies, data shapes, and failure modes in a specific system.  
- Impact: Incentivizes senior engineers and “architects” to stay hands‑on, and for orgs to value deep codebase familiarity over portable buzzwords.  
- Watch next: Tools that surface real dependency graphs, runtime behavior, and change impact could let more people safely participate in genuinely concrete design.
