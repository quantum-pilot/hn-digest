# DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost

- Score: 395 | [HN](https://news.ycombinator.com/item?id=48256953) | Link: https://esengine.github.io/DeepSeek-Reasonix/

### TL;DR
Reasonix is a terminal-native, open-source coding agent built specifically for DeepSeek models and their prefix cache. It keeps conversation history append-only and byte-identical so DeepSeek’s cache is hit on almost every turn, dramatically reducing token costs in long sessions. On top, it adds structured “thought harvesting,” robust tool-call repair, cost-aware context folding, and a TUI diff/plan workflow with checkpoints, MCP integration, and dashboards. HN discussion centers on whether such DeepSeek-specialization is necessary, versus generic harnesses and tradeoffs in UX, language choice, and cache-breaking strategies.

---

### Comment pulse
- Specialized harness vs generic agents → Some say simple DeepSeek bridges already get high cache hits; supporters argue most agents reorder prompts, dropping hit rates below 20% — counterpoint: blanket append-only may hurt quality.  
- Stack and UX concerns → Critics dislike the Codex-like, AI-generated marketing page, mobile issues, and Node-based stack; some prefer lean Rust/Go single-binary agents.  
- Harness design tradeoffs → Harness authors note they often break prefix cache intentionally after testing; want evidence DeepSeek warrants special handling before changing mainstream agents.

---

### LLM perspective
- View → DeepSeek-specific harnesses probe whether deeply exploiting provider quirks outperforms generic agent frameworks on cost and stability.  
- Impact → Heavy DeepSeek coding users, especially in long interactive sessions, may gain cheaper, more observable, resumable workflows.  
- Watch next → Independent τ-bench-style benchmarks vs OpenCode/Codex; RAM/latency comparisons; whether other vendors formalize similar cache guarantees.
