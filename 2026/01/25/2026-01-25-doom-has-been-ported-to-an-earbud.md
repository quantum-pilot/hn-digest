# Doom has been ported to an earbud

- Score: 318 | [HN](https://news.ycombinator.com/item?id=46753484) | Link: https://doombuds.com

- TL;DR  
An engineer ported 1993’s Doom to a single PineBuds Pro earbud, exposing it online so people queue up and play remotely through their browsers. The earbud’s 300MHz Cortex‑M4F renders frames, JPEG-encodes them, then streams MJPEG over a 2.4Mbps UART bridge, hitting ~18 fps within tight RAM and 4MB flash limits (using a trimmed Squashware WAD). HN discussion centers on how cheap, powerful MCUs and open firmware make such stunts feasible, and what that says about modern hardware and games.

- Comment pulse  
  - Cheap MCUs in earbuds are a feature, not failure → ANC, low latency, updates, and avoiding custom ASICs justify overkill — counterpoint: still feels excessive.  
  - PineBuds Pro are intentionally open-firmware, general-purpose platforms, so running Doom is aligned with their design as hacker-friendly, experiment-ready consumer hardware.  
  - Doom persists as the canonical "it runs Doom" target: open-sourced, moderately demanding, iconic; some wish for similarly compact, replayable modern games instead.

- LLM perspective  
  - View: Open, over-capable IoT hardware turns everyday gadgets into playful computing platforms, blurring lines between dev boards and consumer devices.  
  - Impact: Demonstrations like this market open earbuds, encouraging manufacturers to expose SDKs, debug pads, and modder-friendly firmware policies.  
  - Watch next: More complex engine ports to low-power wearables, and shared tooling for graphics, input, and streaming over constrained links.
