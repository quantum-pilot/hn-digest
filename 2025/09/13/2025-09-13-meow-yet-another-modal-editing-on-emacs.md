# Meow: Yet another modal editing on Emacs

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45228396) | Link: https://github.com/meow-edit/meow

- TL;DR
  - Meow is a Kakoune-style modal editing package for Emacs that emphasizes minimal configuration, few key conflicts, selection-first operations, and reduced modifier use—promising speed and flexible keymaps without dependencies. HN readers praise its clean design and robustness for Kakoune/Helix workflows, but note gaps: Vim-like repeat, visual-mode familiarity, and accidental selection loss; some prefer non‑modal workflows (Meta chords, Hydra, god‑mode). Others stick with Evil for its vast ecosystem of mode-specific bindings (e.g., Magit). Alternatives like meep and repeat‑fu were mentioned.

- Comment pulse
  - Best Kakoune-like option in Emacs → clean, lightweight design; customizable; downsides: brittle repeat, selection-dropping, no familiar visual mode.
  - Prefer non‑modal editing → Meta chords, Hydra, god‑mode reduce mode switching; Emacs feels tool‑centric, not compositional. — counterpoint: modal models cut keystrokes, feel faster.
  - Ecosystem matters → Evil’s collection supplies per‑mode bindings (e.g., Magit); switching risks losing polished integrations.

- LLM perspective
  - View: Good fit if you like Kakoune/Helix semantics; expect selection-first mental model and sparse “visual mode” affordances.
  - Impact: Time-to-edit depends on repeat reliability and key discovery; keypad helps chord-heavy commands; plugin coverage trails Evil.
  - Watch next: Meow repeat fixes, clearer selection UX, and Magit/org-mode recipes; MELPA status of meep; benchmarks versus Evil for latency.
