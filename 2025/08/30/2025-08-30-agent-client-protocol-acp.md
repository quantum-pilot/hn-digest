# Agent Client Protocol (ACP)

- Score: 281 | [HN](https://news.ycombinator.com/item?id=45074147) | Link: https://agentclientprotocol.com/overview/introduction

### TL;DR

The Agent Client Protocol aims to standardize communication between code editors and coding agents, reducing the need for a custom integration for every pairing. Inspired by the Language Server Protocol, ACP runs agents as editor subprocesses and uses JSON-RPC over standard input and output. It reuses MCP's JSON representations where practical while adding coding-specific interface concepts such as diffs, tool calls, file access, terminals, plans, modes, and commands. The documentation says the protocol remains under development but is usable for experiments.

### Comment pulse

- Supporters hope ACP lowers switching costs and lets editors compete on editing rather than proprietary agent integrations.
- Questions centered on overlap with LSP, unsaved-buffer search consistency, and whether CLI agents will adopt it.

### LLM perspective

- View: ACP targets a real compatibility seam between interactive editors and increasingly capable agent runtimes.
- Impact: A shared protocol could make agents portable while preserving editor-native review, diff, and approval experiences.
- Watch next: Adoption beyond Zed, version stability, unsaved-file semantics, and boundaries with LSP and MCP.
