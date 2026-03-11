# Two Years of Emacs Solo

- Score: 334 | [HN](https://news.ycombinator.com/item?id=47317616) | Link: https://www.rahuljuliato.com/posts/emacs-solo-two-years

### TL;DR
Emacs Solo is a full daily‑driver Emacs setup built with a hard rule: no external packages—only core Emacs and 35 tiny, self‑written modules. The author refactored it into a clear “core tweaks in `init.el`” vs “extras in `lisp/`” architecture, re‑implementing things like themes, gutters, LSP helpers, containers, and AI integration in a few hundred lines each. The experiment shows how far stock Emacs can go, how much Elisp you learn by building, and how Emacs 31 further reduces the need for third‑party packages.

---

### Comment pulse
- Emacs’ backup and lockfile defaults are annoying in system dirs → many immediately redirect them to `~/.emacs.d/backups` or disable lockfiles.  
- Non-obvious keybindings like `C-z` suspending the editor confuse even “experienced” users → disabling suspend in terminal Emacs avoids mysterious “crashes”.  
- No‑packages stance → some see it as wasteful vs reusing ELPA and reading others’ code; defenders say it’s a fun learning challenge, not a prescription.

---

### LLM perspective
- View: Emacs’ introspective environment plus Elisp make it unusually friendly for LLM-assisted customization and automation.  
- Impact: Power users can offload boilerplate Elisp and config exploration to models, focusing on workflow design.  
- Watch next: Purpose-built “Emacs agent” frameworks that expose buffers, commands, and docs as tools for LLMs to orchestrate.
