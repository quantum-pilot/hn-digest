# Phoenix: A modern X server written from scratch in Zig

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46380075) | Link: https://git.dec05eba.com/phoenix/about/

### TL;DR
Phoenix is a new X server written from scratch in Zig, aiming to be a modern, security-hardened alternative to Xorg while intentionally dropping much legacy. It targets only relatively recent hardware, limits X11 features to what modern applications actually use, integrates a built-in compositor for no-tearing, and focuses on isolation-by-default with permission-gated global operations. Currently it only runs nested on an existing X server, but HN readers see it as a pragmatic “Wayland-like X” for those who still need X11.

---

### Comment pulse
- Modernized X for holdouts → People who still need X11 but dislike Xorg’s complexity/bitrot welcome a fresh implementation—counterpoint: unclear long-term niche beside Wayland.
- “Wayland-ish X” appeals → Built-in compositor, isolation, dropped legacy, no remote GLX feel sensible; seen as more realistic than grand “fix all of X” projects.
- Compositor disabling with no-vsync fullscreen → Avoids extra latency and buffering for games needing minimal input lag.

---

### LLM perspective
- View: This is effectively an X-speaking Wayland-style compositor: smaller surface, security defaults, modern GPU path.
- Impact: Niche but valuable for X-only apps, WM/compositor developers, and distros needing hardened X without full Xorg baggage.
- Watch next: Real-world app compatibility, HDR/multi-monitor behavior, and whether it can viably replace Xwayland in some stacks.
