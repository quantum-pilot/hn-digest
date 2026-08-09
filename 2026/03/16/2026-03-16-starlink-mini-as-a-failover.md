# Starlink Mini as a failover

- Score: 168 | [HN](https://news.ycombinator.com/item?id=47396264) | Link: https://www.jackpearce.co.uk/posts/starlink-failover/

### TL;DR

A £159 Starlink Mini on a £4.50 monthly standby plan gives the author unlimited 500 kbps backup service and on-demand full speed, averaging 26 ms latency while drawing about 13 W. UniFi can fail over automatically from FTTP, and solar batteries keep satellite connectivity alive when local powered infrastructure fails. The rough edge is IPv6: Starlink delegates a `/56`, but a UniFi bug requires manually adding the default route, potentially after updates. HN liked the resilience but questioned whether rare home outages justify it over phone tethering or cellular backup.

### Comment pulse

- Rain fade, a 50°C operating limit, hail exposure, and sky visibility complicate “pretty guaranteed” connectivity.
- Some users get 400 Mbps tethering or nearly instant 5G failover at little extra cost.
- Cellular is simpler for routine outages — counterpoint: congested or powerless towers make an independent satellite path more valuable.

### LLM perspective

- **View:** Failover earns its cost when it avoids the primary connection’s geographic and power dependencies.
- **Impact:** Remote workers and homelabs gain continuity; casual households may buy resilience they rarely consume.
- **Watch next:** Failover drills, activation time, weather performance, firmware persistence, battery runtime, and annual cost.
