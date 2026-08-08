# Can LLMs model real-world systems in TLA+?

- Score: 117 | [HN](https://news.ycombinator.com/item?id=48065254) | Link: https://www.sigops.org/2026/can-llms-model-real-world-systems-in-tla/

### TL;DR

SysMoBench tests whether LLM-generated TLA+ specifications model actual implementations rather than recite textbook protocols. Across eleven concurrent and distributed systems, models usually produce valid syntax, yet average about 46% on trace-based conformance and 41% on invariants. Common failures misrepresent data structures or collapse multi-step code into incorrect atomic actions, creating impossible states or omitting real ones. The benchmark checks syntax, execution, transition windows, and properties at action-level granularity. Its limits include trace coverage, lossy state abstraction, and hand-built scaffolding; Specula reportedly aces current tasks.

### Comment pulse

- Practitioners say liveness properties remain especially hard, and generated models can cause state-space explosions without close guidance.
- “Looks passable” drew skepticism: superficial plausibility is precisely the failure mode formal verification should expose.
- Some favor implementation-coupled verification such as Verus — counterpoint: TLA+ deliberately prioritizes readable specifications and refinement over executable models.

### LLM perspective

- Held-out implementations and contamination-resistant tasks matter because public protocol specifications invite memorization.
- Counterexample-guided agents could use failed transition windows as localized repair signals.
- The hardest evaluation dependency is human-authored abstraction: a flawed harness can certify the wrong semantics.
