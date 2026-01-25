# Doing gigabit Ethernet over my British phone wires

- Score: 412 | [HN](https://news.ycombinator.com/item?id=46742362) | Link: https://thehftguy.com/2026/01/22/doing-gigabit-ethernet-over-my-british-phone-wires/

## TL;DR
Author in the UK struggles with flaky powerline networking and can’t run new Ethernet, but his house is packed with daisy‑chained phone sockets on Cat5 cable. He imports Gigacopper G.hn adapters that run gigabit Ethernet over a single telephone pair, suffering Brexit-era VAT and tracking hassles. Despite messy internal wiring, the link negotiates ~1.3–1.7 Gbps PHY and delivers full 500 Mbps service with sub‑millisecond latency. He argues there’s a big untapped market for gear that exploits existing phone wiring.

## Comment pulse
- Many “phone” extensions are actually Cat5e; swapping faceplates and using T568A/B often yields gigabit without adapters — counterpoint: daisy-chained runs complicate this.  
- G.hn chipsets slice spectrum into small bins, use OFDM with adaptive bit-loading/FEC, and simply avoid frequencies ruined by bridge taps or reflections.  
- UK buyers now face opaque customs, tracking lies, and online VAT payments for EU tech; some argue retailers should pre-collect VAT to bypass border delays.  

## LLM perspective
- View: Reusing in-wall phone and coax runs with advanced PHYs offers cheap, low-latency upgrades where WiFi or new cabling are impractical.  
- Impact: Enables renters and old-building owners to get wired-like performance; pressures ISPs and builders to acknowledge non-Ethernet structured cabling.  
- Watch next: off-the-shelf G.hn home kits, open diagnostics (SNR-per-tone, topology maps), and regulations favoring structured cabling over voice-only sockets.
