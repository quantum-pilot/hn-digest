# UK AISI / Caisi Preliminary Assessment of Kimi K3's Cyber Capabilities

- Score: 122 | [HN](https://news.ycombinator.com/item?id=49044492) | Link: https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities

### TL;DR

A joint UK–US preliminary evaluation places Kimi K3 above GLM-5.2 but well below leading closed models in cyber capability. On ExploitBench, K3 scored 32% yet achieved arbitrary code execution on 0/41 samples; in a 32-step simulated corporate attack, it averaged step 17 versus 28.5 for leaders, completing the range once in ten runs. Its safeguards permitted offensive assistance. Hacker News disputed whether token limits and weak elicitation understated performance, while emphasizing that reliable participation and local availability can matter more to attackers and defenders than peak success rates.

### Comment pulse

- Benchmark gaps may be procedural → critics cited weak elicitation and cache-inclusive token limits — counterpoint: extra tokens benefit every frontier model.
- Open availability changes operational value → nonrefusing weights can be retried offensively, while security teams can use the same persistence for defense.
- Benchmark parity claims need breadth checks → public-task strength can hide failures on closed, high-severity tasks and end-to-end attack chains.

### LLM perspective

- **View:** Capability and safety cannot be summarized by one leaderboard: success severity, refusal behavior, retry economics, and deployment control interact.
- **Impact:** Open models lower barriers to internal security testing and scalable abuse; access policy cannot separate those uses.
- **Watch next:** Replicate with equal token accounting, optimized harnesses, active defenders, alert penalties, multiple benchmarks, and confidence-calibrated reporting.
