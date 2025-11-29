# Show HN: Glasses to detect smart-glasses that have cameras

- Score: 468 | [HN](https://news.ycombinator.com/item?id=46075882) | Link: https://github.com/NullPxl/banrays

### TL;DR
Ban-Rays is an experimental project to detect camera-equipped smart glasses, focusing on two routes: optical sensing and wireless fingerprinting. Optically, it uses IR LEDs and a photodiode to exploit cameras’ retro-reflectivity, but tests on Meta Ray-Bans show weak, inconsistent signals at realistic distances, making robust classification hard without more complex sweeps and better hardware. Networking-wise, it reliably identifies Meta Ray-Bans only during pairing/power-on via BLE manufacturer/service IDs; continuous passive detection during normal use needs more capable sniffers and possibly active probing. HN discussants debate personal vs venue use-cases, social reactions, and complementary counter-surveillance tricks.

---

### Comment pulse
- Personal and venue protection → People want to know if nearby glasses are filming them; roaming security in no-filming spaces is a natural user.  
- Social impact → Widespread detectors could trigger public confrontations and “glasshole” backlash, yet many see stealth AR glasses as inevitable.  
- Countermeasures → Ideas include IR-flooding wearables and reflective clothing to blind sensors or ALPRs—counterpoint: modern cameras’ IR filters and daylight limit effectiveness.

---

### LLM perspective
- View: Practical success likely comes from wireless fingerprints first, with optics as a close-range or offline complement.  
- Impact: Could empower individuals and venues to set recording norms, while pushing smart-glasses vendors toward clearer signaling or opt-out modes.  
- Watch next: BLE-sniffer prototypes with quantified range/false-positives, tests against other brands, and any legal or policy responses to active probing.
