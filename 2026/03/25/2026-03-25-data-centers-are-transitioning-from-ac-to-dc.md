# Data centers are transitioning from AC to DC

- Score: 299 | [HN](https://news.ycombinator.com/item?id=47511703) | Link: https://spectrum.ieee.org/data-center-dc

### TL;DR
AI data centers are hitting megawatt-per-rack levels, making today’s AC-centric power paths—AC → DC → AC → DC—too lossy, bulky, and copper‑hungry. Hyperscalers and vendors (Nvidia, Vertiv, Eaton, Delta, SolarEdge) are pushing 13.8 kV AC directly to ~800 V DC at the perimeter, then DC buses into racks, cutting conversion stages, copper use by ~45%, and gigawatt‑scale TCO by ~30%. Commenters debate safety of 800 V hot‑plugging, practical DC adoption, and whether hyperscaler demand finally breaks the long‑standing chicken‑and‑egg problem.

### Comment pulse
- DC everywhere (even PoE homes) → Fewer bricks and AC-DC stages could help, but idle transformer losses, cable gauge, and AC input remain limiting—counterpoint: centralized smart DC could still win.  
- 800 V hot-plug racks → Needs sophisticated MOSFET control, pin sequencing, shutters, and liquid-cooling quick-connects; EV fast-charger experience suggests it’s feasible but nontrivial.  
- Adoption pattern → 48 V DC and DC options are old news, yet 800 V is new; skeptics see a niche, others think hyperscalers will force an ecosystem shift.

### LLM perspective
- View: 800 V DC is a power-distribution optimization, not a revolution; it coexists with local 48 V and point-of-load converters.  
- Impact: Hyperscale AI sites gain most; colos and smaller operators will follow once standards, safety codes, and modular PSUs mature.  
- Watch next: Concrete 800 V DC reference designs, standardized rack connectors, comparative PUE/TCO benchmarks versus AC, and updates from Mt. Diablo / OCP efforts.
