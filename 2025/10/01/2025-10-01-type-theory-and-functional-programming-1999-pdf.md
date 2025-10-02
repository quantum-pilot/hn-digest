# Type Theory and Functional Programming (1999) [pdf]

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45435100) | Link: https://www.cs.cornell.edu/courses/cs6110/2015sp/textbook/Simon%20Thompson%20textbook.pdf

- TL;DR
    - Simon Thompson’s 1999 text introduces Martin-Löf constructive type theory as a unified logic and functional language via Curry–Howard (propositions-as-types). It builds from logic and lambda calculus to dependent types, total functions, normalization, universes, equality, and program extraction, with applications and critiques of extensions (subset/quotient/coinductive types). HN debates whether FP’s theory will drive broad adoption versus pragmatism; why type theory aligns with FP; and whether the book remains a good, if dense, starting point alongside TAPL/Coq resources.

- Comment pulse
    - FP theory will win → lambdas/promises/typeclasses permeate; Rust borrows OCaml ideas; effects next — counterpoint: pure FP unpopular; pragmatism/performance/tooling drive choices (cf. NoSQL vs SQL).
    - Type theory ties to FP → Curry–Howard links proofs to typed lambda calculi; imperative effects encode via monads/linear types; mutation weakens static guarantees.
    - Is it good today? → Still solid but dense; out-of-print; alternatives include Pierce’s TAPL and Coq/Rocq manuals for hands-on typing rules.

- LLM perspective
    - View: Use dependent types to make specifications executable; extract witnesses directly from proofs to reduce post-hoc verification.
    - Impact: PL designers, verification teams, and safety-critical developers gain stronger guarantees; mainstream languages adopt selective features without full totality.
    - Watch next: Algebraic effects, linear types, and lightweight dependent typing in industry; metrics on proof effort vs defects; better IDE/prover integration.
