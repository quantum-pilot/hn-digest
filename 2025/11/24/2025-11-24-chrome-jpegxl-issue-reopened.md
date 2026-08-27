# Chrome Jpegxl Issue Reopened

- Score: 205 | [HN](https://news.ycombinator.com/item?id=46033330) | Link: https://issues.chromium.org/issues/40168998

### TL;DR

Chromium reopened its long-running JPEG XL decoding feature request after previously removing experimental support. Chrome leadership now welcomes contributions for a performant, memory-safe decoder, contingent on long-term maintenance and normal launch criteria; a linked effort is integrating the Rust-based jxl-rs decoder. Supporters cite lossless JPEG recompression, progressive decoding, HDR, and growing platform adoption. Commenters still debate whether JPEG XL offers enough web benefit over AVIF, whose existing browser decoder and low-to-medium-quality performance reduce implementation cost.

### Comment pulse

- JPEG XL offers a migration bridge → byte-preserving JPEG recompression and progressive delivery could ease deployment.
- AVIF already covers common web needs → counterpoint: JPEG XL targets high fidelity, lossless storage, and different HDR workflows.

### LLM perspective

- View: Reopening changes the question from interest to sustainable, secure implementation.
- Impact: Browser support could unlock interoperable deployment by CDNs, archives, and image-heavy sites.
- Watch next: jxl-rs performance, memory-safety review, maintainer commitments, and a Chrome launch decision.
