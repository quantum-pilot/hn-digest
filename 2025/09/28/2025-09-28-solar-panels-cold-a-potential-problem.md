# Solar panels + cold = A potential problem

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45401051) | Link: https://www.linspyre.com/ecoholics/temps.html

- TL;DR
    - The article warns that building panel strings near an inverter’s published max input voltage can blow the MPPT on cold, sunny days because panel open‑circuit voltage rises as temperature drops. It offers climate‑based Voc limits and stringing rules (volts add in series; keep headroom). HN pushes back: vendors advertise absolute maximums with little margin or shutdown, confusing buyers. Others note panel temp coefficients are documented, but products should enforce safe limits or give plain “max N‑panels‑in‑series” guidance.

- Comment pulse
    - Manufacturer at fault → 150 V spec used as max; consumers expect 148<150 to work — counterpoint: panel temp coefficients are published; installers should derate.
    - Design criticism → No fast over‑voltage shutdown; likely under‑rated input FETs and marketing used absolute max ratings, not recommended limits.
    - Simpler UX → State “max 2 panels in series” by model or include crowbar/TVS protection; the gas/diesel analogy misleads users.

- LLM perspective
    - View: Spec and protection design should target cold-morning Voc transients; publish recommended limits, not absolutes.
    - Impact: Better derating and auto-shutdown reduce RMAs, liability, and installer errors across consumer solar generators.
    - Watch next: Independent teardowns, firmware updates adding fast OVP, and datasheets listing “max Voc by −10/0/25°C” on the port label.
