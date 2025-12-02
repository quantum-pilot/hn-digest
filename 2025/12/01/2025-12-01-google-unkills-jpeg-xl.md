# Google unkills JPEG XL?

- Score: 228 | [HN](https://news.ycombinator.com/item?id=46108563) | Link: https://tonisagrista.com/blog/2025/google-unkills-jpegxl/

- TL;DR  
Google’s Chromium team has reversed its 2022 decision to drop JPEG XL, reopening the ticket and planning support once a performant, memory‑safe Rust decoder is ready. The article reviews how Chrome ignored broad industry enthusiasm (Meta, Intel, Adobe, etc.) while Safari, Firefox and the PDF Association slowly aligned behind JPEG XL. Thanks to features like lossless JPEG recompression, HDR, huge dimensions, many channels and progressive decoding, many expect JPEG XL to become a major web image format.

- Comment pulse  
  - Security concern → C++ libjxl is viewed as unsafe; browser vendors want memory‑safe decoders, making the Rust-based jxl‑rs crate the favored implementation path.  
  - Google’s motives → Some recall Chrome’s hostility and PR backlash, seeing a face‑saving reversal—counterpoint: others think they simply waited for Rust decoder maturity.  
  - Practical limits → Huge maximum resolutions impress but raise DoS and tiling concerns; others note progressive decoding helps keep large images usable over networks.

- LLM perspective  
  - View: JPEG XL’s revival underlines how sustained ecosystem pressure can redirect even dominant browser vendors when a format’s benefits are compelling.  
  - Impact: Web developers gain a strong default for archival, HDR and large imagery, while CDNs and browsers must modernize their image stacks.  
  - Watch next: Follow Firefox and PDF adoption, encoder/decoder performance benchmarks, and whether AVIF/WebP remain necessary alongside one rich, general‑purpose format.
