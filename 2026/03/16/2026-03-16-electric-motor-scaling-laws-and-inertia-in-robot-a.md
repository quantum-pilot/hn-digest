# Electric motor scaling laws and inertia in robot actuators

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47350016) | Link: https://robot-daycare.com/posts/actuation_series_1/

### TL;DR

Under first-order scaling, shrinking radius cuts rotor inertia cubically but torque quadratically, so gearing needed to restore output torque exactly cancels the gear ratio’s squared reflected-inertia penalty. In the ideal massless, lossless gearbox model, reflected inertia at fixed torque depends on power dissipation, not motor size or gearing. A normalized motor constant supports cross-size comparison; TQ data stayed within roughly 1.5× for feasible designs despite two orders of magnitude in mass and ratio. HN stressed that real gears, heat, saturation, backdrivability, force sensing, and rotor construction restore practical tradeoffs.

### Comment pulse

- High ratio alone is misleading → smaller rotors reduce inertia dramatically — counterpoint: excessive reduction still hurts backdriving, sensing, efficiency, noise, and cost.
- Cooling is decisive → smaller motors must reject comparable heat through less surface area; liquid cooling adds mass, expense, and reliability concerns.
- Application profiles set optimum gearing → inertial loads favor inertia matching, frictional loads favor loss balancing, and mixed trajectories require simulation.

### LLM perspective

- **View:** The derivation reframes actuator selection around thermal budget and magnetic efficiency rather than reflexively minimizing gear ratio.
- **Impact:** Robot designers can narrow motor families analytically before modeling real transmissions, temperature, duty cycle, and control needs.
- **Watch next:** Gearbox-inclusive benchmarks, transient torque limits, cooling models, custom rotor designs, and comparisons with capstan or remote-actuation systems.
