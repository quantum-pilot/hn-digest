# Flow: Actor-based language for C++, used by FoundationDB

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46191763) | Link: https://github.com/apple/foundationdb/tree/main/flow

### TL;DR

FoundationDB’s repository exposes Flow, an actor-oriented extension around C++ with an actor compiler and runtime components spanning networking, files, scheduling, tracing, memory, and platform support. Its defining payoff, according to the discussion, is deterministic simulation: physical interfaces and the event loop can be replaced so an entire distributed cluster runs reproducibly as concurrent actors in one thread. Commenters praise typed message passing and FoundationDB’s operational reliability, but flag Flow’s unusual build-time dependency on a C#/.NET compiler for an incomplete C++ subset.

### Comment pulse

- Deterministic simulation drives confidence → failures become reproducible, enabling post-failure instrumentation and extensive stress testing before real deployment.
- Production users report low operational burden → Snowflake, Matterport, Tigris, and s2.dev rely on FoundationDB for critical metadata or datastore workloads.
- Flow’s compiler choice puzzles developers → a C#/.NET build dependency seems awkward where a Clang rewriter or plugin might fit.

### LLM perspective

- View: Flow’s value lies less in syntax than controllable, deterministic execution.
- Impact: Database teams can test distributed failures at cluster scale without nondeterministic reproduction.
- Watch next: Compiler modernization, public reuse outside FoundationDB, and comparisons with Rust channels or async runtimes.
