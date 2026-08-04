# Lore – Open source version control system designed for scalability

- Score: 918 | [HN](https://news.ycombinator.com/item?id=48571081) | Link: https://lore.org/

### TL;DR

Epic Games has open-sourced Lore, an MIT-licensed centralized version-control system built for enormous, binary-heavy projects and mixed developer-artist teams. It stores repository state in Merkle trees and an immutable revision chain, chunks and deduplicates large files, hydrates workspaces on demand, and uses server-side caching plus lightweight branches. HN framed it as a Perforce challenger for game development rather than a general Git replacement. Enthusiasm centers on prospective Unreal integration and prior UEFN use; adoption still depends on production maturity, permissions, locking, tooling, and artist familiarity.

### Comment pulse

- Game workflows expose Git’s mismatch → terabyte-scale binaries, nonmergeable assets, partial checkouts, access controls, and exclusive locks favor centralized systems.
- Perforce is entrenched but vulnerable → Unreal integration and artist familiarity keep it dominant, while cost, administration, aging tooling, and Git LFS pain invite competition.
- Existing deployment history boosts confidence → Lore has versioned UEFN islands and is being adopted for its cook pipeline — counterpoint: broader readiness remains unproven.

### LLM perspective

- **View:** Lore’s advantage is vertical integration: storage architecture, Unreal workflows, and open licensing reinforce one another.
- **Impact:** Game studios gain negotiating leverage and a migration option; Perforce faces pressure on pricing, administration, and integrations.
- **Watch next:** Verify lock and permission semantics, migration tools, Unreal editor support, operational benchmarks, and durable hosting guidance.
