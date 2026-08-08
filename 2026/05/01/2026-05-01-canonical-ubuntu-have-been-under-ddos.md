# Canonical/Ubuntu have been under DDoS

- Score: 160 | [HN](https://news.ycombinator.com/item?id=47972213) | Link: https://status.canonical.com/#/incident/KNms6QK9ewuzz-7xUsPsNylV20jEt5kyKsd8A-3ptQEHpOd8VQ40ZQs-KD81fboQXeGZB94okNHdHBGlCv58Sw==

### TL;DR

Canonical’s status page recorded a resolved major outage lasting 20 hours, 9 minutes, and 46 seconds, from April 30 at 18:33 CEST to May 1 at 14:43. A broad set of Ubuntu and Canonical services was affected, including package archives, PPAs, Launchpad, security notices and CVEs, Livepatch, login, Landscape, keyservers, MAAS images, and websites. The status text supplies no cause. Commenters debated simultaneous update demand around copy.fail versus a deliberate campaign reportedly encouraged by a pro-Iran group.

### Comment pulse

- “Agent pickup” could create synchronized infrastructure spikes when many automated systems react to releases or vulnerabilities simultaneously.
- Users reported intermittent package-site slowness before this incident, suggesting capacity or attack pressure may predate the headline outage.
- Speculation that attackers blocked patches remained unproven — counterpoint: affected update and Livepatch services made the theory intuitively concerning.

### LLM perspective

- Post-incident reporting should separate traffic volume, attack signatures, and organic update demand.
- Package ecosystems need geographically diverse mirrors and graceful degradation for security metadata.
- Agent clients should add jitter, caching, backoff, and coordinated rate limits.
