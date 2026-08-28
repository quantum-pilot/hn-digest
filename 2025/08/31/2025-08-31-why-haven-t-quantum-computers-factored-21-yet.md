# Why haven't quantum computers factored 21 yet?

- Score: 340 | [HN](https://news.ycombinator.com/item?id=45082587) | Link: https://algassert.com/post/2500

### TL;DR

Craig Gidney explains that factoring 21 is not a 25% step beyond factoring 15. His optimized circuit needs 2,405 entangling gates, versus 21 for the famous 15 circuit—a 115× increase. Fifteen is exceptionally cheap because most modular multiplications become multiplication by one, the first multiplication is nearly free, and the remaining operation reduces to swaps. For 21, every multiplication matters and uses expensive Toffoli-heavy circuits. Error correction could multiply the practical resource gap still further.

### Comment pulse

- Claimed demonstrations of factoring 21 often compile in information equivalent to the factors, avoiding the hard modular multiplications.
- Post-quantum migration is prudent despite uncertain timelines because recorded traffic could become readable after future key-exchange breakthroughs.
- The author cited an estimate of seven billion Toffoli gates and roughly one million physical qubits for RSA-2048 under stated assumptions.

### LLM perspective

- View: Fifteen is a pathological benchmark whose arithmetic structure conceals the scaling cost of genuine quantum factoring.
- Impact: Progress assessments should emphasize error correction and scalable architectures rather than tiny factoring records.
- Watch next: Surface-code error suppression, logical-gate fidelity, sustained operation counts, and replaceable neutral-atom architectures.
