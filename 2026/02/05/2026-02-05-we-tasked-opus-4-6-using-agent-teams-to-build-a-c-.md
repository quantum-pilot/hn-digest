# We tasked Opus 4.6 using agent teams to build a C Compiler

- Score: 718 | [HN](https://news.ycombinator.com/item?id=46903616) | Link: https://www.anthropic.com/engineering/building-c-compiler

### TL;DR
Anthropic used 16 parallel Claude Opus 4.6 agents, a custom Docker/git harness, and very strong test suites to autonomously build a 100k‑line Rust C compiler. In ~2,000 sessions and ~$20k of API usage, it produced a clean-room (no internet during development) compiler that builds a bootable Linux 6.9 for x86/ARM/RISC‑V and many major projects, though with poor optimization, gaps (16‑bit x86, assembler/linker), and brittle regressions. HN discussion centers on correctness, “clean-room” claims, and how much credit belongs to tests vs agents.

---

### Comment pulse
- Impressive milestone → Compiling and booting Linux plus QEMU/FFmpeg/DBs shows serious capability, even if codegen is slower and less optimized than GCC.  
- Not truly “clean-room” → Model is trained on GCC/Clang code, so this resembles fuzzy recall steered by tests, not legal clean-room isolation — counterpoint: copyright protects text, not ideas.  
- Tests over agents → Success highlights exhaustive test harnesses and CI; some argue a single strong model with the same tests could match this without parallel agent complexity.

---

### LLM perspective
- View: This is a concrete blueprint for long-running agent systems: infinite loops, file locks, CI, and carefully structured logs/tests.  
- Impact: Compiler, tooling, and infrastructure work with rich test suites will be first areas where autonomous agents add real, sustained value.  
- Watch next: Independent audits of correctness/performance, “agent team” frameworks generalized beyond compilers, and experiments where agents propose their own tests and CI scaffolding.
