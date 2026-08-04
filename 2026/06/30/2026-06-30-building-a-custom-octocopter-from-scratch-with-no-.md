# Building a custom octocopter from scratch with no prior hardware experience

- Score: 320 | [HN](https://news.ycombinator.com/item?id=48704289) | Link: https://karolina.mgdubiel.com/drone/

### TL;DR

A sim-only PPO controller for an eight-motor drone reached 100% survival across hover, single-motor, and dual-motor failures by roughly 9.5 million steps, then handled some unseen triple failures. Progress stalled until two systemic bugs were found: hard-clipped actions lost corrective gradients outside motor bounds, and the survival bonus exactly canceled the hover altitude penalty. Tanh-squashed residual commands around hover and a larger survival reward fixed learning. The 43,400-parameter policy still lacks domain randomization or real-world validation; HN praised the project and raised structural and fabrication-safety questions.

### Comment pulse

- Expert feedback validated relevance → a NASA fault-tolerant octorotor researcher shared related control and UAV-physics material as a possible next reference.
- Airframe geometry remains open → commenters proposed a load-bearing ring or tiled hexagons, weighing shorter perimeter against central-component support and structural complexity.
- Composite machining needs precautions → commenters questioned tool wear and warned that G10 and carbon-fiber dust create serious inhalation hazards.

### LLM perspective

- **View:** The decisive gains came from aligning optimization geometry and incentives, not from tuning PPO harder.
- **Impact:** Safe action parameterization and reward sanity checks should precede long training runs in any constrained-control task.
- **Watch next:** Domain randomization, actuator latency, sensor noise, battery sag, mass variation, and controlled failure tests will determine transfer.
