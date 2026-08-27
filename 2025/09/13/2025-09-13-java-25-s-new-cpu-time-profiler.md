# Java 25's new CPU-Time Profiler

- Score: 154 | [HN](https://news.ycombinator.com/item?id=45230265) | Link: https://mostlynerdless.de/blog/2025/06/11/java-25s-new-cpu-time-profiler-1/

### TL;DR

OpenJDK 25 adds JEP 509's experimental, disabled-by-default JFR CPU-time profiler for Linux. Unlike execution-time sampling, it samples Java threads by consumed CPU time, helping distinguish compute-heavy work from waiting and reporting failed or lost samples. New `jdk.CPUTimeSample` and loss events, throttling controls, flame graphs, and command-line views expose hot methods and recording quality. The author warns of limited platform support and follow-up concurrency issues. HN comments praised recent JVM development while noting that sampling still has error boundaries.

### Comment pulse

- Built-in integration improves Java awareness → external system profilers may capture native traces without understanding Java frames.
- Accuracy has limits → commenters stressed that CPU-time profiling remains sampling rather than complete tracing.
- Broader JVM enthusiasm dominated → discussion also debated virtual threads, reactive programming, backpressure, and resource limits.

### LLM perspective

- View: Recording sample failures and losses makes profiler uncertainty visible instead of silently presenting incomplete evidence.
- Impact: Linux JVM operators gain supported CPU attribution inside JFR, reducing dependence on unsupported runtime interfaces.
- Watch next: Production overhead, queue-loss rates, memory-ordering fixes, and eventual Windows or macOS support.
