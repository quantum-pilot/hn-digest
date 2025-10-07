# Ladybird passes the Apple 90% threshold on web-platform-tests

- Score: 656 | [HN](https://news.ycombinator.com/item?id=45493358) | Link: https://twitter.com/awesomekling/status/1974781722953953601

- TL;DR
    - Ladybird, a new browser engine, hit Apple’s 90% web‑platform‑tests pass rate—a prerequisite for alternative engines on iOS (notably under the EU’s DMA). HN applauds the pace and funding, but warns WPT percentages skew toward easy suites and miss performance, security, and real‑world compatibility. Interop’s curated tests may be a better bar, yet Apple set this one. The hard part remains: perf, stability, and long‑tail quirks could take years, but the milestone signals credible competition beyond Chromium/Gecko.
    - Content unavailable; summarizing from title/comments.
- Comment pulse
    - WPT pass rate is a poor metric → unbalanced suites (e.g., many encoding tests); Interop subsets reflect coverage better — counterpoint: Apple requires 90%, not Ladybird.
    - Milestone matters for iOS eligibility → EU DMA forces browser choice; outside EU, Apple may still block non‑WebKit engines.
    - Impressive progress, but far from daily‑driver → performance, crash‑hardening, security bounties, and long‑tail site quirks are the slow, costly last 10%.
- LLM perspective
    - View: Treat WPT 90% as gate, not goal; track Interop scores plus real‑world site compatibility and startup/scroll/render latency.
    - Impact: If Apple accepts, iOS gains a third engine; pressures WebKit, improves standards accountability, and reduces Chromium monoculture risk.
    - Watch next: Publish curated conformance dashboard, perf regressions, and crash rates; land JS JIT milestones; demonstrate top‑100 sites reliability without site‑specific hacks.
