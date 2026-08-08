# Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc

- Score: 360 | [HN](https://news.ycombinator.com/item?id=48073680) | Link: https://twitter.com/jarredsumner/status/2053047748191232310

### TL;DR

Bun’s experimental 960,000-line Rust rewrite reportedly reached 99.8% compatibility with its test suite on Linux x64 glibc, only days after it had more than 16,000 compiler errors and could not run JavaScript. Jarred Sumner says a fuller account will cover performance, memory use, maintainability, and the actual workflow, emphasizing that this was not a one-command Claude conversion. The milestone makes the experiment unexpectedly viable, but it does not yet establish that Bun will adopt the rewrite or that test parity translates into maintainable production software.

### Comment pulse

- Developers see translation plus comprehensive tests as an ideal agent task because the existing implementation supplies behavior and rapid feedback.
- Rust’s strict compiler is praised as an error-correction loop — counterpoint: refactoring cascades and weak architecture can still produce unreadable, tangled code.
- Reaction is polarized: some celebrate accelerated systems work, while others distrust Bun’s Anthropic ties, changing priorities, and recent reliability.

### LLM perspective

- Compare equivalent Zig and Rust implementations under identical workloads before attributing gains to language or agent use.
- Track unsafe blocks, dependency growth, compile times, and reviewer effort alongside benchmark wins.
- Publishing compute cost and human intervention would make the experiment reproducible rather than merely spectacular.
