# UHF X11: X11 Built for VisionOS and Apple Vision Pro

- Score: 147 | [HN](https://news.ycombinator.com/item?id=48610853) | Link: https://www.lispm.net/apps/uhf-x11/

### TL;DR

UHF X11 turns Apple Vision Pro into a rootless X11 display server: top-level windows from trusted remote Xlib clients appear as separate native visionOS windows. It supports standard TCP connections authenticated with MIT-MAGIC-COOKIE-1, native-resolution nearest-neighbor framebuffer scaling, bundled or imported bitmap fonts, optional CRT effects, and experimental indirect GLX. HN appreciated the technically faithful nostalgia, joked that X11 may outlive visionOS, and compared alternative headset paths for developers wanting fewer platform constraints.

### Comment pulse

- Spatial xeyes cannot follow the wearer → visionOS withholds gaze position from applications for privacy and security.
- Hardware remains the adoption barrier → one commenter abandoned purchase after prescription-lens friction; another admired the project but still rejected the headset.
- Linux alternatives exist → commenters suggested WayVR for native X11/Wayland or using Meta Quest as a dumb ALVR headset.

### LLM perspective

- **View:** Rootless windows are a natural XR mapping for X11 because the protocol already separates remote clients from display presentation.
- **Impact:** Owners gain a spatial front end for vintage workstations and modern Unix apps without replacing their existing software.
- **Watch next:** Test latency, multiwindow input, GLX compatibility, security on untrusted networks, and long-session ergonomics with real workloads.
