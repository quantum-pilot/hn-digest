# Win32 is the stable Linux ABI

- Score: 165 | [HN](https://news.ycombinator.com/item?id=46433035) | Link: https://loss32.org/

### TL;DR

loss32 proposes a Linux distribution whose desktop and userland are predominantly Win32 software running through WINE, augmented by ReactOS components. It aims to preserve decades of `.exe` compatibility and classic Windows power-user ergonomics while retaining Linux’s kernel, hardware support, and ability to run native software. HN discussion largely validated the compatibility problem: kernel interfaces stay stable, but GUI toolkits and system libraries churn. Skeptics questioned feasibility, while gamers cited Proton running old Windows titles more reliably than modern Windows.

### Comment pulse

- Linux desktop compatibility breaks above the kernel → glibc, GTK, Qt, display stacks, and packaging conventions evolve independently.
- Win32 preserves cultural software → abandoned games and creative tools often remain runnable without source or rebuilds.
- A faithful classic desktop could attract users → counterpoint: hardware support, polish, and distribution remain formidable maintenance burdens.

### LLM perspective

- View: Treating WINE as the primary platform turns compatibility middleware into a deliberate product architecture.
- Impact: Users could access old binaries consistently, while maintainers inherit WINE’s desktop-integration edge cases.
- Watch next: The promised proof of concept, HiDPI behavior, Wayland integration, packaging, and ReactOS shell compatibility.
