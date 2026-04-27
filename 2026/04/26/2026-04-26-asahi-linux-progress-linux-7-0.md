# Asahi Linux Progress Linux 7.0

- Score: 586 | [HN](https://news.ycombinator.com/item?id=47909226) | Link: https://asahilinux.org/2026/04/progress-report-7-0/

### TL;DR
Linux 7.0 coincides with a major Asahi Linux progress update: the installer is now fully automated and continuously built, fixes UEFI-only boot issues, and gains firmware‑update support. New drivers drastically cut idle power via Apple’s Power Management Processor, fix Broadcom Bluetooth/Wi‑Fi coexistence, and enable (hidden) VRR on external and ProMotion displays. Audio work goes upstream, including speaker‑safety plumbing, bus‑keeper APIs, and new hardware sample rates beyond what macOS uses. M3 support approaches “daily‑driver,” and Fedora Asahi Remix 44 aligns closely with upstream Fedora.

---

### Comment pulse
- Audio sleuthing enables 44.1–192 kHz on Apple’s CS42L84 → better, bit‑perfect playback and less CPU resampling—counterpoint: why doesn’t power‑obsessed Apple expose these rates?
- Project maturity debated → critics fear a permanent “80%” solution; supporters note heavy upstreaming, shrinking diff, and that many already daily‑drive Asahi despite quirks.
- Why Apple withholds docs → likely to avoid Linux support obligations for a tiny audience; framed as a right‑to‑repair issue over “owning” hardware vs bundled drivers.

---

### LLM perspective
- View: Asahi is methodically converting Apple Silicon from a closed appliance into a well‑supported Linux target, using upstream first and clever reverse‑engineering.
- Impact: Extends the usable life of ARM Macs, pressures audio/display subsystems upstream, and offers a credible macOS alternative for developers and researchers.
- Watch next: Upstream decisions on HDMI/VRR semantics, full PMP enablement and idle-power parity, and official installer support for all M3‑class machines.
