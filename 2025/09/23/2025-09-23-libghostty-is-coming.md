# Libghostty is coming

- Score: 499 | [HN](https://news.ycombinator.com/item?id=45347117) | Link: https://mitchellh.com/writing/libghostty-is-coming

- TL;DR
  - Mitchell Hashimoto announces libghostty, starting with libghostty‑vt: a zero‑dependency (no libc) library that parses terminal escape sequences and maintains terminal state, extracted from Ghostty’s optimized, fuzzed core. An alpha‑stage Zig API is available now; a clean C API is coming soon. Initial targets: macOS/Linux on x86_64 and aarch64, with plans for Windows, embedded, and WASM. Longer term, additional libs will cover input, GPU rendering, and UI widgets. HN reacts with enthusiasm, speed praise, Zig curiosity, and notes about Ghostty feature gaps and workarounds.

- Comment pulse
  - Admiration for Hashimoto’s hacker ethos and system design; Ghostty feels instant versus iTerm2, reflecting careful abstractions and performance attention.
  - Feature gaps keep some on WezTerm/Terminal: search, keyboard-only selection/copy, Cmd+. for Ctrl‑C, font rendering — counterpoint: keybind workaround exists; features scheduled soon.
  - Portability and Zig excite developers; hopes for mobile targets; several report switching daily, boosting confidence that Zig is production-ready.

- LLM perspective
  - View: A shared, correct VT parser could replace scattered implementations and standardize behavior across editors, multiplexers, and web consoles.
  - Impact: Teams ship faster by offloading VT quirks; fewer rendering bugs; easier portability to WASM, mobile, and embedded.
  - Watch next: Public C API release, stability signals; community bindings; benchmarks versus libvte/xterm.js; early adopters in VS Code, JetBrains, tmux, CI providers.
