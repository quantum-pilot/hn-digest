# To study how chips work, MIT researchers built their own operating system

- Score: 346 | [HN](https://news.ycombinator.com/item?id=48543311) | Link: https://news.mit.edu/2026/to-study-how-chips-really-work-mit-researchers-built-their-own-operating-system-0610

### TL;DR

MIT’s Fractal is a 31,000-line research kernel for x86-64, ARM64, and RISC-V that boots bare metal and minimizes interrupts, scheduling, and address-space noise. Its outer kernel threads let identical instructions run in one address space while switching privilege levels, making privilege the independent variable. On Apple M1, Fractal found cross-boundary instruction-cache fetches, Phantom speculation across privileges and processes, and no conditional-branch-predictor isolation. HN praised the reproducible infrastructure but debated whether behaviors observable only outside production operating systems constitute practical vulnerabilities, and noted earlier specialized low-noise environments.

### Comment pulse

- Hardware behavior is not automatically user risk → commenters asked whether shipped OS constraints prevent exploitation and whether fetch-only leakage justifies calling it a vulnerability.
- The clean-room method has precedent → Microsoft engineers reportedly built specialized low-noise environments under Spectre/Meltdown embargo, and minimal research operating systems were historically common.
- Fractal could support compiler benchmarks → reduced OS noise is attractive, but commenters cautioned that sound performance measurement requires broader experimental discipline.

### LLM perspective

- **View:** The major contribution is control, not another kernel: eliminating confounders can overturn architectural conclusions drawn from noisy production systems.
- **Impact:** Researchers gain portable experiments; chip vendors receive cleaner evidence, while defenders must still connect effects to deployable attacks.
- **Watch next:** Reproduce findings across chip generations, quantify attack primitives under real operating systems, and test benchmark variance across harnesses.
