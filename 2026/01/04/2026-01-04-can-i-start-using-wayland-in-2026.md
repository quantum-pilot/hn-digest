# Can I start using Wayland in 2026?

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46485989) | Link: https://michael.stapelberg.ch/posts/2026-01-04-wayland-sway-in-2026/

### TL;DR

The i3 creator’s annual Wayland trial finally ran Sway on an NVIDIA-driven 8K tiled display, but only after explicit-sync updates, an unmerged TILE patch, and a custom workaround for an NVIDIA source-coordinate bug. A workday exposed cursor lag, duplicate shortcuts, scaling glitches, blurry Xwayland apps, Emacs latency, Chrome GPU crashes, lost workspace restoration, and awkward low-resolution window sharing. He returned to X11/i3, judging parity closer but still months away for his setup. Commenters contrasted this edge case with smooth AMD/Intel GNOME or KDE deployments.

### Comment pulse

- Critics blamed fragmented compositor and portal implementations for duplicated quirks, while defenders said missing companion protocols—not Wayland’s narrow display protocol—are the issue.
- Satisfied users cited mixed-DPI and fractional scaling on GNOME or KDE—counterpoint: automation, NVIDIA, wlroots, and specialized displays remain uneven.
- Migration pressure comes from distributions dropping X11 maintenance, even when existing users see few benefits beyond avoiding a deprecated stack.

### LLM perspective

- View: Wayland readiness is workload-specific; mainstream laptops and this 8K Sway workstation represent materially different compatibility tests.
- Impact: Advanced users bear integration costs spread across drivers, compositors, portals, toolkits, applications, and replacement utilities.
- Watch next: NVIDIA TILE output, Sway scaling, Chrome acceleration, Emacs latency, session restoration, and sharing fixes decide this migration.
