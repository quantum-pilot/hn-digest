# Show HN: I made a calculator that works over disjoint sets of intervals

- Score: 288 | [HN](https://news.ycombinator.com/item?id=47812341) | Link: https://victorpoughon.github.io/interval-calculator/

### TL;DR

This open-source calculator evaluates expressions over unions of closed, disjoint intervals rather than single numbers. Interval-union arithmetic preserves an inclusion guarantee: every result from choosing real inputs within the supplied sets lies inside the reported output. Unlike ordinary interval arithmetic, it remains closed when division crosses zero and can return separated ranges for inverse or discontinuous functions. Full-precision mode uses outward IEEE 754 rounding to contain the mathematically exact answer. Commenters suggested graphing, many-valued functions, open endpoints, and comparisons with standardized interval arithmetic.

### Comment pulse

- The author emphasizes uncertainty propagation and inverse operations as richer uses than merely correcting floating-point error.
- Related projects apply interval methods to implicit-surface optimization, graphing, and language-native range abstractions.
- Closed intervals keep implementation manageable — counterpoint: open endpoints would express infinities and excluded boundary values more precisely.

### LLM perspective

- Add property-based tests comparing sampled real evaluations against reported unions.
- Separate input rounding from display precision so users can control semantics independently.
- Watch support for intersection, empty sets, reusable results, and periodic inverse-function families.
