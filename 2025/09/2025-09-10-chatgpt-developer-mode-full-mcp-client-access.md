# ChatGPT Developer Mode: Full MCP client access

- Score: 353 | [HN](https://news.ycombinator.com/item?id=45199713) | Link: https://platform.openai.com/docs/guides/developer-mode

TL;DR
ChatGPT’s Developer Mode now works as a full Model Context Protocol (MCP) client, letting the chatbot connect to user-controlled MCP servers for tools, data, and actions. Commenters split: builders celebrate standardization and new agent workflows; security-minded folks warn the attack surface expands sharply. Main risks: prompt injection via untrusted content chaining into powerful tools, brittle UI gating, and coarse OAuth scopes mismatched with dynamic prompts. There’s confusion resolved: this is for the online chatbot, not just a CLI agent.

Content unavailable; summarizing from title/comments.

Comment pulse
- Full MCP access heightens prompt-injection and toolchain pivoting risk → untrusted outputs can trigger other tools; static scopes vs dynamic contexts — counterpoint: hidden toggle and warnings mitigate accidents.
- AI firms decry agentic risks yet ship broad access → enabling executable access to personal data without mature safeguards seems inconsistent.
- Builders welcome MCP standardization → plan local control planes with sandboxing/permission prompts; want concrete use cases and connectors for daily workflows.

LLM perspective
- View: ChatGPT becomes a pluggable agent runtime; security must prioritize isolation, least privilege, and robust injection defenses.
- Impact: Security teams and MCP authors must design granular scopes, audit tool graphs, and monitor cross-tool call chains.
- Watch next: Per-call scopes, signed tool invocations, sandboxed execution, and red-team benchmarks for injection and tool-escape rates.
