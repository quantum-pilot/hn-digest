# Replacing Protobuf with Rust

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46730214) | Link: https://pgdog.dev/blog/replace-protobuf-with-rust

### TL;DR

Profiling PgDog’s Rust bindings to PostgreSQL’s C parser showed Protobuf conversion, not parsing, dominated CPU time. Caching prepared statements missed ORM-generated variants and older clients, so the team forked the bindings. In two days, Claude helped generate roughly 6,000 lines of direct C-to-Rust mappings, checked byte-for-byte against existing parse and deparse output. Throughput rose from 613 to 3,357 parses per second and 759 to 7,319 deparses; changing four hot methods improved pgbench by 25 percent. The price is extensive unsafe, version-coupled glue.

### Comment pulse

- The headline obscures the mechanism → removing in-memory serialization caused the win, not Rust replacing C.
- Protobuf retains ergonomic value → typed multi-language bindings and schema evolution matter — counterpoint: hot proxy paths justify maintained FFI glue.
- Profiling prevented guesswork → the flame graph isolated conversion while the mature parser barely registered.

### LLM perspective

- View: Specialized FFI is rational when measured serialization cost dominates and compatibility is automatically testable.
- Impact: PgDog reduces proxy CPU and latency but owns thousands of unsafe conversion lines.
- Watch next: AST changes, fuzzing, stack depth, differential tests, upstream helpers, and maintenance cost.
