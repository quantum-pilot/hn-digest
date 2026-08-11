# AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47167763) | Link: https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf

### TL;DR

AirSnitch finds that vendor-defined Wi-Fi client isolation often fails across encryption, routing, and switching layers. An already connected malicious client—or one using a co-located open SSID—can abuse shared group keys, bounce packets through the gateway, or spoof MAC identities to steal switch ports, enabling injection, interception, and sometimes bidirectional machine-in-the-middle access across BSSIDs or APs. Every tested router and network had at least one weakness. The authors and HN commenters stressed that this bypasses isolation; it does not crack arbitrary Wi-Fi credentials or a lone private SSID.

### Comment pulse

- Enterprise segmentation is the sharpest risk → an attacker on guest Wi-Fi intercepted traffic meant for a co-located encrypted university network.
- Home exposure depends on topology → multiple bands, guest SSIDs, or APs create pivot paths — counterpoint: attackers still need local network access.
- Isolation also breaks device discovery → stronger hotel and campus safety can conflict with Chromecast, speaker, and smart-light usability.

### LLM perspective

- **View:** Cross-layer identity must bind credentials, MAC, IP, SSID, and switch port.
- **Impact:** Operators should separate trust domains with VLANs and reject duplicate or gateway MACs.
- **Watch next:** Vendor patches, Passpoint updates, standardized guarantees, and per-client group-key deployment.
