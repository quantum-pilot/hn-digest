# GPT-5.6 Sol Ultra will be in Codex

- Score: 402 | [HN](https://news.ycombinator.com/item?id=48799614) | Link: https://twitter.com/thsottiaux/status/2073933490513752151

### TL;DR

An OpenAI employee said GPT‑5.6 Sol Ultra will come to Codex, responding to disappointment that GPT‑5.5 Pro stayed unavailable. The announcement itself provides no timing, pricing, limits, or architecture. HN readers inspecting Codex source argued Ultra currently maps to maximum reasoning plus instructions to use subagents proactively, rather than exposing a distinct backend effort level or Pro-style inference. Others suggested dynamic orchestration could still be meaningful. Enterprise commenters said management had reversed from rewarding token consumption to urging cheaper models and usage monitoring, exposing rising inference costs and capacity constraints.

### Comment pulse

- Source inspection narrows Ultra’s meaning → it appears to alias maximum effort and add proactive-subagent prompting — counterpoint: dynamic orchestration can exceed ordinary manual delegation.
- Ultra is not evidently Pro → commenters found no backend effort level or trace of parallel candidate generation and judge-model selection.
- Enterprise incentives reversed rapidly → token-use leaderboards became cost-warning emails, showing adoption metrics can hide unsustainable inference spending.

### LLM perspective

- **View:** The announcement confirms intent only; architecture, automatic delegation, billing, limits, and whether Ultra differs materially from prompting remain unresolved.
- **Impact:** Packaging orchestration behind a named mode can normalize multi-agent work, but opaque aliases make capability and cost comparisons difficult.
- **Watch next:** Codex source changes, picker labels, automatic spawning behavior, token accounting, concurrency limits, subscription availability, and comparisons against Pro.
