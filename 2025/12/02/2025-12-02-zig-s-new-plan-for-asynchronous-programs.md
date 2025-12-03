# Zig's new plan for asynchronous programs

- Score: 194 | [HN](https://news.ycombinator.com/item?id=46121539) | Link: https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/

- TL;DR  
Zig is replacing its abandoned async/await system with an Io interface that abstracts I/O policy (threaded vs evented) behind a value passed into functions. The same function body can run with blocking syscalls or an event loop; async() and concurrent() express potential or required parallelism, making asynchronicity a performance choice rather than an API color. Commenters like the explicit, testable design but argue it merely shifts the function-coloring problem to “uses Io” and adds verbosity and potential concurrency pitfalls.

- Comment pulse  
  - Design recolors functions as “uses Io” → callers pass an Io token, like Go context or IO monad — counterpoint: avoids viral async keywords.  
  - Andrew Kelley clarifies Io.Threaded usually dispatches async tasks to a thread pool, and asyncConcurrent() has been renamed concurrent(); misuse causes logic bugs, not UB.  
  - Critiques: still two colors and no preemption, so CPU-bound work can starve async tasks; explicit Io passing feels verbose despite benefits for testability and mocking.

- LLM perspective  
  - View: Treating I/O policy as an injected capability aligns with dependency-injection patterns and fits Zig’s allocator-and-error-return style.  
  - Impact: Library authors must design around Io early; retrofitting legacy code may prove tedious but yields cleaner boundaries and testing.  
  - Watch next: Concrete patterns for safe concurrent(), OS-level backends for all targets, and story for suspend/resume-style flows and WebAssembly support.
