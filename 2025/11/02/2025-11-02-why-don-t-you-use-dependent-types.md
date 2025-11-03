# Why don't you use dependent types?

- Score: 171 | [HN](https://news.ycombinator.com/item?id=45790827) | Link: https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html

- TL;DR
    - Paulson isn’t anti–dependent types—he used AUTOMATH and Martin‑Löf—but argues Isabelle’s LCF/HOL avoids bulky proof objects, remains stable, and scales via automation. ALEXANDRIA formalized schemes and additive combinatorics in HOL, rarely needing ZF axioms, undermining “DTs are necessary.” He flags practical frictions: intensional equality headaches, performance complaints, and that DTs often work best when avoided. HN echoes: DTs excel at shape/index safety; HOL’s strength can be augmented with axioms; Lean’s community/process may matter more than foundations.

- Comment pulse
    - Dependent types improve shape/index safety → catch out-of-bounds and dimensional errors statically; but debugging and equality coercions become painful—counterpoint: use them sparingly at boundaries.
    - HOL is too weak for modern math → limited strength and size handling; — counterpoint: extend with axioms/universes; Isabelle formalised schemes and BSG within HOL.
    - Community/process outweigh foundations → mathlib’s PR workflow and Blueprint speed contributions; AFP’s journal-style curation trades agility for review.

- LLM perspective
    - View: Favor a stable core logic plus libraries; add axioms when needed; use dependent types where they simplify interfaces, not internals.
    - Impact: Mathematics teams gain from automation and ecosystem; proof engineers should prioritize equality ergonomics and build reproducible, PR-friendly workflows.
    - Watch next: Cross-project benchmarks: Lean vs Isabelle on large theories; equality tooling (heterogeneous congruence); Lean Blueprint-like planning in Isabelle/AFP.
