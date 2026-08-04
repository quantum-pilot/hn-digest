# Correlated randomness in Slay the Spire 2

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48552844) | Link: https://tck.mn/blog/correlated-randomness-sts2/

### TL;DR

Slay the Spire 2 creates separate RNG streams by adding fixed hashes to one run seed, but C#’s System.Random initializes nearly linearly from that seed, making their outputs correlated and predictable. Consequences include Neow’s Bones yielding Debt about 54% of the time in Underdocks, Rebound being unobtainable from Trash Heap in single-player, and first-fight potion rates differing 76% versus 4% by Act 1 variant. The author proposes PCG32; HN treated deterministic procedural-generation machinery as gameplay code, not a mutable platform dependency.

### Comment pulse

- Testing should expose biased streams → commenters expected large simulations and per-action metrics to detect inadequate shuffling or unexplained correlations.
- Determinism invites worst-case analysis → commenters wondered whether time-seeded games could produce prolonged unwinnable periods, echoing known impossible seeds.
- The engine already offers an alternative → Godot’s GDScript RNG reportedly uses PCG32, avoiding this specific System.Random failure mode.

### LLM perspective

- **View:** Independent streams require domain separation through a mixing function, not merely seed offsets fed into a linear initializer.
- **Impact:** Hidden correlation changes balance, strategy, unlockability, and competitive seed analysis even for players unaware of the bug.
- **Watch next:** Verify Mega Crit’s patch with distribution tests, compendium completion, seed compatibility, and correlations across successive RNG calls.
