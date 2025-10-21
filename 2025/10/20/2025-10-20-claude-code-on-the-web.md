# Claude Code on the web

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45647166) | Link: https://www.anthropic.com/news/claude-code-on-the-web

TL;DR
- Anthropic launched Claude Code on the web: a browser and iOS interface that runs coding tasks on Anthropic-managed sandboxes, with GitHub integration, real-time steering, parallel sessions, and automatic PRs/change summaries. Security emphasizes OS‑native, open‑sourced sandboxing with restrictive filesystem/network access and configurable allowlists; it’s a Pro/Max research preview and bridges to the CLI. HN compares it with GPT‑5 Codex: many report Codex better on long, hard tasks and cheaper, while others prefer Claude’s speed and workflow features. Debates center on sandbox escape/exfil risks and a desire for IDE‑attachable, persistent devboxes.

Comment pulse
- Codex CLI outperforms Claude on long, complex tasks → higher quality, fewer stalls, lower cost — counterpoint: Claude is faster with key workflow features.
- Sandboxing praised but questioned → OS‑native, open‑sourced sandboxes and allowlists help, yet exfiltration and regex‑style controls feel brittle to some.
- Cloud PR agents misfit inner dev loop → developers want persistent, IDE‑attachable environments for live testing, not ephemeral sandboxes pushing PRs.

LLM perspective
- View: This moves Claude Code toward fully managed, parallelizable agents with pragmatic guardrails, not just a chat-plus-CLI wrapper.
- Impact: Erodes value of third‑party 'Claude-in-the-cloud' tools; intensifies head‑to‑head with GPT‑5 Codex on speed, reliability, and price.
- Watch next: Feature parity vs Codex: faster runtimes, approvals, plan/skills UX, persistent devboxes, plus sandbox benchmarks for data egress and escape resistance.
