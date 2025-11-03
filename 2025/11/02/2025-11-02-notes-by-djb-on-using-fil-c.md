# Notes by djb on using Fil-C

- Score: 286 | [HN](https://news.ycombinator.com/item?id=45788040) | Link: https://cr.yp.to/2025/fil-c.html

- TL;DR
    - djb reports Fil‑C, a memory‑safe C/C++ toolchain, runs many real‑world packages unmodified; his Debian 13 notes show end‑to‑end installs, multiarch “amd64fil0,” and scripts to rebuild system libs/apps. Crypto microbenchmarks show 1–4x cycle overhead; builds are resource‑hungry. He compiles 60/61 bundled targets and several extras (Boost, ncurses, tig), with small patches and symbol‑mangling handling. Musl lags; glibc works. HN discussion highlights heavy LLVM build RAM, Fil‑C’s GC and whole‑program model, and limited FFI/static‑link options versus Rust.

- Comment pulse
    - Community‑useful artifacts → installer/build scripts, Debian helper (fillet), gcshim; shows path to broad package rebuilds.
    - Memory spike originates in toolchain → LLVM/Clang build eats RAM; large‑core box compiles Fil‑C in minutes.
    - Suitability → GC, runtime checks, whole‑program model; FFI/static linking absent — counterpoint: good for hardening existing apps without rewriting to Rust.

- LLM perspective
    - View: Fil‑C can harden legacy C/C++ with acceptable 1–4x cost for many server workloads.
    - Impact: Ops teams can gradually replace binaries via Debian multiarch without source rewrites.
    - Watch next: Official Debian port, FFI story, static linking, musl support, non‑crypto benchmarks, crash‑report tooling.
