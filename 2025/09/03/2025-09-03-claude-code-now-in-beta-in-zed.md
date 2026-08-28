# Claude Code: Now in Beta in Zed

- Score: 681 | [HN](https://news.ycombinator.com/item?id=45116688) | Link: https://zed.dev/blog/claude-code-via-acp

### TL;DR

Zed's public-beta Claude Code integration runs the agent as an independent process behind its open Agent Client Protocol, with Zed providing live multi-file edits, syntax and language-server context, granular hunk approval, task lists, and custom workflows. The Apache-licensed adapter translates Claude Code's SDK into ACP's JSON-RPC interface and can serve other compatible editors. However, SDK gaps leave plan mode and many built-in slash commands unavailable. Commenters also report context-limit dead ends, weak model/session controls, auto-accept issues, and incomplete background-task visibility.

### Comment pulse

- Early users praise the native review interface but often prefer Claude Code in Zed's terminal until missing controls arrive.
- ACP's editor-neutral ambition draws interest, while adoption still depends on agent vendors exposing complete SDK or protocol support.

### LLM perspective

- View: ACP is the durable contribution; this beta currently demonstrates the protocol more convincingly than it replaces Claude Code's CLI.
- Impact: Standardized adapters can give agents richer editor interfaces without binding every editor to bespoke vendor integrations.
- Watch next: Plan mode, context compaction, model switching, sessions, diagnostics, slash-command parity, and Anthropic's ACP position.
