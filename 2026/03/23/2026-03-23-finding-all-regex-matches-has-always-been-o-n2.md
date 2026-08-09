# Finding all regex matches has always been O(n²)

- Score: 143 | [HN](https://news.ycombinator.com/item?id=47443903) | Link: https://iev.ee/blog/the-quadratic-problem-nobody-fixed/

### TL;DR

Many linear-time regex engines become quadratic when finding leftmost-longest matches: at each position, a failing long alternative can rescan the remaining input before a short alternative succeeds. RE# instead uses a reverse pass to mark starts and a forward pass to resolve endings. Its opt-in hardened mode keeps all-match semantics in O(n×S), where S is active DFA states, but costs roughly 3–20× on text and currently rejects lookarounds. HN notes practical patterns often have clear boundaries and cites NFA engines that appear linear, challenging the universal claim.

### Comment pulse

- The pathology is distinct from exponential backtracking → even DFA-style repeated search can revisit suffixes once per reported match.
- Sandboxing arbitrary patterns limits time and memory — counterpoint: feature restrictions and hardened algorithms can provide stronger predictable guarantees.
- bablr/regex and nim-regex reportedly scale linearly in examples → RE#’s first-engine claim needs comparison across semantics, captures, and memory use.

### LLM perspective

- **View:** The contribution is preserving leftmost-longest output under adversarial iteration, not merely avoiding backtracking.
- **Impact:** Log search and extraction can avoid silent quadratic latency; common workloads may prefer the faster unhardened path.
- **Watch next:** Independent benchmarks, proof scope, capture groups, lookaround support, automatic hardening inference, streaming, and NFA comparisons.
