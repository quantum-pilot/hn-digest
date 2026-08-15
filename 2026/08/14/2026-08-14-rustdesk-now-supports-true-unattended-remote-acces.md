# RustDesk now supports true unattended remote access on Wayland

- Score: 271 | [HN](https://news.ycombinator.com/item?id=49300759) | Link: https://rustdesk.com/blog/unattended-remote-access-wayland/

### TL;DR

RustDesk’s preview build enables Wayland hosts to accept remote sessions without local approval, including at the login screen after reboot and across multiple monitors. It currently targets x86_64 Debian- and Ubuntu-based systems; broader Fedora, Arch, and standard-release support waits on real-world stability testing. The release addresses a gap that AnyDesk still handles through Xorg and TeamViewer labels experimental. Commenters welcomed the timing but centered on encryption assumptions, trust, and RustDesk’s performance and network simplicity relative to VNC, Remmina, and Sunshine/Moonlight.

### Comment pulse

- Modern video codecs and temporal compression generally outperform VNC’s framebuffer updates, while multi-monitor support broadens practical administration.
- Encryption criticism applies to Direct IP on local networks, disabled by default; self-hosted relays encrypt, while mesh overlays can protect LAN access.
- Some prefer Remmina over SSH and Tailscale for trust; others found Sunshine/Moonlight difficult to operate beyond local networks.

### LLM perspective

- View: Surviving reboots makes Wayland support useful for actual unattended administration rather than occasional assisted sessions.
- Impact: Linux administrators can avoid Xorg, but preview scope and connection-mode security choices still limit production adoption.
- Watch next: Fedora and Arch previews, standard integration, multi-monitor reliability, login-screen behavior, and clearer security documentation.
