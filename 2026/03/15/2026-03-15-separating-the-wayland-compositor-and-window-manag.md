# Separating the Wayland compositor and window manager

- Score: 197 | [HN](https://news.ycombinator.com/item?id=47388137) | Link: https://isaacfreund.com/blog/river-window-management/

### TL;DR

River 0.4.0 separates its Wayland compositor/display server from window-management policy through the stable `river-window-management-v1` protocol. Unlike X11, composition remains beside input and scene handling, avoiding per-frame or per-input round trips; the external manager exchanges atomic management and render state instead. This lets users crash, restart, or swap window managers without ending applications, write managers in higher-level languages, and batch frame-perfect layouts. HN welcomed restored modularity, while probing whether synchronization artifacts or remote-desktop gaps remain; 15 managers already exist.

### Comment pulse

- X11-style pluggability returns without splitting rendering → enthusiasts can build personal managers while retaining Wayland’s coherent input-to-frame pipeline.
- Atomic state exchange addresses asynchronous layout concerns → compositor deadlines prevent slow clients from blocking frames indefinitely.
- Remote access remains the sore spot → commenters still find Wayland less dependable than mature X11 workflows.

### LLM perspective

- **View:** A stable policy protocol could make Wayland experimentation practical without resurrecting X11’s compositor-manager coupling.
- **Impact:** Desktop tinkerers and language communities gain freedom; compositor maintainers inherit a clearer interoperability boundary.
- **Watch next:** River 1.0, cross-compositor protocol adoption, animation support, crash recovery, and remote-desktop behavior.
