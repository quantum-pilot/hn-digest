# Doing gigabit Ethernet over my British phone wires

- Score: 412 | [HN](https://news.ycombinator.com/item?id=46742362) | Link: https://thehftguy.com/2026/01/22/doing-gigabit-ethernet-over-my-british-phone-wires/

### TL;DR

To replace unstable powerline networking, the author connected two German Gigacopper G.hn adapters through a daisy-chained British phone circuit and achieved the full 500 Mbps internet rate plus a gigabit iperf transfer. Debugging showed a 1.385 Gbps link despite inconsistent three- and four-wire Cat5 terminations. Switching from client-server to InHome firmware enabled peer networking for up to 16 devices with sub-millisecond latency. Commenters explained that OFDM can avoid damaged frequency bins, while noting that simple RJ45 conversion is cheaper when Cat5e runs are direct.

### Comment pulse

- Daisy chains block ordinary Ethernet reuse → standard gigabit needs four point-to-point pairs, whereas G.hn can exploit a shared phone pair.
- Short-range spectrum provides headroom → 200 MHz signaling and adaptive subcarriers tolerate reflections that severely constrain long-distance DSL.
- Import friction was the least technical obstacle → post-Brexit tracking hid unpaid VAT until failed-delivery status triggered the payment workflow.

### LLM perspective

- View: Existing phone wiring can be valuable network infrastructure when topology prevents direct Ethernet conversion.
- Impact: Older homes gain low-latency wired backhaul without opening walls, but adapter availability and import support remain weak.
- Watch next: Multi-room throughput, stability across bridge taps, SNR-per-tone diagnostics, power use, and wider retail distribution.
