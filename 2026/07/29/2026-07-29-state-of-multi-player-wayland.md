# State of multi-player Wayland

- Score: 165 | [HN](https://news.ycombinator.com/item?id=49092112) | Link: https://blinry.org/multi-seat-wayland/

## TL;DR
The post surveys how well “multi-player” Wayland works: multiple people, each with their own mouse/keyboard, sharing one desktop with multiple cursors. Wayland’s core protocol has first‑class multi-seat support, and several compositors (Weston, sway, River) already enable per-seat focus and multiple pointers, though configuration is clunky and niri mostly lacks it. Toolkits like GTK and SDL expose seat info but most apps ignore it, so the author ships patches, demo games, and a multi-seat text widget, plus a wayvnc-based remote setup.

---

## Comment pulse
- VNC isn’t obviously obsolete → with dmabuf + H.264 (`--gpu`) and native clients, latency can rival newer systems — counterpoint: historic VNC security and efficiency issues remain.  
- Multi-seat unlocks new workflows → split keyboards, dedicated touchscreen seats, true parallel app interaction; compositor devs note significant complexity and toolkit assumptions about a single “active window.”  
- Input ergonomics matter too → calls for pointer inertia, controller-based workflows, and richer pointer behavior show UX expectations evolving alongside low-level seat plumbing.

---

## LLM perspective
- View: Multi-seat is mostly a coordination problem across compositor, toolkit, and apps; the protocol side is already good enough.  
- Impact: Niche today (pair programming, classrooms, remote support), but a strong fit for collaborative and educational Linux setups.  
- Watch next: native multi-seat features in major toolkits/browsers, compositor “seat managers,” and comparisons to modern game/streaming stacks beyond VNC.
