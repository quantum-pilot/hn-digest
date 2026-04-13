# How Complex is my Code?

- Score: 170 | [HN](https://news.ycombinator.com/item?id=47673171) | Link: https://philodev.one/posts/2026-04-code-complexity/

### TL;DR
The article surveys different meanings of “code complexity”: from classic computational complexity (Big-O) to code-level metrics like cyclomatic and Halstead, then argues that human mental effort is at least as important as machine cost. Drawing on psycholinguistics, it connects readability to familiarity, working-memory load, coherence, dependency distance, and entropy. Metrics are useful only when combined thoughtfully (e.g., with churn and coupling) and used as guides for refactoring decisions—not as targets to game or replace judgment.

---

### Comment pulse
- Complexity is pervasive; most effort fights accidental complexity → good abstractions occasionally “solve” entire problem classes, keeping software engineering interesting—counterpoint: increasing abstraction power also magnifies societal risks.
- Function-level metrics miss “Rube Goldberg” feature chains → reasoning about end-to-end workflows and data flow, often organizing code by feature, better captures real-world complexity.
- Tools that mix structural metrics with git churn can prioritize refactors → helps catch LLM-generated complexity early, but over-optimizing numbers risks Goodhart’s law and worse designs.

---

### LLM perspective
- View: Use multiple, human-centered complexity metrics to steer refactors and agent behavior, but always keep a human as the complexity arbiter.
- Impact: Helps tech leads, reviewers, and code agents focus on genuinely painful hotspots rather than large-but-stable or merely “ugly” files.
- Watch next: Benchmark psycholinguistic-style metrics on real teams, then integrate into CI/IDEs to auto-flag complex diffs and guide agents to simplify.
