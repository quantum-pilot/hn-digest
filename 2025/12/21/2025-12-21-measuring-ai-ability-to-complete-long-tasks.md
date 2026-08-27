# Measuring AI Ability to Complete Long Tasks

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46342166) | Link: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

### TL;DR

METR measures agent capability by the human-expert time required for tasks completed at a chosen reliability. Across multi-step software and reasoning evaluations, its estimated 50%-success horizon doubled about every seven months over six years: models nearly always solved sub-four-minute tasks but rarely solved tasks beyond roughly four hours. Continued exponential growth would imply week-long tasks within several years, though METR acknowledges task-selection, human-baseline, trend-change, and external-validity uncertainty. Commenters stressed that human-equivalent duration measures complexity, not agent runtime, making cheap retries potentially useful despite 50% reliability.

### Comment pulse

- Real projects suggest agents can remove incidental toil, but users risk losing understanding or inheriting unmaintainable code.
- Human checkpoints may catch drift; counterpoint: inexpensive parallel attempts can make failure acceptable without continuous supervision.

### LLM perspective

- View: Human-equivalent duration is interpretable, but reliability and recovery determine operational usefulness.
- Impact: Longer horizons expand delegated project scope while increasing the cost of unnoticed compounding errors.
- Watch next: Replicate across messy domains and measure backtracking, verification cost, agent runtime, and 80%-success horizons.
