# Qwen3-Max-Thinking

- Score: 402 | [HN](https://news.ycombinator.com/item?id=46766741) | Link: https://qwen.ai/blog?id=qwen3-max-thinking

### TL;DR

Alibaba’s Qwen team presents its latest model as comparable with GPT-5.2-Thinking, Claude Opus 4.5, and Gemini 3 Pro across 19 vendor-reported benchmarks. Results are mixed: it leads on tool-assisted HLE and Arena-Hard, but trails competitors on knowledge, coding, tool-use, and long-context tests. Qwen Chat adds automatic Search, Memory, and Code Interpreter selection, while a heavy mode iteratively distills prior attempts. OpenAI- and Anthropic-compatible APIs are available, but commenters want pricing, latency, and token usage alongside scores.

### Comment pulse

- Benchmark rank lacks economic context → heavier inference may buy accuracy, yet the release omits comparative cost, speed, energy, and token counts.
- Censorship may be deployment-specific → one hosted prompt was rejected — counterpoint: earlier downloadable Qwen models reportedly answered the topic fully.
- Search can alter model comparisons → retrieval quality and source filters influence tool-assisted scores independently of base reasoning.

### LLM perspective

- View: Strong vendor results justify testing, not equivalence claims across uncontrolled evaluation stacks.
- Impact: Developers gain another protocol-compatible model, but must evaluate policy constraints and total inference cost for their workloads.
- Watch next: Independent benchmarks, heavy-mode token budgets, regional pricing, latency, downloadable weights, and hosted-versus-local safety behavior.
