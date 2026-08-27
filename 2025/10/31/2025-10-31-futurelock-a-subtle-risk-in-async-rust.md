# Futurelock: A subtle risk in async Rust

- Score: 217 | [HN](https://news.ycombinator.com/item?id=45774086) | Link: https://rfd.shared.oxide.computer/rfd/0609

### TL;DR

Oxide defines “futurelock” as a deadlock where one future receives a queued resource but its task has stopped polling it, while that task instead awaits another future needing the same resource. A representative `tokio::select!` case combines a borrowed future, an awaited branch, and a fair mutex; every primitive behaves as documented, yet progress stops. Similar risks affect future streams and bounded channels. Recommended mitigations include spawning independent tasks, dropping abandoned futures, avoiding awaits while partially polling collections, and reviewing borrowed `select!` branches carefully.

### Comment pulse

- Readers emphasized that the bug defeats local reasoning and can remain invisible until an entire service hangs.
- Some compared it with priority inversion, but replies noted runtimes cannot inspect inert futures nested inside a task.

### LLM perspective

- View: Futurelock is an emergent liveness failure, not a faulty mutex, scheduler, or obviously careless programmer.
- Impact: Async Rust services can retain memory safety yet suffer severe, diagnostically opaque denial of service.
- Watch next: Develop Clippy warnings, executor diagnostics, adversarial tests, and clearer guidance for `select!` and future collections.
