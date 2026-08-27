# Phoenix: A modern X server written from scratch in Zig

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46380075) | Link: https://git.dec05eba.com/phoenix/about/

### TL;DR

Phoenix is an early Zig X server built from scratch as a simpler, safer modern alternative to Xorg, though it currently only renders basic accelerated applications while nested inside X. It deliberately supports a reduced X11 subset and recent Linux graphics hardware, adds per-application isolation, automatic protocol parsing, a built-in compositor, mixed-refresh displays, VRR, HDR ambitions, and possible Wayland bridging. HN characterized it as a Wayland-like reinterpretation of X: promising for users needing X11, but with an uncertain audience and intentional compatibility breaks.

### Comment pulse

- Preservation strategy → a new maintainable implementation may serve remaining X users better than extending aging Xorg internals.
- Design convergence → isolation, integrated composition, dropped legacy features, and no remote GLX make Phoenix resemble a Wayland compositor.
- Practical niche → supporters want secure modern X11; others question who accepts incomplete core-protocol compatibility rather than adopting Wayland.

### LLM perspective

- View: Phoenix tests whether X semantics can survive by shedding historical guarantees instead of preserving complete compatibility.
- Impact: Window-manager developers gain a potential nested testbed before desktop users gain a standalone replacement.
- Watch next: Track real-world client coverage, standalone DRM support, Wayland nesting, permissions UX, latency, HDR, and multi-monitor behavior.
