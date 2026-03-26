# Running Tesla Model 3's computer on my desk using parts from crashed cars

- Score: 234 | [HN](https://news.ycombinator.com/item?id=47523330) | Link: https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/

### TL;DR
A security researcher builds a fully booting Tesla Model 3 computer on his desk using salvaged MCU/autopilot units, a touchscreen, and a 12V bench supply. Tesla’s public electrical schematics reveal pinouts and part numbers, but a proprietary Rosenberger display connector forces him to buy an entire dashboard wiring harness. A failed DIY cable attempt burns a power chip, later repaired via rework. With the loom attached, the system boots, exposing SSH and a diagnostic HTTP API for deeper security research.

---

### Comment pulse
- Car wiring uses large harness looms, not individual cables → some readers amazed the author missed this—counterpoint: even knowing looms exist doesn’t imply zero modular cables.
- Tesla documentation is excellent and detailed → but access came only after right-to-repair pressure and earlier “malicious compliance” barriers to parts and manuals.
- Bench setups of ECUs are standard in automotive dev → great for diagnostics and hacking, yet still diverge enough from real vehicles to limit what you can validate.

---

### LLM perspective
- View: Salvage hardware plus official schematics now make serious automotive security research possible without owning the car.
- Impact: Encourages more independent researchers; may push automakers to harden in-car networks and exposed service interfaces.
- Watch next: Public tooling for Tesla bench setups, disclosures using ODIN/SSH, and manufacturer responses in policy and firmware updates.
