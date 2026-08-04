# The Computer at the Bottom of a Canal

- Score: 139 | [HN](https://news.ycombinator.com/item?id=48956231) | Link: https://negroniventurestudios.com/2026/07/18/the-computer-at-the-bottom-of-a-canal/

### TL;DR

In the 1980s, Linn Products built Rekursiv, a custom object-oriented processor whose hardware enforced types and bounds, relocated and garbage-collected objects, unified memory with persistent disk storage, and accepted loadable language-specific instruction sets. It arrived as RISC workstations and commodity CPUs rapidly overtook bespoke designs; only about 20–30 boards existed, and one engineer dumped his hardware in a canal after resigning. The author argues its concepts resurfaced in CHERI-style capabilities, specialized accelerators, persistent stores, and GC research—but its enduring lesson is to preserve semantics above replaceable silicon.

### Comment pulse

- Historians challenged the novelty framing → capability, tagged, and object-oriented machines were active research traditions, constrained chiefly by integration, cache, and pin economics.
- Readers accepted the timing thesis → Rekursiv’s team was technically bold but lost to Moore’s Law, echoing recurring centralized-versus-distributed technology cycles.
- The revival case remained open → commenters noted capability systems never vanished and still ship, but offered little evidence that bespoke silicon now wins economically.

### LLM perspective

- **View:** Rekursiv bundled established ideas coherently, but froze its abstractions into hardware during extreme commodity acceleration.
- **Impact:** Modern tooling improves prototyping economics, yet specialization pays only when workload durability and volume outrun process-node and ecosystem obsolescence.
- **Watch next:** Separate historical analogy from investment proof: track tape-out cost, software portability, compiler behavior, market size, and upgrade paths.
