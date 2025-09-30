# Optimizing a 6502 image decoder, from 70 minutes to 1 minute

- Score: 185 | [HN](https://news.ycombinator.com/item?id=45412022) | Link: https://www.colino.net/wordpress/en/archives/2025/09/28/optimizing-a-6502-image-decoder-from-70-minutes-to-1-minute/

- TL;DR
    - On a 1 MHz Apple II, the author cut QuickTake 150 decoding from 70 minutes to under 1 by redesigning for constraints: keep only green Bayer samples, remove intermediate buffers and interpolation, precompute per-row division tables, switch to line-wise indexing, adopt bit-by-bit Huffman, and apply 6502-specific assembly tricks (special-casing common factors, lookup shifts, self-modifying addressing). He questions how dcraw first cracked the proprietary format. HN reacts with nostalgia for constraint-driven craft, perceptual notes about “sharper” half-sampled images, and debate over hard performance limits.

- Comment pulse
    - Constraints are refreshing → Low-level work with tight memory teaches cost; fewer abstractions reveal what compilers can’t fix.
    - Black-grid looks sharper → Acts like structured dithering; the 320×240 version may be browser-upscaled, introducing aliasing.
    - Seconds vs physics → Ambition says “optimize more”; cycle budgets suggest <10s unlikely on 1 MHz 6502 — counterpoint: AI-assisted perf work can still help.

- LLM perspective
    - View: Favor eliminating work over micro-optimizing it; shape dataflow and bit handling to the CPU.
    - Impact: Reusable patterns for embedded/retro devs; faster QuickTake decoding aids digital preservation.
    - Watch next: Publish cycle/per-pixel budgets, compare 6502 vs Z80/6809 approaches, document QuickTake 150 format.
