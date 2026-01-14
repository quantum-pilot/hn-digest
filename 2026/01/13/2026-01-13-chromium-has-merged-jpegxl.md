# Chromium Has Merged JpegXL

- Score: 408 | [HN](https://news.ycombinator.com/item?id=46597927) | Link: https://chromium-review.googlesource.com/c/chromium/src/+/7184969

TL;DR
- Chromium has re-merged support for JPEG XL, a modern image codec aiming to replace JPEG and PNG by delivering better compression at equal or higher visual quality. Benchmarks referenced in the thread show JPEG XL frequently outperforming WebP and AVIF, particularly without AVIF’s high encoding cost. Commenters note growing support across Apple, Microsoft, and major tools, but remain wary of the paywalled ISO spec, Google’s prior backtracking, and assuming Rust-based implementations alone guarantee security.

Comment pulse
- JPEG XL currently best general-purpose codec → Pareto-front benchmarks show superior lossless/lossy compression and quality—counterpoint: tests ignore hardware-accelerated codecs, so real-world performance gap may shrink.
- Rust decoder calms some security fears → memory safety removes many bugs, but commenters warn it can foster complacency without real threat modeling.
- Adoption seen as viable → Apple, Microsoft, Adobe, Gimp already support JPEG XL; paywalled ISO spec and long rollout timeline still worry some developers.

LLM perspective
- View: JPEG XL in Chromium revives a credible JPEG/PNG successor, increasing pressure on lagging formats like baseline JPEG and GIF.
- Impact: Web developers and CDNs gain a single high-quality format, simplifying pipelines and potentially reducing storage, bandwidth, and decode complexity.
- Watch next: Key signals: default Chrome enablement, hardware decode, W3C standardization, and major hosts offering JPEG XL as a first-class option.
