# We replaced H.264 streaming with JPEG screenshots (and it worked better)

- Score: 117 | [HN](https://news.ycombinator.com/item?id=46367475) | Link: https://blog.helix.ml/p/we-mass-deployed-15-year-old-screen

### TL;DR
HelixML built a sophisticated H.264 streaming stack over WebSockets (to survive enterprise firewalls that block UDP/WebRTC), but real-world high-latency networks caused huge buffering and 30–45s lag. A desperate debug endpoint—polled JPEG screenshots over HTTP—turned out more robust: stateless frames, naturally rate-limited by request–response, and dramatically lower average bandwidth. They now run a hybrid: full H.264 at low RTT, automatic switch to 2–10 fps JPEG polling while keeping input over WebSockets. HN likes the story but disputes much of the codec reasoning.

---

### Comment pulse
- JPEG “fix” → Works because each request waits for completion, so only one frame is in-flight; TCP still buffers—counterpoint: article over-attributes this to JPEG itself.  
- H.264 claims wrong → 40 Mbps is overkill; encoder likely misconfigured. Proper bitrate control, short keyframes, DASH/HLS, or WebRTC would handle congestion better.  
- Alternatives → VNC-style tiled diffing or neko-like systems match coding workloads; commenters split between “fun, practical hack” and “sloppy, maybe LLM-written, reinvention of MJPEG.”  

---

### LLM perspective
- View: For text-heavy, low-motion desktops on hostile networks, pull-based JPEG/MJPEG remains a sane, low-risk baseline.  
- Impact: Remote dev/AI tools should prioritize resilient, debuggable fallbacks over perfect video, and separate input from bulk media.  
- Watch next: Benchmark JPEG polling vs tuned H.264 and VNC-style tiling under packet loss and high RTT; add simple bandwidth probing before redesigning again.
