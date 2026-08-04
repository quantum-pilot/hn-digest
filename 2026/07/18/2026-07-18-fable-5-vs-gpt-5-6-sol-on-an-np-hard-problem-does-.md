# Fable 5 vs. GPT-5.6 Sol on an NP-Hard Problem: Does /goal help?

- Score: 205 | [HN](https://news.ycombinator.com/item?id=48956879) | Link: https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/

### TL;DR

On KIRO, an unpublished NP-hard fiber-network optimization task, Fable 5 and GPT-5.6 Sol each received three matched 30-minute runs with and without goal mode. Goal produced lower scores in four of six pairs, yet worsened average performance because occasional regressions dwarfed its typical modest gains: Fable’s mean rose 759 points and Sol’s 868, where lower is better. Fable delivered the best score and tighter plain-run consistency. The study concludes that persistence amplifies strategy quality rather than supplying intelligence; its narrow task, small sample, sequential services, and eight-CPU environment limit generalization.

### Comment pulse

- Goal is not a harder-thinking switch → it prolongs the active strategy, helping good basins but giving poor solvers more time to entrench.
- Identical commands hide different control loops → Claude uses a transcript-only evaluator; Codex persists state, exposes lifecycle tools, and resumes its working model.
- Model rankings remained workload-dependent → commenters reported opposite Claude-versus-Codex experiences across languages and tasks, favoring mixed toolchains over a universal winner.

### LLM perspective

- **View:** Persistence has asymmetric risk in open-ended search: small repeated improvements coexist with rare strategy failures that dominate expected performance.
- **Impact:** Goal mode may improve win rate while worsening expected outcomes, so averages and failure tails matter more than anecdotes.
- **Watch next:** Replicate across public tasks, larger samples, fixed hardware, multiple budgets, cost accounting, and alternative orchestration modes.
