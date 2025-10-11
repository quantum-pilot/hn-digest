# Notes on switching to Helix from Vim

- Score: 255 | [HN](https://news.ycombinator.com/item?id=45539609) | Link: https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/

- TL;DR
  - Julia Evans switched from Vim/Neovim to Helix after 20 years, mainly for built-in, zero-config LSP. She praises project-wide search with rich context and inline key-hint popups, and prefers multiple cursors over macros. Annoyances: weaker text reflow, Markdown list continuity, no persistent undo, and occasional crashes. Switching felt easy after embracing Helix’s model and minimal config. HN debates batteries-included editors vs modern Neovim distros, highlights portability and fewer plugins, notes feature gaps, and lauds which‑key-style contextual help.

- Comment pulse
  - Helix’s batteries‑included approach beats Neovim config → built‑in LSP and portability with fewer plugins — counterpoint: Neovim distros already make LSP simple.
  - Gaps block some: auto‑reload, code actions on save; crashes plus no persistent undo risk data loss; HEAD adds fuzzy picker and a basic explorer.
  - Contextual key-hint popups are widely praised → reduce recall load; but too many choices risk overload; long‑term Vim muscle memory hinders switching.

- LLM perspective
  - View: Opinionated LSP‑first editor minimizes setup; differentiation is defaults and ergonomics, not extensibility.
  - Impact: Best for remote/ephemeral dev boxes and plugin‑averse teams; least for heavy macro users with entrenched Vim habits.
  - Watch next: Ship auto‑reload and persistent undo; stabilize Markdown workflows; track crash rates; clarify plugin/explorer roadmap.
