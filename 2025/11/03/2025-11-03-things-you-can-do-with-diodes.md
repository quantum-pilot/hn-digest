# Things you can do with diodes

- Score: 287 | [HN](https://news.ycombinator.com/item?id=45805900) | Link: https://lcamtuf.substack.com/p/things-you-can-do-with-diodes

- TL;DR
    - The post gives a clear, practical tour of ordinary diodes: p–n junction physics, forward drop and reverse breakdown, then hands-on uses—TVS overvoltage protection and reverse‑polarity guard, Zener references (including cascaded stages), rectifiers and envelope followers, full‑wave bridges, charge‑pump doublers, clampers/DC restorers, and simple OR/AND “diode logic” with caveats about fan‑out. Author notes modern transistorized or op‑amp solutions often outperform but diodes remain versatile building blocks. HN adds analog tricks (mixers, varactors, diode ladders, clipping) and flags the 0.6 V drop pain at low rails; tools for simulating included.

- Comment pulse
    - Analog extras: mixers, log converters, diode rings for gain control, varactors for tunable capacitance, clippers, samplers, rectennas → exploit nonlinearity/capacitance.
    - Low-voltage caution: ~600 mV drop is big at 3.3–5 V; prefer Schottky or active rectifiers—counterpoint: fine at high voltages or RF peaks.
    - Hands-on: CircuitLab examples cover rectifiers, Zener references, charge pumps; readers asked for beginner-friendly guides to build safely and choose components.

- LLM perspective
    - View: Treat diodes as voltage- and field-controlled switches; combine with RC to shape, shift, multiply, and protect signals cheaply.
    - Impact: Better mental models for embedded and RF tinkerers; fewer ICs, faster prototypes, and safer inputs in resource-constrained designs.
    - Watch next: Quantify diode vs. Schottky vs. active losses; temperature drift of Zeners; varactor-tuned filters/VCOs; rectenna efficiency measurements.
