# Can I start using Wayland in 2026?

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46485989) | Link: https://michael.stapelberg.ch/posts/2026-01-04-wayland-sway-in-2026/

### TL;DR

Michael Stapelberg (creator of i3) spends a full workday trying to live on Wayland+sway in 2026 on NixOS with Nvidia and an 8K tiled monitor. Thanks to explicit sync, wlroots TILE support, and a Claude‑assisted workaround for an Nvidia DRM bug, he finally gets sway running correctly on 8K. But he hits many regressions vs. X11/i3: pointer lag, no proper Xwayland scaling, Emacs pgtk latency/rendering differences, Chrome GPU crashes, awkward screen‑sharing, scaling glitches, and sway/IPC incompatibilities. His conclusion: still worse than his flawless X11 setup; not ready as his daily driver yet.

---

### Comment pulse

- Architecture concern → Wayland is “just a protocol”; multiple compositors re‑implement low‑level pieces instead of sharing a standard library like wlroots—counterpoint: in theory the layered design is sound.  
- Adoption calculus → End users see little benefit over Xorg unless they need fractional scaling or multi‑DPI docking; real push comes from GNOME/KDE dropping X11 support.  
- Hardware and Nvidia → AMD+Wayland often reported flawless; Nvidia is polarizing, with conflicting anecdotes and debate over whether GBM vs. EGLStreams blame lies more with Mesa/freedesktop or Nvidia.

---

### LLM perspective

- View: Core Wayland tech is “good enough”; the pain is ecosystem gaps: Nvidia, portals, compositor quirks, and legacy app behaviors.  
- Impact: Power users with exotic displays or deep tooling are last to migrate; mainstream GNOME/KDE users will be nudged by defaults.  
- Watch next: wlroots and sway scaling/TILE fixes, xdg‑session‑management, Emacs pgtk performance work, Chrome/Nvidia GBM stability, and any emerging shared compositor libraries.
