# WireGuard makes new Windows release following Microsoft signing resolution

- Score: 379 | [HN](https://news.ycombinator.com/item?id=47719942) | Link: https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html

### TL;DR
WireGuard has released a long-awaited Windows update: WireGuardNT v0.11 (kernel driver/API) and WireGuard for Windows v0.6 (UI/tools). The release focuses on accumulated bug fixes, performance gains, and a much cleaner codebase by dropping pre-Windows 10 support, plus a few features like per-allowed-IP removal and very low IPv4 MTUs. The previous holdup was Microsoft suspending their driver-signing account; this was quickly reversed after public attention, sparking debate about Windows code-signing power dynamics and risks for smaller FOSS projects.

---

### Comment pulse
- Public attention fixed WireGuard’s signing issue → HN/Twitter visibility gave leverage in an otherwise “no appeal” process — counterpoint: maintainer insists it was simple bureaucracy, not malice.  
- Code-signing regime worries FOSS devs → kernel-driver signing plus opaque lockouts feel like a structural threat, especially for less-known projects without an audience.  
- Some see workarounds → pay for higher-tier support or reapply under a new account; others note this is unrealistic and leaves many small developers stranded.

---

### LLM perspective
- View: Driver-signing centralizes power; even benign bureaucracy can functionally censor critical low-level software like VPNs and disk encryption.  
- Impact: High-profile tools get rescued by publicity; niche security and hobbyist drivers risk silent abandonment on Windows.  
- Watch next: Microsoft process changes, telemetry-based “VIP” handling, FOSS driver attestation programs, and whether similar incidents recur with VeraCrypt or others.
