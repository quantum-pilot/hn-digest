# How to turn anything into a router

- Score: 557 | [HN](https://news.ycombinator.com/item?id=47574034) | Link: https://nbailey.ca/post/router/

### TL;DR
The post walks step‑by‑step through turning nearly any Linux-capable box—mini PC, old laptop, SBC—into a full home router and Wi‑Fi AP. Using Debian, hostapd, dnsmasq, bridges, and nftables, it sets up WAN/LAN, wireless, NAT, firewalling, DHCP/DNS, and even serial-console access. The author emphasizes that consumer routers are just small computers, so e‑waste can be repurposed into reliable networking gear. HN comments add tools, nostalgia, and performance/appliance tradeoffs between DIY Linux routers and purpose-built router OSes or ASIC hardware.

---

### Comment pulse
- Bare-minimum DIY routing is educational → same kernel features underlie Docker NAT, Android hotspots, and consumer routers—counterpoint: many still prefer turnkey router distros or UIs.
- Tools and nostalgia → create_ap script and 90s/00s Linux-on-junkbox war stories show this pattern is old, cheap, and highly reusable.
- Performance vs. architecture → x86 + Linux bridges are flexible but slower and higher-latency than ASIC-based routers; Mikrotik-style PCIe router boards intrigue performance-minded tinkerers.

---

### LLM perspective
- View: This is really a hands-on Linux networking primer disguised as a router how‑to.
- Impact: Empowers hobbyists to demystify routers, audit configuration, and extend hardware life instead of buying opaque appliances.
- Watch next: Better comparisons of latency/throughput vs. ASIC routers, updated “Linux router” documentation, and small, open, hardware-accelerated cards.
