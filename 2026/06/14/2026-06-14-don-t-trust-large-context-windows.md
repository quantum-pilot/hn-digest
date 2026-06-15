# Don't trust large context windows

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48524620) | Link: https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows

### TL;DR
Large advertised context windows (200k–1M tokens) don’t behave uniformly: models have a “smart zone” where attention is reliable and a “dumb zone” where recall and reasoning degrade, often well before the limit. Coding agents rapidly push sessions into this dumb zone. The author treats context as a scarce budget: keep live context small, frequently start fresh sessions, and hand off via concise, human-written artifacts (specs, plans, PRDs). HN comments debate anecdotal impressions vs benchmarks and share various strategies for controlling context growth.

---

### Comment pulse
- LLM practice feels like cargo culting → non-determinism, rapid model churn, and weak theory make rigorous, shared “best practices” hard to establish or verify.  
- Constrain tools to recursive sub-calls → keep the main thread tiny while burning millions of tokens off-thread; aligns with user costs, not vendor revenue.  
- Long-context quality is model- and version-specific → some push Claude Opus to 800k tokens, others see failures <100k; cited studies may already lag current models.

---

### LLM perspective
- View: Design workflows assuming only a modest prefix is reliable, and periodically distill progress into external, structured documents the model can re-ingest.  
- Impact: Agent frameworks, IDE integrations, and “AI memory” systems should prioritize document generation, indexing, and retrieval over ever-larger flat context windows.  
- Watch next: Public long-context benchmarks on latest models, plus tools that visualize where attention/recall degrades across an active session.
