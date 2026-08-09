# Bombadil: Property-based testing for web UIs

- Score: 220 | [HN](https://news.ycombinator.com/item?id=47436592) | Link: https://github.com/antithesishq/bombadil

### TL;DR

Bombadil is an experimental MIT-licensed executable that fuzzes browser interfaces with randomized action generators and checks temporal correctness properties as the UI evolves. Default generators are picked randomly; custom JavaScript/TypeScript specs define generators and weights while inspecting DOM-derived state using linear temporal logic. It runs locally, in CI, or inside Antithesis. The author says reliable replay and shrinking are not implemented yet because browser runs can diverge and are slow. HN likes the single-binary design but wants realistic comparisons with Playwright or Cypress and clearer examples of found bugs.

### Comment pulse

- LTL monitoring expresses eventual and next-state properties over DOM snapshots → JavaScript closures can relate prior and later values.
- Random exploration finds unexpected flows — counterpoint: missing shrinking and shaky replay make failures harder to minimize and reproduce.
- A single executable avoids dependency sprawl → adoption still needs side-by-side examples showing maintenance advantages over scripted browser tests.

### LLM perspective

- **View:** The design combines stateful fuzzing and executable temporal specifications; its practical ceiling is reproducibility.
- **Impact:** Frontend teams could cover more interaction sequences, while framework noise may generate failures outside application code.
- **Watch next:** Best-effort replay, divergence detection, shrinking, deterministic demos, browser throughput, and head-to-head defect yield.
