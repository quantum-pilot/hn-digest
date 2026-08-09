# New 10 GbE USB adapters are cooler, smaller, cheaper

- Score: 533 | [HN](https://news.ycombinator.com/item?id=47899053) | Link: https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/

### TL;DR

New RTL8159-based USB-C adapters make 10 GbE over RJ45 smaller, cooler, and cheaper than older Thunderbolt boxes: the tested WisdPi costs $80 and reached 42.5°C under a short bidirectional load. Full roughly 9.5 Gb/s performance appeared only through a 20 Gb/s USB 3.2 Gen 2x2 desktop port; 10 Gb/s host links delivered about 6–7 Gb/s, and Windows required a Realtek driver. A $30 5 GbE adapter reached 4.6 Gb/s. HN agreed confusing USB capabilities, not CPU threading, are the main purchasing trap.

### Comment pulse

- Apple hardware lacks USB 3.2 Gen 2x2, so Thunderbolt remains the reliable route to symmetric 10 GbE on supported Macs.
- RJ45 advocates cite existing in-wall Cat5e/Cat6 — counterpoint: SFP+ users prefer cooler DAC or fiber links and flexible used switches.
- Parallel `iperf3` runs changed results by under 2%, supporting host-link bandwidth rather than single-core limits as the bottleneck.

### LLM perspective

- Label adapters by required host bandwidth and measured throughput, not Ethernet link rate alone.
- Compare sustained thermals and power at full speed; the reported 0.86 W measurement used USB 2.
- Validate Linux drivers, jumbo frames, latency, packet rate, sleep recovery, and multi-gig fallback before deployment.
