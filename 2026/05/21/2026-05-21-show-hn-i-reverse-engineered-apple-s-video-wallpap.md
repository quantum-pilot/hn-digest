# Show HN: I reverse engineered Apple's video wallpapers

- Score: 404 | [HN](https://news.ycombinator.com/item?id=48215979) | Link: https://github.com/kageroumado/phosphene

### TL;DR

Phosphene is an MIT-licensed macOS Tahoe app that lets personal videos appear beside Apple’s Aerials in the native wallpaper picker for desktop and lock-screen use. Its out-of-process extension uses Apple’s private WallpaperExtensionKit, reflected XPC types, and manual sample-buffer rendering for gapless loops; it also supports multiple displays and Spaces, power-aware quality, occlusion pausing, and adaptive variants. HN praised the reverse engineering and clearer use case, traded desktop nostalgia, and noted Tahoe’s own animation stutters plus the fragility and value of private wallpaper and screensaver APIs.

### Comment pulse

- The product’s hook is user-supplied video, not extracted Apple assets → commenters initially misunderstood the project because its framing buried that distinction.

- Animated desktops trigger nostalgia → Vista and X-root-window memories resurfaced — counterpoint: Tahoe’s native lock-screen animation reportedly stutters even on an M3 Pro.

- Private extension knowledge unblocks adjacent projects → screensaver developers compared WallpaperAgent with a separate private appex route and older window-overlay workarounds.

### LLM perspective

- **View:** The project succeeds by conforming to macOS lifecycle and selection semantics instead of painting an always-on window behind icons.

- **Impact:** Users gain native-feeling customization; developers gain a working reference for undocumented extension, XPC, rendering, and snapshot behaviors.

- **Watch next:** Test OS-update breakage, battery and thermal savings, multi-display persistence, lock-transition smoothness, and whether Apple exposes public APIs.
