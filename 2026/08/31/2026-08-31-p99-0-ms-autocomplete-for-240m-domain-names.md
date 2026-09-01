# P99 0 ms* autocomplete for 240M domain names

- Score: 220 | [HN](https://news.ycombinator.com/item?id=49505219) | Link: https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names

### TL;DR

Wirewiki claims perceived p99 autocomplete latency of zero milliseconds by prefetching every possible next-character result on keydown, then rendering cached suggestions on keyup. The author's measured p99 typing budget was 121 ms. A memory trie covers the top million domains; a 2.5 GB memory-mapped, delta-compressed block index searches 240 million more. Server processing was usually a few milliseconds, leaving network distance dominant. Commenters questioned keyup semantics, remote-region performance, and fallback suggestions that append common suffixes to nonexistent domains.

### Comment pulse

- Predictive prefetch hides network work inside typing time → compressed responses remain around 2.5 kB despite branching across valid characters.
- “Zero” measures readiness after key release → users farther from the European server still reported noticeable latency.
- Fallback suffixes increase coverage → counterpoint: suggesting unregistered domains can defeat typo prevention and confuse users.

### LLM perspective

- View: The strongest optimization is redefining when work begins, then matching storage to prefix-access patterns.
- Impact: Search interfaces can feel immediate without exotic servers, but bandwidth and semantic quality become deliberate tradeoffs.
- Watch next: Test input events, global percentiles, cache hit rates, real-domain precision, accessibility, and user-perceived timing.
