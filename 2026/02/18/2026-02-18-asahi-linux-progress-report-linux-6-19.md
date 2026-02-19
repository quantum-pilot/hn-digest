# Asahi Linux Progress Report: Linux 6.19

- Score: 392 | [HN](https://news.ycombinator.com/item?id=47059275) | Link: https://asahilinux.org/2026/02/progress-report-6-19/

### TL;DR
Asahi Linux’s 6.19-era work delivers long-awaited, experimental USB‑C external display output on Apple Silicon via the new “fairydust” kernel branch, plus 120 Hz internal displays on MacBook Pros. M3 Macs now boot to Plasma with most core hardware working, but GPU, display firmware (DCP), speakers, and polish still need substantial reverse engineering before a release. The team is also refactoring the display stack for HDR/VRR, fixing tricky webcam bugs, massively speeding GPU buffer ops, upstreaming the GPU driver, and modernizing Fedora Asahi packaging.

---

### Comment pulse
- Asahi devs praised for deep, multi-year reverse engineering → community sees it as a model hardware enablement project.
- M1/M2 Macs predicted as future hacker laptops → great build, falling prices — counterpoint: soldered SSD wear may kill long-term secondary market.
- Users ask “which Mac for Asahi?” → M1/M2 Air seen as sweet spot; M2 Air more attractive now that external display support is emerging.

---

### LLM perspective
- View: Asahi is turning Apple Silicon into a de facto reference ARM laptop platform for serious Linux use.
- Impact: Encourages upstream GPU/display work, better ARM app support, and saner package/vendor transitions in mainstream distros.
- Watch next: Upstream AGX GPU driver, stable DP Alt Mode, first polished M3 release, and Rust-based DCP driver with HDR/VRR.
