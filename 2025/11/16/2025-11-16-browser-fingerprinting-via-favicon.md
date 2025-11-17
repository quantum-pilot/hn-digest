# Browser fingerprinting via favicon

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45947770) | Link: https://github.com/jonasstrehle/supercookie

- TL;DR
  - Supercookie shows how sites can encode a bitstring via favicon cache misses/hits across redirected paths, yielding a stable ID that survives cookies/cache clears, VPNs, and incognito. README claims major and mobile browsers are affected; the demo surfaces IDs after ~18 redirects. HN notes long-standing favicon cache glitches, inconsistent demo behavior (e.g., Safari iOS loops), and that this is a 2021 technique. Some mitigations reportedly landed, but coverage appears uneven.

- Comment pulse
  - Favicon cache misbehavior is widespread → wrong icons persist across devices, profiles, and private mode — counterpoint: likely UI cache bugs, not deliberate tracking.
  - Demo inconsistent on Safari iOS → endless redirect loop without ID; authors say Safari fixed after earlier disclosure.
  - This isn’t new → technique and repo date to 2021; thread asks whether vendors fully shipped defenses in 2023+.

- LLM perspective
  - View: Cache partitioning by top-level site largely defeats this; per-context isolation for private windows closes cross-mode leakage.
  - Impact: Expect further hardening: stricter favicon TTLs, network-state partitioning, and blocking favicon loads during redirects.
  - Watch next: Independent test pages tracking modern releases; browser bug reports citing residual bypasses on mobile and third-party iframes.
