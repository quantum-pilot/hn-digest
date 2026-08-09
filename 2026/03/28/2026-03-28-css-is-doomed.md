# CSS is DOOMed

- Score: 144 | [HN](https://news.ycombinator.com/item?id=47557960) | Link: https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/

### TL;DR

An experimental DOOM renderer builds every wall, floor, sprite, projectile, and effect from HTML elements, leaving JavaScript to run game logic and feed coordinates while CSS handles 3D transforms, trigonometry, clipping, animation, lighting, billboarding, and responsive HUD placement. Modern features such as `hypot()`, `atan2()`, `@property`, anchor positioning, and `shape()` make the separation surprisingly capable. HN found it playable and impressive across browsers, but the author says thousands of transformed elements require manual culling, expose compositor bugs, crash some phones, and cannot compete with WebGL or WebGPU.

### Comment pulse

- Pure CSS logic remains impractical for real-time play, despite demonstrations of CSS CPUs; JavaScript is still essential here.
- Deleting wall divs enables literal wall hacks, making developer tools part of the joke.
- Firefox users reported smooth rendering but broken Alt-based controls; some found Chromium choppier and Safari mobile unexpectedly strong.

### LLM perspective

- **View:** The demo succeeds as a browser stress test and CSS showcase, not as an argument for DOM-based game engines.
- **Impact:** Web developers gain concrete examples of production-ready math, typed properties, clipping, filters, anchors, and compositing behavior.
- **Watch next:** Bug reports, wider `if()` and `random()` support, automatic compositor culling, input fixes, profiling, and browser-specific stability.
