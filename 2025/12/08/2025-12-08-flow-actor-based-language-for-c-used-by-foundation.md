# Flow: Actor-based language for C++, used by FoundationDB

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46191763) | Link: https://github.com/apple/foundationdb/tree/main/flow

### TL;DR
Flow is FoundationDB’s internal, actor-based extension to C++: `.actor.cpp` files are compiled by a custom C# “actorcompiler” into state-machine-style C++. This enables type-safe message-passing and, crucially, a fully deterministic single-threaded simulation of an entire distributed cluster, letting Apple torture-test FoundationDB with injected failures before ever touching real networks or disks. Hacker News discussion focuses on this testing model, where Flow underpins tools like Antithesis, plus real-world FoundationDB adopters, and debates Flow’s unusual toolchain and relation to Rust-like async/channel abstractions.

---

### Comment pulse
- Flow + simulation → tightly coupled actor model enables deterministic, single-thread cluster simulations with fault injection; FoundationDB was built this way for 18 months.  
- Adoption stories → Snowflake, Apple, Tigris, Matterport, s2.dev and others run critical metadata on FoundationDB and rarely need to touch it.  
- Language design → Flow offers type-safe message-passing and actor semantics but uses a niche C# compiler; some compare it to Rust channels/async and older QNX/ASN.1 models.  

---

### LLM perspective
- View: Flow shows the power of domain-specific concurrency layers embedded in a host language instead of rewriting everything in a new language.
- Impact: Teams needing rock-solid distributed systems can copy the “deterministic simulation + actor runtime” pattern without adopting the whole FoundationDB stack.
- Watch next: Rust, C++, and Go ecosystems may adopt more Flow-like deterministic simulators and actor compilers built atop mainstream toolchains (clang/LLVM, proc-macros).
