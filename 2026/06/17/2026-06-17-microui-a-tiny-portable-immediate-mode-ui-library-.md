# MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C

- Score: 173 | [HN](https://news.ycombinator.com/item?id=48569205) | Link: https://github.com/rxi/microui

### TL;DR
MicroUI is a ~1.1k‑line ANSI C immediate‑mode UI library that runs in a fixed memory region and delegates all rendering to user code. It provides basic widgets (windows, panels, sliders, textboxes, etc.) and simple layout, making it easy to embed in games, tools, or experiments that already draw rectangles and text. HN commenters praise its tiny footprint (including small WASM binaries), find it ideal for toy projects and debug menus, but note a few unmaintained bugs and limited widgets.

---

### Comment pulse
- MicroUI shines for tiny binaries and minimal backends → WASM demos show it half Nuklear’s size, far below Dear ImGui—counterpoint: higher-level toolkits avoid low-level fiddling.  
- Great for toy projects and quick embedding → trivial to integrate anywhere with text and mouse; one misaligned-access bug exists and upstream feels unmaintained.  
- Alternatives clarify niches → libagar offers larger retained-mode C GUI; others pair MicroUI with Odin/Raylib or Cosmopolitan Libc for cross-platform tools.  

---

### LLM perspective
- Best suited to small, deterministic UIs → e.g., game debug panels, embedded tools, educational projects showing immediate-mode patterns.  
- C and Zig ecosystems benefit most → compile-anywhere codebases, tiny containers, or sandboxes where dynamic allocation is undesirable.  
- Track maintained forks or successors that fix alignment issues, add more widgets, and publish formal binary-size and performance benchmarks.
