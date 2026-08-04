# QuadRF can spot drones and see WiFi through my wall

- Score: 412 | [HN](https://news.ycombinator.com/item?id=48861717) | Link: https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/

### TL;DR

QuadRF is an open-source 4×4 MIMO phased-array software-defined radio combining a Raspberry Pi 5 and FPGA hardware across 4.9–6 GHz. Its browser-based augmented-reality viewer overlays beamformed RF energy on a camera feed; a prototype localized 5 GHz Wi-Fi through walls and tracked a DJI drone, though manual gain and alignment were clunky. The design streams low-latency I/Q data over the Pi’s MIPI lanes above 5 Gbps and supports chaining modules toward arrays. The $499 crowdfunded kit remains pre-production. HN focused on ADC design, frequency coverage, multi-unit localization, and acoustic-imaging analogues.

### Comment pulse

- Visualization is band-limited → the current 4.9–6 GHz front end covers higher-frequency Wi-Fi, not 2.4 GHz Wi-Fi or Bluetooth.
- The data path is unusually inventive → camera/display MIPI links provide cheap, low-latency I/Q streaming while preserving PCIe for storage or networking.
- Consumer accessibility expands experimentation → open software invites custom sensing — counterpoint: crowdfunding risk, rough controls, calibration, and RF expertise constrain immediate utility.

### LLM perspective

- **View:** The significant contribution is affordable directional RF imaging, not novel proof that radio signals traverse walls or expose traffic.
- **Impact:** Researchers and licensed operators gain a modular platform for localization, interference hunting, beamforming, radio astronomy, and security education.
- **Watch next:** Validate sensitivity, angular resolution, calibration stability, emissions compliance, production hardware, automatic gain, and synchronized multi-device 3D localization.
