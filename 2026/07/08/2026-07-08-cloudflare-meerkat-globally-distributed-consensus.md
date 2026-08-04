# Cloudflare Meerkat - Globally distributed consensus

- Score: 202 | [HN](https://news.ycombinator.com/item?id=48831565) | Link: https://blog.cloudflare.com/meerkat-introduction/

### TL;DR

Cloudflare’s experimental Meerkat implements QuePaxa for globally shared control-plane state and is not yet in production. Unlike Raft, any replica can drive a proposal; an optional leader only reduces round trips, so failed or slow leaders and election timeouts do not halt progress while a majority communicates. It provides linearizable operations, but consistent reads also enter the log and non-leader proposals typically need three wide-area round trips. HN valued its unstable-network promise but noted Cloudflare is operationalizing, not inventing, QuePaxa; concerns include niche applicability, implementation complexity, and tail latency.

### Comment pulse

- The novelty is timeout-free liveness under variable delay → QuePaxa may keep progressing where Raft elections flap — counterpoint: normal-case performance remains unproven.
- Linearizability is bought with consensus-ordered reads → this simplifies semantics but imposes WAN latency, confining Meerkat to infrequently changed control-plane state.
- Failure may shift from outages to long tails → abandoned and retried requests can later succeed, complicating client idempotency and outcome tracking.

### LLM perspective

- **View:** Meerkat trades election outages for coordination latency and uncertain completions; it changes the failure shape rather than eliminating failure.
- **Impact:** For globally sparse control-plane writes, continuous majority progress can matter more than low median latency or local reads.
- **Watch next:** Production rollout, p99 latency, ambiguous completions, replica placement, formal verification, simulation findings, and recovery after partitions.
