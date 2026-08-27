# Libghostty is coming

- Score: 499 | [HN](https://news.ycombinator.com/item?id=45347117) | Link: https://mitchellh.com/writing/libghostty-is-coming

### TL;DR

Ghostty is extracting its terminal core into embeddable libraries, beginning with libghostty-vt: a zero-dependency parser and terminal-state engine that does not require libc. It inherits Ghostty’s SIMD parsing, Unicode support, fuzzing, memory work, and compatibility with protocols such as Kitty graphics and tmux control mode. A Zig module is available for alpha testing; the clean C API is still being designed, with macOS and Linux first and Windows, embedded, and WebAssembly targets planned. Commenters welcomed reusable, cross-platform terminal behavior.

### Comment pulse

- Terminal parsing is deceptively hard → shared, tested code could replace incomplete one-off implementations in editors, consoles, and multiplexers.
- Modularity broadens adoption → separate libraries can expose parsing, input, rendering, and native widgets without imposing every dependency.
- Ghostty itself still has gaps → users mentioned search, keyboard selection, shortcuts, and font rendering.

### LLM perspective

- View: A stable terminal core could matter more than another standalone terminal application.
- Impact: Application teams may gain consistent escape handling without becoming terminal-emulation specialists.
- Watch next: Evaluate C API stability, bindings, binary size, conformance tests, portability, and the first tagged release.
