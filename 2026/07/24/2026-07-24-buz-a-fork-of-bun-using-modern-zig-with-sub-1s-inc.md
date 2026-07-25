# Buz – A fork of Bun using modern Zig, with sub-1s incremental builds

- Score: 219 | [HN](https://news.ycombinator.com/item?id=49033099) | Link: https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891

### TL;DR
Buz is a work‑in‑progress fork of Bun taken from the last pre‑Rust commit, updated to current Zig and restructured for very fast incremental builds (sub‑1s, aiming for <300 ms once Zig’s linker is ready). The maintainer is aggressively deleting dead code (11k+ lines), modernizing to Zig’s stdlib, and importing Rust Bun’s newer tests to become a drop‑in replacement around 1.4.0. Controversially, they plan to use LLMs heavily to untangle what they call an “AI slop” 600k‑LOC codebase.

---

### Comment pulse
- Bun is more than “glue” → large Zig subsystems (package manager, Node/Web APIs) mean a fork can improve real functionality, not just bindings—counterpoint: core perf still driven by C/C++ deps.  
- Incremental builds excite Zig community → Buz showcases Zig’s build system; people suggest blog posts and videos as incremental linking matures and replaces mold.  
- LLM-heavy refactor worries some → fear of repeating “slop” and abandoned forks; maintainer argues manual cleanup is infeasible without AI assistance.

---

### LLM perspective
- View: Using LLMs as power tools for dead‑code removal and refactoring is pragmatic on a huge, messy legacy codebase.  
- Impact: If successful, Buz becomes a real‑world case study for AI‑assisted “codebase refurbishment” and fast‑iteration tooling in systems languages.  
- Watch next: Concrete benchmarks vs Bun/Deno/Node, stability reports under real workloads, and governance/maintainer plans once the “AI rehab” phase ends.
