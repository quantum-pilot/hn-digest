# GotaTun – Mullvad's WireGuard Implementation in Rust

- Score: 523 | [HN](https://news.ycombinator.com/item?id=46324543) | Link: https://mullvad.net/en/blog/announcing-gotatun-the-future-of-wireguard-at-mullvad-vpn

### TL;DR
Mullvad is replacing its Go-based WireGuard userspace implementation (wireguard-go) with GotaTun, a Rust fork of Cloudflare’s BoringTun. The aim is tighter integration with their mostly-Rust stack, fewer FFI headaches, and better performance on resource-constrained devices. On Android, where 85% of Mullvad app crashes came from wireguard-go, user-perceived crashes dropped from 0.40% to 0.01% after GotaTun, with reports of faster connects, higher throughput, and lower battery use. A security audit and rollout to desktop/iOS are planned for 2026.

---

### Comment pulse
- GotaTun feels faster on phones → users report 5×+ throughput and quicker connects, though some see new sleep-state/battery issues—counterpoint: likely Android/MTU quirks, not GotaTun itself.  
- Rust vs Go for networking → Rust wins for firmware/embedded (no GC, predictable timing, better FFI as a library), but Go remains “good enough” and developer familiarity often dominates.  
- WireGuard and censorship → protocol isn’t meant to evade DPI; obfuscation should be separate (Shadowsocks, amnezia-wg). Mullvad already layers obfuscation, though some wish it were native.

---

### LLM perspective
- View: This is a textbook “reduce FFI, standardize on one language” move, using Rust to harden a critical security and reliability component.  
- Impact: Mullvad’s mobile stability improves now; other VPNs may reassess Go-based WireGuard on Android if similar crash patterns exist.  
- Watch next: Independent audit findings, cross-platform performance benchmarks, and whether any Rust WireGuard work feeds back into broader projects like BoringTun or kernel-adjacent tooling.
