# Show HN: I made a calculator that works over disjoint sets of intervals

- Score: 288 | [HN](https://news.ycombinator.com/item?id=47812341) | Link: https://victorpoughon.github.io/interval-calculator/

- TL;DR  
  - A web calculator implements interval union arithmetic, where values are unions of disjoint closed intervals rather than single numbers. Using the inclusion property with outward rounding, it guarantees that evaluating any compatible real inputs always yields a result inside the computed union, even around discontinuities or division by intervals containing zero. It supports many functions, unions, and nested intervals, and a full‑precision mode. Discussion centers on standards (IEEE 1788), multi‑valued functions, interval notation, and related interval‑based visualization tools.

- Comment pulse  
  - Interval unions praised for inclusion property → guarantees any choice of real inputs maps into output union; enables true inverse‑square, robust uncertainty propagation.  
  - Ecosystem references → readers link implicit‑surface renderers, graphing calculators, and language libraries that also exploit interval arithmetic for correctness and pruning.  
  - Semantics and notation questions → desire for open intervals, many‑valued inverses, clearer brackets—counterpoint: author restricts to closed intervals to avoid major complexity.

- LLM perspective  
  - View: Interval‑union calculators make set‑based numerics tangible, bridging constraint solving and everyday computation directly in the browser.  
  - Impact: Strong fit for spreadsheets, safety‑critical simulations, testing numeric code, and teaching floating‑point quirks and discontinuities.  
  - Watch next: Compare against IEEE‑1788 libraries, add open intervals and multi‑valued functions, and publish benchmarks for performance and interval over‑widening.
