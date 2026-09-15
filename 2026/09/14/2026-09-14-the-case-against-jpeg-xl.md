# The case against JPEG XL

- Score: 267 | [HN](https://news.ycombinator.com/item?id=49690554) | Link: https://giannirosato.com/blog/post/case-against-jxl/

### TL;DR

Compression engineer Gianni Rosato argues JPEG XL is impressive outside browsers but poorly matched to common Web needs. His tests favor modern AVIF encoders for lossy efficiency, progressive usefulness, and decoding speed, while JPEG XL’s flexibility, complex tools, and worst-case decoding create implementation and security costs. He considers its roughly 12% lossless-WebP advantage and JPEG recompression insufficient for browser adoption. Commenters challenge benchmark methodology, progressive comparison points, decoder configurations, and commercial conflicts, while emphasizing archival, lossless, high-bit-depth, and universal-viewing benefits that browser support could unlock.

### Comment pulse

- Web delivery favors narrow efficiency → AVIF allegedly offers stronger lossy compression and faster usable progressive renders for dominant workloads.
- Benchmark choices are disputed → commenters cite warmup-inclusive timing, single-threaded JXL decoding, mismatched formats, and selectively favorable progressive points.
- Browser support serves long-tail interoperability → archives, lossless art, high bit depth, intranets, and documents benefit from ubiquitous decoding.

### LLM perspective

- View: The article raises legitimate deployment costs, but contested methodology prevents its measurements from settling the codec-level question.
- Impact: Browser vendors must balance attack surface and maintenance against broader format interoperability beyond typical public-Web images.
- Watch next: Reproduce size-matched tests with equivalent pixel formats, threading, pure decode timing, multiple corpora, and progressive-quality curves.
