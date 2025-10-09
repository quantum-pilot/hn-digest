# We found a bug in Go's ARM64 compiler

- Score: 674 | [HN](https://news.ycombinator.com/item?id=45516000) | Link: https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/

- TL;DR
    Cloudflare tracked sporadic crashes on ARM64 Go services to a compiler/assembler interaction: large stack-pointer restores in function epilogues were split into two ADDs. Async preemption between them left SP “between frames,” so GC’s stack unwinder read garbage, triggering segfaults or “traceback did not unwind completely.” They built a minimal reproducer with a >64 KiB frame and confirmed the race. Fix landed in Go 1.23.12, 1.24.6, 1.25.0: build the offset in a temp register, then single ADD to SP. HN debated compiler vs assembler fixes, safepoints, and trusting compilers.

- Comment pulse
    - Make SP adjustment atomic → load constant to a temp, do one ADD; avoids mid-epilogue preemption — counterpoint: assembler should special-case SP immediates; handwritten asm remains risky.
    - “Stack moves once” matters → unwinder needs consistent SP; alternatives like LDR-literal or safepoints noted, but GC still requires valid frames.
    - Compiler bugs are hard to suspect → extreme-performance domains routinely hit corner cases; experience helps avoid misattributing crashes to app code.

- LLM perspective
    - View: Enforce atomic SP updates; preemption-sensitive epilogues are a recurring runtime hazard on fixed-width ISAs.
    - Impact: Go ARM64 users should upgrade; audit custom AArch64 asm touching SP; add preemption stress tests to CI.
    - Watch next: Assembler guards for SP immediates; runtime invariants tests around prologue/epilogue; survey for similar risks on other architectures.
