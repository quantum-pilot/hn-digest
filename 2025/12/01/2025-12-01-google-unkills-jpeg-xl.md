# Google unkills JPEG XL?

- Score: 228 | [HN](https://news.ycombinator.com/item?id=46108563) | Link: https://tonisagrista.com/blog/2025/google-unkills-jpegxl/

### TL;DR

Chromium changed its JPEG XL issue from obsolete to assigned and now welcomes a performant, memory-safe decoder, reversing its 2022 removal. Momentum includes Safari support, Firefox interest, a Rust implementation, and proposed PDF adoption for HDR images. The format offers lossless recompression of existing JPEG libraries at roughly 30% smaller size, progressive decoding, HDR, animation, alpha, and unusually large dimensions. Discussion remained guarded about implementation readiness and the governance of dominant browser engines.

### Comment pulse

- Decoder security remains the gate → substantial image-processing code in C++ creates attack-surface concerns, making Rust implementation central.
- Chromium’s reversal split interpretation → readiness may explain the delay — counterpoint: critics recall explicit hostility despite broad ecosystem support.
- Extreme dimensions invited caution → progressive and tiled decoding help practicality, but compact files could still create denial-of-service risks.

### LLM perspective

- View: Assigned status signals intent, not shipped compatibility; implementation quality now matters more than format advocacy.
- Impact: Broad Chromium support could make lossless JPEG migration and HDR delivery viable across the web.
- Watch next: jxl-rs integration, security review, performance parity, release flags, and Firefox’s final position.
