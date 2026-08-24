# December in Servo: multiple windows, proxy support, better caching, and more

- Score: 128 | [HN](https://news.ycombinator.com/item?id=46745259) | Link: https://servo.org/blog/2026/01/23/december-in-servo/

### TL;DR

Servo 0.0.4 and December nightlies add multiple windows, basic HTTP proxies, system roots on most platforms, cache and site-data management APIs, embedder dialogs and console messages, broader WebCrypto, and many compatibility fixes. Cache eviction, media leak repairs, selector and reflow optimizations, safer garbage-collector interfaces, and crash fixes improve stability. Recurring donations reached $7,110 monthly, up 10.5 percent. Commenters successfully loaded several sites from prebuilt binaries but not YouTube, viewing progress as evidence that an independent embeddable engine is becoming practical.

### Comment pulse

- Multiple windows mark embedding maturity → applications can manage richer interfaces, although direct window opening on macOS has a known settings-dependent issue.
- Web compatibility is advancing incrementally → encoding, legacy CSS, event, layout, crypto, and devtools changes close many small platform gaps.
- Engine diversity attracts support → commenters value alternatives to Blink, WebKit, and Gecko while comparing Servo’s speed and coverage with Ladybird.

### LLM perspective

- View: The release is less about one headline feature than steady conversion of an experiment into infrastructure.
- Impact: Embedders gain control over networking, storage, dialogs, diagnostics, and lifecycle without adopting a mainstream engine.
- Watch next: Window reliability on macOS, Web Platform Test trends, media playback, alpha releases, and donation-funded maintainer output.
