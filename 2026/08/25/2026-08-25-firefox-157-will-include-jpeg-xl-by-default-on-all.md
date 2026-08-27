# Firefox 157 will include JPEG XL by default on all platforms

- Score: 428 | [HN](https://news.ycombinator.com/item?id=49437946) | Link: https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1

### TL;DR

Firefox 157 will enable JPEG XL decoding on every platform using Google Research’s Rust-based jxl-rs. Mozilla says the decoder now supports animation, progressive display, broad correctness testing, fuzzing, and forthcoming multithreading, with large-image performance near other formats and slightly ahead of Safari in one test. Chromium also announced intent to ship. HN welcomed emerging cross-browser support and JPEG XL’s broad feature set, while a thread benchmark warned that lossless decoding could cost roughly 30 times more CPU than WebP for 10% smaller files.

### Comment pulse

- Rust unlocked browser adoption → jxl-rs recently surpassed libjxl in some dashboards, while Apple’s platform tooling still favors its shipped C++ decoder.
- JPEG XL aims beyond ordinary JPEG → it supports reversible JPEG recompression, HDR, animation, alpha, layers, progressive coding, and wide color.
- Cross-browser support could finally create an ecosystem → Firefox and Chromium commitments help — counterpoint: graphics applications still lag even on WebP.

### LLM perspective

- View: Browser convergence removes JPEG XL’s largest adoption barrier, but decoding cost now becomes an operational rather than political question.
- Impact: Publishers gain a feature-rich format; users may save bandwidth while paying different CPU, battery, and latency costs.
- Watch next: Compare multithreaded jxl-rs across image sizes, lossless workloads, mobile power, Safari, and final Chromium releases.
