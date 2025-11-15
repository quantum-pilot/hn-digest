# A brief look at FreeBSD

- Score: 106 | [HN](https://news.ycombinator.com/item?id=45899189) | Link: https://yorickpeterse.com/articles/a-brief-look-at-freebsd/

TL;DR
- Author experiments with FreeBSD in a VM before trying it on a Framework laptop, attracted by a cohesive base system, package breadth, and stability. Early impressions: DHCP management surprises, local_unbound DNSSEC gotcha, sensible hardening via sysctls, pkgbase still rough, pkg downloads are sequential, and GNU vs BSD CLI differences grate. ZFS/jails/profiling and laptop hardware (especially Wi‑Fi) still untested; community tone feels unwelcoming. HN responses split between tinkerers’ enthusiasm and concerns about hardware/Wi‑Fi; some note ZFS on Ubuntu is straightforward.

Comment pulse
- Power-user appeal → PF clarity, jails, native ZFS, Linuxulator; desktop viable but Wi‑Fi lags — counterpoint: others report stable multi-display setups.
- Hardware support remains thin → few corporate sponsors; commenters cite Wi‑Fi generations incomplete; historic vendor hostility blamed.
- Why choose it → less churn and durable knowledge; docs likened to Arch/void; official Swift support noted.

LLM perspective
- View: FreeBSD’s cohesive base is attractive, but pkgbase polish, tooling, and desktop ergonomics still trail mainstream Linux.
- Impact: Best fit for developers/admins prioritizing ZFS, jails, and predictable interfaces over latest hardware support.
- Watch next: FreeBSD 15: pkgbase GA, laptop/Wi‑Fi drivers, KDE installer; pkg concurrent downloads and profiling UX progress.
