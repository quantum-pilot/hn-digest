# Xfwl4 – The Roadmap for a Xfce Wayland Compositor

- Score: 247 | [HN](https://news.ycombinator.com/item?id=46779645) | Link: https://alexxcons.github.io/blogpost_15.html

- TL;DR  
Xfce is funding core dev Brian Tarricone to build xfwl4, a new Rust-based Wayland compositor using smithay, targeting xfwm4-level behavior and config compatibility. Instead of retrofitting xfwm4, they want clean Wayland-first architecture, safety and flexibility, plus XWayland and session-management support, with a first dev release hoped around mid‑2026. HN discussion focuses on Wayland’s mandatory compositing and latency—especially on low-end machines—Rust and “traditional” users, and whether Wayland’s fragmented ecosystem is progress or needless churn.

- Comment pulse  
  - Wayland performance/latency: mandatory compositing adds delay versus uncomposited X; overlays, higher refresh and unredirected planes reduce but don’t eliminate it—counterpoint: modern GPUs make overhead negligible.  
  - Xfce audience: some fear Wayland+Rust will bloat a traditionally lightweight, stable desktop; others argue users only care that things work and don’t crash.  
  - Wayland ecosystem: libraries like smithay, wlroots enable small teams and experimentation, but duplicate compositors risk missing features, burnout, and inconsistent desktop APIs.

- LLM perspective  
  - View: Rewriting as a Rust Wayland compositor isolates risk, aligns with future drivers, and keeps Xfce’s UX intentionally conservative.  
  - Impact: If xfwl4 stays resource-light, it becomes the go‑to desktop for modest hardware once Xorg support fades.  
  - Watch next: latency benchmarks, XWayland app behavior, and how session startup and crash recovery work under the new stack.
