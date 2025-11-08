# We chose OCaml to write Stategraph

- Score: 144 | [HN](https://news.ycombinator.com/item?id=45845958) | Link: https://stategraph.dev/blog/why-we-chose-ocaml

TL;DR
Stategraph, a Terraform/OpenTofu state store by Terrateam, is written in OCaml to make state corruption provably hard: strong types for state and SQL, PPX-generated JSON codecs, default immutability plus PostgreSQL locks, and exhaustive error handling push failures to compile time. HN debates whether language choice is mostly preference, the real-world value of strong types in cutting validation/tests, and whether Terraform concurrency is a real pain; the CTO argues resource‑level parallelism avoids module-splitting and long queues.

Comment pulse
- Stack choices are often subjective → aesthetics, morale, and team strengths matter; formalize as fit-to-software/process/skills to stay professional — counterpoint: evangelism can mask post‑hoc reasoning.
- Strong type systems cut boilerplate → move validation and many tests to compile time; TypeScript migrants report fewer unit tests.
- Terraform concurrency need questioned → many serialize applies; CTO says Stategraph enables per-resource parallelism without splitting modules, reducing waits.

LLM perspective
- View: OCaml reduces unknown-unknowns in stateful backends more than marginal runtime optimizations.
- Impact: Better developer throughput via fewer flaky tests and safer schema evolution; faster CI feedback with parallel plans.
- Watch next: Open licensing, migration path from existing state backends, reproducible benchmarks comparing plan/apply latency under contention.
