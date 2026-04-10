# Native Instant Space Switching on macOS

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47708818) | Link: https://arhan.sh/blog/native-instant-space-switching-on-macos/

### TL;DR
The post argues that macOS’s Space-switching animation is slow, disorienting, and impossible to disable natively, especially on newer 120 Hz MacBooks where it’s even slower. Existing workarounds either require disabling System Integrity Protection, adopting a tiling window manager, paying for commercial tools, or faking virtual desktops. The author highlights InstantSpaceSwitcher, a tiny open-source menubar app that simulates a very fast trackpad swipe to switch Spaces instantly and offers a simple CLI, without touching SIP or window management.

---

### Comment pulse
- Space-switching is slower on 120 Hz displays → users hit shortcuts before focus changes, causing frequent misfires and frustration—counterpoint: some only notice after it’s pointed out.  
- Many prefer alternatives like Aerospace or even Asahi Linux with GNOME/Sway → more predictable, scriptable window/space management than Apple’s opaque behavior.  
- Community scripts and dotfiles integrate InstantSpaceSwitcher quickly → reinforces that tiny, sharable glue tools can meaningfully improve daily macOS ergonomics.

---

### LLM perspective
- View: This is a classic micro-friction issue where a 300–400 ms animation meaningfully harms expert users’ flow.  
- Impact: Power users and developers gain a low-risk workaround; highlights demand for finer-grained macOS UI motion controls.  
- Watch next: Whether Apple exposes animation-duration settings or third-party tools standardize around stable, non-SIP hacks for Spaces control.
