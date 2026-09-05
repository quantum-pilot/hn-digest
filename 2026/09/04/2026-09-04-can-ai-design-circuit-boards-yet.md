# Can AI design circuit boards yet?

- Score: 265 | [HN](https://news.ycombinator.com/item?id=49569366) | Link: https://eebench.org/blog/can-ai-design-circuit-boards-yet/

### TL;DR

The atopile team argues that AI can already solve a growing subset of circuit-design tasks, but credible evaluation requires more than screenshots or syntactically valid boards. Its EEBench V1 lets agents edit declarative circuit code, then deterministically grades simulations, component tolerances, availability, and cost across 13 analog and digital tasks. The reported leaderboard peaks at 61.6%, and GPT-6 Astra has not yet been tested. EEBench excludes layout, manufacturing, and bring-up, so its results support bounded design assistance rather than autonomous product engineering.

### Comment pulse

- Experienced hobbyists reported working fabricated boards with repairable mistakes, while stressing that expert verification remained essential.
- Others favored agents generating deterministic board scripts instead of directly manipulating graphical CAD tools.
- One commenter noted that choosing a capacitor is elementary; the benchmark’s value lies in sizing and worst-case verification.

### LLM perspective

- View: Simulation-backed tests turn plausible circuit generation into measurable engineering, while leaving physical validation unresolved.
- Impact: Skilled designers may iterate faster; novices risk accepting failures they cannot recognize or repair.
- Watch next: Astra results, harder tasks, layout grading, manufactured-board yield, and independent benchmark replication.
