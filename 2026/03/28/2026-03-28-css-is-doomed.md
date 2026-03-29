# CSS is DOOMed

- Score: 144 | [HN](https://news.ycombinator.com/item?id=47557960) | Link: https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/

### TL;DR
A developer rebuilt classic DOOM so its entire 3D rendering pipeline runs in CSS, with JavaScript only driving the game loop and updating a few custom properties. Walls, floors, sprites, projectiles, doors, lifts, lighting, and even spectator camera math are implemented via CSS transforms, trig functions, `@property`, `clip-path`, filters, and keyframe animations. The project exposes both how powerful modern CSS has become and how fragile browser compositors are when pushed into quasi–3D-engine territory.

---

### Comment pulse
- Browser game nostalgia → People recall early “LOL a big game in a browser!” jokes; now DOOM and Quake-like experiences are normal—counterpoint: still far from native-engine performance.
- Cross-browser behavior → Runs smoothly in Firefox and Safari mobile, more choppy in Chromium; default Alt bindings conflict with browser shortcuts, and mobile play surprisingly works.
- Pure CSS potential → With CSS-based CPUs now possible, some wonder about fully CSS DOOM; author notes such techniques are far too slow for a real-time game loop.

---

### LLM perspective
- View: This is a stress test and showcase for modern CSS, not a practical rendering strategy for serious games.
- Impact: Frontend engineers gain concrete patterns for using trig, custom properties, and animations to offload UI logic to CSS.
- Watch next: Better compositor diagnostics, broader support for `if()` in CSS, and demos benchmarking complex 3D-ish UIs across browsers.
