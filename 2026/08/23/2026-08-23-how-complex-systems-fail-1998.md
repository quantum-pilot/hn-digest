# How Complex Systems Fail (1998)

- Score: 211 | [HN](https://news.ycombinator.com/item?id=49409473) | Link: https://how.complexsystems.fail/

### TL;DR

Richard Cook’s 1998 treatise argues that hazardous complex systems normally operate with shifting latent defects, held together by layered defenses and practitioners’ continual adaptation. Catastrophes emerge when multiple small failures align, so isolating one root cause and blaming sharp-end operators distorts how accidents occur. Hindsight hides the uncertainty and production pressures present before failure; technological fixes can introduce new rare hazards. Safety is therefore an emergent, changing system property built through human expertise and calibrated exposure to failure. Commenters applied this framework to software resilience, incident analysis, and chaos engineering.

### Comment pulse

- Literal single-root analysis is misleading → defenders say properly practiced RCA already traces multiple contributors and asks what system changes are warranted.
- Complex systems always degrade locally → robust orchestration and operator adaptation keep component failures from becoming catastrophe.
- Controlled failure builds operational knowledge → counterpoint: safety-critical domains cannot freely experiment where real failures hospitalize or kill people.

### LLM perspective

- View: The essay redirects investigation from blame toward interactions, incentives, defenses, and locally rational decisions under uncertainty.
- Impact: Operators become sources of resilience and evidence, not merely error generators; organizations must examine conditions shaping their tradeoffs.
- Watch next: Track near misses, test recovery paths, preserve operational context, and evaluate whether fixes reduce risk without adding coupling.
