# I tried Gleam for Advent of Code

- Score: 220 | [HN](https://news.ycombinator.com/item?id=46255991) | Link: https://blog.tymscar.com/posts/gleamaoc2025/

### TL;DR

A programmer who has completed Advent of Code for seven years used Gleam for 24 parts of 2025’s shortened event and found it unusually pleasant. Clean syntax, strong compiler errors, a reliable LSP, pipelines, safe option handling, and rich list functions made parsing and transformations concise. Friction included missing standard-library file I/O and regex, limited list patterns, verbose comparisons, target-dependent big integers, and no Z3 bindings. HN broadly confirmed the developer experience and surprising speed, while noting sparse libraries, formatter choices, namespace verbosity, and that BEAM and OTP are distinct.

### Comment pulse

- Users praised the LSP, pipelines, type system, and double-digit-microsecond solutions, while warning that performant patterns differ from other languages.
- Library gaps and verbose namespaces drew criticism — counterpoint: selective imports reduce repeated module prefixes, and maintainers fixed one break within a day.
- Commenters corrected a terminology error: Gleam targets BEAM; its type-safe OTP library implements a smaller subset than Erlang or Elixir.

### LLM perspective

- View: Gleam’s appeal comes from coherent tools and constrained functional patterns, not a single novel feature.
- Impact: Puzzle fluency suggests a low-friction learning path, but production adoption depends on ecosystem depth and interoperability.
- Watch next: Real-project experience, library coverage, cross-target integer behavior, native bindings, formatter control, and OTP parity.
