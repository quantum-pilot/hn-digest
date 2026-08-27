# Profiling with Ctrl-C (2024)

- Score: 76 | [HN](https://news.ycombinator.com/item?id=46475296) | Link: https://yosefk.com/blog/profiling-with-ctrl-c.html

### TL;DR

Pausing a slow program in a debugger and inspecting its stack is an extremely low-frequency sampling profiler. A few interruptions can quickly expose dominant problems, such as repeated JSON parsing or GDB spending time decoding problematic DWARF, without special builds or profiler setup. The method fails for small distributed regressions, tail latency, and complex multi-threaded systems, where tracing, conventional sampling, or simulation is needed. HN commenters largely agree it is excellent for finding one glaring offender, not replacing proper profiling.

### Comment pulse

- Random interruption cheaply samples time → analogous techniques inspect random memory pages or periodically capture embedded-system stacks.
- The technique excels at dominant bottlenecks → repeated stacks quickly expose one overwhelming path.
- Real profilers remain necessary → 20% hotspots, dispersed 5% costs, and transient latency demand denser or targeted measurement.

### LLM perspective

- View: Ctrl-C is a high-value diagnostic probe precisely because its setup cost approaches zero.
- Impact: Developers in constrained environments can localize gross stalls before investing in specialized instrumentation.
- Watch next: Escalate when repeated samples diverge, delays are brief, or performance differences remain statistically small.
