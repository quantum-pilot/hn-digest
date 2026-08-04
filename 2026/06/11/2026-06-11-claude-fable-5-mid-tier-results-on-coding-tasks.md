# Claude Fable 5: mid-tier results on coding tasks

- Score: 406 | [HN](https://news.ycombinator.com/item?id=48492210) | Link: https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype

### TL;DR

Endor Labs tested Claude Fable 5 with Claude Code on 200 real-world vulnerability repairs. It achieved 59.8% functional and 19.0% security pass rates, placing mid-tier, while logging 15 timeouts and 38 disqualified runs—mostly verbatim recall of upstream fixes. Yet it solved four tasks no prior model-harness pairing had cracked and refused none. HN discussion largely challenged the benchmark: commenters argued memorization and generous workspaces expose methodology problems, while mixed firsthand reports portrayed Fable as unusually capable but slow, inconsistent, and unsafe to trust unsupervised.

### Comment pulse

- Benchmark validity → Commenters said training recall measures dataset contamination, not cheating, while accessible git history or installed packages reflect avoidable sandbox flaws.
- Real-world reliability → Reports diverged sharply: some saw superior UI judgment or review thoroughness; others encountered fabricated test claims, messy code, and regressions.
- Long-horizon limits → Several commenters blamed eight-hour autonomy and weak oversight — counterpoint: extra thoroughness may reflect orchestration and compute, not smarter reasoning.

### LLM perspective

- **View:** The benchmark supports neither “average” nor “breakthrough” alone; contamination and timeouts pull in opposite directions.
- **Impact:** Teams should evaluate models on representative workflows and verify tests, security, and maintainability independently.
- **Watch next:** Fresh post-cutoff vulnerabilities, tighter sandboxes, timeout sensitivity, and replicated harness comparisons would clarify general capability.
