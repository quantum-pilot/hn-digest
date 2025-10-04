# Cancelling async Rust

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45464632) | Link: https://sunshowers.io/posts/cancelling-async-rust/

- TL;DR
    - Async Rust cancellations are implicit: futures are passive state machines that get cancelled when dropped, and parent drops cancel children. Rain distinguishes cancel safety (local) from cancel correctness (system-wide). Common pitfalls: mpsc send+timeout losing messages, awaits while holding Tokio mutexes breaking invariants, try_join/select silently cancelling other work. Mitigations: redesign APIs (reserve+send, write_all_buf), pin to resume instead of restarting, run critical work in tasks. Systemic ideas (async drop, linear types, cancellation tokens) exist but are challenging. HN debates naming and proposes unified cancellation tokens; contrasts with eager-future languages.

- Comment pulse
    - Unify cancellation across sync/async → CancellationTokens and “must-run-to-completion” async functions enable graceful teardown.
    - 'Cancel safety' misleads → desired behavior depends on context; 'cancel correctness' better captures system invariants — counterpoint: runtime-spawned tasks lingering can also be a bug.
    - Eager-future ecosystems flip risks → send+timeout often fine; recv+timeout may drop data after readiness; fix by selecting readiness and peeking.

- LLM perspective
    - View: Treat cancellation as a first-class failure mode; design APIs to expose progress or acquire-permit semantics.
    - Impact: Rust async libraries, services, and infra teams; fewer heisenbugs, clearer invariants, safer shutdown paths.
    - Watch next: CancellationTokens RFCs, async drop experiments, Tokio adding more cancel-safe variants, Clippy lints adoption, benchmarks on pinned-reserve fairness.
