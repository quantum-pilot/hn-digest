# Agent Client Protocol (ACP)

- Score: 281 | [HN](https://news.ycombinator.com/item?id=45074147) | Link: https://agentclientprotocol.com/overview/introduction

- TL;DR
  - The Agent Client Protocol standardizes communication between editors and AI coding agents, decoupling them LSP-style. Agents run as subprocesses via JSON-RPC over stdio, reusing MCP formats and adding UX types like diffs; Markdown is the default text. It’s early but usable. HN sees potential to lower switching costs and broaden interoperability, debates extending LSP instead, notes early experiments integrating Claude Code and CLI tools, and flags practical issues like workflows avoiding deep integration and unsaved-buffer search mismatches.

- Comment pulse
  - ACP lowers switching costs → shared protocol lets editors and CLI agents interoperate; Gemini CLI already works.
  - Use LSP instead → extend mature standard; avoid fragmentation — counterpoint: ACP targets agent UX beyond LSP (diffs, tools).
  - Deep integration optional → many use git-based 'prompt coding'; avoid auto-commits due to hallucinations; unsaved buffers can desync ripgrep-based search.

- LLM perspective
  - View: ACP could become the ‘LSP for agents’ if it stays minimal, editor-agnostic, and aligns with MCP.
  - Impact: Winners: editors avoiding bespoke plugins; agent vendors shipping once; CLI tools integrating via stdio. Losers: monolithic AI IDE forks.
  - Watch next: Spec stability, VS Code/JetBrains adapters, and solutions for unsaved-buffers search (virtual FS overlays, content streams, or rg replacement).
