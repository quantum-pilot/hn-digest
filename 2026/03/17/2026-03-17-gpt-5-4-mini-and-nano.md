# GPT‑5.4 Mini and Nano

- Score: 203 | [HN](https://news.ycombinator.com/item?id=47415441) | Link: https://openai.com/index/introducing-gpt-5-4-mini-and-nano

### TL;DR

OpenAI’s GPT‑5.4 mini targets responsive coding, multimodal tool use, computer interaction, and subagents, running over twice as fast as GPT‑5 mini while scoring 54.4% on SWE-Bench Pro and 72.1% on OSWorld-Verified. Its API offers a 400k context window at $0.75 per million input tokens and $4.50 output; it also reaches Codex and ChatGPT. The API-only nano costs $0.20/$1.25 and targets classification, extraction, ranking, and simpler support work. HN reported strong release-day throughput but mixed instruction-following, pricing, and evaluation confidence.

### Comment pulse

- Raw speed impressed testers → mini reached roughly 180–190 tokens/second and nano about 200 — counterpoint: release-day load may understate normal latency.
- Throughput comparisons need context → time-to-first-token, reasoning effort, prompt processing, and total task completion can reverse tokens-per-second rankings.
- Small models divide users → constrained automation benefits from cost and responsiveness; complex agents still expose instruction-following and context-retention failures.

### LLM perspective

- **View:** Mini’s strongest case is orchestration economics: near-frontier narrow-task quality at substantially lower latency and quota use.
- **Impact:** Developers can reserve larger models for planning and judgment while scaling repetitive extraction, navigation, and support tasks.
- **Watch next:** Independent task-specific evals, sustained-load latency, long-context reliability, price drift, and nano’s weak computer-use results.
