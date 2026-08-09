# Two Years of Emacs Solo

- Score: 334 | [HN](https://news.ycombinator.com/item?id=47317616) | Link: https://www.rahuljuliato.com/posts/emacs-solo-two-years

### TL;DR

At its two-year mark, Emacs Solo refactors its dependency-free configuration into two layers: `init.el` tunes only built-in features, while 35 optional, self-contained Elisp modules recreate selected package functionality. The tour argues core Emacs supplies most of a modern environment—completion, projects, Git, LSP, workspaces, mail, feeds, and process management—and previews Emacs 31 improvements that will remove several polyfills. HN readers admired the control and learning value, but disputed the purity boundary: bundled code can lag ELPA fixes, and rewriting packages pays mainly when customization or enjoyment justifies maintenance.

### Comment pulse

- Personal modules optimize for one user → small scope makes failures understandable and removes pressure to support every edge case.
- Core-only is not automatically safer → bundled versions may miss ELPA fixes, while copied code still carries maintenance obligations.
- Emacs remains unusually malleable → commenters see its introspection and Elisp runtime as especially compatible with agent-assisted customization.

### LLM perspective

- **View:** This works best as a learning project and curated appliance, not a general prescription against dependencies.
- **Impact:** Users can first exhaust built-ins, then add narrow modules only where their workflow proves a persistent gap.
- **Watch next:** Emacs 31 stabilization, compatibility-code deletion, and whether 35 modules remain easier than package upgrades.
