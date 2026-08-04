# Major P2P issues in Israel and possibly other Middle East countries

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48431461) | Link: https://github.com/ValveSoftware/GameNetworkingSockets/issues/398

### TL;DR

Since mid-March, players report Steam-based PC-to-PC games in Israel—and apparently China and elsewhere—failing to establish direct P2P links and falling back to Steam Datagram Relay. Same-country Street Fighter 6 latency reaches about 120 ms, while PC-to-PS5 measures 5–10 ms. Multiple games and ISPs are affected; Share IP Address appears ignored. Replacing Steam WebRTC libraries or using a January client restores STUN-based links when both peers comply, suggesting a client regression, but no cause is confirmed. HN debated regional blocking versus Valve behavior and requested a postmortem.

### Comment pulse

- A Valve regression fits the evidence → newer clients skip STUN, whereas January builds and older WebRTC libraries restore direct connections across several games.
- Regional interference remains plausible → conflict-related filtering and China’s controls could disrupt traversal — counterpoint: successful old clients weaken a network-only explanation.
- STUN is only traversal support → it discovers public mappings; peers still need a separate signaling path to exchange connection details.

### LLM perspective

- **View:** Controlled version substitution is stronger evidence than geography; investigators should bisect Steam client and library changes.
- **Impact:** Relay-dependent action games need regional capacity and explicit telemetry showing direct-attempt failure reasons, chosen route, and added latency.
- **Watch next:** Reproduce across countries, ISPs, game versions, IPv4/IPv6, NAT types, and client builds; publish packet traces and Valve’s fix.
