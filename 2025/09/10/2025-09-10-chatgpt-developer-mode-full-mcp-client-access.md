# ChatGPT Developer Mode: Full MCP client access

- Score: 353 | [HN](https://news.ycombinator.com/item?id=45199713) | Link: https://platform.openai.com/docs/guides/developer-mode

### TL;DR

ChatGPT Developer Mode lets eligible web users connect remote MCP servers and expose both read and write tools inside conversations. It supports streaming HTTP or SSE plus several authentication configurations, tool toggles, server instructions, JSON inspection, and per-conversation confirmations. Unannotated tools default to write actions, and approvals can be remembered within a conversation. The documentation labels the feature elevated risk because model mistakes, malicious servers, and prompt injection can expose data or trigger destructive actions. HN welcomed interoperability but questioned whether users understand the security model.

### Comment pulse

- Tool composition expands attack paths → untrusted output reaching a model may influence any other connected write-capable tool.
- Confirmations help but are brittle → users can habituate to warnings or remember approval for later actions in the same conversation.
- Developers still value openness → arbitrary MCP connectivity enables custom data sources, workflows, and remote agents.

### LLM perspective

- View: MCP standardizes capability discovery faster than it standardizes safe delegation across dynamic contexts.
- Impact: Developers gain flexible integrations while becoming responsible for server trust, scopes, annotations, and destructive-action review.
- Watch next: Prompt-injection containment, least-privilege scopes, confirmation usability, audit logs, and sandboxed control-plane designs.
