# To study how chips work, MIT researchers built their own operating system

- Score: 346 | [HN](https://news.ycombinator.com/item?id=48543311) | Link: https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610

### TL;DR
MIT’s CSAIL built Fractal, a research-focused operating system kernel that runs directly on bare metal to study modern CPUs with minimal software noise. Its key innovation, “multi-privilege concurrency” with outer kernel threads, lets the same code run across privilege levels in one address space, isolating hardware effects. Using Fractal on Apple’s M1, researchers found new branch prediction behaviors, evidence of “Phantom” speculation, and cache-side channels that survive CSV2 protections, while also correcting earlier, macOS-based measurements.

---

### LLM perspective
- View: Treating hardware as the primary object of study via a purpose-built OS is a powerful pattern for systems research.
- Impact: Microarchitecture reverse-engineering, side-channel analysis, and CPU security validation become more reliable and comparable across vendors.
- Watch next: Port experiments to newer Apple Silicon, Intel, AMD, and RISC-V; standardize benchmarks; see whether vendors patch newly exposed leaks.
