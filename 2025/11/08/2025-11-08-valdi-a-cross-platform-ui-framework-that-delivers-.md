# Valdi – A cross-platform UI framework that delivers native performance

- Score: 468 | [HN](https://news.ycombinator.com/item?id=45852854) | Link: https://github.com/Snapchat/Valdi

### TL;DR

Snap open-sourced Valdi, a beta cross-platform UI framework used internally for eight years. Developers write declarative TSX that compiles to native iOS, Android, and macOS views without webviews or JavaScript bridges. The project advertises view recycling, incremental rendering, a C++ layout engine, viewport-aware inflation, hot reload, VS Code debugging, generated native bindings, worker threads, and gradual embedding in existing apps. Discussion compared it with React Native and Lynx, while questioning Swift integration, ecosystem maturity, Discord-based support, and whether web-first delivery is simpler.

### Comment pulse

- Supporters welcomed competition and Snap’s production history; performance claims still lack independent comparison in the supplied material.
- WebView advocates favored one web UI, while native proponents cited platform gestures, new APIs, signing, and store rules.

### LLM perspective

- View: Valdi competes on native compilation and incremental adoption, not merely shared TypeScript syntax.
- Impact: Its value depends on whether smaller teams can operate the toolchain without Snap’s internal infrastructure.
- Watch next: Benchmark startup, scrolling, memory, build times, native interoperability, and upgrade stability against React Native.
