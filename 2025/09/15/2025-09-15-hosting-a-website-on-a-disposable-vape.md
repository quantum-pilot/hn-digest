# Hosting a website on a disposable vape

- Score: 975 | [HN](https://news.ycombinator.com/item?id=45252817) | Link: https://bogdanthegeek.github.io/blog/projects/vapeserver/

TL;DR
- An inventive hack serves a website from a disposable vape’s PUYA Cortex‑M0+ (24MHz, 24KB flash, 3KB RAM) by tunneling SLIP over ARM semihosting via pyOCD/socat/slattach. The author ports uIP, fixes 16‑bit alignment issues, and adds ring buffers/batched writes, cutting pings from ~1.5s/50% loss to ~20ms and page loads to ~160ms, using ~5KB flash and ~1.4KB RAM. HN admires the constraints, debates e‑waste and regulation, and suggests $5 LTE sticks with Linux as more practical hack platforms.

Comment pulse
- $5 MSM8916 LTE dongles run Linux with 512MB RAM and 4GB eMMC; great homelab value — counterpoint: fast‑moving parts and limited time/skills stall projects.
- Disposable vapes are e‑waste: reusable LiPos, MCUs, and USB‑C get trashed; standardize for reuse or donate to schools.
- Perspective check: 3KB RAM and 24MHz MCU vs 1980s machines; impressive for a “disposable,” yet dwarfed by classic ARM desktops.

LLM perspective
- View: Hijacking debugger semihosting for IP networking avoids radios, drivers, and RTOS; a reusable pattern for constrained boards.
- Impact: Could seed classroom labs on protocols and embedded systems; adds pressure for modular, documented, refillable consumer devices.
- Watch next: Benchmark semihosting vs USB CDC/PPP; try lwIP; package scripts and images; stress‑test under load; power it from recovered vape batteries.
