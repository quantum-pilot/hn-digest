# It's hard to build an oscillator

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46002161) | Link: https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator

### TL;DR

The author derives practical analog oscillators from first principles rather than presenting unexplained schematics. A lone MOSFET settles at a stable midpoint, so a Schmitt trigger adds hysteresis and eliminates that equilibrium; an inverter plus resistor-capacitor delay then produces a predictable relaxation oscillator near 3 kHz. An op-amp version trades components for simplicity, while a three-stage RC phase-shift loop creates frequency-selective positive feedback. Measurements also expose where constant-current approximations diverge, showing why stable frequency and clean sine waves require careful gain control.

### Comment pulse

- Commenters expanded on lightbulb-based gain stabilization and the gap between merely oscillating and remaining predictable.
- A topology-search project prompted debate over whether rediscovered LC circuits were genuinely novel.

### LLM perspective

- View: Deriving failure first makes hysteresis, delay, and phase conditions easier to understand than cookbook circuits.
- Impact: Measurement-versus-model discrepancies teach more transferable analog intuition than an idealized exact formula.
- Watch next: Temperature sensitivity, component tolerances, amplitude stabilization, and measured spectral purity.
