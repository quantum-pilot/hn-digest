# Make macOS consistently bad (unironically)

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47547009) | Link: https://lr0.org/blog/p/macos/

### TL;DR
The post complains that macOS 26’s new ultra-rounded window corners are ugly, but argues the real sin is *inconsistency* between apps. Rather than disable System Integrity Protection to flatten everything, the author injects a small AppKit-based dynamic library via `DYLD_INSERT_LIBRARIES` to swizzle private `NSThemeFrame` methods and force a fixed, larger corner radius for third‑party GUI apps. The result: a deliberately “consistently bad” but visually uniform UI, trading purity and safety for sanity.

---

### Comment pulse
- macOS window model assumes overlapping, non-maximized windows → many users like half-sized, side-by-side apps; others find non-snapping, pill-styled UI elements disorienting and space-wasting.  
- Performance feels worse in macOS 26 → WindowServer and kernel_task spikes, UI lag, and workarounds erode confidence; some look to QubesOS or AI-built OSes—counterpoint: AI UIs already look worse.  
- Corner-radius drama = bikeshedding to some → surface nitpicks imply a solid OS; others see it as evidence of opinionated, unfixable design rot.

---

### LLM perspective
- View: Clever, targeted use of method swizzling avoids SIP, but relies on private APIs and global `DYLD_INSERT_LIBRARIES`, so it’s brittle.  
- Impact: Appeals to power users wanting consistent aesthetics without full theming engines; regular users remain stuck with Apple’s design decisions.  
- Watch next: Whether Apple locks down such injection vectors, offers official window-theming controls, or third-party window managers fill the gap.
