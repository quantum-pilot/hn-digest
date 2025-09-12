# Claude Code: Now in Beta in Zed

- Score: 681 | [HN](https://news.ycombinator.com/item?id=45116688) | Link: https://zed.dev/blog/claude-code-via-acp

- TL;DR
    - Zed released a public‑beta integration of Anthropic’s Claude Code via its open Agent Client Protocol (ACP). Claude runs natively as a first‑class, multi‑file editing agent with live follow‑along, granular diff approval, task lists, and custom workflows. The ACP adapter is open‑sourced and also enables Claude Code in other ACP editors (e.g., Neovim). HN likes the direction but reports a rushed beta: SDK gaps block Plan mode, slash commands (/compact, /clear), model switching, and context controls; prompt errors and UX rough edges push some to stick with terminal or Cursor for now.

- Comment pulse
    - Rushed beta → SDK limits block Plan mode, slash commands, model switching; prompt errors and missing context derail sessions — counterpoint: foundation first, features coming.
    - Autocomplete gap → Cursor’s inline predictions feel stronger; users request local models via Ollama and buy-once, offline options.
    - Editing model friction → Helix mode is young; calls for pluggable/keymap-agnostic engines or server-mode integrations to reduce switching costs.

- LLM perspective
    - View: ACP decouples agents from editors, enabling cross‑IDE competition and faster iteration beyond a single integration.
    - Impact: If Anthropic ships SDK parity or adopts ACP natively, Plan mode, slash commands, and model controls arrive across ACP editors.
    - Watch next: Measure refactor accuracy, revert granularity, and latency vs Cursor; track Neovim adapter maturity and local‑model support.
