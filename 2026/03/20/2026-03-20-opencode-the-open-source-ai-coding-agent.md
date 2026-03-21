# OpenCode – The open source AI coding agent

- Score: 303 | [HN](https://news.ycombinator.com/item?id=47460525) | Link: https://opencode.ai/

### TL;DR
OpenCode is an open source AI coding agent that runs in the terminal, IDEs, or as a desktop app, and can talk to many models (Claude, GPT, Gemini, local, etc.) while auto-wiring language servers and supporting multi-session workflows. It emphasizes privacy (no code retention) and offers a curated “Zen” model set for reliable coding performance. HN commenters praise its productivity and flexibility but criticize rapid, under-tested releases, heavy TypeScript bloat, security posture, and occasionally confusing UX and configuration.

---

### Comment pulse
- Development feels chaotic → high release cadence, frequent breakage, big TS codebase, RAM-heavy TUI; hard-to-track features — counterpoint: creator publicly acknowledged debt and cleanup need.  
- Security posture worries some → permissive-by-default capabilities, remote config loading, and a concerning GitHub issue; feels risky for sensitive orgs and regulated environments.  
- When stable, it’s extremely productive → multi-model and subagent support, plugins like prune/retrieve, and spec-driven workflows let some users largely replace Claude Code and frontier UIs.

---

### LLM perspective
- View: Open, model-agnostic coding agents shift value to orchestration, context management, and tooling, not just raw LLM quality.  
- Impact: Puts pressure on proprietary copilots by offering flexibility, self-hosting paths, and integration with existing AI subscriptions.  
- Watch next: Whether they invest in testing, security reviews, and plugin standards will determine adoption inside larger, risk-averse teams.
