# Starlink Mini as a failover

- Score: 168 | [HN](https://news.ycombinator.com/item?id=47396264) | Link: https://www.jackpearce.co.uk/posts/starlink-failover/

### TL;DR
Starlink Mini can be a practical home failover link: £159 hardware, then £4.50/month “standby” for always-on low-speed connectivity and instant upgrades to full bandwidth when needed. Latency and power draw are surprisingly good, and UniFi makes dual-WAN failover straightforward. The tricky bit is IPv6: Starlink gives a /56 via SLAAC, but UniFi has a bug requiring a manual default-route + boot script. Hacker News compares this to simpler 4G/5G or phone-tether failover and debates whether such uptime is actually necessary.

---

### Comment pulse
- Many home users don’t truly need 99.99% uptime → phone tethering or a cheap 5G modem covers rare outages—counterpoint: Starlink shines when cell networks are congested or offline.  
- Several report smooth Unifi + cellular/Starlink failover → secondary WAN kicks in nearly instantly, often included or cheap on existing mobile plans.  
- Some treat Starlink as “backup” but end up cancelling ISP → 300–400 Mbps with higher reliability beats flaky gigabit cable/fiber in practice.

---

### LLM perspective
- View: This setup is ideal for self-hosters, remote workers, or rural users who truly lose money when the main line drops.  
- Impact: Networking gear vendors should fix IPv6 edge cases; dual-WAN + sane IPv6 should be one-click, not an SSH ritual.  
- Watch next: Compare Starlink Mini vs 5G CPE failover on latency, congestion, and outage resilience; track UniFi firmware for native Starlink IPv6 fixes.
