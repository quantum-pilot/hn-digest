# It's hard to build an oscillator

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46002161) | Link: https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator

### TL;DR

The tutorial derives reliable analog oscillators rather than presenting unexplained schematics. A lone MOSFET and resistor fail because the transistor finds a stable partially conducting equilibrium. A two-transistor Schmitt trigger adds hysteresis; feeding its inverted output through an RC delay produces a roughly 3 kHz relaxation oscillator. An op-amp version alternately charges a capacitor between thresholds, while a three-stage RC network creates a frequency-selective 180-degree phase shift. Measurements expose where constant-current approximations diverge, emphasizing that gain, delay, thresholds, and loading jointly determine behavior.

### Comment pulse

- Predictable stability is the real challenge → temperature, supply, component tolerance, and aging can move frequency even when oscillation starts reliably.
- LC designs offer compact alternatives → commenters cite single-transistor topologies — counterpoint: allegedly novel circuits may be century-old Colpitts variants.
- A lightbulb can stabilize sine-wave gain → slow filament heating raises resistance, preventing both decaying oscillation and saturation distortion.

### LLM perspective

- View: Building from feedback principles makes failures and approximations legible.
- Impact: Learners gain reusable intuition for amplifiers, hysteresis, phase shift, filtering, and stability.
- Watch next: Startup margin, temperature drift, component tolerances, harmonic distortion, loading, and Allan variance.
