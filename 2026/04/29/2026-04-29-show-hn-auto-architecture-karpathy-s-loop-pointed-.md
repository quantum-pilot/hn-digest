# Show HN: Auto-Architecture: Karpathy's Loop, pointed at a CPU

- Score: 228 | [HN](https://news.ycombinator.com/item?id=47937380) | Link: https://github.com/FeSens/auto-arch-tournament/blob/main/docs/auto-arch-tournament-blog-post.md

### TL;DR
An LLM-driven “Karpathy loop” is pointed at a plain 5-stage in-order RISC‑V core on a small FPGA. The agent proposes microarchitectural tweaks; a hard-coded orchestrator runs formal verification, ISS cosim, multi-seed P&R, and CoreMark with independent CRC checks. Out of 73 hypotheses, 10 survive, yielding +92% throughput and 40% fewer LUTs than the baseline and beating a published VexRiscv config. The author argues the competitive edge is not the loop, but the rigor and domain-specificity of the verifier.

---

### Comment pulse
- Is this a genetic algorithm? → Many argue it’s closer to hill climbing/SGD; others note AlphaEvolve-style LLM evolutionary work as precedent — counterpoint: population/crossover are missing here.  
- Writing style concerns → Several dislike the LLM-flavored prose and speculate it’s AI-written, yet still praise the concrete results and “verification-first” framing; request broader benchmarks.  
- Verifier and fitness dominate → Practitioners report similar loops where testsuites and fitness definitions are the real bottleneck, as agents eagerly exploit any gaps in constraints.

---

### LLM perspective
- View: Strong demonstration that LLMs can co-design hardware when tightly leashed by formal, simulation, and benchmarking gates.  
- Impact: Hardware, compilers, and infra teams with good specs can offload exploration, turning verification artifacts into core IP.  
- Watch next: Population-based search, multi-workload validation, and porting this verifier-centric pattern to domains like billing, clinical workflows, and large-scale data pipelines.
