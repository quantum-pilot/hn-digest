# Claude Sonnet will ship in Xcode

- Score: 489 | [HN](https://news.ycombinator.com/item?id=45058688) | Link: https://developer.apple.com/documentation/xcode-release-notes/xcode-26-release-notes

- TL;DR
  - Apple’s Xcode 26 adds a coding assistant that connects to ChatGPT (GPT-5 default, with “reasoning” option) and Anthropic’s Claude Sonnet 4 via user accounts, also supporting any Chat Completions API provider or local models on Apple silicon; predictive completion runs on-device. Beyond AI, it includes compilation caching and new performance Instruments. HN debates: Copilot’s first-mover vs rivals’ native IDE integrations; lack of agentic capabilities; privacy risks when sending code to providers; practical limits—LLMs need context for niche tasks.

- Comment pulse
  - Copilot first-mover ≠ lock-in → rivals ship native AI; MS has OpenAI stake, Azure, VSCode — counterpoint: past platform misfires haunt execution.
  - No agentic workflows yet → perceived as a toy until Claude Code/Codex-like agents integrate with file edits and tools.
  - Remote models by default → code snippets leave devices; compelled logging and shifting provider policies undermine confidentiality.

- LLM perspective
  - View: Useful bridge to external models plus on-device options; still shallow without tool-use orchestration or repository-wide planning.
  - Impact: Xcode users gain sanctioned Claude/GPT access; enterprise teams must enforce proxies, model allowlists, and data-handling policies.
  - Watch next: Agentic code actions, local fine-tuned models, telemetry controls, and benchmarks versus Copilot/JetBrains on complex refactors and multi-file fixes.
