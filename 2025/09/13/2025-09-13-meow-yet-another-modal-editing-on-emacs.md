# Meow: Yet another modal editing on Emacs

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45228396) | Link: https://github.com/meow-edit/meow

### TL;DR

Meow is a dependency-free modal editing mode designed to coexist with ordinary Emacs keymaps rather than replace them. It uses selection-first editing, a keypad mechanism to reduce modifier-heavy chords, and ideas from Kakoune and avy while aiming for minimal configuration and interference. Commenters praised its lightweight, composable model and compatibility, but identified tradeoffs around repeat behavior, accidentally dropped selections, and the mental cost of tracking modal state. Some preferred Evil’s broader ecosystem integrations or conventional non-modal Emacs instead.

### Comment pulse

- Fans described the selection-first model as clean and flexible, especially for users already comfortable with Kakoune-style editing.
- Skeptics found keypad sequences or modal state less ergonomic, and noted Evil’s stronger package-specific bindings.

### LLM perspective

- View: Meow’s strongest idea is preserving Emacs composition while adding modality as a focused layer.
- Impact: Its smaller surface can reduce configuration burden, though ecosystem coverage still influences long-term adoption.
- Watch next: Improvements to repeat semantics, selection persistence, discoverability, and integrations with workflows such as Magit.
