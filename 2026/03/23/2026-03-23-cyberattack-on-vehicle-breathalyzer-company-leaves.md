# Cyberattack on vehicle breathalyzer company leaves drivers stranded in the US

- Score: 146 | [HN](https://news.ycombinator.com/item?id=47489058) | Link: https://techcrunch.com/2026/03/20/cyberattack-on-vehicle-breathalyzer-company-leaves-drivers-stranded-across-the-us/

### TL;DR

Intoxalock paused systems after a March 14 cyberattack, preventing service centers from calibrating some court-required ignition interlocks. Devices can time-lock vehicles when calibration deadlines pass, so affected drivers from Maine to Minnesota reported being unable to start cars; this was not a remote attack on the vehicles themselves. Intoxalock operates in 46 states and serves 150,000 drivers annually, but did not identify the attack type, a possible data breach, ransom contact, or recovery date. HN sees a dangerous dependency on one central vendor for legally mandated mobility.

### Comment pulse

- Calibration time locks made an IT outage a transportation outage → one user received only a temporary ten-day extension.
- Safety-critical software needs minimum resilience and testing — counterpoint: broad software codes risk bureaucracy; regulation can target the vehicle function instead.
- Interlocks already impose awkward rolling retests and false positives → users lack market leverage because courts, not drivers, choose the requirement.

### LLM perspective

- **View:** The central design flaw is fail-closed dependency on unavailable servicing, not over-the-air vehicle compromise.
- **Impact:** Drivers can lose work and mobility while mechanics cannot reset deadlines; courts and vendors inherit continuity obligations.
- **Watch next:** Recovery timing, offline calibration paths, deadline waivers, breach disclosure, regulatory response, and compensatory procedures.
