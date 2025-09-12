# Raspberry Pi 5 support (OpenBSD)

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45096585) | Link: https://marc.info/?l=openbsd-cvs&m=175675287220070&w=2

TL;DR
OpenBSD has landed initial Raspberry Pi 5 support on arm64. Early reports say it installs and behaves like other OpenBSD systems, but with caveats: WiFi currently fails on some newer “D0” Pi 5 boards, and PCIe storage HATs aren’t yet supported. Users share mixed Pi 3/4 experiences—solid for servers, but installer/firmware quirks can bite, and forced power cuts risk filesystem issues. Linux support is maturing; scarce vendor documentation slows BSD driver work, though contributors expect rapid fixes.
Content unavailable; summarizing from title/comments.

Comment pulse
- Pi 3/4 feel like standard OpenBSD → extra boot/firmware steps; no arm64 power-saving; >3GB RAM on Pi 4 needs third‑party firmware — counterpoint: 7.6/7.7 fine.
- FS reliability concern → lack of journaling led to corruption after hard power cut; user avoids OpenBSD until FFS journaling ships.
- Pi 5 caveats → WiFi broken on some D0 boards, PCIe storage HATs and fan control unsupported; likely driver gaps, not the CPU stepping change.

LLM perspective
- View: Early but usable for headless roles; avoid WiFi-dependent, low-power, or PCIe-heavy setups for now.
- Impact: Homelabs and small servers benefit; embedded products should wait for power management, WiFi, fan, and PCIe maturity.
- Watch next: Fixes for Pi 5 WiFi on D0 boards, fan/thermal drivers, PCIe storage, FFS journaling roadmap, and upstream Linux firmware/documentation updates.
