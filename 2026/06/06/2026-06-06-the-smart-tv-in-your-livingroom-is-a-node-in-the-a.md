# The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy

- Score: 194 | [HN](https://news.ycombinator.com/item?id=48422993) | Link: https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/

### TL;DR

Include Security reverse-engineered Bright Data’s iOS SDK and monitored it for 30 days, finding that partner apps can turn consenting phones and smart TVs into residential proxy exits for web scraping. The SDK reports device state, accepts tunnel jobs over a persistent WebSocket, and can bind to physical interfaces to bypass iOS VPN routing. Public configuration names large media partners but does not prove their current apps ship the SDK. HN readers favored offline TVs, VLANs, and DNS blocking, while questioning whether apps should ever bypass VPNs.

### Comment pulse

- Keeping smart TVs offline is safest → owners distrust forced connectivity, latent telemetry, advertising, and firmware changes.
- Network segmentation offers a compromise → isolated VLANs preserve local control APIs while denying internet access; DNS blocks provide simpler protection.
- VPN bypass divided commenters → required-interface APIs support VPN and local-network apps — counterpoint: ordinary apps should not evade a user’s security boundary.

### LLM perspective

- **View:** Consent describing free resources obscures that strangers’ requests inherit the household’s IP reputation and risk.
- **Impact:** App stores, TV OEMs, and MDM teams need explicit SDK disclosure plus enforceable network-use limits.
- **Watch next:** Verify named partners per app, track QUIC migration, and test whether platform policies restrict physical-interface binding.
