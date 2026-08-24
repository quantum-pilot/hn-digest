# Zig's new plan for asynchronous programs

- Score: 194 | [HN](https://news.ycombinator.com/item?id=46121539) | Link: https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/

### TL;DR

Zig is moving asynchronous I/O behind a generic Io value passed through library calls. The same straight-line function can use Io.Threaded or the experimental Io.Evented backend, while async expresses optional parallelism and concurrent marks execution required for correctness. This avoids async-specific language syntax and lets callers choose scheduling, but behavior still depends on the supplied implementation. Andrew Kelley corrected that Threaded normally dispatches through a configurable thread pool and that asyncConcurrent was renamed concurrent. Discussion concentrated on whether the abstraction clarifies or conceals execution differences.

### Comment pulse

- Ergonomics divide readers → one Io parameter preserves ordinary control flow — counterpoint: repeatedly threading it through file methods feels noisy.
- Coloring claims remain disputed → critics call Io an explicit effect token; defenders say call syntax and library compatibility no longer bifurcate.
- Execution-context flexibility carries risk → backend-dependent scheduling may expose deadlocks, thread-safety errors, or interference; old suspend-and-resume use cases remain unclear.

### LLM perspective

- View: The design trades visible async syntax for explicit capability injection and backend-dependent semantics.
- Impact: Library authors can share APIs across blocking and evented callers, while application authors own scheduling choices.
- Watch next: Evented platform coverage, WebAssembly support, cancellation behavior, migration guidance, and concurrency bug patterns.
