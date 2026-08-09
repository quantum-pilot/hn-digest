# Windows 9x Subsystem for Linux

- Score: 871 | [HN](https://news.ycombinator.com/item?id=47861270) | Link: https://social.hails.org/@hailey/116446826733136456

### TL;DR

WSL9x runs a modern Linux kernel cooperatively beside the Windows 9x kernel in ring 0, without modern hardware virtualization, making even 486-era machines eligible. Its author says the integration needed only a few Windows VMM services, including thread creation and memory-context operations, after six years of considering the design. Hacker News compared it with CoLinux’s side-loaded kernel, flinux and WSL1’s syscall translation, and Cygwin’s recompiled POSIX layer. Commenters praised the arcane driver work and craftsmanship, while conceding that scarce memory leaves little practical use beyond experimentation and retrocomputing.

### Comment pulse

- CoLinux is the closest precedent: both side-load Linux kernels, but WSL9x targets pre-NT Windows rather than XP-era systems.
- Cygwin keeps native Windows processes — counterpoint: its POSIX emulation required recompilation, DLL management, and complicated `fork()` semantics.
- The project’s six-year gestation and no-AI authorship became a symbol of deep craft amid increasingly cheap generated demos.

### LLM perspective

- **View:** The hack turns Windows 9x’s weak isolation into an integration surface, letting Linux assume responsibilities the host barely enforces.
- **Impact:** Retro systems gain unmodified Linux binaries beside Windows applications; useful workloads remain bounded by old hardware.
- **Watch next:** Hardware compatibility, Linux’s 486-support timeline, driver conflicts, memory limits, and possible graphical desktop experiments.
