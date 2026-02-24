# The JavaScript Oxidation Compiler

- Score: 238 | [HN](https://news.ycombinator.com/item?id=47117459) | Link: https://oxc.rs/

### TL;DR
Oxc is a Rust-based “oxidation compiler” ecosystem that re-implements core JavaScript tooling—linter, formatter, parser, transformer, resolver, and minifier—with a heavy focus on speed and compatibility. Oxlint targets ESLint parity but claims 50–100x faster runs with type-aware rules; Oxfmt aims to be a Prettier-compatible formatter, dramatically faster than both Prettier and Biome. HN commenters praise its performance and Rust integration, flag sharp edges like Oxfmt’s recursive default behavior, and speculate about long-term monetization and the gap between fast tooling and slow web apps.

### Comment pulse
- Rust-native JS workflows → Using oxc_traverse plus boa_engine enables JS instrumentation as a single static binary, avoiding Node-based toolchains and easing distribution.  
- Oxfmt defaults surprise some → Running it bare recursively rewrites JS/TS; critics call this dangerous, others say it’s expected and VCS should protect you — counterpoint: discoverability of such behavior could be better.  
- Strategy and priorities → Users question how VoidZero will monetize (hinted: Vite Plus) and note devs obsess over tooling perf while browser-side perf remains harder and often neglected.

### LLM perspective
- View: A unified, Rust-based toolchain reduces duplicated concerns across linting, formatting, parsing, and transforming, making “fast by default” builds more attainable.  
- Impact: CI pipelines, large repos, and cloud IDEs benefit most, where tool latency directly affects developer throughput and costs.  
- Watch next: Deeper editor/IDE integrations, formatter/minifier stability milestones, and a transparent business model to encourage enterprise adoption.
