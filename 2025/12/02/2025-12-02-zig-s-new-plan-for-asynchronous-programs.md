# Zig's new plan for asynchronous programs

- Score: 194 | [HN](https://news.ycombinator.com/item?id=46121539) | Link: https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/

### TL;DR

Zig's proposed asynchronous design passes a generic `Io` interface through I/O-using functions, letting the same straight-line code run with threaded or event-driven backends. Explicit `async` marks work that may run concurrently as an optimization; `concurrent` is required when parallel progress is necessary for correctness. This avoids new language-specific async control flow while preserving `try` and `defer`, but adds parameter plumbing and backend-dependent behavior. `Io.Evented` remains experimental and incomplete. HN debated whether the design solves function coloring or merely makes it ergonomic.

### Comment pulse

- Andrew Kelley corrected that `Io.Threaded` normally dispatches async tasks to a configurable pool and that `asyncConcurrent` became `concurrent`.
- Supporters saw an explicit, controllable execution interface; critics compared it with effect tokens, Scala execution contexts, and Haskell IO.
- Users worried about deadlocks, backend interference, suspend/resume use cases, and repeatedly passing `io` into file methods.

### LLM perspective

- View: Zig sidesteps syntax coloring by making execution strategy an explicit dependency, not invisible runtime policy.
- Impact: Library authors can share APIs across synchronous and evented callers while application authors retain backend control.
- Watch next: Cross-platform Evented implementations, WebAssembly support, deadlock guidance, and API stability before 1.0.
