# Show HN: Vibe Coding a static site on a $25 Walmart Phone

- Score: 60 | [HN](https://news.ycombinator.com/item?id=46480677) | Link: https://stetsonblake.com/%2425+Walmart+Phone+for+Hackers

### TL;DR

A $25 Moto G 2025 becomes a pocket Linux server through F-Droid Termux, optional Andronix or proot, SSH, nginx, and Cloudflare Tunnel. The guide covers boot scripts, wake locks, Android process restrictions, service supervision, and Tailscale access, with Claude Code helping configure and document the system. HN questioned whether “vibe coding” described the project accurately, whether AI-authored guidance reflected the actual build, and whether a static site justified the extra Linux layer beyond Termux or a simple server app.

### Comment pulse

- The guide reflects a real build → the author recorded manual and Claude-assisted steps, then used Claude to organize them.
- The stack may exceed the task → Termux or a static-server app suffices, while proot enables broader Linux experimentation.
- Cheap hardware invites playful learning → commenters valued hands-on systems practice even when simpler deployment options existed.

### LLM perspective

- View: The phone matters less as hosting infrastructure than as an inexpensive laboratory for Linux constraints.
- Impact: Beginners can practice SSH, process supervision, and tunneling without renting hardware.
- Watch next: Measure uptime, battery drain, thermal throttling, and recovery after Android kills background processes.
