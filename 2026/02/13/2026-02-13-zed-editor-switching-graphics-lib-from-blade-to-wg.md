# Zed editor switching graphics lib from blade to wgpu

- Score: 277 | [HN](https://news.ycombinator.com/item?id=47002825) | Link: https://github.com/zed-industries/zed/pull/46758

### TL;DR

A merged 27-commit pull request removes Blade from Zed’s Linux GPUI renderer and ports it to wgpu, aiming to fix Nvidia and Smithay-Wayland freezes while sharing improvements with Rust’s larger graphics ecosystem. The change remains Linux-only; maintainers prefer native macOS and Windows renderers for performance and compatibility. Reviewers refined adapter selection, buffer reuse, transparency, formats, and binding allocation, but reported unresolved memory and VRAM differences. Commenters welcomed ecosystem convergence yet noted that browser support still requires web-compatible tasks, filesystem, and input layers, while broader GPUI development is being deprioritized.

### Comment pulse

- One empty-window comparison showed roughly 100 MB for wgpu versus 10 MB for GPUI on Windows—counterpoint: real workloads and tuning may narrow it.
- Rust GUI users described an immature, understaffed ecosystem forcing tradeoffs among egui, iced, Slint, web shells, or older native frameworks.
- GPUI’s community ambitions are paused for business priorities; a community fork exists, but maintainers question whether extraction effort has enough support.

### LLM perspective

- View: Standardizing the Linux backend buys shared maintenance, while preserving native renderers acknowledges abstraction costs differ by platform.
- Impact: Linux users may lose freeze bugs but face resource regressions; GPUI consumers gain wgpu interoperability amid uncertain stewardship.
- Watch next: Benchmark RAM, VRAM, latency, power, adapter coverage, Wayland compositors, and whether post-merge reports confirm resolved freezes.
