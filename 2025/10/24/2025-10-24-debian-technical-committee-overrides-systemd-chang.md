# Debian Technical Committee overrides systemd change

- Score: 148 | [HN](https://news.ycombinator.com/item?id=45692915) | Link: https://lwn.net/Articles/1041316/

- TL;DR
  - Debian’s Technical Committee directed Debian’s systemd package to keep a usable /var/lock (→ /run/lock) after systemd v258 tightened permissions and plans v259 removal, breaking UUCP, cu, and some alsa-utils. Policy (via FHS) still applies until a migration updates software and Policy. Systemd cited DoS/security risks and FHS obsolescence; upstream leaves overrides to distros. Debian will fix via packaging; stable (v257) unaffected. Longer term: move to flock/TIOCEXCL or lockdev and update Policy.

- Comment pulse
  - FHS still valuable → Predictability for packagers/admins; standards prevent surprises — counterpoint: outdated in places; distros already diverged; UAPI effort mirrors current practice.
  - Systemd behavior criticized → Maintainer seen as dismissive of breakages; others note upstream allows downstream overrides and Debian packaging must follow Policy.
  - Legacy still exists → UUCP/serial workflows survive in niches; breaking defaults blocks real users today despite security rationale.

- LLM perspective
  - View: Debian chose user stability while mandating a time-bounded migration; that aligns governance with practical distro responsibilities.
  - Impact: Debian systemd packaging will ship an override; maintainers of serial/ALSA tools must migrate to flock+TIOCEXCL or lockdev.
  - Watch next: TC migration plan, Policy update timeline, affected package list; benchmarks: breakage counts, DoS mitigations (separate tmpfs/quota), systemd v259 packaging.
