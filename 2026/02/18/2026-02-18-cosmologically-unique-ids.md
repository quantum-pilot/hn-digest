# Cosmologically Unique IDs

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47064490) | Link: https://jasonfantl.com/posts/Universal-Unique-IDs/

## TL;DR

The article is a long thought experiment on how to assign truly unique identifiers at “universe scale.” It first shows that random IDs are extremely safe: with 798 random bits you’d expect no collision even if the entire observable universe were turned into an optimal computer doing 10^120 ID-generating operations. It then explores purely deterministic, decentralized tree-based schemes (Dewey-style counters, binary trees, token passing), proving any such scheme has worst‑case linear growth in ID length. Simulations of plausible galactic expansion models suggest deterministic schemes would yield absurdly long IDs (gigabits), so large random IDs remain the only practical “cosmological” solution. HN discussion mainly argues that once you consider causality and locality, the required random-ID size can likely be far smaller than the article’s ultra‑conservative 798‑bit upper bound.

---

## Comment pulse

- Collisions must respect causality → only IDs that can ever interact matter; light-cone limits shrink the effective birthday-paradox population—counterpoint: relativistic travel complicates that boundary.  

- CSPRNGs don’t create entropy → if seeds repeat, streams repeat; “banning” patterns like all‑zeros is unnecessary if randomness is sound.  

- Addressability is storage-bounded → each address consumes particles; as ID length grows, fewer distinct things can be simultaneously named.  

---

## LLM perspective

- View: For any realistic, causally-bounded system, 128-bit UUIDs plus basic collision-handling protocols are already beyond practically necessary.  

- Impact: Distributed-system and database designers should favor simple random IDs; deterministic trees mainly add structure, not safety.  

- Watch next: Models combining light cones, device lifetimes, and storage limits to give tighter, engineering-grade bounds on safe ID sizes.
