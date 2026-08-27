# Writing an operating system kernel from scratch

- Score: 224 | [HN](https://news.ycombinator.com/item?id=45240682) | Link: https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/

### TL;DR

The tutorial builds a minimal single-core RISC-V time-sharing kernel in Zig atop OpenSBI and runs it in QEMU. Kernel and user code share one unikernel binary, but threads execute in user mode and issue system calls into supervisor mode. Periodic timer interrupts save register state, swap stack pointers, and thereby context-switch among three statically allocated, nonterminating threads. The author presents it as a deliberately rough educational starting point. HN readers praised RISC-V and Zig accessibility while debating whether such kernels are impressive or well-trodden coursework.

### Comment pulse

- RISC-V reduces legacy distraction → clear documentation and emulators let learners focus on privilege levels, interrupts, stacks, and scheduling.
- Zig fits bare-metal exploration → commenters compared it favorably with C while noting similar exercises translate readily across languages.
- Minimal kernels are approachable, not production systems → existing guides lower barriers, while persistence still supplies educational value.

### LLM perspective

- View: The project’s value is exposing a context switch directly, not claiming novel operating-system design.
- Impact: Students can connect architecture concepts to executable code before confronting loaders, dynamic processes, filesystems, or multicore synchronization.
- Watch next: Real-hardware ports, memory isolation, dynamic threads, stronger error handling, and audits of AI-generated boilerplate.
