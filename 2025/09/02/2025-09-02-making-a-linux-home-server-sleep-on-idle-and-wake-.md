# Making a Linux home server sleep on idle and wake on demand (2023)

- Score: 296 | [HN](https://news.ycombinator.com/item?id=45108066) | Link: https://dgross.ca/blog/linux-home-server-auto-sleep

### TL;DR

The author makes an Ubuntu home server suspend when no users or Time Machine connections are active, then wake from ordinary network requests. Unicast Wake-on-LAN works only while clients retain the server's IP-to-MAC mapping, so an always-on Raspberry Pi runs a small ARP stand-in that answers requests with the sleeping server's MAC address. Optional Avahi advertising keeps services discoverable. The setup requires compatible network hardware, disables IPv6 because it relies on ARP, and needs filtering to avoid unwanted wakeups.

### Comment pulse

- Readers shared simpler alternatives: scheduled wakeups, mechanical timers, router-generated magic packets, power-button wiring, and PiKVM.
- Hardware behavior varies; NIC power during sleep and BIOS settings can make Wake-on-LAN unexpectedly unreliable.

### LLM perspective

- View: The clever step is preserving network identity during sleep, not merely sending a wake packet.
- Impact: Demand-driven suspension can reduce idle energy while keeping familiar services reachable without client-side wake rituals.
- Watch next: IPv6 Neighbor Discovery support and safeguards against chatty devices would make the approach more general.
