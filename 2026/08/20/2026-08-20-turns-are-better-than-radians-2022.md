# Turns are Better than Radians (2022)

- Score: 332 | [HN](https://news.ycombinator.com/item?id=49369408) | Link: https://www.computerenhance.com/p/turns-are-better-than-radians

### TL;DR

Casey Muratori argues that graphics and game code should often represent angles as turns—zero to one per circle—and expose turn-based trigonometry, avoiding a caller’s multiplication by tau that fast sine implementations soon cancel during range reduction. Binary fractions exactly represent quarter, half, and three-quarter turns, improving common-angle precision; existing `sincospi` functions offer half-turns. He suggests radian wrappers for legacy callers. Commenters narrowed the claim: turns suit periodic phases, but radians keep Euler identities, derivatives, Taylor series, and differential equations free of repeated 2π factors; dual interfaces may be best.

### Comment pulse

- Calculus objections emphasized simple derivatives and Euler’s formula; replies scoped turns to numerical code, not symbolic mathematics.
- Application-dependent advocates favored turns for phase accumulators and radians for optimization, small-angle approximations, or geodesy.
- An alternative stores sine-cosine pairs or half-angle tangents, reducing trig calls but introducing representation and API complications.

### LLM perspective

- View: Angle representation should follow workload semantics rather than become another universal convention.
- Impact: Graphics-style code may gain exact common phases and fewer conversions; calculus-heavy systems retain radians.
- Watch next: Cross-library speed and error benchmarks, dual APIs, explicit types, and conversion-boundary mistakes.
