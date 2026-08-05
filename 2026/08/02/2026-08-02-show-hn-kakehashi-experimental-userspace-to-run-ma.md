# Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM

- Score: 159 | [HN](https://news.ycombinator.com/item?id=49145937) | Link: https://github.com/wie-project/kakehashi

### TL;DR

Kakehashi is a Rust, CLI-first userspace layer that loads macOS ARM64 Mach-O binaries on Linux aarch64, supplies a freestanding libSystem, and translates BSD syscalls without JIT instruction emulation. Current demonstrations run multithreaded Darwin 7-Zip and curl, including HTTPS, with host filesystem bridging and 4 KiB or 16 KiB pages. A 309 MiB archive took 54.8 seconds versus Linux-native 44.1 seconds, about 1.24× slower. GUI, codesigning, Apple frameworks, complete curl, and stable Xcode tools remain unsupported. HN welcomed the direction but stressed its early scope and overlap with Darling.

### Comment pulse

- Native ARM execution leaves syscall crossings as the main tax; replacing an O(n²) allocator reduced an earlier roughly 5.2× slowdown substantially.
- Cheap Linux ARM CI could beat hosted macOS pricing for Darwin CLI tests — counterpoint: GUI, notarization, and Xcode UI workloads still require macOS.
- Commenters asked about target-version behavior, shell environment fidelity, proprietary-rootfs approaches, Audio Units, and cooperation with Darling’s ARM64 work.

### LLM perspective

- View: The narrow compatibility slice is strategically sound: prove useful CLI binaries before attempting the API surface of desktop macOS.
- Impact: Cross-platform projects could test Darwin command-line artifacts on cheaper Linux ARM capacity while retaining macOS runners for platform-bound stages.
- Watch next: Add Git stability, versioned Darwin semantics, broader syscalls, correctness suites, reproducible performance, licensing boundaries, and comparisons with Darling.
