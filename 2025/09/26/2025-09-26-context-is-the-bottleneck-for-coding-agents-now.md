# Context is the bottleneck for coding agents now

- Score: 164 | [HN](https://news.ycombinator.com/item?id=45387374) | Link: https://runnercode.com/blog/context-is-the-bottleneck-for-coding-agents-now

- TL;DR
    - The post argues coding agents now fail from missing context, not intelligence: models can ace contests but stall beyond one-commit tasks without understanding codebase structure, conventions, historical rationale, deployment practices, and product/business constraints. Much of this knowledge is scattered, requiring preprocessing and human gap-filling; agents should detect missing context and ask. HN debate: some blame attention/forgetting over context size, others doubt real intelligence gains; many emphasize clarifying business intent. Takeaway: prioritize human-in-the-loop workflows and richer org-context pipelines over raw model upgrades.

- Comment pulse
    - Bottleneck is focus/forgetting, not more context: models overweight stale exploration; need explicit pruning or human-curated “chat flows” — counterpoint: large codebases still exceed windows.
    - Business context trumps code: senior engineers ask clarifying questions; instruct agents to request missing details before coding; communication is solvable.
    - Skeptics: intelligence isn’t improving; benchmarks mislead; models hallucinate confidently; treat LLMs as junior tools; hiring resumes; some report wins in law/health.

- LLM perspective
    - View: Context ingestion isn’t enough; agents need selective memory, codebase schemas, and uncertainty-aware prompts to ask humans.
    - Impact: Teams will invest in context pipelines, governance of tribal knowledge, and agent UX for focus/forgetting controls.
    - Watch next: Benchmarks on multi-PR tasks, long-horizon repos, and “ask-or-act” rates; releases adding memory pruning and org-knowledge connectors.
