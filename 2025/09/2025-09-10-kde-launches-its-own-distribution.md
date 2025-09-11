# KDE launches its own distribution

- Score: 119 | [HN](https://news.ycombinator.com/item?id=45204393) | Link: https://lwn.net/SubscriberLink/1037166/caa6979c16a99c9e/

TL;DR
KDE launched an alpha of KDE Linux: an immutable, Wayland‑only desktop using Arch for the base, EROFS image updates (no pacman), and apps via Flatpak; Snap via CLI, plus Distrobox for extras. System images (~4.8GB) update atomically; expect big disk use, no Secure Boot, occasional rough edges (Podman uid/gid, NVIDIA setup), and slower security turnarounds than Arch. Three editions are planned; neon’s future is undecided. HN debates resource split and Flatpak reliability, with comparisons to SteamOS; defenders note it’s alpha and KDE actively improves Flatpak.

Comment pulse
- Another distro splits focus → Neon/elementary drained resources; GNOME thrives without distro — counterpoint: KDE wants control like GNOME OS; shipping directly improves integration.
- Flatpak/immutable objections → bugs, disk bloat, weak maintenance; Arch base seen unstable — counterpoint: alpha status; KDE contributes to Flatpak and experiments to package Plasma.
- SteamOS sibling? → Similar immutable Arch-style base, Wayland-only; KDE adds Discover, Distrobox, no pacman, KDE-first defaults.

LLM perspective
- View: KDE Linux tests an opinionated, image-based desktop stack; trade-offs: simpler updates and control versus flexibility, security lag, larger footprints.
- Impact: Could reduce distro variance for KDE apps, easing QA and support; OEM-target ambitions hinge on Flatpak maturity and security processes.
- Watch next: Delta updates in systemd-sysupdate, AUR removal, move to KDE infra, security advisories; telemetry on cache size, rollback rates, container UX.
