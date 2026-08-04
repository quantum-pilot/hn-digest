# Should you normalize RGB values by 255 or 256?

- Score: 168 | [HN](https://news.ycombinator.com/item?id=48360054) | Link: https://30fps.net/pages/255-vs-256-division/

### TL;DR

For ordinary 8-bit image processing, decode channels as value/255: it preserves exact 0.0 and 1.0, round-trips losslessly, matches GPU and common-file conventions, and avoids surprising masks or alpha. Mapping each code to (value+0.5)/256 gives equal-width bins, exact binary fractions, slightly lower theoretical reconstruction error, and simpler dithering, but only helps when one controls both encoding and decoding. HN agreed the visual difference is usually negligible yet debated endpoint meaning; hardware voltage ladders, clipping, low-bit color, and zero-sensitive compositing make the convention operationally significant.

### Comment pulse

- Exact endpoints are semantic contracts → masks and premultiplied alpha often require 0.0 and 1.0; midpoint decoding can leak pixels or transparency.
- Equal bins model quantized intervals better → no physical sample is exactly known — counterpoint: saturated 255 may represent arbitrary clipping, not a centered interval.
- At low bit depth, scaling is visible → 2-bit blue and 3-bit red/green voltage ladders share only endpoint levels, distorting grays and gradients.

### LLM perspective

- **View:** This is chiefly a protocol question, not a precision contest; decode according to the producer’s quantization contract.
- **Impact:** Library authors should expose explicit conversion modes and document endpoint, rounding, clamping, and color-space assumptions.
- **Watch next:** Round-trip, mask, alpha, dithering, clipping, and cross-library tests covering both formulas and mixed encode/decode failures.
