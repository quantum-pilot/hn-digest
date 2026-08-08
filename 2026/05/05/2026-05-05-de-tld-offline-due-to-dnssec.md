# .de TLD offline due to DNSSEC?

- Score: 490 | [HN](https://news.ycombinator.com/item?id=48027897) | Link: https://dnssec-analyzer.verisignlabs.com/nic.de

### TL;DR

A transient .de failure appears to have been DNSSEC validation, not an authoritative-server outage. Commenters observed intact zone data but a malformed signature over an NSEC3 record under zone-signing key 33834. Direct authoritative queries, or recursive queries with checking disabled, still worked; validating resolvers correctly returned SERVFAIL for .de names. Intermittent success suggested anycast instances were serving mixed old and new signatures, consistent with a botched key rollover. The supplied debugger snapshot later showed valid chains for the root, .de, and nic.de, indicating recovery had propagated.

### Comment pulse

- The incident exposed national-scale blast radius — counterpoint: DNS already assigns each TLD one operator; DNSSEC authenticates that hierarchy.
- Timing raised an on-call concern: emergency rollback authority must remain available when key operators attend the same social event.
- Critics cited prior DNSSEC outages, while defenders stressed that only .de failed and forged answers remained rejected.

### LLM perspective

- Key rollovers need staged validation from diverse networks plus automated rollback on signature failure.
- Mixed anycast state complicates diagnosis; fleet-wide telemetry should expose which instances serve each zone version.
- Watch DENIC’s postmortem for trigger, monitoring gaps, cache duration, rollback timing, and recurrence controls.
