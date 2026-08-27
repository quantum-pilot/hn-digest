# Optimizing a 6502 image decoder, from 70 minutes to 1 minute

- Score: 185 | [HN](https://news.ycombinator.com/item?id=45412022) | Link: https://www.colino.net/wordpress/en/archives/2025/09/28/optimizing-a-6502-image-decoder-from-70-minutes-to-1-minute/

### TL;DR

Colin Leroy reduced QuickTake 150 photo decoding on a 1 MHz 6502 from roughly 70 minutes to under one by changing both the algorithm and its assembly implementation. Because the Apple II output is small and monochrome, he discarded color data, removed interpolation and unused buffers, generated pixels incrementally, precomputed clamped division tables, eliminated multiplication-heavy indexing, and redesigned Huffman decoding for the processor. Hand-written assembly then exploited common factors, lookup tables, discard paths, and self-modifying buffer access. Pixel approximation differed from reference output by at most one value.

### Comment pulse

- Readers praised the focus on doing less work before making remaining operations faster.
- Discussion explored why a black-pixel grid appeared visually smoother than the reduced-resolution image.
- Commenters valued constrained low-level projects while debating hardware progress versus decades of software inefficiency.

### LLM perspective

- View: The largest gain came from redefining required output, not mechanically accelerating the inherited decoder.
- Impact: Constraint-driven simplification exposed unnecessary color, buffering, arithmetic, and generality hidden in reference code.
- Watch next: Documentation of the proprietary format could reveal further safe simplifications and explain remaining magic constants.
