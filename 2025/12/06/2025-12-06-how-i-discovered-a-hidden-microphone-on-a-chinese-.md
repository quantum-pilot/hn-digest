# How I discovered a hidden microphone on a Chinese NanoKVM

- Score: 352 | [HN](https://news.ycombinator.com/item?id=46173383) | Link: https://telefoncek.si/2025/02/2025-02-10-hidden-microphone-on-nanokvm/

### TL;DR

A NanoKVM audit found a working 2×1 mm microphone that the product documentation did not clearly disclose, with installed tools able to record audio over SSH. The author also reported an initial default SSH password, shared hardcoded cryptographic material, weak session and update protections, Chinese server dependencies, and root-heavy embedded Linux. Commenters said the microphone appears on the underlying LicheeRV Nano board’s specification and likely reflects board reuse, not espionage. They distinguished serious credential and firmware flaws from ordinary embedded choices such as omitting systemd or apt.

### Comment pulse

- Undisclosed microphone remains a trust failure → buyers were not clearly warned — counterpoint: board reuse and limited server-room utility weaken malicious-implant claims.
- Security criticism needs triage → default credentials, hardcoded secrets, unchecked updates, and root execution matter more than bundled diagnostic tools.
- Open code enables replacement firmware → users still must open the case and reflash its internal card, possibly removing the microphone physically.

### LLM perspective

- View: Intent is unknowable here; product risk follows reachable capabilities, insecure defaults, and opaque supply-chain behavior.
- Impact: Administrators should isolate remote-management hardware because compromise exposes screens, keystrokes, virtual media, network access, and potentially audio.
- Watch next: Vendor fixes, signed-update verification, independent traffic captures, firmware audits, and community Linux ports.
