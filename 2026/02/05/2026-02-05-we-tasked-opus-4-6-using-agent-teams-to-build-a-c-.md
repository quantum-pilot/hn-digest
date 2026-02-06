# We tasked Opus 4.6 using agent teams to build a C Compiler

- Score: 306 | [HN](https://news.ycombinator.com/item?id=46903616) | Link: https://www.anthropic.com/engineering/building-c-compiler

## TL;DR
Anthropic used teams of Claude Opus 4.6 agents to iteratively build a ~100k‑line Rust C compiler that, without external dependencies, compiles Linux 6.9 (x86/ARM/RISC‑V), QEMU, PostgreSQL, Redis and more, passing most GCC torture tests and even running Doom. The project cost roughly $20k in API calls and hit clear limits: missing 16‑bit boot code, no assembler/linker, and poor optimization. HN debates how “clean‑room” this really is, its originality, practicality, and what it signals about near‑term agent capabilities.  

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Impressive but prototype → Commenters question production worthiness: reliance on GCC for early boot, unknown long‑run correctness, and major performance gaps versus mature compilers.  
- Clean-room claim disputed → Critics say the model regurgitates patterns from GCC/Clang training data, “decompressing” learned compilers rather than independently designing one.  
- Progress vs practicality → Some foresee agentic tools for test-heavy domains; others note $20k cost, AI backlash over flaws, and limited relevance to fuzzy real-world business software.

## LLM perspective
- View: This showcases LLMs as powerful automated implementers when goals are well-specified and correctness is machine-checkable via large regression suites.  
- Impact: Compiler and systems teams gain a template for semi-automated porting, refactoring, and new backend work rather than greenfield design.  
- Watch next: Replicate this on novel languages or ISAs with benchmarks and diff analysis to measure originality and reliability claims.
