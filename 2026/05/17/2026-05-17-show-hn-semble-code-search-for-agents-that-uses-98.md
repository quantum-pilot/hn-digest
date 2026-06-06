# Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep

- Score: 125 | [HN](https://news.ycombinator.com/item?id=48169874) | Link: https://github.com/MinishLab/semble

## TL;DR
Semble is a local-first, CPU-only semantic code search engine designed for AI agents. It chunks code, combines static code embeddings with BM25, and re-ranks with code-aware heuristics, achieving near-transformer retrieval quality while indexing whole repos in hundreds of milliseconds and answering queries in ~1.5 ms. Instead of grep+reading entire files, agents (or humans) ask natural-language or symbolic questions and receive only relevant snippets, saving ~98% tokens. HN discussion centers on real-world agent benchmarks, comparisons to LSPs/other tools, and harness-level integration.

---

## Comment pulse
- Agent behavior concern → Models are RL-tuned on grep; without fine-tuned prompts, they may distrust new tools and retry, erasing token savings.  
- Comparison gap → Commenters want head‑to‑head results vs LSPs and tools like ck and colgrep, not just grep or generic transformer baselines.  
- Integration questions → Some argue this belongs inside the harness so all agents benefit automatically; others note semantic search is directly useful for human developers too.

---

## LLM perspective
- View: Tools like Semble push agents toward structured retrieval workflows instead of ad‑hoc filesystem exploration, enabling more reliable multi-step coding sessions.  
- Impact: If widely adopted, agent providers could standardize on fast, local semantic search backends, lowering costs and improving latency for large codebases.  
- Watch next: Look for task-level benchmarks measuring bug-fix success, edit quality, and retries when swapping grep/LSP search for Semble-style retrieval.
