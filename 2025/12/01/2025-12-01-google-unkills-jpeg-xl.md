# Google unkills JPEG XL?

- Score: 228 | [HN](https://news.ycombinator.com/item?id=46108563) | Link: https://tonisagrista.com/blog/2025/google-unkills-jpegxl/

### TL;DR

Chromium has changed its JPEG XL issue from “Obsolete” to “Assigned” and welcomed a performant, memory-safe decoder, reversing its 2022 removal stance but not yet shipping browser support. The reconsideration follows Safari adoption, Firefox interest, PDF Association plans, and development of the Rust jxl-rs decoder. The author highlights lossless JPEG recompression, HDR, progressive decoding, animation, alpha, large dimensions, and many channels as advantages. Commenters welcome renewed momentum while emphasizing decoder complexity, memory safety, and the risk of one browser vendor controlling web formats.

### Comment pulse

- Memory-safe decoding is the practical gate → both Chromium and Firefox interest appears tied to a viable Rust implementation.
- Supporters remain angry about the earlier “insufficient interest” rationale after extensive ecosystem feedback.
- Extreme image dimensions enable specialized uses but raise resource-exhaustion and tiling concerns.

### LLM perspective

- View: Reassignment signals a path back, not a commitment date or completed implementation.
- Impact: Chromium support could unlock broad web deployment and make lossless migration from JPEG economically useful.
- Watch next: Follow jxl-rs security review, performance, standards position, default enablement, and cross-browser interoperability.
