# It took a year to ship WebAssembly in Anubis

- Score: 218 | [HN](https://news.ycombinator.com/item?id=49590611) | Link: https://anubis.techaro.lol/blog/2026/anubis-wasm/

### TL;DR

Anubis v1.28.0 will ship an optional WebAssembly challenge path using memory-hard Argon2id proof of work. What began as a short implementation became a year of compatibility and reproducibility work: Rust consolidated algorithms, SIMD and baseline builds serve different browsers, wasm2js provides a JavaScript fallback, an LLVM ordering bug broke deterministic builds, and a sandboxed “chromesweep” harness tests old Chrome versions. The author plans real-world testing before possibly enabling it by default. Commenters praised the compatibility effort while questioning disabled-WebAssembly messaging and fallback abuse.

### Comment pulse

- Maintainers appreciated the author’s candor about demanding users and the hidden labor behind broad browser compatibility.
- WebAssembly-disabled users requested explicit guidance—counterpoint: the article already describes a wasm2js-generated JavaScript escape path.
- Commenters suggested Rust’s baseline target, though its no-standard-library constraint would change the implementation trade-off.

### LLM perspective

- View: The hard part was not hashing; it was making one implementation deterministic, portable, testable, and survivable across browsers.
- Impact: Administrators gain stronger configurable challenges while users inherit new compatibility, battery, and accessibility considerations.
- Watch next: Monitor fallback bypasses, mobile cost, difficulty tuning, progress reporting, challenge rotation, and v1.29 default decisions.
