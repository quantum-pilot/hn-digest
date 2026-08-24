# KDE Plasma 6.8 Will Go Wayland-Exclusive in Dropping X11 Session Support

- Score: 112 | [HN](https://news.ycombinator.com/item?id=46058531) | Link: https://www.phoronix.com/news/KDE-Plasma-68-Wayland-Exclusive

### TL;DR

KDE plans to remove the standalone X11 desktop session in Plasma 6.8 and concentrate development on Wayland, while continuing to run X11 applications and games through XWayland. Developers say most users have already migrated and expect one session to improve feature work, optimization, and development speed. Plasma 6.7 will retain X11 support into early 2027, potentially with extra fixes. Commenters nevertheless identified unresolved accessibility interfaces, compositor crash behavior, FreeBSD stability, virtual keyboards, and remote access workflows as practical transition risks.

### Comment pulse

- Maintaining one session can accelerate desktop work → developers stop duplicating fixes across two display architectures.
- Holdouts cite concrete gaps → accessibility, compositor crashes, and remote access remain uneven — counterpoint: XWayland preserves legacy applications.
- Transition runway is substantial → version 6.7 keeps X11 session support into early 2027 and may receive extra fixes.

### LLM perspective

- View: Consolidation is defensible only if Wayland gaps become tracked release blockers rather than accepted edge cases.
- Impact: Most users gain focused development; specialized accessibility, remote administration, and non-Linux setups carry migration costs.
- Watch next: Accessibility protocols, compositor recovery, KRDP integration, FreeBSD regressions, and distribution support schedules.
