# Make macOS consistently bad (unironically)

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47547009) | Link: https://lr0.org/blog/p/macos/

### TL;DR

macOS 26’s mixed window radii annoy the author more than roundness itself, so they make third-party AppKit windows uniformly worse: a signed injected dynamic library swizzles private `NSThemeFrame` corner methods to return 23 points, while skipping Apple applications, daemons, and command-line tools. A LaunchAgent sets `DYLD_INSERT_LIBRARIES`, avoiding edits to protected system libraries and therefore preserving SIP. HN broadened the complaint to Tahoe’s pill-shaped tabs, wasted space, resize behavior, and sluggishness, but disagreed about the design premise: many users never maximize windows, especially on ultrawide displays, while others expect edge-to-edge layouts.

### Comment pulse

- Overlapping windows with exposed corners are longstanding macOS practice; maximization can waste widescreen space or create excessively long editor lines.
- Critics called Tahoe a thousand-cut regression — counterpoint: some saw corner outrage as harmless bikeshedding around a capable OS.
- High WindowServer CPU may reflect apps flooding updates rather than compositor failure, though users reported serious post-upgrade latency.

### LLM perspective

- **View:** Consistency improves coherence, but global injection through private methods is brittle whenever AppKit internals change.
- **Impact:** The tweak preserves SIP yet affects every eligible process inheriting the environment, so compatibility testing matters.
- **Watch next:** Selector changes, per-app exclusions, Intel/Apple Silicon behavior, performance impact, and whether Apple normalizes radii upstream.
