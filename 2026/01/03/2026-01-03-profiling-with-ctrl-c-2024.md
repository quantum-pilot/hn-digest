# Profiling with Ctrl-C (2024)

- Score: 76 | [HN](https://news.ycombinator.com/item?id=46475296) | Link: https://yosefk.com/blog/profiling-with-ctrl-c.html

### TL;DR
The post argues that “profiling with Ctrl-C” — attaching a debugger to a slow program, interrupting it, and inspecting the stack — is a surprisingly powerful, low-effort way to find obvious performance bugs. It excels for dumb, glaring issues (e.g., debug builds stuck deep in JSON parsing, tools slowed by DWARF debug info interactions) and works even in hostile or constrained environments. However, it fails for small, distributed slowdowns, tail latency, or complex multi-threaded systems, where proper profilers remain essential.

---

### Comment pulse
- Ctrl-C time sampling parallels “random page from core” memory-leak sampling → crude, but often enough to catch large leaks or hotspots.
- Technique is no substitute for learning perf/Instruments/UIForETW → modern profilers are approachable and needed once problems aren’t dominated by a single hotspot.
- People frequently automate this idea → periodic SIGALRM stack dumps, gdbserver sampling on embedded, scripts collecting traces to approximate a sampler.

---

### LLM perspective
- View: Treat Ctrl-C sampling as a first-line diagnostic: nearly zero setup, great for “what’s obviously wrong here?”.
- Impact: Helps generalists, managers-turned-coders, and teams on weird hardware or build setups get value without deep tooling knowledge.
- Watch next: Document “Ctrl-C triage → real profiler” workflows; add built-in low-friction sampling modes to debuggers and runtimes.
