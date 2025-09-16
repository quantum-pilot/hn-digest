# Lucky 13: a look at Debian trixie

- Score: 235 | [HN](https://news.ycombinator.com/item?id=45059160) | Link: https://lwn.net/Articles/1033474/

- TL;DR
  - Debian 13 “trixie” lands as a conservative, polished stable: APT 3.0 by default, 64‑bit RISC‑V added, i386/MIPS removed; GNOME 48/Plasma 6.3 atop kernel 6.12 LTS and GCC 14.2. It favors predictability over bleeding edge, still offering X.org sessions. Installer is powerful but verbose; skip root password to auto‑enable sudo. Upgrades: convert to DEB822, watch NIC renames; /tmp now tmpfs; 64‑bit time_t and DSA SSH removal. Discussion centers on extrepo/deb-get, Firefox ESR vs latest, and stable/testing/unstable/backports tradeoffs.

- Comment pulse
  - extrepo simplifies third‑party installs → curated DEB822 entries and GPG keys; deb-get complements it. — counterpoint: occasional dependency clashes (e.g., libasound2 vs libasound2t64 on trixie).
  - Stable vs freshness → prefer stable+backports; testing delays security fixes; experts pin unstable for updates; some daily-drive sid successfully.
  - Firefox ESR defaults → predictable security; to get latest, enable Mozilla repo; Debian builds keep offline translation, auto-download models; unattended-upgrades can restart prompts.

- LLM perspective
  - View: Conservative release modernizes plumbing (APT 3, DEB822, 64‑bit time_t, tmpfs /tmp) while expanding architectures and retaining X.org sessions.
  - Impact: Enterprises, RISC‑V adopters, and accessibility users benefit; desktop tinkerers need backports, Flatpak, or extrepo to track newer apps.
  - Watch next: Forky plans; GNOME 49 X.org removal; APT 3 migration edge cases; DEB822 tooling; RISC‑V performance; testing-with-pinning security guidance.
