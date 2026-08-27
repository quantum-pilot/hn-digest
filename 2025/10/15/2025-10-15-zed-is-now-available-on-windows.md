# Zed is now available on Windows

- Score: 168 | [HN](https://news.ycombinator.com/item?id=45594920) | Link: https://zed.dev/blog/zed-for-windows-is-here

### TL;DR

Zed now treats Windows as a fully supported platform with weekly releases and a dedicated team. Its native build uses DirectX 11 and DirectWrite, supports WSL and SSH through a lightweight remote process, runs existing WebAssembly-based extensions without platform changes, and includes its agentic coding features. HN feedback focused on practical rough edges: blurry text on lower-density displays, GPU requirements, absent ARM64 support, and slow TypeScript navigation in one large codebase, despite praise for responsiveness and native performance.

### Comment pulse

- Rendering quality remains contentious → users reported blurry fonts on non-HiDPI displays despite recent Linux improvements.
- Native acceleration has costs → software-emulated GPUs trigger warnings, prompting questions about graceful fallback for a text editor.
- Responsiveness matters, but workloads differ → low input latency impressed some; others prioritized huge files, startup, LSP speed, and ARM64.

### LLM perspective

- View: Windows support completes Zed's platform story, while exposing hardware and typography assumptions inherited from its design.
- Impact: Windows developers gain native WSL workflows without Electron, but compatibility gaps may block broader adoption.
- Watch next: Track IME, multi-monitor, high-refresh, LoDPI, ARM64, emulated-GPU, and large-TypeScript-project fixes.
