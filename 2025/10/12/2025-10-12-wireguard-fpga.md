# Wireguard FPGA

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45559857) | Link: https://github.com/chili-chips-ba/wireguard-fpga

TL;DR
- Open-source effort to implement WireGuard in hardware on a low-cost Artix‑7 board (4×1G), with a soft RISC‑V control plane and a wire‑speed RTL dataplane (ChaCha20‑Poly1305). It’s a Phase‑1 PoC with a co-sim testbench (VProc), targeting a fully auditable, hostless VPN node and eventual open toolchain builds (OpenXC7). HN debates practicality versus kernel WireGuard’s 1–10G performance, suggests QUIC/MASQUE or WG‑over‑QUIC for obfuscation, and values the educational and auditability angles despite “grantware” concerns.

Comment pulse
- QUIC/MASQUE as VPN → mTLS/FIPS TLS1.3, NAT traversal, traffic camouflage; used by Cloudflare WARP, Mullvad’s WG-over-QUIC — counterpoint: WireGuard’s simplicity suits FPGA acceleration.
- 1G hardware seems redundant → kernel WireGuard saturates 1G and nears 10G; value is educational, auditable RTL and worst-case, large-table throughput.
- Scaling beyond 1G → interest in 10–25G+ ports; CPUs can hit 10G, maybe 40G with larger frames; hardware helps per-watt and small-packet PPS limits.

LLM perspective
- View: Treat as open, auditable WireGuard dataplane reference, not a product; co-sim + CSR generation workflow is the reusable artifact.
- Impact: Enables academics/hobbyists to prototype hardware VPNs without proprietary toolchains; drives bug reports/improvements into OpenXC7, Verilator, and Ethernet/crypto IP cores.
- Watch next: Publish end-to-end throughput/PPS at small MTUs; OpenXC7 timing closure status; roadmap to 10G+ PHYs or Corundum port; clarify licensing/compliance.
