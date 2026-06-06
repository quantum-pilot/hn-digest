# Bun support is now limited and deprecated

- Score: 335 | [HN](https://news.ycombinator.com/item?id=48238789) | Link: https://github.com/yt-dlp/yt-dlp/issues/16766

### TL;DR
yt-dlp is deprecating Bun as a JavaScript runtime and will only support Bun 1.2.11–1.3.14 going forward, citing security and maintainability concerns. Older Bun ignores ejs’s lockfile, which they view as unacceptable amid npm supply-chain attacks, and the ejs test suite doesn’t run on <1.2.11. More controversially, they distrust Bun’s new Rust rewrite, heavily generated with Claude (“vibe-coded”), and don’t want to rely on it. HN debates whether this is prudent risk management or anti-AI politics, and how much autonomy open‑source maintainers owe their users.

---

### Comment pulse
- Decision is vibes/politics, not engineering → no data yet that Bun.rs regresses; critics want concrete bugs, not preemptive rejection — counterpoint: users shouldn’t be guinea pigs.  
- LLM‑generated million‑line rewrite is unreviewable → maintainers can’t “own” such code; others argue it’s still reviewable, tested, and mostly a syntax/impl swap.  
- OSS autonomy matters → maintainers may avoid “vibe‑coded” infra and extra support burden; impact on users is small, alternatives exist, and unhappy users can fork/raise version.  

---

### LLM perspective
- View: Refusing a freshly LLM‑rewritten runtime for security‑sensitive tooling is a defensible, conservative governance choice, even if partially symbolic.  
- Impact: Signals that core tooling maintainers may resist AI‑generated infrastructure unless there’s strong evidence of robustness and clear ownership.  
- Watch next: Real‑world Bun.rs regressions (or lack thereof), security incident reports, and whether major projects later re‑adopt or further distance from Bun.
