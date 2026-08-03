# State of multi-player Wayland

- Score: 165 | [HN](https://news.ycombinator.com/item?id=49092112) | Link: https://blinry.org/multi-seat-wayland/

### TL;DR

Wayland’s core protocol already associates every pointer and keyboard event with a logical seat, enabling several people to share one desktop with independent cursors and focus. The ecosystem is uneven: sway, River, GTK, and wayvnc fare well; Weston lacks easy reconfiguration, niri lacks native support, SDL loses device identity in absolute mode, and most applications assume one seat. The author released configurators, patches, a collaborative text widget, a multi-cursor game, and a VNC setup. Commenters highlight touchscreen workflows, GUI focus assumptions, and remote-display latency and security tradeoffs.

### Comment pulse

- Compositor support has standalone value → separate touchscreen input can scroll documents without stealing keyboard focus from an editor.
- Application assumptions run deeper → active-window APIs, enter/leave events, selections, clipboards, and simultaneous focus require multi-seat semantics throughout GUI stacks.
- VNC remains disputed → GPU capture and dedicated clients reduce latency — counterpoint: legacy authentication, transport, and device-sharing limitations persist.

### LLM perspective

- View: Protocol readiness is insufficient when toolkits and applications encode singleton focus and input assumptions.
- Impact: Pair programmers, co-located collaborators, remote helpers, and touchscreen users gain parallel control without document synchronization.
- Watch next: Dynamic seat hotplug, absolute-pointer IDs, per-seat clipboards, browser support, and modern low-latency remote transport.
