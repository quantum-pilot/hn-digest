# UUID package coming to Go standard library

- Score: 342 | [HN](https://news.ycombinator.com/item?id=47283665) | Link: https://github.com/golang/go/issues/62026

### TL;DR
Go is standardizing UUID support, adding a first‑party type and generators (notably v4 and v7) aligned with RFC 9562. The design treats UUIDs as opaque 16‑byte values with secure randomness, a `New` convenience constructor, parsing/string support, and comparison helpers, while avoiding version‑specific methods. Debate focuses on whether `New` should always be v4, how much parsing/format flexibility to expose given “opacity” guidance, and whether to add more advanced v7 features (monotonic counters, generators) without bloating the API.

---

### Comment pulse
- Version choice is contextual → v4 still favored for random, privacy‑preserving IDs; v7 preferred when index locality/ordering matters—counterpoint: any standardized UUID can fail some app requirements.  
- Stdlib UUID type matters most → shared type that implements JSON/Text/db interfaces will de‑duplicate google/uuid and unify ecosystem; similar desire expressed for a standard dec128.  
- Go’s pace is praised → many like small, boring, compatible additions while UUID specs churn; others worry about locking Go into a premature, hard‑to‑change UUID policy.

---

### LLM perspective
- View: This mostly canonizes existing practice; the hard part is API minimalism vs future‑proofing around version semantics and parsing.  
- Impact: Libraries, ORMs, and services converge on one UUID type, simplifying interoperability, migrations, and security audits.  
- Watch next: Final placement (crypto/uuid vs crypto/rand helpers), v7 monotonicity/counter strategy, and guarantees around `New`’s behavior over Go releases.
