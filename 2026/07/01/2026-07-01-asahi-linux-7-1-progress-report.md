# Asahi Linux 7.1 Progress Report

- Score: 525 | [HN](https://news.ycombinator.com/item?id=48744518) | Link: https://asahilinux.org/2026/06/progress-report-7-1/

### TL;DR

Asahi’s Linux 7.1 report fixes two macOS 27 beta incompatibilities: a newly enforced APFS bootable flag hid intact Linux installs, while an SMC battery-ABI change could trigger emergency shutdowns. M3 support now includes audio, frequency scaling, big.LITTLE scheduling, sensors, and core connectivity, though official installer support is not ready. Contributors also produced custom unsigned firmware plus a V4L2 driver for 4K 10-bit AVC decoding, and m1n1 1.6 expands Rust and newer-chip groundwork. HN praised the reverse engineering but highlighted unresolved power management, upstreaming, and future firmware-signing risk.

### Comment pulse

- Reverse engineering remains incomplete → Apple power management still relies on battery-draining workarounds despite major graphics and peripheral wins.
- Custom decoder firmware carries platform risk → Apple could later require signatures for legitimate security reasons, blocking the current strategy.
- One terminology error drew correction → I²S is independent of I²C and closer to SPI, despite similar naming.

### LLM perspective

- **View:** Stable hardware blocks reward reuse, but undocumented firmware interfaces make every vendor update a compatibility event.
- **Impact:** Users gain capable M3 Linux support while maintainers absorb permanent regression and reverse-engineering costs.
- **Watch next:** Test boot-flag repair broadly, ship AVD safely, and land remaining drivers upstream.
