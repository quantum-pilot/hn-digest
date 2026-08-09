# Autoresearch on an old research idea

- Score: 244 | [HN](https://news.ycombinator.com/item?id=47493460) | Link: https://ykumar.me/blog/eclip-autoresearch/

### TL;DR

A researcher revived an older eCLIP project and let Claude Code run a constrained hypothesize-edit-train-evaluate loop on roughly 11,000 annotated Japanese prints. Across 42 short experiments on one RTX 4090, it committed 13 changes, reverted 29, and cut validation mean rank from 344.68 to 157.43; full training reached 34.30 test mean rank. The largest gain came from fixing a temperature clamp, then hyperparameter tuning, while architectural and moonshot ideas mostly failed. HN sees a reasoning-guided optimization tool whose value depends on cheap experiments, clear metrics, and sandboxing.

### Comment pulse

- Overnight search turns low-value suggestions into useful discoveries → it works only when trials are fast enough to waste.
- The loop resembles hyperparameter optimization with contextual judgment → unlike blind search, an LLM can inspect code and prior techniques.
- Extensive prompts and permissions invite skepticism — counterpoint: targeted scaffolding produced measurable gains while limiting arbitrary code and network access.

### LLM perspective

- **View:** The result demonstrates efficient bug-finding and tuning, not autonomous discovery in open-ended research.
- **Impact:** Researchers can delegate repetitive experiments while retaining metric design, dataset choices, safety boundaries, and final interpretation.
- **Watch next:** Held-out replication, median-rank optimization, compute and token costs, multi-change planning, longer runs, and comparisons with AutoML baselines.
