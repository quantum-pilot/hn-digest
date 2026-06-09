# Stop the Apple Music app from launching

- Score: 559 | [HN](https://news.ycombinator.com/item?id=48447935) | Link: https://lowtechguys.com/musicdecoy/

## TL;DR
Music Decoy is a tiny macOS utility that prevents Apple’s Music app from auto-launching when you hit the Play key or a Bluetooth device sends play/pause. It “wins” by registering the same bundle identifier as Apple Music, so the system thinks Music is already running and does nothing; no polling or background work. You can optionally redirect media keys to another player via a defaults setting. HN discussion praises the elegance, debates Apple’s behavior, and shares alternative workarounds.

---

## Comment pulse
- Elegant system-level hack → Reusing the Music bundle ID avoids daemons, polling, and CPU use; seen as deep-understanding, low-code engineering — counterpoint: most humans and agents default to heavier, cruder solutions.

- Apple Music resentment → Some distrust Apple since iTunes’ breakup and streaming push; others note Music still handles local libraries fine if cloud features are disabled.

- Real-world pain → Musicians and multi-device users risk random Music playback during live sets; some argue it’s still reasonable for Play to open a default player.

---

## LLM perspective
- View: This is a classic “use the platform’s rules against it” fix, unlikely to emerge from generic boilerplate-based coding agents.

- Impact: Benefits power users, performers, and anyone rejecting Apple Music’s nudges while keeping media-key functionality intact.

- Watch next: Whether Apple hardens bundle-ID assumptions or finally exposes a preference to choose/disable the default media responder.
