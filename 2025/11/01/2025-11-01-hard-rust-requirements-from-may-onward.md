# Hard Rust requirements from May onward

- Score: 309 | [HN](https://news.ycombinator.com/item?id=45779860) | Link: https://lists.debian.org/debian-devel/2025/10/msg00285.html

- TL;DR
    - Debian’s APT will require Rust no earlier than May 2026, starting with the Rust toolchain and Sequoia for parsing .deb/.ar/.tar and verifying HTTP signatures. Ports without Rust have six months to add a toolchain or sunset. HN reactions split: proponents cite memory safety and better contributor supply; skeptics warn rewrites of mature parsers risk regressions and prefer mitigations like Fil-C. Others note Rust is already required on most Debian release architectures; GCC-based Rust efforts aren’t ready.

- Comment pulse
    - Security-first stance → untrusted archive parsing is a chronic CVE source; Rust’s safety and ecosystem help, and it draws maintainers amid an aging C talent pool.
    - Rewrite skepticism → mature .tar/.ar code is stable; new Rust may regress readability and compatibility; projects like Fil-C harden C — counterpoint: security flaws evade “happy-path” reliability.
    - Scope and tooling realities → affected ports are already unofficial; alpha/hppa/m68k/sh4 lack Sequoia; GCCRS lags libcore/std while rustc_codegen_gcc may mature sooner.

- LLM perspective
    - View: Favor incremental Rust for parsers and crypto, keeping interfaces stable and reusing tests to cap rewrite risk.
    - Impact: Ports without Rust or Sequoia likely freeze; distro builders must budget toolchain bootstrapping and CI for new targets.
    - Watch next: Announced APT components rewritten; Sequoia rollout; concrete GCCRS/rustc_codegen_gcc timelines; which legacy architectures deliver toolchains versus accept deprecation.
