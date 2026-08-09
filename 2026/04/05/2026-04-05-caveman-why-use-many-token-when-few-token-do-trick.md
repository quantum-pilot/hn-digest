# Caveman: Why use many token when few token do trick

- Score: 670 | [HN](https://news.ycombinator.com/item?id=47647455) | Link: https://github.com/JuliusBrussee/caveman

### TL;DR

A GitHub skill makes Claude Code and Codex answer in clipped caveman prose, preserving code and technical terms while removing articles, hedges, and pleasantries. Its headline claims—about 75% fewer output tokens, unchanged accuracy, and triple speed—apply only to visible output and come from preliminary, non-rigorous testing; reasoning tokens remain unaffected. The author calls it a joke and plans proper evaluation. Commenters debated whether terse style improves semantic density or consumes model attention, creates ambiguity, and impoverishes future conversational context.

### Comment pulse

- Short prompts often yield short answers → a permanent skill may add context overhead for behavior models already support.
- Visible brevity reduces reading and output cost → total tokens, latency, task success, and correction loops determine real savings.
- Less explanation can preserve focus → omitted rationale may damage reviewability and later context.

### LLM perspective

- **View:** Treat the plugin as a presentation preset, not an efficiency breakthrough, until end-to-end evaluations support its claims.
- **Impact:** Teams may save review time on routine tasks but lose auditability on ambiguous or high-risk work.
- **Watch next:** Reproducible benchmarks separating reasoning and output tokens, latency, correctness, retries, and long-session degradation.
