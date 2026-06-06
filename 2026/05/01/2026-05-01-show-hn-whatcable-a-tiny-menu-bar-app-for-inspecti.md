# Show HN: WhatCable, a tiny menu bar app for inspecting USB-C cables

- Score: 388 | [HN](https://news.ycombinator.com/item?id=47972511) | Link: https://github.com/darrylmorley/whatcable

### TL;DR
WhatCable is a small macOS menu bar app (plus CLI) that tells you, in plain English, what each USB‑C cable and charger on your Apple Silicon Mac actually supports: data speed, power rating, Thunderbolt/USB4 capability, and active transports. It also shows live USB Power Delivery negotiation, highlights what’s bottlenecking charging (cable, charger, or Mac), and lists attached USB devices per port. It’s built on public IOKit interfaces, requires macOS 14+, and is distributed outside the App Store.

---

### LLM perspective
- View: This neatly productizes obscure IOKit and USB-PD details into something non-engineers can act on when debugging chargers and hubs.  
- Impact: Helps power users, support teams, and reviewers validate USB-C cables/docks and explain “slow charging” without hardware tools.  
- Watch next: Similar tooling for Windows/Linux controllers, better PD 3.2 coverage, and standardized OS-level “cable capability” UIs across platforms.
