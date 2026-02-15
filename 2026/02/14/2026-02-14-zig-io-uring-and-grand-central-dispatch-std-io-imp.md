# Zig – io_uring and Grand Central Dispatch std.Io implementations landed

- Score: 342 | [HN](https://news.ycombinator.com/item?id=47012717) | Link: https://ziglang.org/devlog/2026/#2026-02-13

## TL;DR
Zig’s standard library now has experimental `std.Io.Evented` backends for Linux `io_uring` and macOS Grand Central Dispatch, both built on userspace stack-switching (fibers/green threads). You can swap between traditional threaded I/O and evented I/O by changing only how `std.Io` is constructed; the application code stays identical. The Zig compiler itself can already run on these backends, though there’s an unresolved performance regression and missing features. HN debates Zig’s instability, language tribalism, practical business value, and comparisons to Rust’s slower io_uring adoption.

---

## Comment pulse
- New stack → long-term maintenance cost. Distros must support Zig for years; language still unstable and niche. — counterpoint: users can just pick tools that fit their needs.  
- Zig is already productive → simpler than Rust for low-level, data-oriented work; good performance, especially for hot paths and cloud cost savings.  
- Pre-1.0 instability worries some → others prefer a “living” language; say most breakage is in stdlib and manageable for many projects.

---

## LLM perspective
- View: A unified `std.Io` abstraction with swappable backends makes serious evented I/O practical without framework lock-in.  
- Impact: Systems developers gain more ergonomic, high-performance async I/O on Linux/macOS; could attract projects needing tight control without Rust’s complexity.  
- Watch next: performance fixes, stronger testing, networking for GCD backend, and stack-size introspection will determine whether this becomes production-ready or stays a demo.
