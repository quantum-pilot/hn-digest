# I tried Gleam for Advent of Code

- Score: 220 | [HN](https://news.ycombinator.com/item?id=46255991) | Link: https://blog.tymscar.com/posts/gleamaoc2025/

### TL;DR

After completing all 24 parts of 2025’s shortened Advent of Code, the author found Gleam unusually pleasant for puzzle solving: pipelines, options, strong error messages, a capable LSP, rich list helpers, and `fold_until` made transformations clear and safe. Friction included external dependencies for file I/O and regex, limited list patterns, verbose comparisons, cross-target integer differences, and no Z3 bindings. Commenters largely confirmed the strong developer experience and performance while adding ecosystem, syntax, formatting, and OTP-support caveats.

### Comment pulse

- Gleam’s tooling earns unusual praise → its LSP offers formatting, imports, fixes, pattern completion, and broad editor support.
- Language simplicity has costs → commenters cite verbose qualification, Boolean branching, recursion constraints, aggressive formatting, and missing specialist libraries.
- BEAM support is not OTP equivalence → Gleam’s type-safe OTP library reportedly covers less than Erlang or Elixir.

### LLM perspective

- View: Gleam’s advantage is coherent ergonomics, not any single novel feature.
- Impact: Puzzle success justifies testing it on a real service, where ecosystem gaps become clearer.
- Watch next: Compare web-service reliability, library coverage, profiling, and deployment experience against established BEAM languages.
