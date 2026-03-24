# Finding all regex matches has always been O(n²)

- Score: 143 | [HN](https://news.ycombinator.com/item?id=47443903) | Link: https://iev.ee/blog/the-quadratic-problem-nobody-fixed/

### TL;DR
Modern “linear-time” regex engines (RE2, Rust `regex`, .NET non-backtracking, etc.) are only linear for a single match. When you iterate to find *all* non-overlapping matches, the standard “find, advance, repeat” loop can become Θ(m·n²) in the worst case (e.g., `.*a|b` over long `b…b`), even for DFA-based engines. Ian Varatalu’s RE# fixes this by using a reverse pass to mark possible start positions and a forward pass to resolve leftmost-longest matches, plus an optional hardened mode that guarantees true linear time without changing semantics, at a constant-factor cost. RE# also competes with Aho–Corasick and Rust’s `regex` on throughput, but currently omits capture groups and lazy quantifiers.

---

### Comment pulse
- Alternative NFAs (bablr, nim-regex) claim linear-time all-matches → avoid quadratic behavior, but trade throughput for memory and complexity; often unsuitable for huge inputs.  
- Safety via sandboxing → cap time/memory and abort misbehaving regexes; author counters that semantics-preserving algorithms can often avoid needing such coarse controls.  
- “Real” regexes rarely hit worst-case → practical patterns have clear boundaries; author replies backtracking still frequently explodes without strong anchors or rare prefixes.

---

### LLM perspective
- View: RE# demonstrates that full leftmost-longest, all-matches linearity is attainable, challenging long-standing assumptions in both theory and libraries.  
- Impact: Most relevant to log search, security scanning, and tools executing untrusted patterns at scale or in latency-sensitive paths.  
- Watch next: Wider benchmarks, language bindings, capture-group design, and whether mainstream engines adopt two-pass or hardened modes.
