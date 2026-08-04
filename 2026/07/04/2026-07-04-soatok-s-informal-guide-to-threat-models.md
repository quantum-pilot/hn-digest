# Soatok's Informal Guide to Threat Models

- Score: 121 | [HN](https://news.ycombinator.com/item?id=48781597) | Link: https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/

### TL;DR

A useful threat model names protected assets, adversaries, attack paths, and mitigations, then adds the pieces checklists miss: asset relationships, explicit assumptions, and threats deliberately left open. The guide recommends graphing a system, recursively narrowing into components and data flows, and labeling risks prevented, mitigated, addressable, or open; the document must evolve with the system. Examples cover passkeys, decentralized messaging, and post-quantum choices. HN praised the assumptions-first framing but disputed how much formalization reduces subjectivity, how living models stay current, and whether post-quantum hybrids hedge the right risks.

### Comment pulse

- Living documents are operationally hard → commenters wanted mechanisms for updating assumptions as architectures, dependencies, adversaries, and environments evolve.
- Formalization does not create objectivity → identifying assets and actors exposes variables but cannot prove a scenario reasonable, legitimate, or likely.
- Post-quantum hedging stayed contested → commenters raised a never-arriving Q-Day and pre-Q-Day ML-KEM breaks — counterpoint: the author still favors preparing now.

### LLM perspective

- **View:** Threat modeling is architecture under uncertainty: its value comes from documented boundaries and assumptions, not exhaustive attack enumeration.
- **Impact:** Teams gain earlier design leverage by removing dangerous relationships before compensating controls and operational complexity accumulate.
- **Watch next:** Version models with architecture, assign assumption owners, link risks to tests, and revisit accepted threats after system changes.
