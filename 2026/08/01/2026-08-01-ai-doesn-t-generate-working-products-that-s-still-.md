# AI doesn't generate working products, that's still your job

- Score: 249 | [HN](https://news.ycombinator.com/item?id=49132130) | Link: https://weeraman.com/the-prototype-isnt-the-product/

### TL;DR

AI can compress a software prototype from weeks to minutes, but the article argues it does not erase production engineering: scaling, security, error handling, observability, data design, concurrency, and maintainability still require judgment. Computer-science fundamentals therefore become more valuable, because reviewers must recognize plausible code that fails under real conditions. HN experiences were sharply mixed: autonomous changes often accumulated into coherent-looking architectural debt, while planned, tested, human-reviewed workflows produced internal tools and healthier codebases. Consensus clustered around treating generated code as raw material, with scope and risk determining acceptable oversight.

### Comment pulse

- Autonomy compounds local mistakes → individually reasonable patches can leave a system nobody fully understands or can safely extend.
- Structured collaboration works better → engineers report gains when they own architecture, approve detailed plans, constrain tasks, and review tests.
- Use case determines tolerance → disposable prototypes and low-risk tools benefit most — counterpoint: legacy or long-lived systems punish shallow reasoning.

### LLM perspective

- **View:** The scarce resource has shifted from code production to system comprehension, verification, and responsibility for long-term trade-offs.
- **Impact:** Experienced engineers gain leverage; novices risk dependency on implementations they cannot diagnose when requirements or load change.
- **Watch next:** Measure escaped defects, review time, architectural churn, maintenance cost, incident recovery, and comprehension after six months.
