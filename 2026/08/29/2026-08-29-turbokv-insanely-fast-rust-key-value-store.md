# TurboKV: Insanely fast Rust key-value store

- Score: 171 | [HN](https://news.ycombinator.com/item?id=49486334) | Link: https://github.com/kingroryg/turbokv

### TL;DR

TurboKV is an asynchronous Rust key-value store offering atomic batches, coherent ordered scans, compression, compaction, and three persistence presets. Its published Apple M4 benchmark reports very high throughput in Fast and Durable modes, but Fast disables the WAL and Durable does not synchronize every acknowledged write; Paranoid does, with sharply lower single-write performance. Commenters therefore dispute both the Durable label and “insanely fast” framing, while also questioning an 84 MB benchmark that fits easily within 32 GiB of memory and lacks larger-than-RAM testing.

### Comment pulse

- Durability naming misleads → acknowledged Durable writes may be lost on power failure, while Paranoid supplies the expected sync barrier.
- Benchmark scope is narrow → in-memory-sized data and unmatched persistence semantics limit cross-engine conclusions.
- Database building remains instructive → commenters enjoy the engineering exercise despite questioning terminology such as embedded versus embeddable.

### LLM perspective

- View: TurboKV exposes useful persistence tradeoffs, but its headline performance depends heavily on which acknowledgement guarantee users select.
- Impact: Developers must map presets to failure tolerance before treating throughput numbers as purchasing evidence.
- Watch next: Power-cut testing, larger-than-memory workloads, random reads, and durability-matched competitors would strengthen the evaluation.
