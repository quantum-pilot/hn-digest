# Utah to hold websites liable for users who mask their location with VPNs

- Score: 209 | [HN](https://news.ycombinator.com/item?id=47997358) | Link: https://www.tomshardware.com/software/vpn/utah-becomes-first-us-state-to-target-vpn-use-with-age-verification-law

### TL;DR

Utah’s Senate Bill 73, effective May 6, treats people physically in Utah as accessing from the state even when a VPN hides their location, making covered websites responsible for age checks and barring bypass instructions. Critics call this an impossible liability trap: sites can flag known datacenter addresses, but rotating, residential, and self-hosted tunnels resemble ordinary traffic; reliable protocol detection requires ISP-level inspection. HN expected VPN blocking or global identity checks, raised vagueness and free-speech objections, and warned sophisticated users would evade restrictions while ordinary privacy users suffer.

### Comment pulse

- Website-level detection cannot reveal true location reliably → IP databases miss residential endpoints and personal tunnels; deep packet inspection belongs to network operators.
- Blocking known VPN ranges is feasible → counterpoint: it catches mainstream privacy users while leaving inexpensive self-hosted or obfuscated routes available.
- Unclear compliance duties may invite constitutional challenges → commenters cited vagueness, due process, and least-restrictive-means requirements for speech regulation.

### LLM perspective

- **View:** The law assigns liability to the party least able to observe the fact it must prove.
- **Impact:** Sites may overcomply through universal verification, geoblocking, or VPN bans, expanding data collection beyond Utah.
- **Watch next:** Enforcement guidance, court challenges, site withdrawals, false-positive blocking rates, statewide VPN use, and movement toward ISP-level controls.
