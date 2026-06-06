# Show HN: I reverse engineered Apple's video wallpapers

- Score: 404 | [HN](https://news.ycombinator.com/item?id=48215979) | Link: https://github.com/kageroumado/phosphene

## TL;DR
Phosphene is an open-source macOS Tahoe app that makes any video file a first-class desktop and lock-screen wallpaper, using the same private WallpaperExtensionKit framework Apple uses for its Aerials. The author reverse engineered the framework, manually drives AVSampleBufferDisplayLayer for seamless looping, and adds power-aware playback, multi-display support, and pause-when-occluded behavior. HN discussion centers on the clever use of private APIs, nostalgia for animated desktops, frustration with Apple’s janky LegacyScreenSaver and Tahoe performance, and interest from other screensaver/wallpaper devs.

## Comment pulse
- This actually lets you use your own videos as desktop/lock wallpapers → some wish the title highlighted that instead of focusing on reverse engineering.  
- Animated desktops evoke Vista/xscreensaver nostalgia → others note Tahoe’s official video wallpapers stutter, so third‑party solutions should at least match normal 4K playback.  
- Framework reverse‑engineering is valuable to other devs → they struggled with WallpaperAgent and LegacyScreenSaver’s jank/memory use, and are excited to pair this with custom screensaver frameworks.

## LLM perspective
- View: Makes Apple’s hidden wallpaper pipeline tangible, enabling serious, power-aware video wallpapers instead of hacky always-on-top windows.  
- Impact: macOS theming enthusiasts and screensaver authors gain a reference implementation; Apple may see pressure to document or stabilize these APIs.  
- Watch next: Whether future macOS releases break the private WallpaperExtensionKit hooks, and if similar techniques appear for iOS/iPadOS lock screens.
