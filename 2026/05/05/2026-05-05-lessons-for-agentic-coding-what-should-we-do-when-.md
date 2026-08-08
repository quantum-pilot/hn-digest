# Lessons for Agentic Coding: What should we do when code is cheap?

- Score: 226 | [HN](https://news.ycombinator.com/item?id=48019025) | Link: https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html

### TL;DR

Cheap agent-generated code should change engineering practice, not erase engineering. The author recommends implementing and rebuilding early to learn, anchoring rewrites with end-to-end behavioral tests, documenting intent, keeping specifications synchronized, automating routine work, seeking hard problems, and cultivating domain taste. Agents amplify experienced developers, while every generated line still creates maintenance, support, and security obligations. HN agreed verification becomes the bottleneck but disputed how cheap code truly is: prototypes and small features accelerate dramatically, whereas production systems still demand architecture, stage-gate checks, operational knowledge, and sustained human ownership.

### Comment pulse

- Behavioral tests protect outcomes across rewrites → stage-boundary checks can catch flawed plans and designs before expensive generation and integration cycles.
- Agents raise implementation throughput → teams report better documentation and coverage — counterpoint: subtle errors and unreadable output can transfer work into review.
- Producing code is cheaper than owning it → abandoned repositories, security exposure, support, and complexity preserve long-term cost.

### LLM perspective

- **View:** The scarce resource is trustworthy change: clear intent, fast evidence, and maintainers able to explain decisions.
- **Impact:** Senior judgment becomes more leveraged, while eliminating junior roles risks shrinking the future expertise pipeline.
- **Watch next:** Defect escape rates, maintenance hours, user adoption, security incidents, and rebuild frequency in agent-heavy teams.
