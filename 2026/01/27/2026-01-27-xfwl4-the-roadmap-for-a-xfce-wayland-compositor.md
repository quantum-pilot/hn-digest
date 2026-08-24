# Xfwl4 – The Roadmap for a Xfce Wayland Compositor

- Score: 247 | [HN](https://news.ycombinator.com/item?id=46779645) | Link: https://alexxcons.github.io/blogpost_15.html

### TL;DR

Xfce will spend a significant share of community donations funding longtime contributor Brian Tarricone to build xfwl4, a Wayland compositor intended to preserve xfwm4 behavior and reuse its settings and configuration dialogs. Rather than retrofit the X11-oriented C code, he is writing a separate Rust implementation atop Smithay, isolating legacy stability while enabling deeper graphics and input customization. Scope includes session-startup changes, xdg-session-management, XWayland, and Rust-capable CI. A first development release is targeted around midyear, with performance and exact feature parity still open.

### Comment pulse

- Supporters welcomed memory safety and Wayland momentum — counterpoint: skeptics fear mandatory compositing will erode Xfce’s low-end responsiveness and latency.
- Smithay’s breadth and customization appealed, though a Rust island may add build friction and narrow the contributor pool.
- Commenters split over compositor diversity: competition can improve libraries, but duplicated implementations may omit features and exhaust maintainers.

### LLM perspective

- View: A clean parallel implementation lowers risk to existing X11 users while making behavioral compatibility an explicit requirement.
- Impact: Success gives lightweight-desktop users a migration path without forcing Xfce to inherit another compositor’s interface.
- Watch next: Midyear build, input-to-pixel latency, DRM-plane use, XWayland compatibility, session recovery, and xfwm4-settings reuse.
