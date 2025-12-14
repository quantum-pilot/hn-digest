# I tried Gleam for Advent of Code

- Score: 220 | [HN](https://news.ycombinator.com/item?id=46255991) | Link: https://blog.tymscar.com/posts/gleamaoc2025/

- TL;DR  
  Author used Gleam, a statically typed FP language on the BEAM, for Advent of Code’s shortened 12‑day edition and found it an excellent fit for “parse → transform → fold” problems. Standout features were ergonomic debugging (`echo`), safe grid handling via options, a strong list toolbox (`transpose`, `combination_pairs`), and `fold_until` for clean early exits. Friction points included missing stdlib file IO/regex, some pattern‑matching and comparison verbosity, JS vs BEAM integer differences, and having to shell out for LP solving. HN broadly praises Gleam’s dev experience, performance, and LSP, while debating verbosity, OTP maturity, ecosystem gaps, and adoption dynamics in an LLM era.

- Comment pulse  
  - Gleam admired for clean typing on BEAM; some correct confusion between BEAM and OTP; worry LLMs might slow new-language adoption—counterpoint: models learn from examples.  
  - Dev experience lauded: fast code, exceptional LSP, pleasant FP pipelines; downsides include aggressive formatter, module-qualified names like list.map, limited libraries, and verbose boolean branching.  
  - Some miss recursive inner functions and richer pattern matching; compare Gleam unfavorably to Scheme/Erlang elegance, yet value static typing and BEAM interoperability.

- LLM perspective  
  - View: AoC highlights Gleam’s strengths for data‑heavy FP: pipelines, algebraic types, list utilities, and early‑exit folds reduce incidental complexity.  
  - Impact: Could attract FP‑curious web and backend developers to BEAM; feedback here prioritizes better stdlib IO, regex, boolean ergonomics, and OTP completeness.  
  - Watch next: Track ecosystem growth: numerical and SAT/SMT libraries, JS/BEAM integer unification, and whether LSP quality plus AoC visibility drive broader production adoption.
