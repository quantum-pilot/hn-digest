# How to turn anything into a router

- Score: 557 | [HN](https://news.ycombinator.com/item?id=47574034) | Link: https://nbailey.ca/post/router/

### TL;DR

A practical guide turns any Linux computer into an IPv4 router using two network interfaces—or one plus USB Ethernet—and Debian’s standard tools. It bridges wired and wireless LAN ports, enables forwarding, applies default-deny filtering and NAT with nftables, serves DHCP and DNS through dnsmasq, and creates Wi-Fi through hostapd. Even an old 1.5GHz Celeron reportedly routes 820–850 Mbps wired, though the author recommends a dedicated access point for dependable wireless. HN valued seeing the minimal primitives, while many preferred OpenWrt, OPNsense, or pfSense for updates and appliance-like administration.

### Comment pulse

- `create_ap` packages the same kernel features into one customizable command and supports test networks, WPA2/3, and simultaneous client/AP hardware.
- GUI distributions reduce weekend maintenance — counterpoint: their abstractions can obscure Linux concepts and block unconventional topologies.
- General-purpose CPUs handle home throughput, but dedicated switch ASICs should win on efficiency and latency; commenters wanted measurements beyond bandwidth.

### LLM perspective

- **View:** Building once from primitives teaches the failure domains that make later appliance choices and troubleshooting better informed.
- **Impact:** Reused PCs can replace consumer routers cheaply, at the cost of power, size, wireless quality, and maintenance responsibility.
- **Watch next:** IPv6 configuration, security updates, NIC reliability, latency under inspection, power-loss recovery, backups, and hardware-offload benchmarks.
