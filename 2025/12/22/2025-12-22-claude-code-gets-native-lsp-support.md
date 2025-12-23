# Claude Code gets native LSP support

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46355165) | Link: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### TL;DR
Claude Code’s latest release adds a native Language Server Protocol (LSP) tool, letting the agent call language servers for go‑to‑definition, find‑references, and hover docs directly from its CLI/desktop environment. HN sees this as a crucial step toward compiler- and LSP-backed refactoring instead of brittle search/replace, but notes that current support is hidden behind plugins, under-documented, and far from deep mutation tooling. Discussion branches into JetBrains/Microsoft underusing their powerful refactoring engines, open-source alternatives like OpenCode, and whether agents belong in CLIs or IDEs.

---

### Comment pulse
- Real opportunity is compiler/LSP-powered refactoring → analyzers like Roslyn or JetBrains can do precise, global transformations that current agents approximate with fragile text edits.  
- Claude Code + LSP/deterministic codemods excites users → they’re already gluing in tools like Rope, but today’s LSP integration feels hard to discover and configure.  
- Debate: CLI vs IDE agents → terminal form factor is editor-agnostic, scriptable, and “orchestration-first,” while IDEs give richer UIs and already have LSP wired in. — counterpoint: IDE agents rarely expose that info to models.

---

### LLM perspective
- View: Next leap is agents issuing structured refactor commands to compilers/LSPs, not editing source text directly.  
- Impact: Large, long-lived codebases benefit most; safer sweeping changes and fewer review cycles.  
- Watch next: First end-to-end “agent + refactor API” stacks (e.g., Roslyn/TypeScript/Go) with benchmarks on correctness over huge repos.
