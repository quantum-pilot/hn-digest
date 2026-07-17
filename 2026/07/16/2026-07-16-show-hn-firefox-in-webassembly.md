# Show HN: Firefox in WebAssembly

- Score: 241 | [HN](https://news.ycombinator.com/item?id=48926939) | Link: https://developer.puter.com/labs/firefox-wasm/

### TL;DR
Puter Labs compiles Mozilla’s Gecko engine (Firefox) to WebAssembly, letting a full Firefox instance run inside another browser tab. Rendering is done via WebGL, with optional GPU acceleration for web content and an experimental JS-to-WASM JIT for JavaScript execution. All network traffic is tunneled through a Puter-hosted Wisp WebSocket proxy, powered by Puter.js, so the embedded Firefox talks to the internet through a controlled backend. It’s a self-contained, remotely-networked browser running entirely as WASM.

---

### LLM perspective
- View: Demonstrates that a full browser engine fits in WASM, but real-world usability depends on startup time and responsiveness.  
- Impact: Useful as an ultra-portable, strongly sandboxed test browser for developers, QA, education, and potentially high-security or kiosk environments.  
- Watch next: Measure Wisp latency/CPU, clarify how profiles persist, and compare against native Firefox and simple remote-desktop streaming.
