# Rust Glancer: Rust LSP using 100x less RAM

- Score: 409 | [HN](https://news.ycombinator.com/item?id=49393052) | Link: https://rust-glancer.github.io/blog/hello-world/

### TL;DR

Rust Glancer targets under 100MB on reasonable projects and instant reuse of indexes after restart. Instead of rust-analyzer’s in-memory incremental model, it freezes analysis on save, stores results on disk, loads query data, and uses shallow analysis while typing. Initial indexing was modestly faster in two author-run MacBook tests, but the four-month-old project remains incomplete, delays new-item indexing until save, and lacks some actions, syntax, and macro/build-script support. Comments welcomed a lower-memory option yet requested direct comparative memory measurements; supplied benchmarks report indexing time, not the title’s 100-fold RAM claim.

### Comment pulse

- The author says LLMs supplied domain expertise but sometimes created costly duplicate architecture; human review and code ownership remained essential.
- Technical discussion examined serialized disk caches, query-scoped loading, corruption awareness, and whether persistent storage could also improve rust-analyzer.
- Users asked about proc macros and Zed support; several welcomed an incomplete alternative after encountering rust-analyzer setup or memory problems.

### LLM perspective

- View: Disk-backed analysis makes persistence central, accepting saved-file boundaries rather than optimizing every keystroke.
- Impact: Developers on constrained machines or duplicate IDE sessions may reclaim RAM if missing features fit their workflows.
- Watch next: Side-by-side peak and steady-state memory tests, larger repositories, correctness suites, code actions, editor support, and proc-macro experiments.
