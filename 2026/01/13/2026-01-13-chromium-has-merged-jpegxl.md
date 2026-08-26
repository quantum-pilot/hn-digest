# Chromium Has Merged JpegXL

- Score: 408 | [HN](https://news.ycombinator.com/item?id=46597927) | Link: https://chromium-review.googlesource.com/c/chromium/src/+/7184969

### TL;DR

Chromium merged a JPEG XL decoder implemented through jxl-rs, adding image/jxl MIME handling, request Accept headers, format sniffing, metrics, and a user-facing flag. The 663-line change is enabled by default at build time and landed January 13. HN readers welcomed renewed browser support and JPEG XL’s potential across lossy and lossless images, while cautioning that cited benchmarks may compare different libraries or encoder settings. Discussion also covered decoding versus encoding speed, Rust’s partial security benefits, specification access, adoption barriers, and possible JPEG code sharing.

### Comment pulse

- Browser support unlocks adoption → developers cannot deploy JPEG XL broadly until dominant clients decode it reliably.
- Performance claims need context → codec, implementation, settings, hardware acceleration, and encode-versus-decode workloads materially change comparisons.
- Rust improves memory safety → reviewers welcomed jxl-rs — counterpoint: language guarantees cannot replace threat modeling or auditing.

### LLM perspective

- View: The merge matters more for ecosystem coordination than for proving JPEG XL superior in every workload.
- Impact: Publishers and tooling vendors gain a credible path toward broader JPEG XL deployment.
- Watch next: Default runtime enablement, interoperability results, decode benchmarks, security audits, and competing browser support.
