# Mouseless – keyboard-driven control of macOS/Linux/Windows

- Score: 430 | [HN](https://news.ycombinator.com/item?id=48383667) | Link: https://mouseless.click

### TL;DR

Mouseless is a cross-platform utility that replaces pointer handling with keyboard commands: users type overlay coordinates to click, or use a free-movement mode for scrolling, dragging, and every mouse button. It targets faster context switching, reduced hand strain, accessibility, and situations without a usable surface, offering a 14-day trial and paid cross-platform access. HN compared it with ShortCat, Homerow, Keynav, Waynav, Vimium, and keyboard firmware, while debating whether coordinate-based cursor emulation builds useful muscle memory or merely compensates for interfaces lacking semantic keyboard navigation.

### Comment pulse

- Fixed coordinate codes may become fast → repeated screen locations can form muscle memory, while dynamic element labels require fresh visual scanning.
- Semantic navigation reaches named or hidden controls without simulating a cursor — counterpoint: typing may take longer.
- The ecosystem is mature but fragmented → Keynav derivatives, wl-kbptr, Vimium, QMK mouse keys, and tiled window managers cover narrower platforms.

### LLM perspective

- **View:** Mouseless succeeds as a universal fallback precisely because application-level keyboard accessibility remains inconsistent.
- **Impact:** Users with RSI or pointer limitations gain immediate control without waiting for every application to improve.
- **Watch next:** Latency benchmarks, Wayland compatibility, coordinate stability across layouts, and comparisons with object-detection or accessibility-tree navigation.
