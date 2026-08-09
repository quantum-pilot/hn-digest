# The unlikely story of Teardown Multiplayer

- Score: 214 | [HN](https://news.ycombinator.com/item?id=47366435) | Link: https://blog.voxagon.se/2026/03/13/teardown-multiplayer.html

### TL;DR

Teardown’s developers retrofitted multiplayer into a released, moddable, destructible-voxel game after an early bandwidth-heavy prototype failed. Their hybrid architecture replicates structural changes as ordered deterministic commands, while transforms and velocities use per-client prioritized, unreliable state updates capped around 1 Mbit; clients simulate locally and accept corrections. Server-run terminals stream delta-compressed draw commands, and late joiners replay a bounded command history. HN admired the achievement, especially making destruction deterministic years later, while discussion explored floating-point consistency across CPUs and why globally grid-constrained voxel physics produces awkward rotations and collisions.

### Comment pulse

- Cross-platform determinism requires controlling compilers, rounding, NaNs, underflow, and approximate instructions; practitioners disagreed on how restrictive this is.
- Readers called the original game a technical marvel and praised adding determinism to an engine never designed for multiplayer.
- Folding multiplayer into one product preserved the community — counterpoint: sustaining the retrofit may still require new purchases or monetization.

### LLM perspective

- **View:** Selective determinism replicates irreversible structure exactly while allowing transient motion merely to converge.
- **Impact:** Existing players and mod authors gain multiplayer without splitting the installed base.
- **Watch next:** Cross-architecture desync telemetry, late-join limits, snapping under chaos, and lessons transferred to the new engine.
