# Codex Is Live in Zed

- Score: 167 | [HN](https://news.ycombinator.com/item?id=45606698) | Link: https://zed.dev/blog/codex-is-live-in-zed

### TL;DR

Zed now supports OpenAI Codex through the Agent Client Protocol, selectable beside Claude Code and Gemini CLI. Zed says external-agent prompts and code go directly to OpenAI, with billing and terms remaining between user and provider; its Codex ACP adapter is open source. Integration exposed a protocol wrinkle: Codex runs commands itself and streams bytes, unlike agents that ask the client to execute them, limiting terminal interactivity but avoiding some deadlocks. Commenters welcomed interoperability while requesting broader editor improvements.

### Comment pulse

- ACP adoption could reduce bespoke integrations → commenters want agent CLIs to implement the protocol directly instead of relying on adapters.
- Editor gaps still block switching → worktree diffs, Jupyter, debugging, and stronger inline predictions mattered more to some users.

### LLM perspective

- View: ACP separates editor experience from agent choice, though execution ownership still leaks into user-visible behavior.
- Impact: Developers can retain Zed’s interface while choosing external agents and direct vendor relationships.
- Watch next: Track native ACP support, conversation persistence, PTY conventions, adapter maintenance, and feature parity across agents.
