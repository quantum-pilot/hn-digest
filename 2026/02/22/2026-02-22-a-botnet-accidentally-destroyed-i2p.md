# A Botnet Accidentally Destroyed I2P

- Score: 148 | [HN](https://news.ycombinator.com/item?id=47106985) | Link: https://www.sambent.com/a-botnet-accidentally-destroyed-i2p-the-full-story/

### TL;DR

Kimwolf, an IoT botnet controlling hundreds of thousands of compromised devices, tried to add as many as 700,000 nodes to I2P as backup command-and-control infrastructure. The influx dwarfed I2P’s estimated 15,000–20,000 active devices, overwhelmed legitimate routing, and left the anonymity network operating at about half capacity; operators reportedly admitted the disruption was accidental. HN viewed it as a massive Sybil event but noted the reporting never clearly established whether nodes were malformed, noncompliant, or simply too numerous for a correct implementation.

### Comment pulse

- Decentralization met its hard case → good nodes could not reliably find one another when identities multiplied far beyond normal scale.
- Intent remains ambiguous → Kimwolf sought resilient control channels, not an outage — counterpoint: compromised nodes were still hostile infrastructure.
- Rapid mitigation drew mixed reactions → resilience work is welcome, but adversarial-node floods should be a foundational design assumption.

### LLM perspective

- **View:** Scale alone can become an attack even without protocol violations.
- **Impact:** Small volunteer networks need admission, reputation, and peer-selection defenses that tolerate hostile majorities.
- **Watch next:** I2P release performance, restored capacity, and a technical root-cause analysis.
