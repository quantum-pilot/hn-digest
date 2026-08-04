# Haiku OS runs on M1 Macs now

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48183579) | Link: https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2

### TL;DR

Haiku’s experimental arm64 port now reaches the desktop on a bare-metal M1 MacBook Air, using m1n1 and U-Boot to present USB UEFI booting. All eight CPU cores run, and an initial 10-bit-per-channel display mismatch was corrected, but USB remains barely functional. Earlier UTM boots had choppy mouse input, while nightly images lack a complete development/package ecosystem and dedicated haikuports builder. HN celebrated the milestone and Haiku’s responsive user experience, while emphasizing limited applications, peripheral support, documentation, and platform-specific developer capacity.

### Comment pulse

- Users reported fast, stable operation on old ThinkPads and virtual machines; BeFS metadata and compact applications made Haiku useful for focused tasks.
- Perceived speed can exceed benchmarks: commenters estimated roughly 60% of Linux throughput, but credited deliberate responsiveness and user-experience priorities.
- Practicality depends on needs: browsers, LibreOffice, IntelliJ, GIMP, and GNU tools exist — counterpoint: native software and some BeOS compatibility remain limited.

### LLM perspective

- View: Booting is a platform-validation milestone, not product readiness; drivers and package infrastructure determine whether curiosity becomes sustained use.
- Impact: Apple Silicon gives Haiku fast, available ARM hardware, potentially accelerating native builds and reducing emulation costs.
- Watch next: Track USB reliability, package-manager fixes, haikuports buildbot availability, bootstrap documentation, native application coverage, and ARM hardware support.
