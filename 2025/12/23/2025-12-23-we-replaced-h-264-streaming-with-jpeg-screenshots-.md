# We replaced H.264 streaming with JPEG screenshots (and it worked better)

- Score: 117 | [HN](https://news.ycombinator.com/item?id=46367475) | Link: https://blog.helix.ml/p/we-mass-deployed-15-year-old-screen

### TL;DR

Helix's remote agent desktops used 60-fps H.264 over WebSockets after enterprise networks blocked WebRTC, but weak links accumulated stale TCP video and delayed input. The team added a fallback that disables video and serially polls 100–150 kB JPEG screenshots, preserving the WebSocket for controls; after fallback, users manually retry to prevent oscillation. It worked operationally, but HN experts argue JPEG is not inherently superior: the original 40 Mbps encoder, congestion handling, backpressure, and protocol choices were poorly configured.

### Comment pulse

- Serialization prevents backlog → each screenshot request waits for completion, so obsolete frames never queue behind newer ones.
- Codec comparisons are misleading → H.264 keyframe size and quality are configurable, and 40 Mbps is excessive for mostly static desktops.
- Older remote-desktop ideas fit better → VNC-style tiled diffs and scrolling operations could reduce bandwidth substantially.

### LLM perspective

- View: The fallback succeeds through bounded in-flight work, not because JPEG solves TCP congestion.
- Impact: Users retain responsive control on constrained networks, while maintainers inherit a deliberately coarse but understandable mode.
- Watch next: Benchmark tuned H.264, VNC-style damage updates, adaptive frame rates, queue depth, bandwidth probes, and full fallback latency.
