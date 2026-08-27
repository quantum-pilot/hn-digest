# Building a macOS app to know when my Mac is thermal throttling

- Score: 214 | [HN](https://news.ycombinator.com/item?id=46410402) | Link: https://stanislas.blog/2025/12/macos-thermal-throttling-app/

### TL;DR

MacThrottle arose because macOS’s public `ProcessInfo.thermalState` merges “moderate” heat and actual “heavy” throttling into one “fair” state. The author discovered that `thermald` exposes the finer five-level pressure value through Darwin notifications, enabling a rootless Swift menu-bar app instead of polling privileged `powermetrics`. The app combines pressure history, SMC temperature with an IOKit fallback, fan speed, alerts, and login startup. HN readers valued diagnosis but noted charging, docks, external displays, and fan curves as confounding factors or mitigations.

### Comment pulse

- Accurate pressure visibility enables action → users can kill runaway processes, adjust fan behavior, or pause workloads before severe slowdown.
- Heat has multiple contributors → charging, USB controllers, external displays, and inadequate adapters can mimic or trigger CPU throttling.
- Distribution remains awkward → absent notarization adds installation friction, while commenters suggested Homebrew as a route forward.

### LLM perspective

- View: Undocumented system signals can be more operationally useful than Apple’s intentionally coarse public abstraction.
- Impact: Passive Mac users gain evidence separating thermal pressure from swapping, power constraints, or overloaded processes.
- Watch next: Test pressure mappings and SMC keys across Apple Silicon generations, docks, chargers, and macOS updates.
