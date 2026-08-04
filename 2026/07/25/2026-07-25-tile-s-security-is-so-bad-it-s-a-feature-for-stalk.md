# Tile's security is so bad it's a feature for stalkers

- Score: 132 | [HN](https://news.ycombinator.com/item?id=49050152) | Link: https://blog.adafruit.com/2026/03/05/tiles-security-is-so-bad-its-a-feature-for-stalkers/

### TL;DR

Researchers report that Tile’s crowd-sourced tracking protocol breaks several advertised protections: Tile servers can continuously learn user and tag locations, unprivileged attackers can follow devices through Bluetooth advertisements, and anti-theft mode is readily bypassed. They argue Tile intentionally weakens anti-stalking defenses for theft recovery, then relies on an accountability system that is itself subvertible and creates additional vulnerabilities. HN discussion contrasts this design with encrypted, rotating identifiers used elsewhere and debates whether cheap GPS trackers reduce the concern or miss the network’s distinctive abuse potential.

### Comment pulse

- Rotating keys limit linkage → commenters describe pairing-derived keypairs that change with time, preventing one identified advertisement from revealing later visits.
- Network scale changes attacker economics → Tile-like devices outsource GPS and transmission to surrounding phones, enabling smaller hardware and longer battery life.
- Risk remains contested → critics note purpose-built GPS trackers exist — counterpoint: Tile users may unknowingly carry an exploitable tracker already.

### LLM perspective

- View: Accountability cannot substitute for preventive privacy when identity checks and abuse evidence can themselves be bypassed or weaponized.
- Impact: Millions of users and tags may require protocol migration, firmware changes, server-side limits, and clearer stalking-response procedures.
- Watch next: Look for Tile’s remediation, independent reproduction, disclosure timelines, identifier rotation, encrypted location reports, and formal accountability definitions.
