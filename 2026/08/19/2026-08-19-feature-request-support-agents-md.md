# Feature Request: Support AGENTS.md

- Score: 239 | [HN](https://news.ycombinator.com/item?id=49367350) | Link: https://github.com/anthropics/claude-code/issues/6235

### TL;DR

The request asks Claude Code to recognize AGENTS.md, a unified Markdown instruction file reportedly gaining adoption across Codex, Amp, Cursor, and other coding agents. The author argues CLAUDE.md unnecessarily ties repository guidance to one product and complicates collaboration among developers using different tools. No implementation details, compatibility behavior, precedence rules, migration approach, or maintainer response are included. The proposal’s goal is portability: one checked-in set of codebase instructions that multiple agent clients can consume instead of duplicating vendor-named files.

### Comment pulse

- Readers interpreted file naming as an early lock-in battle in a market without durable command-line-agent moats.
- One commenter proposed injecting custom JavaScript into Claude Code as an unofficial compatibility workaround.
- Broader criticism compared closed ecosystems with platform decline; replies noted developer loyalties between vendors have already shifted.

### LLM perspective

- View: The interoperability request is simple; predictable precedence and scoping are the real design work.
- Impact: Shared instructions could reduce duplicated files and tool-specific friction across collaborating developers.
- Watch next: Official support, nested-file semantics, conflicts with CLAUDE.md, migration guidance, and maintainer response.
