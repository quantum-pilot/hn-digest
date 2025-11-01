# Nix Derivation Madness

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45772347) | Link: https://fzakaria.com/2025/10/29/nix-derivation-madness

- TL;DR
    - The author hits a classic Nix trap: the Ruby binary’s cache “Deriver” .drv doesn’t exist locally, and a different .drv still reproduces the same output. Fixed-output derivations decouple .drv identity from output paths—changing attributes churns entire .drv trees while outputs and substitutes remain unchanged. They show two distinct FOD inputs can be pruned and still yield the same result. HN commenters: “Deriver” is a misfeature; provenance/build-trace is coming; content-addressed derivations formalize non-uniqueness and shift Nix toward better traceability.

- Comment pulse
    - Deriver is a misfeature; provenance/build-trace mapping planned to record exact evaluation and build; expected to improve SBOMs and UX.
    - CA derivations make non-unique derivers explicit; move toward content-addressing; may yield user-specific outputs if builds aren’t reproducible — counterpoint: behavior is intentional, not a bug.
    - Rewrite versus refine: core store is small and being specified; Guix offers similar model but fewer packages.

- LLM perspective
    - View: Treat Deriver as advisory; rely on content hashes and closures, especially around FOD/CA.
    - Impact: Provenance, SBOMs, and cache debugging depend on build-trace; current ambiguity risks misattribution and wasted rebuilds.
    - Watch next: CA derivations rollout, PR 11749 landing, and reproducibility benchmarks for major packages.
