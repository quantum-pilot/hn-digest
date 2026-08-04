# Memory Safe Context Switching

- Score: 207 | [HN](https://news.ycombinator.com/item?id=48727177) | Link: https://fil-c.org/context_switches

### TL;DR

Fil-C 0.681 makes C’s nonlocal jumps and ucontext fiber APIs memory-safe despite their ability to restore dead stacks. setjmp creates an opaque runtime object tied to its originating frame; longjmp walks ancestor frames and panics unless the target remains valid, while saved GC roots preserve capability state. ucontext similarly hides internal fiber stacks, enforces a strict lifecycle and thread affinity, and rescans suspended stacks during garbage collection. HN praised the explanation, discussed copied-stack continuations and pointer-relocation hazards, and noted ucontext’s signal-mask overhead versus specialized assembly fiber switches.

### Comment pulse

- Stack copying can implement continuations → restoring copies to the same address range avoids relocating pointers into C stack frames.
- Safety precedes performance → Fil-C wraps glibc’s heavier signal-mask behavior first; a sigmask-free backend can follow after adversarial testing.
- Boost comparison needs nuance → its fast paths use platform-specific assembly, with ucontext serving only as a slow fallback.

### LLM perspective

- **View:** Memory safety can encompass control-flow state when contexts become capabilities with explicit lifetimes.
- **Impact:** Legacy C libraries can retain exception and fiber idioms while converting dangling-stack exploits into deterministic panics.
- **Watch next:** Expand misuse tests, improve compiler diagnostics, and validate GC-root restoration under optimized builds.
