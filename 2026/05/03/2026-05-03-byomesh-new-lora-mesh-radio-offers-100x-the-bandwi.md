# BYOMesh – New LoRa mesh radio offers 100x the bandwidth

- Score: 222 | [HN](https://news.ycombinator.com/item?id=47999636) | Link: https://partyon.xyz/@nullagent/116499715071759135

### TL;DR
BYOMesh is a tiny dual-band LoRa dev board combining sub‑GHz SX1276 with 2.4 GHz SX1281 to enable higher-bandwidth mesh backhaul links, e.g. between mountain-top nodes. The creator claims up to 100× more throughput versus traditional long-range LoRa meshes, without jumping to Wi‑Fi/Arden/HaLow’s higher power and complexity. HN discussion probes FCC-compliant operation, realistic 2.4 GHz range, and modulation details, concluding it’s a promising experimental platform for campus/industrial or hobbyist meshes but not a magic bullet for high-reliability or military drone networks.

---

### Comment pulse
- Regulatory skepticism → 100× claim questioned; MeshCore/Meshtastic sometimes violate FCC limits. — counterpoint: that issue targets firmware/channel choices, not BYOMesh’s dual-band hardware alone.  
- Range vs frequency → LoRa’s chirp spread spectrum beats Wi‑Fi’s OFDM for sensitivity; even at 2.4 GHz, multi‑km links possible with line‑of‑sight and tall antennas.  
- Use-cases debated → good fit for campus/industrial sensing, redundant backhaul, hobby “LoRaLAN”; poor fit for drone swarms due to low data rate and jamming vulnerability.  

---

### LLM perspective
- View: Treat BYOMesh as a lab for experimenting with mixed-band meshes and protocol design, not a drop-in bandwidth upgrade.  
- Impact: Could accelerate open-source work on bridging LoRa, Wi‑Fi, and packet radio, especially for HAM operators and resilience-focused communities.  
- Watch next: independent link-budget tests at different SF/bandwidths, explicit FCC-safe presets, and upstream support in Meshtastic/MeshCore firmware.
