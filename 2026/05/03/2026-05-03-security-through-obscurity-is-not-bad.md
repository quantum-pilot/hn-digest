# Security through obscurity is not bad

- Score: 109 | [HN](https://news.ycombinator.com/item?id=47997486) | Link: https://mobeigi.com/blog/security/security-through-obscurity-is-not-bad/

### TL;DR

Mo Beigi argues that obscurity is useful atop sound controls: it cannot stop a determined attacker, but can raise the cost of commodity exploitation. His examples include a randomized WordPress table prefix defeating a stock SQL-injection script, stripped CS:GO debug symbols slowing cheat developers, and obfuscation protecting browser and anti-cheat logic. Even an LLM needed 4.5 hours, 72 million tokens, and about $300 to solve one CTF challenge. HN accepted delay as valuable but warned that automation erodes it and obscurity breeds false confidence, maintenance costs, and weaker primary defenses.

### Comment pulse

- Obscurity resembles concealment, not cover → it can prevent targeting, but offers no protection once an attacker finds the weakness.
- Attack friction may redirect commodity scanners → counterpoint: tireless automation increasingly makes unusual ports, names, and code transformations cheap to probe.
- Low-value data is safest when never collected → minimizing assets reduces breach impact without adding brittle, confusing layers.

### LLM perspective

- **View:** Obscurity is best evaluated as attacker-cost inflation, not as a correctness or confidentiality guarantee.
- **Impact:** Defenders should budget it only after controls, recovery plans, and data minimization are demonstrably adequate.
- **Watch next:** Measured attacker delay, operational overhead, AI deobfuscation costs, incident outcomes, and whether obscurity causes control gaps.
