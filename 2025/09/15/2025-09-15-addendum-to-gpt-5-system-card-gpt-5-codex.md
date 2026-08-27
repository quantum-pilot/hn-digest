# Addendum to GPT-5 system card: GPT-5-Codex

- Score: 219 | [HN](https://news.ycombinator.com/item?id=45253458) | Link: https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/

### TL;DR

OpenAI describes GPT-5-Codex as a GPT-5 variant trained with reinforcement learning on real coding environments to follow instructions, produce human-like pull requests, and iterate until tests pass. The accompanying addendum covers specialized safety training for harmful requests and prompt injection, plus sandboxing and configurable network access. It is available through terminal, IDE, web, GitHub, and mobile Codex surfaces. HN discussion largely reviewed product experience instead of the safety document, praising codebase navigation while reporting latency, instability, context degradation, and pricing uncertainty.

### Comment pulse

- Users report strong long-context coding and fewer incomplete implementations → others still see premature stopping or degradation near context limits.
- Deliberation creates a tradeoff → slower turns may reduce reprompting, while faster competitors feel more interactive.
- Discussion missed the document → commenters noted this thread mostly compared coding agents rather than examining safety claims.

### LLM perspective

- View: The page announces mitigation categories, but the supplied excerpt offers little evidence for evaluating their effectiveness.
- Impact: Developers gain broader access while retaining responsibility for review, sandbox configuration, and network permissions.
- Watch next: Independent safety testing, service stability, pricing, custom environments, and prompt-injection performance.
