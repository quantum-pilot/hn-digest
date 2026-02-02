# What I learned building an opinionated and minimal coding agent

- Score: 339 | [HN](https://news.ycombinator.com/item?id=46844822) | Link: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/

### TL;DR
A single developer built “pi,” a full coding-agent stack (unified LLM API, agent loop, TUI, and CLI) optimized for simplicity, observability, and tight context control. Core ideas: minimal system prompt and four tools (read/write/edit/bash), no plan mode, no MCP, no background bash, and explicit YOLO security (you sandbox it yourself). The LLM API handles multi-provider quirks, streaming, tool calls, and cross-provider context handoff. Benchmarks (Terminal-Bench 2.0) show this minimalist approach competing with or beating heavyweight coding agents.

---

### Comment pulse
- Context trees/graphs beat linear chats → users want reusable context artifacts (MIND_MAP.md, PLAN.md) to spawn side quests and subagents without polluting the main session.  
- Framework > proprietary client → pi-agent-core likened to llama-cpp; a customizable agent kit that agents can improve themselves may outlast polished but rigid tools—counterpoint: some expect hosted tools and subscriptions to keep getting cheaper and better.  
- Security posture is contentious → pi’s YOLO stance matches real usage, but others insist on sandboxes, containers, and mandatory human approval for any write/exec tools.

---

### LLM perspective
- View: Modern models already “know” how to be coding agents; minimal prompts and tools plus good context engineering can rival complex harnesses.  
- Impact: Power users, infra engineers, and researchers gain a controllable, multi-model testbed for agent behavior, context strategies, and self-hosted deployments.  
- Watch next: Tool-result streaming, compaction strategies, and more public benchmarks will clarify when minimal agents fail and where extra orchestration actually pays off.
