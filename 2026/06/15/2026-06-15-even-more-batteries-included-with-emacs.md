# Even more batteries included with Emacs

- Score: 342 | [HN](https://news.ycombinator.com/item?id=48535886) | Link: https://karthinks.com/software/even-more-batteries-included-with-emacs/

### TL;DR

The third installment catalogs 20 useful, little-mentioned features bundled with Emacs 28.1+, each intended to be learned in under five minutes without extra packages. Examples span wildcard file opening, URI extraction, lightweight window and directory comparison, live change highlighting, retrospective keyboard macros, image controls, automatic text refilling, synchronized scrolling, buffer locks, and restoration of closed frames. The broader lesson is that Emacs’s problem is discovery, not capability. HN veterans found commands that replaced homegrown code, while debating stability, distributions, Neovim, and whether starting vanilla better teaches the help system.

### Comment pulse

- Built-ins prevent reinvention → several readers discovered they had duplicated ruler-mode or forgotten compare-windows, validating the article’s archaeological approach.
- Stability depends on configuration → Doom users report slow-moving reliability — counterpoint: heavily customized setups can still freeze or crash weekly.
- Distributions accelerate onboarding but hide fundamentals → vanilla exploration teaches apropos, function lookup, variables, manuals, and composability before plugins duplicate existing behavior.

### LLM perspective

- **View:** Emacs’s durable advantage is inspectability: every key invokes a discoverable function that users can read, combine, or redefine.
- **Impact:** Better feature discovery can shrink configurations, reduce dependency churn, and convert bespoke snippets into consistent built-in workflows.
- **Watch next:** Improve command surfacing, help, mouse support consistency, crash telemetry, and LLM access to Info and function metadata.
