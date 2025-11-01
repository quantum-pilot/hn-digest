# John Carmack on mutable variables

- Score: 457 | [HN](https://news.ycombinator.com/item?id=45767725) | Link: https://twitter.com/id_aa_carmack/status/1983593511703474196

- TL;DR
  - Thread reacts to John Carmack’s take on mutable variables: many advocate immutability-by-default or single assignment to eliminate hidden ordering dependencies, simplify testing, and make functions black boxes. Others argue benefits are overstated and real-world code needs controlled mutation, shadowing, or iterative updates. Examples span Clojure, Rust, Python, Haskell, Swift; pipelines and expressions-everywhere reduce mutation pressure. Tooling already flags reassignments; calls for clearer naming, opt‑in mutability, and IDE/compiler hints. Debate also clarifies 'variable' vs 'constant' terminology.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Immutability/single assignment improves reasoning and tests by removing implicit ordering dependencies; pure functions localize context — counterpoint: advantage is oversold; controlled mutation remains practical for iteration.
  - Reusing/shadowing names like result = result.process() invites ambiguity and sanitization bugs; prefer explicit intermediate names or composition/pipelines to signal processed vs raw.
  - Make mutability opt‑in with lightweight IDE/compiler cues; IntelliJ and Swift already flag reassignments, but some prefer explicit annotations over inference that changes behavior.

- LLM perspective
  - View: Immutability by default plus scoped escape hatches and clear naming delivers most benefits without dogma.
  - Impact: Language designers, IDEs, and linters should highlight writes, shadowing, and purity; teams adopt pipelines/composition to reduce state.
  - Watch next: Benchmarks of immutable-by-default codebases, standardized mutability annotations, and tools like 'Mutalator' to visualize state changes across functions.
