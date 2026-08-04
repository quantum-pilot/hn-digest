# Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep

- Score: 125 | [HN](https://news.ycombinator.com/item?id=48169874) | Link: https://github.com/MinishLab/semble

### TL;DR

Semble is a local, CPU-only code-search library for coding agents, exposed through MCP, shell, or Python. It chunks repositories, combines static code embeddings with BM25, fuses rankings, and adds code-aware boosts and penalties. Across 1,250 queries, it reports NDCG@10 of 0.854, 263 ms indexing, 1.5 ms median queries, and 98% fewer retrieved tokens than grep-plus-file-reading. HN welcomed the idea but focused on agent integration behavior and comparisons with established alternatives.

### Comment pulse

- Benchmark skepticism focused on agent behavior: models may retry familiar grep or reread full files, erasing retrieval savings despite strong standalone metrics.
- Readers requested comparisons with LSPs, ck, colgrep, and harness-native search, reflecting uncertainty about whether Semble belongs as a tool or built-in capability.
- Semantic search appealed beyond agents because humans also need conceptual discovery when they lack an exact symbol or identifier.

### LLM perspective

- View: Token efficiency matters only if retrieval changes agent behavior; isolated recall cannot measure retries, verification loops, or task completion.
- Impact: Reliable adoption could lower inference cost and latency while freeing context for architecture, constraints, and edits.
- Watch next: Run controlled coding tasks with tool-call traces, completion quality, wall time, token totals, and grep fallback rates.
