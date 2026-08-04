# Show HN: High-Res Neural Cellular Automata

- Score: 183 | [HN](https://news.ycombinator.com/item?id=48567877) | Link: https://cells2pixels.github.io/

### TL;DR

This SIGGRAPH project scales neural cellular automata by evolving a coarse lattice, then using a lightweight Local Pattern Producing Network to decode interpolated cell states plus local coordinates into high-resolution color and surface properties. Joint training and local computation support arbitrary-resolution, real-time output across 2D, 3D, and mesh domains while preserving growth and repair dynamics. HN found the biological analogy compelling but provisional: regeneration emerged without damage training and can collapse when central regions are heavily erased; commenters also distinguished the method from coordinate-based texture lookup and questioned practical applications.

### Comment pulse

- Repair is emergent, not guaranteed → training included growth from a center seed but no erasure examples, leaving central damage especially destabilizing.
- This is not pixel retrieval → local rules synthesize a changing pattern without global lookup; authors say weights are roughly 3× smaller than JPEG textures.
- Self-healing systems remain speculative → commenters imagined bio-inspired cluster recovery — counterpoint: the model resembles living cells only loosely and lacks demonstrated infrastructure use.

### LLM perspective

- **View:** Separating low-resolution state evolution from continuous local decoding attacks both communication depth and rendering cost without discarding locality.
- **Impact:** Graphics researchers gain resolution-independent procedural textures and materials; robotics or distributed-systems benefits remain analogies, not validated transfers.
- **Watch next:** Benchmark recovery by damage location, decoder scale, temporal stability, memory, frame rate, mesh complexity, and unseen target generalization.
