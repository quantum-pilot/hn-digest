# Emacs 31 is around the corner: The changes I'm daily driving

- Score: 407 | [HN](https://news.ycombinator.com/item?id=48584135) | Link: https://www.rahuljuliato.com/posts/emacs-31-around-the-corner

### TL;DR
Emacs 31 significantly upgrades the “batteries in the box,” especially around tree-sitter, Markdown, completion, navigation, and terminals. Tree-sitter grammars now auto-install and many language modes ship their own sources, sharply reducing config boilerplate. A new experimental `markdown-ts-mode` powers both Markdown editing and nicely formatted LSP docs. Completion becomes more eager and ergonomic; xref buffers gain inline editing; term finally stops mangling fullscreen apps; Speedbar docks as a side window; and new Modus themes improve accessibility. HN commenters mostly celebrate Emacs’ longevity, customizability, and new momentum, with side debates over bloat, performance, and LLM-driven configs.

---

### Comment pulse
- Emacs remains a daily driver for many decades-long users → keybindings work across shells, CLIs, macOS widgets; skills outlast trendy editors and IDEs.  
- Emacs 31’s tree-sitter, LSP, and QoL fixes revive enthusiasm → some still stick to org/magit basics; others complain about slowness or unwanted complexity on Windows and Wayland-native builds.  
- LLMs fit hyper-configurable editors → agents quickly shape `init.el` from natural language requests — counterpoint: opaque, error-prone configs stop being truly “yours” without careful review.

---

### LLM perspective
- View: Emacs 31 turns common third‑party niceties (tree-sitter, markdown, completion, xref editing) into sane defaults, shrinking custom configs.  
- Impact: Power users gain simpler, more portable setups; newcomers get a more competitive out‑of‑the‑box editor versus VSCode/Neovim.  
- Watch next: Performance and UX benchmarks vs other editors; growth of first-class AI/agent workflows and robust remote-editing solutions in core Emacs.
