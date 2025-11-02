# CharlotteOS – An Experimental Modern Operating System

- Score: 145 | [HN](https://news.ycombinator.com/item?id=45781397) | Link: https://github.com/charlotte-os/Catten

- TL;DR
  - Catten is a Rust, monolithic kernel for CharlotteOS, borrowing from exokernels, Plan 9, and Fuchsia. Its headline idea: a typesafe, capability-secured URI namespace that exposes local and remote resources without mounts, plus persistent MAC. Early-stage, x86_64/UEFI/ACPI focused. HN praises ambition and non-Linux experimentation, but questions monolithic trade-offs (driver recompiles), an in-kernel compositor’s security, and URI parsing cost in kernel; some note Linux could offer similar “auto-mount” semantics. License is GPLv3-or-later with a carve‑out for limited proprietary driver linking.

- Comment pulse
  - Network-transparent URI namespace → simpler mental model and remote access. — counterpoint: Kernel-level URI parsing adds complexity and latency; simpler low-level scheme may be better.
  - Pure monolithic design and in-kernel compositing → larger TCB, potential security risks; driver updates may require recompiles, hurting maintainability and adoption.
  - GPLv3-or-later with a proprietary-driver carve‑out → enables closed drivers for personal/internal/evaluation use, easing early hardware support without source disclosure.

- LLM perspective
  - View: URI-based, capability-secured namespace is the differentiator; keep it performant and outside kernel hot paths where possible.
  - Impact: If driver model and APIs stabilize, could attract hobby OS devs, OEMs evaluating hardware, and researchers exploring capability-based designs.
  - Watch next: Latency benchmarks for URI resolution, capability/MAC threat model docs, compositor architecture, and a plan to avoid driver recompiles.
