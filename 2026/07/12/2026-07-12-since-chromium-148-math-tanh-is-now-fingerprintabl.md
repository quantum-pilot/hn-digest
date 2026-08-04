# Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS

- Score: 226 | [HN](https://news.ycombinator.com/item?id=48884853) | Link: https://scrapfly.dev/posts/browser-math-os-fingerprint/

### TL;DR

Since Chromium 148, V8 routes Math.tanh through each operating system’s math library instead of bundled fdlibm, exposing tiny rounding differences that distinguish Linux, macOS, and Windows—and can contradict a spoofed user agent. CSS trigonometry and Web Audio leak related platform or architecture details through separate host libraries. Noise is detectable; faithful spoofing requires bit-exact algorithm reproduction, architecture control, timing parity, and hardware validation. HN noted the change also signals a browser-version floor, debated scraper incentives and AI-written marketing, and favored standardized correctly rounded functions or restored bundled implementations.

### Comment pulse

- The leak identifies more than OS → bundled behavior before version 148 creates a coarse version boundary — counterpoint: ordinary feature tests already reveal versions.
- Correct rounding could remove vendor signatures → shared transcendental results improve privacy, though implementations must avoid pathological worst-case performance.
- Messenger credibility divided readers → the disclosed AI drafting and anti-bot vendor motive looked promotional, while others prioritized reproducible technical truth.

### LLM perspective

- **View:** Determinism becomes identity when standards permit implementation variance; one-bit differences are cheap, stable classifiers across otherwise similar browser surfaces.
- **Impact:** A performance-oriented dependency change silently expanded fingerprinting, demonstrating that privacy regressions can enter below APIs without visible feature changes.
- **Watch next:** Chromium’s response, correctly rounded libm adoption, population measurements, timing signatures, and regression tests for bit-stable web math.
