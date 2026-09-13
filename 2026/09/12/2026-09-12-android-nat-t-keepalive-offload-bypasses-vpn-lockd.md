# Android NAT-T keepalive offload bypasses VPN lockdown

- Score: 198 | [HN](https://news.ycombinator.com/item?id=49665502) | Link: https://supuk.ch/papers/android-natt-keepalive-vpn-bypass

### TL;DR

A security paper reports that an ordinary Android application can use the public NAT-T keepalive API to emit fixed UDP/4500 packets through the physical network despite Always-on VPN lockdown. A Pixel 8 Pro packet capture confirmed leakage; Samsung and Nothing devices showed active physical-path offload slots, with weaker evidence on the latter. The researcher attributes this to unauthenticated resource pairing and missing caller-policy enforcement before hardware offload, estimating broad Android 12+ exposure. HN debated severity, remediation, and Google's handling.

### Comment pulse

- Lockdown's identity boundary is violated → fixed keepalives reveal the physical source address and timing, despite lacking arbitrary payload control.
- Platform enforcement needs redesign → GrapheneOS commenters described multiple leak paths and favored systemic confinement over isolated patches.
- Closing an external report does not prove intent → Google may track valid VPN leaks internally while excluding them from bounty scope.

### LLM perspective

- View: Offloaded networking is a policy boundary, not merely an optimization, because packets bypass ordinary socket routing checks.
- Impact: VPN users and administrators cannot treat lockdown as absolute identity confinement on affected devices.
- Watch next: Reproduction across chipsets, Android's framework fix, backport policy, GrapheneOS mitigation, and packet-level regression tests.
