# Coding is not solved

- Score: 536 | [HN](https://news.ycombinator.com/item?id=49877988) | Link: https://blog.alexewerlof.com/p/coding-is-not-solved

### TL;DR

The author rejects claims that AI has “solved” coding, arguing that cheap generation addresses only a fraction of production software’s cost. Maintenance, security, reliability, scalability, evolving requirements, and incident response still demand understanding and accountable ownership. LLMs can accelerate low-risk prototypes and constrained transformations, but stochastic output and large diffs complicate review and trust. Commenters split sharply: some say agents can generate exhaustive tests and already handle difficult systems; others report hidden defects, architectural decay, review overload, and amplified output from weak developers.

### Comment pulse

- Production ownership exceeds code generation → engineers must understand business logic, trade-offs, failure modes, and non-functional requirements.
- Agents can broaden verification → proponents cite fuzzing and property tests—counterpoint: generated tests may be shallow and cannot exhaust large state spaces.
- Output volume can overwhelm review → faster generation magnifies technical debt when teams cannot inspect thousands of daily changed lines.

### LLM perspective

- View: Coding is increasingly automated; reliable software ownership remains an organizational and epistemic problem.
- Impact: Teams must price review, maintenance, model costs, and incident recovery into claimed productivity gains.
- Watch next: Longitudinal production studies measuring defects, change latency, architecture quality, total cost, and accountable human comprehension.
