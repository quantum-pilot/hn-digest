# SkiftOS: A hobby OS built from scratch using C/C++ for ARM, x86, and RISC-V

- Score: 413 | [HN](https://news.ycombinator.com/item?id=45229414) | Link: https://skiftos.org

- TL;DR
    - SkiftOS is a from-scratch, C/C++ hobby OS targeting ARM, x86, and RISC‑V, built around a Zircon‑influenced microkernel with its own UEFI bootloader, build system, GUI, UI toolkit, and nascent browser. The current build is broken, but individual apps run via skift.sh; the browser works over http only. HN praises the scope and code quality, notes portability via SDL, and asks for microkernel design docs and benchmarks—while acknowledging the time cost and sustainability of a largely solo effort.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Admiration for scope → microkernel, UEFI, GUI, toolkit, browser, build system by one dev; great hiring signal — counterpoint: unsustainable alongside a 9‑to‑5.
    - Practical status → full build broken; run apps with skift.sh; browser via vaev-browser; HTTP only; macOS works through SDL-based OS abstraction.
    - Technical curiosity → Zircon influence; requests for architecture docs, design tradeoffs, and performance benchmarks; interest in non‑UNIX direction and naming origins.

- LLM perspective
    - View: A focused, coherent solo OS can still push design exploration and tooling, especially beyond UNIX conventions.
    - Impact: Raises bar for hobby OSes; demonstrates cross‑platform app layer, inspiring educational forks and hiring pipelines.
    - Watch next: Publish kernel docs and IPC benchmarks, enable HTTPS and CI builds, package releases, and define contribution roadmap.
