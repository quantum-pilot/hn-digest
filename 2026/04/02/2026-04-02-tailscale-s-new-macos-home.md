# Tailscale's new macOS home

- Score: 275 | [HN](https://news.ycombinator.com/item?id=47618189) | Link: https://tailscale.com/blog/macos-notch-escape

### TL;DR
- Tailscale’s macOS menu‑bar icon could vanish into the MacBook notch, confusing users. They hacked around it using occlusionState to show a warning, but now ship a full windowed client (v1.96.2) with searchable devices, Taildrop, and exit‑node controls, making Tailscale discoverable beyond the menu bar. HN discussion centers on Apple’s failure to provide a tray overflow or visibility indicators, the resulting support/refund burden for menu‑bar apps, accessibility concerns, and command‑line tweaks to cram more icons in.

### Comment pulse
- Spacing tweak commands reduce menubar icon width → fit ~2× icons, delaying notch issues; users resent needing shell hacks on a supposedly polished OS.  
- Hidden icons hurt indie apps → users think menu-bar tools failed, causing refunds; Bartender broke on Tahoe — counterpoint: some blame “icon hoarders,” not Apple.  
- No overflow indicator shocks users → notch simply hides icons; commenters cite Windows tray, browser menus, plus accessibility problems with larger fonts or low vision.  

### LLM perspective
- View: Apple’s notch handling shows prioritization of visual minimalism over basic discoverability, offloading UX and support costs onto third‑party developers.  
- Impact: Menu‑bar–centric tools and VPNs must ship redundant UIs, alerts, and spacing workarounds, increasing maintenance complexity across macOS versions.  
- Watch next: Whether macOS introduces a proper tray overflow, occlusion APIs, or new restrictions that again break utilities like Bartender and Tailscale’s notch detection.
