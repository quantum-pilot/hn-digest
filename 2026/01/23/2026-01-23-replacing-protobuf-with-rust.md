# Replacing Protobuf with Rust

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46730214) | Link: https://pgdog.dev/blog/replace-protobuf-with-rust

### TL;DR
PgDog sped up PostgreSQL query parsing 5× (and deparsing ~10×) by bypassing Protobuf in `pg_query.rs` and talking directly to the C `libpg_query` AST via unsafe Rust bindings. They used bindgen plus Claude to generate ~6k lines of recursive C↔Rust conversion code, verified against existing Protobuf outputs, which yielded ~25% better `pgbench` results. Hacker News notes the title over-credits Rust; the real win is removing unnecessary serialization while keeping Protobuf for multi-language, non–perf-critical use cases.

---

### Comment pulse
- Title is Rust-bait → improvement comes from removing Protobuf serialization, not from Rust itself—counterpoint: library’s Protobuf-based API was the odd design choice.  
- Protobuf choice explained → original pg_query author: JSON→Protobuf enabled easy, typed, multi-language bindings where performance wasn’t critical; direct FFI is Rust-specific maintenance overhead.  
- Broader lesson → serialization/deserialization is a frequent hidden bottleneck; profiling plus custom data paths often beats “default” library usage, regardless of programming language.

---

### LLM perspective
- View: LLMs are well-suited to generate large, repetitive, test-oracle-validated glue code like AST mappers and FFI shims.  
- Impact: Expect more C libraries to gain high-performance, language-specific bindings without full rewrites, especially for hot paths.  
- Watch next: Benchmarks comparing Protobuf, direct FFI, and zero-copy formats; new libpg_query APIs that make non-Protobuf bindings first-class.
