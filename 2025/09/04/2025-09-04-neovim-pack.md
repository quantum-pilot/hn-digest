# Neovim Pack

- Score: 308 | [HN](https://news.ycombinator.com/item?id=45121915) | Link: https://neovim.io/doc/user/pack.html#vim.pack

TL;DR
Neovim’s pack docs explain native packages (“start” auto-load, “opt” via :packadd) and introduce vim.pack, a WIP built-in plugin manager. It installs Git-backed plugins into a dedicated directory, supports semver tags or branches/commits, parallel installs, add/update/del/get APIs, and a confirmation buffer with LSP hints. HN sees this as a path away from third‑party managers (e.g., lazy.nvim) and toward default lazy-loading, though Lua’s setup() can complicate it. Expectations: stability and faster startup; caveats: fewer features than lazy, and emphasize reproducible pinning (SHAs/semver over timestamps).

Comment pulse
- Built-in vim.pack could replace complex managers and encourage lazy loading → simpler installation/updates. — counterpoint: Neovim's Lua setup() makes lazy-loading orchestration harder than Vimscript.
- Users crave stability after manager hopping → 'blessed' tool likely widely supported, though less feature-rich than lazy.nvim; some already fine with pack dirs or nixvim.
- Reproducibility matters → pin semver tags or SHAs; datetime checkouts suggested, but clocks differ and aren’t deterministic—use hashes.

LLM perspective
- View: vim.pack formalizes packpath workflows with Git, prioritizing reproducibility and core support over plugin-manager feature breadth.
- Impact: Plugin authors may simplify install docs and adopt lazy-load-friendly patterns; users reduce external dependencies and pin versions by default.
- Watch next: Measure startup/update performance vs lazy.nvim; semver tagging uptake across popular repos; API stabilization, rollback UX, and secure update policies.
