# Ghostel.el: Terminal emulator powered by libghostty

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48879504) | Link: https://dakra.github.io/ghostel/

### TL;DR

Ghostel embeds a modern terminal in Emacs by pairing Elisp integration with a Zig native module built on Ghostty’s VT engine. It auto-downloads binaries for major desktop platforms, uses a background PTY reader for high-throughput local sessions, supports TRAMP remotes, and exposes five input modes balancing terminal keystrokes with Emacs navigation and editing. Its differentiators include Kitty keyboard and graphics, rich terminal protocols, shell integration, searchable buffer-native scrollback, and roughly 75 MB/s benchmarked ASCII throughput. Early adopters report major gains over vterm and eat, alongside freezes and rendering artifacts.

### Comment pulse

- Embedded-terminal value resonated → searchable, selectable scrollback and Emacs extension points let users replace external terminals for many daily workflows.
- Maturity remains disputed → users praised speed and input handling — counterpoint: some still encountered freezes, stale screen content, and Emacs-wide blocking.
- Mode complexity needs teaching → five modes address distinct keyboard-ownership tasks, but newcomers want practical examples for choosing them efficiently.

### LLM perspective

- **View:** Ghostel’s appeal is not emulation alone, but making terminal state ordinary, extensible Emacs buffer content.
- **Impact:** Native parsing and asynchronous PTY I/O narrow the performance gap without abandoning familiar editor workflows.
- **Watch next:** Renderer correctness, freeze reports, process isolation, Eshell parity, and clearer mode guidance will determine daily-driver maturity.
