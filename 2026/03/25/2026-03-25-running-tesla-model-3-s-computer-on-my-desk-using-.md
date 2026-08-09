# Running Tesla Model 3's computer on my desk using parts from crashed cars

- Score: 234 | [HN](https://news.ycombinator.com/item?id=47523330) | Link: https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/

### TL;DR

For Tesla bug-bounty research, the author assembled a desk-side Model 3 system from salvaged MCU/autopilot hardware, a touchscreen, a 12-volt supply, and Tesla’s public wiring references. The computer exposed signed-key SSH and the ODIN diagnostic API on its internal network. An improvised display splice briefly worked before debris shorted a power controller, which a repair shop replaced. Buying an $80 dashboard wiring loom finally supplied the unobtainable connector, producing a working touchscreen and car OS. HN recognized the result as a standard automotive development bench.

### Comment pulse

- Automotive readers were surprised the researcher overlooked wiring harnesses — counterpoint: knowing looms exist does not imply individual leads are unavailable.
- Tesla’s detailed documentation drew praise, tempered by accounts that right-to-repair rules forced earlier reluctant and restrictive access.
- “LVDS cable” prompted terminology corrections: LVDS is signaling, while display-link protocols and connectors vary across laptops, cars, and spacecraft.

### LLM perspective

- **View:** Salvage hardware creates an affordable, repeatable security lab, provided electrical work is treated as seriously as software.
- **Impact:** Researchers can probe interfaces without risking a roadworthy vehicle, though bench behavior may differ materially.
- **Watch next:** Firmware extraction, CAN exploration, root-access findings, harness documentation, and responsible disclosure.
