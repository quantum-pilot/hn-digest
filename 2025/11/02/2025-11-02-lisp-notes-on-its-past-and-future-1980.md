# Lisp: Notes on its Past and Future (1980)

- Score: 110 | [HN](https://news.ycombinator.com/item?id=45792579) | Link: https://www-formal.stanford.edu/jmc/lisp20th/lisp20th.html

- TL;DR
  - McCarthy’s 1980 notes argue Lisp survived by being a local optimum: simple core, code-as-data, and mathematical clarity. He urges scraping “barnacles,” building shared libraries, smoothing the language, and exploiting Lisp’s suitability for machine-checked proofs. He predicts higher-level, declarative systems that can refer to their own programs may supersede Lisp. HN discusses Clojure vs Rust domains and longevity, highlights ongoing Common Lisp activity, and debates whether McCarthy foresaw LLM/agentic coding or Prolog-like declarative systems—raising concerns about LLM nondeterminism and correctness.

- Comment pulse
  - Clojure vs Rust: different problem domains; Clojure JVM-bound and niche; CL/Scheme seen as longer-lived; recent CL tooling shows ongoing vitality.
  - McCarthy’s declarative successor → some see LLM/agentic coding; others say Prolog; skeptics note LLMs’ nondeterminism and errors — counterpoint: LLMs help, not replace languages.
  - Why Lisp lags: some blame functional learning curve; others cite 90s OO/web fads; CL supports procedural and functional.

- LLM perspective
  - View: McCarthy anticipated declarative, self-referential tooling; Lisp's strengths remain: homoiconicity, macros, formal reasoning potential.
  - Impact: If correctness proofs and shared libraries mature, CL could anchor AI tooling; Clojure stays pragmatic on JVM; Rust dominates systems.
  - Watch next: Concrete: verified Lisp subsets, proof assistants integration; standardized CL package registries; benchmarks comparing LLM-driven codegen to Prolog-style planners on tasks.
