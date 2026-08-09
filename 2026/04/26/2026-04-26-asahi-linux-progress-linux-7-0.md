# Asahi Linux Progress Linux 7.0

- Score: 586 | [HN](https://news.ycombinator.com/item?id=47909226) | Link: https://asahilinux.org/2026/04/progress-report-7-0/

### TL;DR

Asahi Linux’s Linux 7.0 report combines infrastructure cleanup with substantial Apple Silicon enablement. Automated installer releases replace a two-year manual bottleneck; new firmware rebuilding unlocks calibrated ambient-light sensors. Experimental PMP support cuts measured idle draw on a 14-inch M1 Pro by roughly 0.5 W, while Bluetooth coexistence fixes audio dropouts. Reverse engineering also produced provisional variable-refresh support, more headphone sample rates, and broader M3 hardware coverage. HN praised the technical sleuthing but debated whether slow polish and Apple’s moving, undocumented platform limit mainstream readiness.

### Comment pulse

- Supporting 44.1 kHz enables bit-perfect CD and FLAC playback; commenters wondered why macOS itself apparently restricts this chip to 48/96 kHz.
- Skeptics see an enduring “last 20%” problem — counterpoint: much Asahi work already goes upstream, and forks are normal kernel-development staging grounds.
- Users split on Apple hardware plus Linux versus Framework or macOS, reflecting differing priorities around openness, polish, battery, and compatibility.

### LLM perspective

- Upstream acceptance, default-enabled PMP, and compositor-compatible VRR will distinguish experiments from dependable features.
- Track suspend drain across supported machines; idle gains alone do not establish laptop battery parity.
- Automated installer delivery reduces compatibility lag but makes release testing and rollback discipline more important.
