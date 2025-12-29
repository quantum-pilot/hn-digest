# Building a macOS app to know when my Mac is thermal throttling

- Score: 214 | [HN](https://news.ycombinator.com/item?id=46410402) | Link: https://stanislas.blog/2025/12/macos-thermal-throttling-app/

### TL;DR
The author wanted a reliable way to tell when an Apple Silicon Mac is *actually* thermal throttling, beyond vague “fair” states and CPU-at-100% heuristics. Apple’s official `ProcessInfo.thermalState` is too coarse, collapsing “moderate” and “heavy” thermal pressure into one value. Digging deeper, they discovered `thermald` publishes precise pressure levels via Darwin notifications (`com.apple.system.thermalpressurelevel`), accessible without root. They built MacThrottle, a SwiftUI menu-bar app that subscribes to this, graphs temperature and fan speed, sends alerts, and auto-starts—albeit without notarization.

---

### Comment pulse
- Intel 2019 i9 MacBooks throttled constantly → users report terrible thermals, fan noise, and even port-side–dependent behavior; Apple Silicon plus new chassis is a huge upgrade.  
- “What can you *do* with this info?” → kill runaway apps, tweak fan curves or use High Power Mode; on fanless Airs, you’re mostly closing stuff or adding external cooling.  
- Power/IO can mimic throttling → weak chargers, docks, or hot USB-C sides cause “thermal soaking,” reduced headroom, and 100% CPU at low watts—counterpoint: still worth distinguishing from true SoC throttling.

---

### LLM perspective
- View: Using `notifyd`’s thermalpressure notifications is a clean, non-root pattern other Mac tools can copy for accurate throttling detection.  
- Impact: Power users, game/compute developers, and monitoring apps gain clearer signals to adapt workloads or guide users.  
- Watch next: Add charger/dock power detection, compare with Intel-era APIs, and monitor whether Apple documents or locks down these thermal interfaces.
