# Formatting code should be unnecessary

- Score: 350 | [HN](https://news.ycombinator.com/item?id=45163043) | Link: https://maxleiter.com/blog/formatting

- TL;DR
  - The piece recalls Ada/R1000’s DIANA era, where code wasn’t stored as text but as an AST; editors pretty‑printed it per user preference, enabling incremental compilation, refactoring, and zero formatting debates. The author argues modern tooling could revive that idea. HN debates the trade‑offs: plain‑text composability (grep/diff/sed, VCS) versus semantic tools; whether formatting conveys meaning and readability; and pragmatism—pick a standard formatter to avoid bikeshedding, while acknowledging some options (trailing commas, line length) materially impact diffs, merges, and productivity.

- Comment pulse
  - Plain text wins → grep/diff/sed and VCS stay universal; AST storage locks teams into heavy tooling — counterpoint: semantic grep/diff and canonical text-on-disk mitigate.
  - Formatting communicates structure → alignment, trailing commas, line length influence readability; some formatters (e.g., Black with SQLAlchemy) hinder clarity.
  - Pragmatists favor one formatter → reduces bikeshedding, diffs, merge conflicts; defaults like gofmt/rustfmt work — counterpoint: certain options materially affect productivity.

- LLM perspective
  - View: Store canonical AST-backed text; editors render personal style; write-back normalizes.
  - Impact: Fewer style debates; better semantic diffs/refactors; tooling needs shared schemas across languages.
  - Watch next: LSP round‑trip formatting, semantic merge for Git, and experiments measuring review/merge conflict reductions.
