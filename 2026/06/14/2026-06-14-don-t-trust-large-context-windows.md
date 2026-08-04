# Don't trust large context windows

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48524620) | Link: https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows

### TL;DR

The article warns that advertised context capacity is not equivalent to reliable working memory: studies and experience suggest attention degrades gradually, with coding agents potentially entering a weak zone near 100,000 tokens. Auto-compaction helps only after quality has fallen and may summarize with an already-degraded model. The author instead starts fresh sessions from concise, human-written specs and stores decisions in PRDs, plans, and handoff artifacts. HN responses challenged any universal cutoff: usable range varies sharply by model, version, harness, and task, with some reporting strong performance beyond 500,000 tokens.

### Comment pulse

- Anecdotes cannot establish thresholds → standardized tests offer rigor — counterpoint: older studies may not describe current models, harnesses, or real agent workloads.
- Keep orchestration context lean → dispatch tool-heavy work to subagents and return compact results; one-level recursion reportedly handles million-line repositories without compaction.
- Persistent memory can become noise → concise repository docs, indexes, and checklists preserve decisions while remaining inspectable by humans and selectively retrievable.

### LLM perspective

- **View:** Context is a relevance budget, not storage; capacity claims matter only when retrieval quality survives realistic workloads.
- **Impact:** Agent systems shift toward hierarchical orchestration, explicit artifacts, and task-scoped sessions rather than endlessly accumulating transcripts.
- **Watch next:** Benchmark modern models by task accuracy across context positions, compaction timing, artifact retrieval, and subagent overhead.
