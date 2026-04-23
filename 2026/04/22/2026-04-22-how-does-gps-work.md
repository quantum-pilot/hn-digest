# How does GPS work?

- Score: 212 | [HN](https://news.ycombinator.com/item?id=47861087) | Link: https://perthirtysix.com/how-the-heck-does-gps-work

TL;DR  
GPS turns time into distance: satellites broadcast timestamped signals, your receiver measures delays, computes distances, then trilaterates its 3D position. A 4th satellite solves for your phone’s clock error, since cheap oscillators would otherwise cause kilometer‑scale mistakes. Relativistic effects make satellite clocks run faster in orbit; hardware is pre‑offset so they align with Earth clocks, avoiding 10‑km‑per‑day drift. Modern receivers use many satellites and constellations, geometry filtering, and multipath rejection to reach meter‑level accuracy.

LLM perspective  
- View: Emphasizes conceptual clarity over modulation/orbit details, good entrypoint before deeper treatments covering signals, error models, and implementations.  
- Impact: Helps non‑engineers grasp why GPS sometimes fails—urban canyons, weak geometry—informing product UX, safety margins, and expectations.  
- Watch next: Wider GNSS adoption, dual‑frequency consumer chips, and local augmentation networks tightening accuracy to centimeters for vehicles, drones, and AR.
