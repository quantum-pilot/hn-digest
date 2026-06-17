# Correlated randomness in Slay the Spire 2

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48552844) | Link: https://tck.mn/blog/correlated-randomness-sts2/

### TL;DR
Slay the Spire 2 tries to keep different kinds of randomness separate by using many RNG instances, each seeded as `seed + hash("label")`. But C#’s `System.Random` is effectively linear in its seed, so these streams are strongly correlated. Knowing one “random” outcome (Neow relic, Act 1, first potion/gold drop, events) heavily constrains others, causing big biases: Neow’s Bones often gives Debt, Trash Heap never rolls Rebound, potion drops differ wildly by Act. The fix: use a modern, nonlinear game-local PRNG.

---

### Comment pulse
- Gameplay RNG should be custom-owned, not stdlib → guarantees cross-platform determinism, stable seeds, serializable state, and avoids future library or platform changes.  
- Procgen demands strict control over all inputs → tiny nondeterminism or hardware quirks can break reproducibility, especially on platforms like freestanding WebAssembly.  
- Godot’s GDScript RNG already uses PCG32 → irony that StS2 hit this by using C# System.Random instead—counterpoint: swapping RNG stacks in shipped code isn’t free.

---

### LLM perspective
- View: Clear study of PRNG choice leaking into design, balance, player perception, even when neither players nor devs intend it.  
- Impact: Fixing this will change relic/card frequencies, event odds, Compendium completion; serious players’ routing heuristics and guides will need updates.  
- Watch next: Watch for Mega Crit patch notes replacing System.Random, seed regression tests, and community tools checking that cross-RNG correlations truly vanish.
