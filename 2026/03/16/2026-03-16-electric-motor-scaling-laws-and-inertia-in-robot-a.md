# Electric motor scaling laws and inertia in robot actuators

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47350016) | Link: https://robot-daycare.com/posts/actuation_series_1/

### TL;DR
The post derives simple scaling laws for electric motors and shows that, under ideal assumptions, **reflected inertia for a given output torque depends only on power dissipation, not on gear ratio or motor size**. A normalized motor constant, dividing out radius and mass, becomes nearly size‑invariant across real frameless motors and matches simple Lorentz-force material limits. Motor topology (radial, axial, double‑sided) barely changes this figure of merit. HN discussion broadens to gearbox realities, motor–muscle comparisons, and whether actuation or software truly limits robotics.

---

### Comment pulse
- Ben Katz’s Mini Cheetah work heavily influenced modern hobby/academic actuators and Aaed Musa’s capstan drives; “zero backlash” marketing is critiqued as physically impossible.
- High gear ratios increase reflected inertia, but when motor geometry is co‑designed, net inertia at fixed torque mainly tracks allowable heating, not ratio.
- Debate: motors vs muscles—motors are heavier but more efficient; tendons/cables reduce limb inertia. Some argue hardware is good enough and autonomy software is now the main bottleneck.

---

### LLM perspective
- View: Treat “force per heating per mass” as a core design metric; optimize actuators around thermal limits, not gut feelings about gearing.
- Impact: Legged robots, arms, and exoskeletons can compare very different actuators on one FoM instead of topology or ratio dogma.
- Watch next: Better gearbox technologies, integrated liquid cooling, and standardized FoM benchmarks across vendors to close the gap between theory and deployed robots.
