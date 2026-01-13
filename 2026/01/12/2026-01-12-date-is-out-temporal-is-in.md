# Date is out, Temporal is in

- Score: 290 | [HN](https://news.ycombinator.com/item?id=46589658) | Link: https://piccalil.li/blog/date-is-out-and-temporal-is-in/

### TL;DR
The article argues that JavaScript’s `Date` is a decades‑old mess: inconsistent parsing rules, timezone surprises, and—more subtly—mutable objects representing conceptually immutable dates. It introduces `Temporal`, a new namespace-based API that separates concerns (plain dates vs instants vs time‑zoned datetimes), returns new objects instead of mutating, and uses explicit, readable operations like `add({ days: 1 })`. `Temporal` is at TC39 stage 3 and already in modern browsers, so developers are encouraged to experiment while `Date` slowly recedes into legacy status.

---

### Comment pulse
- ISO 8601 parsing bug → `YYYY-MM-DD` is treated as UTC against the spec; an attempted fix was reverted for web compatibility.  
- Mutability complaint → some see object mutability as minor versus parsing/timezone bugs — counterpoint: shared mutable dates cause subtle, non‑local bugs.  
- Scope gaps → Temporal ignores leap seconds and assumes POSIX time; also, article sidesteps `Date.now()`, whose raw timestamp still needs safe formatting.  

---

### LLM perspective
- View: Treat Temporal as the default for new code; confine `Date` to legacy interfaces and minimal interop shims.  
- Impact: Date/time libraries, logging, scheduling, and cross‑timezone apps gain safer, clearer semantics and fewer off‑by‑one surprises.  
- Watch next: Standardization to stage 4, polyfill maturity, and browser tooling (devtools, linters) nudging migration away from `Date`.
