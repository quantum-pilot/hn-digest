# Writing an operating system kernel from scratch

- Score: 224 | [HN](https://news.ycombinator.com/item?id=45240682) | Link: https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/

- TL;DR
    - A minimal time-sharing kernel on RISC‑V written in Zig, packaged as a unikernel. OpenSBI in M‑mode handles platform calls; an S‑mode kernel schedules fixed U‑mode threads via timer interrupts. Context switches swap stacks after saving GPRs and key CSRs (sstatus/sepc/scause/stval); syscalls (e.g., debug_print) use ecall. Runs on QEMU virt with UART fallback. It’s an educational, reproducible walkthrough. HN highlights: Zig+RISC‑V ease versus x86 legacy, pointers to “OS in 1000 LOC,” and debate over difficulty vs. impressiveness.

- Comment pulse
    - Zig + RISC‑V speed bring‑up → clean ISA, modern docs, many emulators; avoids x86 legacy hassle — counterpoint: good bootloaders keep x86 boilerplate manageable.
    - Not novel research, solid tutorial → minimal preemptive threading is well‑trodden; value is a clear, reproducible RISC‑V+OpenSBI+Zig walkthrough for students.
    - Getting started is easy → QEMU virt + OpenSBI suffice; cheap RISC‑V boards exist; try “OS in 1000 LOC” for a packaged path.

- LLM perspective
    - View: Zig’s inline assembly and C‑ABI interop make low‑level traps manageable; the design cleanly isolates S‑mode handling from user threads.
    - Impact: Lowers the barrier for OS learners; favors RISC‑V over x86 for simplicity; validates Zig for bare‑metal drivers/syscalls.
    - Watch next: Add MMU and per‑process isolation, richer syscalls and priorities; benchmark context‑switch latency; boot on rp2350 or HiFive boards.
