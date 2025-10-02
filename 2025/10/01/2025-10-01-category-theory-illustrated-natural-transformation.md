# Category Theory Illustrated – Natural Transformations

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45435422) | Link: https://abuseofnotation.github.io/category-theory-illustrated/11_natural_transformations/

- TL;DR
    - Illustrated tour of natural transformations (morphisms between functors) and how natural isomorphisms formalize categorical equivalence (F∘G ≅ Id, G∘F ≅ Id). Explains naturality squares, 2×C encoding, composition/whiskering, and shows polymorphic functions (reverse, flatten) as natural transformations in programming. HN readers liked the exposition, questioned the philosophy prelude, explained CT’s appeal for programmers, and offered a technical correction: state naturality with component subscripts and equality in 1-categories.

- Comment pulse
    - Philosophy critique → Parmenides denied change; essence stems from Aristotelian ousia; Plato’s forms explain constancy, not change — counterpoint: article’s framing overstates Parmenides/essence link.
    - Why CT? → Morphism-first abstraction specifies constraints concisely; accessible basics; drives reusable FP interfaces (functors, monads, lenses) and practical wins (e.g., UMAP).
    - Natural transformation law → Use components: α_e ∘ Ff = Gf ∘ α_a; equality, not isomorphism, in 1-categories; subscripts matter.

- LLM perspective
    - View: Bridges formal CT with programmer intuition; strongest when showing polymorphism-as-naturality and 2×C functor encoding.
    - Impact: Could guide FP library design, refactoring, and proofs of correctness via commuting diagrams and parametricity.
    - Watch next: Tighten notation; add concrete Haskell/TypeScript laws and property tests; cover 2-categories, Yoneda, and adjunctions next.
