# Fil's Unbelievable Garbage Collector

- Score: 598 | [HN](https://news.ycombinator.com/item?id=45133938) | Link: https://fil-c.org/fugc

- TL;DR
    - Fil‑C’s FUGC is a parallel, concurrent, on‑the‑fly, precise, non‑moving GC using a simple Dijkstra store barrier and grey‑stack rescans to avoid load barriers. Safepoints use compiler pollchecks and soft handshakes; new allocations are pre‑marked; sweeping uses SIMD bitvectors. It traps use‑after‑free, supports finalizers and weak refs/maps, and aims for low pauses on multicore. HN debates feasibility for legacy C, performance (author cites 4× worst‑case; typical OK), MMU/32‑bit constraints, and alternatives like lock‑and‑key; funding appears linked to Epic Games.

- Comment pulse
    - Promise for legacy C with safety upgrades → runs major C software; typical slowdown acceptable; author says 4× is worst‑case, measured conservatively.
    - MMU/portability limits → current design leans on OS/MMU; author says a no‑MMU variant is feasible; 32‑bit targets unsupported today.
    - Design: GC over lock‑and‑key → capability model is thread‑safe with atomics; requests for benchmarks and branchless pollchecks — counterpoint: stacking GCs on CPython/Perl could hurt.

- LLM perspective
    - View: Advancing wavefront plus grey‑stack avoids load barriers; simple store barrier and safepoints make concurrent, thread‑friendly GC practical for C.
    - Impact: Legacy C maintainers get UAF traps and fewer pauses without rewrites; portability limits (MMU, 64‑bit) gate embedded adoption.
    - Watch next: Publish end‑to‑end throughput/latency/footprint on CPython, SQLite, OpenSSH; prototype no‑MMU build; add implicit suspend checks and memory‑footprint accounting.
