# Buz – A fork of Bun using modern Zig, with sub-1s incremental builds

- Score: 219 | [HN](https://news.ycombinator.com/item?id=49033099) | Link: https://ziggit.dev/t/buz-a-drop-in-replacement-for-bun-using-modern-zig-with-sub-1s-incremental-builds/16891

### TL;DR

Buz is an experimental fork of the last pre-Rust Bun codebase, updated for current Zig with the complete build graph—including JavaScriptCore—in `build.zig`. Patched incremental compilation produces sub-second rebuilds, potentially below 300 ms once Zig’s linker fills remaining gaps. The solo maintainer has removed over 11,000 trivially dead lines and imported newer Bun tests, many still failing, toward eventual drop-in compatibility. The project is explicitly non-production and will use LLMs extensively while refusing human-written contributions initially. HN debated whether this proves Bun’s slow builds were organizational debt or platform-limited.

### Comment pulse

- Fast builds look partly attainable today → one developer reached one second — counterpoint: incremental support still lacks AArch64 and cross-platform binary patching.
- AI cleanup is deliberately paradoxical → supporters trust stronger human steering, while skeptics fear another unmaintainable fork without a committed maintainer community.
- Eleven thousand dead lines need context → at 1.8% of 600,000 lines, the figure is notable but not extraordinary for large evolving systems.

### LLM perspective

- **View:** The valuable experiment is software refurbishment: modernizing build mechanics and deleting complexity before attempting feature parity.
- **Impact:** Zig contributors gain a demanding incremental-compilation showcase; Bun users gain nothing until compatibility, stability, and sustained maintenance are demonstrated.
- **Watch next:** Track test pass rates, supported architectures, clean and incremental benchmarks, upstream feature drift, bug regressions, and maintainer growth.
