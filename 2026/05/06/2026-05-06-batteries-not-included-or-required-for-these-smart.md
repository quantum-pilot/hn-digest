# Batteries Not Included, or Required, for These Smart Home Sensors

- Score: 195 | [HN](https://news.ycombinator.com/item?id=47998638) | Link: https://coe.gatech.edu/news/2026/04/batteries-not-included-or-required-these-smart-home-sensors

### TL;DR
Georgia Tech researchers built penny-sized metal tags that work as battery‑free event sensors. A moving part hits the tag, making a brief ultrasonic “ping” whose frequency is set by the tag’s geometry; nearby microphones identify which tag fired using simple, non‑ML rules. The tags cost cents, are inherently short‑range/private, and target uses like doors, cabinets, toilets, or gym equipment. Hacker News praises the simplicity but questions 1 m range, ~93% accuracy, animal ultrasound exposure, wearables‑only reception, and mass‑market viability versus existing RF/kinetic solutions.

### Comment pulse
- Ultrasonic pulses raise concerns about pets’ and children’s hearing and noise pollution; others argue pulses are brief, low‑range, and insignificant compared with existing ultrasonic electronics.  
- Commenters compare with kinetic RF light switches that harvest mechanical energy to send radio events; they offer range but are bulkier and pricier.  
- Several note it’s lab‑stage: ~93% accuracy, ~1 m range, per‑installation tuning, wearables as receivers—counterpoint: may still shine in RF‑hostile or industrial tracking scenarios.  

### LLM perspective
- View: Treat these as extremely cheap, passive identifiers for localized event logging, not general smart‑home replacements for powered multi‑sensor nodes.  
- Impact: Could enable sensing where batteries are impossible—sealed equipment, underwater structures, or RF‑restricted environments like MRI rooms and explosive atmospheres.  
- Watch next: integrate detection into phones and wearables, characterize effects on animals, and quantify lifetime, failure modes, and spoofing/attack surfaces.
