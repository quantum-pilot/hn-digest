# Moonshine: Lets you stream games from your PC to any device running Moonlight

- Score: 327 | [HN](https://news.ycombinator.com/item?id=48972970) | Link: https://github.com/hgaiser/moonshine

### TL;DR

Moonshine is a Rust-based Linux streaming host for Moonlight clients. Unlike Sunshine, it creates a separate Wayland compositor for each session, so games can run headlessly at arbitrary resolutions and refresh rates while the physical desktop remains usable. It supports Vulkan GPU encoding for H.264, H.265, experimental AV1, 10-bit HDR, surround audio, and full controller input, but requires systemd, recent GPUs, and Moonlight 6+. Hacker News praised the virtual-display model; the creator still recommends mature Sunshine for newcomers and positions Moonshine as lean, focused software for tinkerers.

### Comment pulse

- Independent compositors solve Sunshine’s central Linux limitation → streaming no longer occupies the host display, requires a monitor, or blocks simultaneous desktop use.
- Narrow scope keeps implementation lean → one Vulkan encoder, Linux only, no GUI, and modern clients reduce compatibility burden — counterpoint: hardware requirements rise.
- A shared gaming server remains constrained → per-session software isolation is promising, but consumer GPU sharing across multiple virtualized hosts is still difficult.

### LLM perspective

- **View:** Owning the compositor turns display state from a physical-machine constraint into per-session configuration.
- **Impact:** Households can stream games without monopolizing the gaming PC’s monitor or interrupting its local user.
- **Watch next:** Test concurrent sessions, encoder contention, HDR correctness, AV1 driver fixes, non-Arch packaging, application compatibility, and VPN-only remote use.
