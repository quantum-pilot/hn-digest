# WireGuard makes new Windows release following Microsoft signing resolution

- Score: 379 | [HN](https://news.ycombinator.com/item?id=47719942) | Link: https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html

### TL;DR

WireGuard released WireGuardNT 0.11 and WireGuard for Windows 0.6 after Microsoft restored its signing account. The long-delayed update adds removal of individual allowed IPs without packet loss, very low IPv4 MTUs, accumulated fixes and performance work, and major simplification from dropping pre-Windows 10 support. Driver, userspace, Go, certificate, and signing toolchains were refreshed; Windows 10 build 10240 remains tested. Jason Donenfeld calls the suspension bureaucracy, not conspiracy, and says attention produced a one-day fix. Commenters celebrate the release but doubt obscure developers would receive equivalent escalation.

### Comment pulse

- Public pressure worked because WireGuard has an audience; projects without visibility face a closed, no-appeal process and uncertain timelines.
- Some call mandatory driver signing a FOSS choke point. — counterpoint: ordinary unsigned Windows applications still run; exposure is narrower than claimed.
- Users welcomed dropping obsolete platforms, though x86 driver compilation still required a workaround after Microsoft removed SDK support.

### LLM perspective

- **View:** Rapid recovery shows the technical gate was easy to reopen; discovering and reaching accountable humans was the real failure.
- **Impact:** The release train resumes, but small kernel-tool maintainers remain dependent on platform discretion for security distribution.
- **Watch next:** Regression reports, 0.6.x updater behavior, reboot disclosure, signing-account safeguards, and whether VeraCrypt and Windscribe recover.
