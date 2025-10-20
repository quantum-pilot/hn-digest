# RFCs: Blueprints of the Internet

- Score: 108 | [HN](https://news.ycombinator.com/item?id=45634678) | Link: https://ackreq.github.io/posts/what-are-rfcs/

- TL;DR
  - Explains RFCs—numbered, archival specifications begun in 1969 by Steve Crocker to coordinate ARPANET—now maintained by the IETF as the Internet’s canonical standards. Covers what RFCs are, how to find/read them (RFC Editor/Datatracker), requirement keywords (RFC 2119), permanence/versioning, and April Fools RFCs. Argues engineers should implement from RFCs for reliability and interoperability. HN adds Jon Postel’s pivotal RFC-editor role, corrects the “nuclear‑survivable ARPANET” myth, shares tributes (RFC 2468) and memories, and debates “forgotten” vs. overshadowed by proprietary stacks—while urging building a protocol straight from the spec.

- Comment pulse
  - ARPANET wasn’t built to survive nuclear attack → early packets-switching resilience came from RAND/Paul Baran; ARPA’s goal was researcher sharing — counterpoint: myth persisted via early papers.
  - Jon Postel’s stewardship made RFCs work → remembered through RFC 2468; insiders say omitting him understates how the series stayed coherent.
  - Are RFCs forgotten? → some cite vendor lock‑in and walled gardens; others use and cite RFCs weekly and advocate implementing a protocol directly from the spec.

- LLM perspective
  - View: Treat RFCs as single source of truth; implement first from spec, then test interoperability against reference servers/clients.
  - Impact: Stronger protocol literacy reduces vendor lock‑in and brittle integrations; benefits open-source stacks, infra teams, and security reviewers.
  - Watch next: Watch IETF evolutions: QUIC/HTTP‑3 maturity, DNS privacy (DoH/DoT) adoption, and tooling that aids conformance testing and RFC errata tracking.
