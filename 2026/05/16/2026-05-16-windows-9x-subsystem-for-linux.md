# Windows 9x Subsystem for Linux

- Score: 212 | [HN](https://news.ycombinator.com/item?id=48120162) | Link: https://codeberg.org/hails/wsl9x

### TL;DR

WSL9x runs a patched Linux 6.19 kernel cooperatively inside Windows 9x, using a VxD driver, a User-Mode Linux adaptation, and a 16-bit `wsl.com` client that turns DOS prompts into terminals. The driver loads Linux at a fixed address, dispatches interrupts, page faults, and syscalls, and traps `int 0x80` through Windows’ general-protection handler. HN admired the retrocomputing feat but corrected claims about modern i386 support, debated the project’s “written without AI” badge, and joked about Microsoft’s subsystem naming.

### Comment pulse

- Modern kernels do not retain true i386 support → commenters noted 386 was dropped in 2012 and 486 support disappeared in 2026.
- “Proudly written without AI” drew approval → counterpoint: critics called process labels performative and judged software by delivered value.
- The title revived WSL’s grammar dispute: “Windows subsystem for running Linux” is defensible, though “Linux Subsystem for Windows” sounds clearer.

### LLM perspective

- **View:** The project demonstrates how much OS integration can emerge from loaders, fault handlers, and cooperative scheduling.
- **Impact:** Retrocomputing developers gain a bridge to modern Linux tools, though setup remains specialist and hardware support constrained.
- **Watch next:** Track syscall coverage, memory isolation, I/O support, application compatibility, performance, and reproducible build instructions.
