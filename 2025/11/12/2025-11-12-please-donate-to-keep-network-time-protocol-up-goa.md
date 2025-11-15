# Please donate to keep Network Time Protocol up – Goal 1k

- Score: 305 | [HN](https://news.ycombinator.com/item?id=45897457) | Link: https://www.ntp.org/

- TL;DR
  - The NTP Project, via Network Time Foundation, is fundraising toward an $8k 2025 goal to maintain the reference NTP implementation and related R&D for critical timekeeping. HN notes the submission title misled many into thinking the NTP Pool would go down; this is about the project, not the pool. Discussion split between “donate or run servers” advice, the shift toward chrony/ntpsec or in-house clients, and frustration with flaky donation UX/progress indicators.

- Comment pulse
  - Misinformation: Not NTP pool; it's NTP Project/Network Time Foundation; title misled readers; bar/goal glitches and CAPTCHA blocked donations — counterpoint: submitter likely erred, not malice.
  - Contribution alternative: Run NTP pool servers; learn ops; cheap to host; but UDP amplification risk and provider complaints exist — counterpoint: many run with filtering.
  - Funding context: Reference NTPd now eclipsed by chrony/ntpsec and in-house; lacks leap-smear; yet time infra remains underfunded; some distrust ntpsec’s claims.

- LLM perspective
  - View: Modest funding makes sense; also encourage contributing pool servers; fix messaging to avoid confusing NTP pool with NTP Project.
  - Impact: chrony dominance reduces NTPd’s footprint, but reference work still anchors standards, interop, and coordinated security fixes.
  - Watch next: Fix donation UX, publish clear finances and metrics; shared roadmap across ntpd/chrony/ntpsec; pool anti-amplification guidance and audits.
