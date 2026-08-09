# Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47897790) | Link: https://alash3al.github.io/stash?_v01

### TL;DR

Stash is an Apache-2.0 memory service for MCP-compatible agents, backed by PostgreSQL and pgvector. It records episodes in hierarchical namespaces, consolidates them into facts, relationships, causal links, patterns, contradictions, goals, failures, and hypotheses, and exposes 28 tools to any OpenAI-compatible model. Its pitch is portable, user-owned continuity beyond platform memory and raw document retrieval. Hacker News remained skeptical: critics saw ordinary vector search plus explicit recall and remember calls, no benchmarks, and risks of stale context; others preferred background chat summarization, selective end-of-session notes, or contextual recall.

### Comment pulse

- Automatic history summarization feels closer to Claude.ai memory — counterpoint: some users report agent-triggered storage creates more purposeful structures.
- Rich terminology does not establish better retrieval; critics wanted benchmarks against plain vector search and details beyond marketing claims.
- Selective memory may age better: preserve rejected alternatives and rationale that neither model knowledge nor source code can recover.

### LLM perspective

- **View:** Durable agent memory is primarily a relevance, updating, and forgetting problem rather than a storage problem.
- **Impact:** A credible portable layer could reduce platform lock-in, but bad recall can quietly bias every downstream session.
- **Watch next:** Longitudinal retrieval benchmarks, deletion semantics, contradiction handling, provenance, privacy controls, and comparisons with simple log files.
