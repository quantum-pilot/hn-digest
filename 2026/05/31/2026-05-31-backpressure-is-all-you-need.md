# Backpressure is all you need

- Score: 132 | [HN](https://news.ycombinator.com/item?id=48345090) | Link: https://www.lucasfcosta.com/blog/backpressure-is-all-you-need

### TL;DR
The post argues that current ways of using coding agents are either reckless (run unattended, drown reviewers in bad PRs) or too constrained (treat them as autocomplete). The proposed middle ground is “backpressure”: a layered set of automated gates—tests, types, linting, benchmarks, review agents, visual checks, and PR monitoring—that the agent must pass repeatedly while working. This shifts validation from humans to tooling, enabling longer, safer autonomous runs, while Hacker News debates originality, terminology, costs, and better primitives like hooks.

---

### Comment pulse
- This is already standard for some: build orchestration harnesses so agents run containers, tests, e2e flows, then report when done—productivity up, but token spend is worrying.  
- Several object to calling this “backpressure”; these are fixed validation gates, not dynamic producer–consumer balancing—author concedes the metaphor may be off.  
- Others see it as structured feedback loops; suggest deterministic hooks and queues instead of more LLMs for pass/fail checks, but note current agent SDKs are weak.

---

### LLM perspective
- View: Treat LLMs as over-eager juniors behind hard, automated gates; design workflows, not prompts, to constrain them.  
- Impact: Teams that already have good CI/tests/types can adopt this fastest; weaker codebases will struggle to automate “no.”  
- Watch next: Native agent workflow APIs (hooks, goals), cheaper mid-tier models for loops, and shared specs like BACKPRESSURE.md-style contracts.
