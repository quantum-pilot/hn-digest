# Futurelock: A subtle risk in async Rust

- Score: 217 | [HN](https://news.ycombinator.com/item?id=45774086) | Link: https://rfd.shared.oxide.computer/rfd/0609

- TL;DR
  - Oxide coins “futurelock”: a deadlock where one task stops polling a future that owns a needed resource, while another future in the same task waits behind it. A typical trigger is tokio::select! on a borrowed future (&mut F) plus an await in another branch; fair Mutex/channel queues hand the resource to the unpolled future, so nothing advances. Debugging is painful; join_all doesn’t suffer. Mitigate by spawning work into tasks (JoinHandle/JoinSet), avoiding borrowed futures across select with awaits, and considering clippy lints; “make the channel bigger” isn’t a fix.

- Comment pulse
  - Futurelock exposes Rust async’s non-local liveness hazards → compiler can’t enforce; hangs are opaque, echoing cancellation-safety woes.
  - Prefer spawning tasks over intra-task concurrency → shared resources can starve FuturesUnordered/select; owned futures reduce risk.
  - Priority-inversion-style fixes seem impractical → runtimes can’t see intra-task futures; futures are inert — counterpoint: OS-like heuristics could help but complicate semantics.

- LLM perspective
  - View: Treat select on borrowed futures and Streams as hazardous; isolate resource-taking work in spawned tasks.
  - Impact: Affects services using fair Tokio Mutex/channels; any code mixing select-loops with awaits.
  - Watch next: Clippy lints for &mut in select; guidance favoring JoinSet; tokio-console patterns to spot stuck-but-woken tasks.
