# Wireguard FPGA

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45559857) | Link: https://github.com/chili-chips-ba/wireguard-fpga

### TL;DR

WireGuard FPGA is a work-in-progress proof of concept for a fully inspectable, standalone VPN appliance on an inexpensive Artix-7 board with four 1GbE ports and open-source tooling. A soft RISC-V CPU handles handshakes, keys, peers, and routing control; RTL handles packet parsing, lookup, ChaCha20-Poly1305 authentication and encryption, encapsulation, and forwarding at line rate. The project contrasts itself with an expensive proprietary 100Gbps predecessor and explicitly acknowledges timing, toolchain, verification, integration, and funding risks. It is educational infrastructure, not yet a deployable product.

### Comment pulse

- Critics questioned dedicated hardware at 1Gbps when commodity CPUs can saturate comparable links and approach 10Gbps.
- Supporters emphasized worst-case packet rates, large routing tables, power efficiency, education, and end-to-end auditability.

### LLM perspective

- View: Its near-term value is open hardware research and verification, not outperforming commodity software on headline bandwidth.
- Impact: A complete auditable stack could expose toolchain gaps and teach practical cryptographic hardware-software co-design.
- Watch next: End-to-end interoperability, minimum-packet throughput, timing closure, licensing clarity, and reproducible bitstreams.
