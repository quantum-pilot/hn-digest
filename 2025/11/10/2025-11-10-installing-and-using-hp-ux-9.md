# Installing and using HP-UX 9

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45873904) | Link: https://thejpster.org.uk/blog/blog-2025-11-08/

TL;DR
- An enthusiast revives an HP 9000/340 (68k) by installing HP‑UX 9.07 on a 9000/705 (PA‑RISC), fixing network quirks and disktab‑limited disk formatting via BlueSCSI. Using SAM, he converts the 705 to a cluster server, then layers the Series 300 Core OS (9.10) to enable a mixed‑architecture, diskless boot. The reveal: HP‑UX’s Context Dependent Filesystems let both machines share one root while transparently serving arch‑specific binaries; a missing X11R5 library is repaired by creating the right CDF and rerunning customize. HN recalls AFS‑style tricks, HP‑UX tooling, and dwindling HP‑UX mindshare.

Comment pulse
- AFS solved cross-architecture binaries → @sys symlinks resolved to per-OS/CPU directories; simple env-based PATH switching can approximate it — counterpoint: AFS centralization scales better.
- HP‑UX excelled at admin UX → manpages, Ignite‑UX imaging, and advanced LVM eased cloning and recovery; many still installed GNU tools and GCC for work.
- HP‑UX pioneered FSS, ServiceGuard, PRM → strong multi‑workload Unix, but Sun’s campus dominance limited visibility; 11.31 support ends 2025‑12‑31.

LLM perspective
- View: CDFs prefigure per-context views; today you’d use arch‑suffixed paths, symlinks, containers, or overlay/bind mounts instead.
- Impact: Shows practical recipe for mixed‑arch netbooting and recovery on vintage HP‑UX; useful for museums, labs, and emulation projects.
- Watch next: Publish disk images and scripts; capture SAM steps; benchmark CDF overhead vs NFS/AFS; mirror HP‑UX docs before 11.31 retirement.
