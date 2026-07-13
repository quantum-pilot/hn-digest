# Ghostel.el: Terminal emulator powered by libghostty

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48879504) | Link: https://dakra.github.io/ghostel/

### TL;DR
Ghostel.el is an Emacs terminal emulator built on libghostty-vt (Ghostty’s terminal core), aiming to replace vterm/eat and even external terminals. It renders fast, complex TUIs accurately, exposes a clean Elisp API, and treats scrollback like a normal Emacs buffer, enabling powerful keyboard-centric search and selection workflows. HN users praise performance and usability but note rough edges (occasional freezes/clearing bugs), weaker text-editing integration than eshell, and conceptual complexity around its multiple input modes and when to keep terminals outside Emacs.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Ghostel vs vterm/eat/externals → faster TUIs, better input handling, Emacs-native scrollback and API; already a daily driver for some, though still early-stage.
- Limits to full Emacs integration → eshell-like arbitrary text editing, Evil/xah-fly compatibility, and WezTerm-style quick-select are missing or partial — counterpoint: extensions exist but remain constrained.
- Workflow considerations → users keep external terminals for long-running/critical tasks and when Emacs can block (e.g., huge Magit diffs); input modes need clearer practical examples.

---

### LLM perspective
- View: This is Emacs embracing a modern terminal core while preserving buffer-centric power—bridging TUI correctness and editor extensibility.
- Impact: Heavy Emacs users, especially those living in Magit and shells, can consolidate tooling and reduce context switches.
- Watch next: Stability fixes, richer editing integration (eshell-like modes), and clearer docs on mode workflows will determine whether Ghostel fully displaces vterm/eat.
