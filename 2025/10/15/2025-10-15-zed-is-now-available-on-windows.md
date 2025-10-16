# Zed is now available on Windows

- Score: 168 | [HN](https://news.ycombinator.com/item?id=45594920) | Link: https://zed.dev/blog/zed-for-windows-is-here

- TL;DR
  - Zed releases a native Windows build using DirectX 11/DirectWrite, with weekly updates, WSL/SSH remoting, WASM-based extensions, and full AI features (ACP/Claude or BYO keys). Remote editing runs a lightweight server for terminals, git, LSPs, and debuggers. HN welcomes it but debates rendering: blurry LoDPI/subpixel issues and a GPU requirement warning vs praise for low-latency, high-refresh responsiveness. Requests include startup/large-file benchmarks and Windows Arm64 support. Some report slow TypeScript navigation compared to VS Code/Cursor.

- Comment pulse
  - Rendering focus questioned → users want startup/large-file metrics; LoDPI/1440p fonts look blurry; subpixel still missing — counterpoint: low input latency and 120–144 Hz improve feel.
  - GPU requirement criticized → DirectX 11 reliance flags Microsoft Basic Render Driver; software rendering triggers severe performance warning.
  - TypeScript LSP slower than VS Code → go-to-definition lags on large repos despite both using tsserver.

- LLM perspective
  - View: Native Windows plus WSL/SSH and WASM extensions differentiates Zed from Electron editors; latency-first positioning may resonate.
  - Impact: Windows developers with remote workflows; teams exploring ACP-based AI agents; VS Code faces pressure on input latency benchmarks.
  - Watch next: Arm64 Windows support, LoDPI/subpixel rendering roadmap, startup and large-file benchmarks, and tsserver latency profiling across big projects.
