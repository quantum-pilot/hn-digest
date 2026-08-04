# Framework's 10G Ethernet module exposes USB-C's complexity

- Score: 313 | [HN](https://news.ycombinator.com/item?id=48681220) | Link: https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/

### TL;DR

WisdPi’s $99 Framework-format 10GbE card shows how connector shape, USB mode, drivers, port routing, and thermals jointly determine performance. The Realtek RTL8159 adapter reached about 7Gbps with built-in drivers, then 9.4Gbps on Windows after installing Realtek’s driver, but its plastic underside approached 70°C and the module protrudes from the laptop. The reviewer recommends Framework’s $40 2.5GbE card for most users. HN debated whether USB 3.2 Gen 2x2 is truly necessary while welcoming the expansion-card ecosystem and citing legitimate laptop 10GbE uses.

### Comment pulse

- Rare Gen 2x2 support is the bottleneck → some blamed the mode’s scarcity — counterpoint: others said 10Gbps USB should already saturate 10GbE.
- Framework’s open slot attracts third parties → commenters compared it favorably with PCMCIA while clarifying WisdPi, not Framework, sells the module.
- Heat is expected at this density → commenters noted full-size 10GbE cards use heatsinks, although newer controllers can consume under 2W.

### LLM perspective

- **View:** Modular hardware moves compatibility risk into the ecosystem; standardized slots do not guarantee standardized bandwidth or cooling.
- **Impact:** Buyers must validate exact port lanes, operating-system drivers, and sustained bidirectional performance before paying for headline speed.
- **Watch next:** Retest Linux with updated RTL8159 drivers and measure throttling, power draw, and surface temperature during prolonged transfers.
