# Zoxide: A Better CD Command

- Score: 295 | [HN](https://news.ycombinator.com/item?id=45342943) | Link: https://github.com/ajeetdsouza/zoxide

- TL;DR
  - Zoxide is a Rust “smarter cd” that tracks frequently used directories and jumps via fuzzy queries (z/zi), with interactive selection, broad shell support, and imports from z/autojump. HN is split: fans say it slashes keystrokes versus path traversal; skeptics find fuzzy ranking unpredictable and stick to tab completion/history. Tips include scoping searches with a basedir and pairing with prompt cues; others recommend simpler alternatives like classic z or Navita and warn about misnavigation risks.

- Comment pulse
  - Fuzzy jumping feels unpredictable → rankings shift; users land in wrong dirs (e.g., thing vs thing-api); prefer tab/history/aliases — counterpoint: scope with basedir for per-repo disambiguation.
  - Zoxide is a daily driver → reduces keystrokes versus tree walking; pairs well with Fish, Starship, eza, bat, Atuin, rg/fd.
  - Safety and alternatives matter → fuzzy mistakes can be costly; classic z or Navita offer simpler setups, just source a script.

- LLM perspective
  - View: Great for large, messy directory trees; less useful when projects are few or names are similar.
  - Impact: Boosts shell navigation speed; adoption hinges on predictable ranking controls and guardrails.
  - Watch next: Expose deterministic shortcuts, per-repo scope defaults, and safer modes: echo-before-cd, confirmations for destructive commands.
