# My first impressions of gleam

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45231852) | Link: https://mtlynch.io/notes/gleam-first-impressions/

- TL;DR
  - A Go/Python developer tries Gleam by writing an AIM log parser. They learn to think functionally with pipelines, pattern matching, map/filter, and Results; miss loops, returns, and indexing; find CLI args via third-party libs and “gleam build” artifacts unclear; and dislike error handling breaking pipeline flow. They praise pipelines, example-driven docs, unused warnings, and the todo keyword. HN highlights parser combinators and decoders, notes the small ecosystem, and debates BEAM’s strengths versus a native target.

- Comment pulse
  - Functional languages fit parsing → parser combinators, ADTs, pattern matching, recursion compose parsers into bigger ones — counterpoint: libraries make this work in Python/C++ too.
  - BEAM over native → lightweight per-process heaps, preemptive scheduling, supervision, and simple message passing enable resilient, scalable servers; some still want an LLVM/native target.
  - Gleam’s appeal → small, readable core; pipelines and docs shine; downside is immature stdlib/ecosystem—though decoders and parser libraries help today.

- LLM perspective
  - View: Gleam lowers FP friction by pairing BEAM reliability with an opinionated core; friction points are tooling clarity and error ergonomics.
  - Impact: Best fit for backends and parsers; teams wanting BEAM safety plus static types, with optional JS interop.
  - Watch next: Add a native compiler target, improve CLI/build docs, and introduce ergonomic pipeline-aware error propagation; track growth of parser/decoder libraries.
