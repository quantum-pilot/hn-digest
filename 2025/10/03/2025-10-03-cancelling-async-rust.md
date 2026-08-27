# Cancelling async Rust

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45464632) | Link: https://sunshowers.io/posts/cancelling-async-rust/

### TL;DR

Rain explains that any Rust future can be cancelled by dropping it at an await point, a powerful mechanism that also makes correctness non-local because parent cancellation propagates to children. The post distinguishes local “cancel safety” from system-level “cancel correctness,” illustrating message loss, partial writes, and broken mutex-protected invariants. Recommended patterns include reserving channel capacity before sending, tracking partial write progress, pinning and resuming futures, and running cancel-unsafe work in tasks. Safe Rust lacks a systematic type-level solution today.

### Comment pulse

- Readers found the cancel-safety versus cancel-correctness distinction useful, though some disputed the value-laden “safety” terminology.
- Discussion noted that eager futures in other languages can reverse which send or receive operation is hazardous.

### LLM perspective

- View: Cancellation's composability gap is unusually at odds with Rust's preference for local reasoning.
- Impact: Ordinary timeout and select patterns can silently violate invariants even when every API call is safe Rust.
- Watch next: Linear types, async drop, structured concurrency, and clearer API contracts may make cancellation properties enforceable.
