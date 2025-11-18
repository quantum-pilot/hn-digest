# Show HN: ESPectre – Motion detection based on Wi-Fi spectre analysis

- Score: 106 | [HN](https://news.ycombinator.com/item?id=45953977) | Link: https://github.com/francescopace/espectre

- TL;DR
  - ESPectre turns a €10 ESP32‑S3 into a camera‑free motion sensor by analyzing Wi‑Fi Channel State Information. It avoids ML, using DSP: moving‑variance segmentation on raw “spatial turbulence,” optional filtered features, and MQTT/Home Assistant integration. Setup ~30–45 minutes; works best 3–8 m from the router. The author stabilizes CSI with ICMP pings for predictable packet timing. HN discussion spans privacy/surveillance risks, “no‑ML” semantics, practical architecture tips, and throughput notes (two S3s can push ~6k CSI packets/s).

- Comment pulse
  - Architecture → Generate ICMP pings to the gateway for steady CSI; segment on raw spatial turbulence; filter only features → more reliable triggers than sniffing ambient traffic.
  - No‑ML claim → rules are DSP, no training or labels — counterpoint: ML is applied math; the boundary is methodological, not mathematical.
  - Surveillance risks → presence detection without cameras can monitor occupants invisibly; ethics require consent, disclosure, and secure data handling.

- LLM perspective
  - View: Deterministic CSI‑based DSP is a strong baseline for presence; multi-room fusion and adaptive thresholds will matter more than model choice.
  - Impact: Enables low-cost, privacy-preserving occupancy sensing for Home Assistant users; nudges router makers toward 802.11bf features.
  - Watch next: Benchmark false alarm rates across homes; compare ping-driven vs dual‑ESP packet sources; publish datasets for pet/person disambiguation and multi-sensor tracking.
