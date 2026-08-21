# Vomit: Clean up Claude 5's token output with a separate LLM

- Score: 169 | [HN](https://news.ycombinator.com/item?id=49375996) | Link: https://github.com/zachahn/vomit

### TL;DR

Vomit is a GPLv3 Go tool that intercepts Claude Code messages through hooks and rewrites them into clearer English using a local LLM; sidecar commands can list or follow sessions without replacing output. It claims no telemetry or external dependencies and supports Llama.app, Ollama, or perhaps OpenAI-compatible APIs. The author warns that the translator sees text but not actions or files, so it can hallucinate, run slowly, and hide important messages; it is vibe-coded and Mac-tested. Commenters shared style frustration but questioned solving one model with another.

### Comment pulse

- Users said communication preferences decay during long sessions; one alternative reinjects instruction files ephemerally on every turn.
- Some urged switching models—counterpoint: cheap style transfer can complement stronger reasoning, and cross-model review may improve results.
- Satire targeted ever-growing stacks of agents needed to manage other agents instead of simplifying work.

### LLM perspective

- View: A local style proxy is practical, but semantic fidelity is its load-bearing weakness.
- Impact: Claude users may read less jargon while accepting extra latency and another failure boundary.
- Watch next: Cross-platform testing, rewrite latency, hallucination measurements, reliable original-text fallback, and hook compatibility.
