# NIST was 5 μs off UTC after last week's power cut

- Score: 152 | [HN](https://news.ycombinator.com/item?id=46355949) | Link: https://www.jeffgeerling.com/blog/2025/nist-was-5-μs-utc-after-last-weeks-power-cut

### TL;DR

After wildfire-prevention power cuts locked down NIST’s Boulder campus and a generator failed, its main clock ensemble drifted less than five microseconds from UTC before staff rerouted emergency power. NIST kept affected Internet time servers online because public-network delay is typically around a millisecond, making the drift negligible; specialized fiber users required direct attention. Other NIST sites and GPS continuity remained intact. HN called the headline overbroad because only Boulder was affected, while focusing on fiber timing, scientific applications, redundancy, and when silence is safer than uncertain time.

### Comment pulse

- Scope correction → five Boulder servers lost synchronization, not NIST’s entire distributed time service; ordinary clients should use diversified pools.
- Precision users → fiber timing may support distributed experiments, radio telescopes, telecommunications, infrastructure, and positioning integrity more than routine finance.
- Failure semantics → known microsecond drift was tolerable; unknown, worsening clock state could justify shutdown to prevent trusted misinformation.

### LLM perspective

- View: The incident demonstrates graceful degradation, but also how physical access and shared power remain timing-system dependencies.
- Impact: Public NTP users saw no practical error; direct high-precision consumers faced a materially different service condition.
- Watch next: Review generator separation, remote management, cross-building transfer, fiber-service resilience, and non-GPS positioning alternatives.
