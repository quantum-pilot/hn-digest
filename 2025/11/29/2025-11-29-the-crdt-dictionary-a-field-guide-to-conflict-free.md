# The CRDT Dictionary: A Field Guide to Conflict-Free Replicated Data Types

- Score: 150 | [HN](https://news.ycombinator.com/item?id=46087022) | Link: https://www.iankduncan.com/engineering/2025-11-27-crdt-dictionary/

### TL;DR
The article is a hands-on “field guide” to CRDTs: data structures that let many replicas accept writes independently and still converge without consensus protocols. It builds intuition from lattices and the three merge laws (associative, commutative, idempotent), then systematically walks through common CRDT families: counters (G-/PN-), sets (G-, 2P-, LWW-, OR-), registers (LWW, MV), maps, sequences (RGA, WOOT, Logoot/LSEQ), trees, and delta-CRDTs. It closes on the real pain point: garbage-collecting ever-growing metadata safely.

---

### Comment pulse
- High-level CRDT systems like Automerge and Triplit provide “collaborative deep data structures” with formal proofs, hiding most low-level CRDT complexity from app developers.  
- CRDTs mainly remove structural/replica-level conflicts; application-specific semantic conflicts (e.g., two users both “approve”) still need resolution in business logic — counterpoint: that’s usually desirable separation of concerns.  
- Some builders report switching from CRDTs to ID-based OT frameworks (e.g., Docnode) because of CRDT tradeoffs in space, complexity, and GC, especially when a central server is acceptable.

---

### LLM perspective
- View: Treat CRDTs as a toolbox; start from your UX and failure model, then choose the simplest CRDT composition that fits.  
- Impact: Best suited for offline-first, real-time collaboration, and multi-master systems where consensus latency or availability costs are unacceptable.  
- Watch next: Benchmark end-to-end systems (Automerge, Yjs, Triplit) on large docs, long-lived tombstones, and realistic mobile offline patterns.
