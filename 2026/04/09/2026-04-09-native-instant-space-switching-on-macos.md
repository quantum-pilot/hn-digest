# Native Instant Space Switching on macOS

- Score: 254 | [HN](https://news.ycombinator.com/item?id=47708818) | Link: https://arhan.sh/blog/native-instant-space-switching-on-macos/

### TL;DR

InstantSpaceSwitcher eliminates macOS’s Space-transition delay by simulating a very high-velocity trackpad swipe, preserving native Spaces without disabling System Integrity Protection or adopting another window manager. The small menu-bar app can move left or right, jump to a numbered Space, and exposes a CLI, though users must build it from source. HN commenters confirmed the delay can make keystrokes target the prior Space, framing the issue as a workflow bug rather than a cosmetic annoyance.

### Comment pulse

- Users traced slower animations to 120 Hz MacBooks; selecting 60 Hz reportedly restores earlier speed, suggesting a frame-rate-dependent calculation bug.
- AeroSpace won praise as an easy, SIP-safe workspace replacement — counterpoint: the featured tool specifically preserves Apple’s native model.
- Some frustration was severe enough to prompt moves to Fedora Asahi Remix or Arch/Sway on Apple hardware.

### LLM perspective

- **View:** A focused accessibility-adjacent workaround can outperform broad window-management replacements when one animation is the actual problem.
- **Impact:** Mac users with rapid workspace habits regain predictable focus timing while keeping their existing layout workflow.
- **Watch next:** Behavior across display refresh rates, macOS releases, multi-monitor setups, and future gesture APIs.
