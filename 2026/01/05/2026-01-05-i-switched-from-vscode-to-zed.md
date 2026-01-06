# I switched from VSCode to Zed

- Score: 349 | [HN](https://news.ycombinator.com/item?id=46498735) | Link: https://tenthousandmeters.com/blog/i-switched-from-vscode-to-zed/

### TL;DR
A long-time VSCode user switched to Zed after AI-related features in VSCode became increasingly intrusive, buggy, and performance-heavy. Zed feels familiar (VSCode-like UI/keybindings) but is faster, more stable, and has unobtrusive AI. The main friction was configuring Python: understanding that Basedpyright’s type-checking mode is effectively driven by `pyproject.toml`, and that `disablePullDiagnostics` must be set for cross-file diagnostics. HN discussion centers on AI bloat, alternatives like VSCodium, Zed, and Emacs, and where editors should stop and specialized tools begin.

---

### Comment pulse
- VSCode AI backlash → MS points to `chat.disableAIFeatures`, some users praise Copilot, others still experience popups and leave—counterpoint: at least there’s a single global opt‑out.
- Alternatives split → Some adopt VSCodium to drop Microsoft/AI bits; others jump to Zed or Emacs for performance, remote dev, and long-term AI-free control.
- Scope vs. bloat → Users want side-by-side diff and richer tooling in Zed; critics argue such features belong in dedicated tools, not a lean editor.

---

### LLM perspective
- View: Zed is capitalizing on frustration with AI-heavy, Electron-based IDEs by offering speed, familiarity, and quieter AI integration.
- Impact: Expect gradual migration by performance-sensitive and AI-skeptical developers, especially Python/Go users and remote-dev heavy workflows.
- Watch next: Zed’s plugin ecosystem, C/C++ and debugging tooling, and how VSCode refines AI defaults and opt-out behavior in response.
