# A faster way to calculate the day of the week

- Score: 244 | [HN](https://news.ycombinator.com/item?id=49323795) | Link: https://www.benjoffe.com/fast-day-of-week

### TL;DR

Ben Joffe derives multiply-add-shift algorithms that convert a signed day count to a weekday faster than conventional modulo-seven code. Restricted-range and full 32-bit variants exploit seven’s Mersenne structure, parallel processor operations, and output rotation; ISO numbering costs no extra instructions. His benchmarks show substantial gains on AMD, Apple, Intel, and Raspberry Pi hardware, with compiler-dependent tradeoffs between latency and throughput. Commenters admired the interactive explanation while debating practical hot paths, citing finance and bulk timestamp formatting as plausible uses.

### Comment pulse

- Readers praised the visualizations and configurable function explorer → the presentation made unusually dense bit arithmetic understandable.
- Practicality drew skepticism → weekday calculation rarely dominates applications; finance and mass timestamp formatting were offered as counterexamples.
- Discussion also favored mental-calendar tricks and noted that real life often requires navigating several cultural or financial calendars.

### LLM perspective

- View: This is rigorous niche optimization whose value depends on measured hot paths and clearly documented integer assumptions.
- Impact: Date libraries and database engines could reduce scalar latency without changing their public calendar semantics.
- Watch next: Independent benchmarks, compiler code generation, wider SIMD tests, library adoption, and regression coverage across supported ranges.
