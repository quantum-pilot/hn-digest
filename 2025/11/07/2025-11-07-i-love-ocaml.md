# I Love OCaml

- Score: 284 | [HN](https://news.ycombinator.com/item?id=45846517) | Link: https://mccd.space/posts/ocaml-the-worlds-best/

TL;DR
Author argues OCaml hits a rare sweet spot: functional expressiveness (sum types, pattern matching, inference), strong static guarantees, a simple predictable runtime, and very fast compiles/tooling—more pleasant than Haskell’s complexity/space‑leak risks and Go’s verbosity and lack of FP constructs. HN discussion largely agrees on the vibe but flags adoption gaps in platform support, tooling/ecosystem, and docs/syntax; F# is proposed as a pragmatic alternative. Others note Go’s deliberate simplicity and that popularity follows platforms or killer apps more than language quality.

Comment pulse
- Adoption hampered by weak Windows support, small stdlib, brittle tooling (opam, ocamlformat), terse docs, hard-to-recover syntax → higher onboarding cost — counterpoint: F#, formatter profile, Windows/opam improving.
- Go shuns FP complexity by design → lowers training time for C-like developers; FP benefits arrive only after a costly mindset shift.
- Popularity follows platforms, killer apps, or marketing → Python’s rise tied to AI ecosystems; some argue its dominance predated PyTorch.

LLM perspective
- View: OCaml balances performance, type safety, and simplicity; adoption lags due to platform/tooling friction and lack of flagship domain.
- Impact: Teams building CLI/services can gain compile-time safety with fast iterations; Windows-heavy shops still face costs.
- Watch next: OCaml 5 effects and multicore benchmarks vs Go/Rust; Windows opam/dune releases; richer docs and curated package sets.
