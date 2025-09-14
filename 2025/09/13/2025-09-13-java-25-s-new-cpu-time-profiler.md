# Java 25's new CPU-Time Profiler

- Score: 154 | [HN](https://news.ycombinator.com/item?id=45230265) | Link: https://mostlynerdless.de/blog/2025/06/11/java-25s-new-cpu-time-profiler-1/

- TL;DR
  - OpenJDK 25 adds an experimental CPU‑time profiler to JFR that samples each Java thread by CPU time (Linux only, off by default), fixing wall‑clock subsampling and execution‑time bias. It introduces jdk.CPUTimeSample and loss metrics, supports throttling by interval or rate, and views for hot methods and sampling stats. In the example, CPU‑time highlights compute‑heavy tenFastRequests over I/O‑bound oneSlowRequest. Discussion: praise for recent JVM stewardship; debate over virtual threads vs reactive backpressure; macOS Instruments traces natively but lacks Java stack insight.

- Comment pulse
  - JVM progress is impressive → Faster releases, solid leadership; Mark Reinhold credited; Oracle praised for stewardship.
  - Virtual threads can replace reactive → simpler code, may be cheaper — counterpoint: reactive enforces backpressure and budgeting; virtual threads don’t solve external limits.
  - Linux CPU-time sampling improves accuracy → per-thread CPU timers beat wall-clock; Apple Instruments offers tracing — counterpoint: lacks Java frames; JFR integrates with JVM.

- LLM perspective
  - View: Embedding CPU-time profiling in JFR normalizes safe, JVM-aware sampling and exposes losses/failures for better trust.
  - Impact: Linux production profiling gets truer CPU hotspots; macOS/Windows devs still stuck with wall-clock or external tools.
  - Watch next: Ports to macOS/Windows, JMC UI polish, benchmarks vs async-profiler/eBPF, and resolution of memory-ordering/synchronization follow-ups.
