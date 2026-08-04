# Postgres rewritten in Rust, now passing 100% of the Postgres regression tests

- Score: 303 | [HN](https://news.ycombinator.com/item?id=48841676) | Link: https://github.com/malisper/pgrust

### TL;DR

pgrust is an AGPL Rust reimplementation of PostgreSQL 18.3 that now passes all 46,066 regression tests and offers wire and SQL compatibility. Its redesign adds a vectorized JIT executor, threads, scheduling, an OOM killer, and optional columnar storage; Graviton4-tuned benchmarks claim 30% higher read-only OLTP throughput and better ClickBench results than ClickHouse. The authors call it buggy and non-production-ready, without PostgreSQL extension compatibility. HN praised the milestone but demanded stronger evidence: Jepsen, fuzzing, crash testing, shadowed production workloads, durability validation, and scrutiny of AI-generated code and benchmark tradeoffs.

### Comment pulse

- Passing regression tests establishes behavioral breadth → it cannot prove crash safety, concurrency correctness, durability, or performance under pathological production workloads.
- AI-scale commit volume changes review strategy → collaborators favor auditing proofs, differential fuzzers, and harnesses over inspecting thousands of machine-generated commits.
- Thread-per-connection promises speed → shared-process failures can widen extension blast radius — counterpoint: extensions remain unsupported, and the project warns against production use.

### LLM perspective

- **View:** Database equivalence is multidimensional; SQL result parity says little about recovery, isolation, replication, resource exhaustion, or operational tooling.
- **Impact:** Rewrites can unlock architecture changes compatibility constrains, but every optimization expands the validation surface before users can trust data.
- **Watch next:** Jepsen results, simulated faults, differential fuzzing coverage, recovery behavior, extension ABI, untuned hardware benchmarks, and sustained mirrored-production equivalence.
