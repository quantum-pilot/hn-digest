# Codex Is Live in Zed

- Score: 167 | [HN](https://news.ycombinator.com/item?id=45606698) | Link: https://zed.dev/blog/codex-is-live-in-zed

- TL;DR
  - Zed now supports OpenAI Codex via the Agent Client Protocol, selectable alongside Claude Code and Gemini. The codex-acp adapter is open-sourced; prompts bypass Zed’s servers and billing stays with OpenAI. Zed details terminal-model differences (Codex streams its own process), weighing PTY interactivity vs fewer deadlocks in non-PTY. With ACP adoption spreading (Neovim, Emacs, JetBrains), Zed will shift from building adapters to protocol stewardship. HN welcomes it but urges missing features and stronger inline suggestions; some want CLIs to adopt ACP.

- Comment pulse
  - Missing pieces block switching: git worktree diff highlighting, Jupyter support, and Dart debugging.
  - Inline suggestions lag Cursor on refactors and multi-line updates; some disable Zed AI — counterpoint: robust renames belong in native refactoring, not AI.
  - Protocol hopes: agent CLIs adopt ACP natively to avoid shims; announcement felt overshadowed by Zed’s new Windows support, reflecting rapid release cadence.

- LLM perspective
  - View: ACP is solidifying as an interoperability layer; Codex validates cross-agent differences in command execution and terminal streaming.
  - Impact: Less lock-in; users keep their IDE while switching models; compliance improves as data and billing bypass editor servers.
  - Watch next: native ACP in agent CLIs, PTY/non-PTY UX studies, and measurable upgrades to inline suggestions latency/quality to rival Cursor.
