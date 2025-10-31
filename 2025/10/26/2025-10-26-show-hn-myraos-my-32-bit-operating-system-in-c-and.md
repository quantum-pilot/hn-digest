# Show HN: MyraOS – My 32-bit operating system in C and ASM (Hack Club project)

- Score: 244 | [HN](https://news.ycombinator.com/item?id=45715055) | Link: https://github.com/dvir-biton/MyraOS

TL;DR
A 32-bit x86 Unix-like OS, MyraOS, written from scratch in C/ASM, ships protected mode, paging/VM, user/kernel separation, scheduler, drivers (keyboard/mouse/framebuffer/PATA), ext2, an ELF loader, and a GUI compositor—enough to run a bundled Doom port. It boots via QEMU from an ISO/fs.img and has a first release. HN celebrates the technical depth and perseverance of OSDev, suggests publishing an ISO and an in-browser demo via copy.sh/v86, highlights career value, and contrasts deliberate systems building with “vibe coding” trends.

Comment pulse
- Ship ISO and integrate with copy.sh/v86 → lowers friction; users can try in-browser — counterpoint: README implies ISO available in releases.
- OSDev is hard but rewarding → vector tables/IRQs and assembly detours resonate; this project shows patience and depth.
- Strong hiring signal → complex C/ASM, filesystem/drivers, and a working GUI/game demonstrate ownership beyond “vibe coding.”

LLM perspective
- View: Ambitious hobby OS hits memory mgmt, drivers, ELF, GUI; Doom proves userland stack works end-to-end.
- Impact: Attracts contributors, recruiters, and OSDev learners; could seed a teaching platform or retrocomputing distro.
- Watch next: Add networking, SMP/ACPI, USB, package tool; publish perf metrics and test coverage; provide v86 demo and hardware support matrix.
