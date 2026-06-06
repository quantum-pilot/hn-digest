# Multi-stroke text effect in CSS

- Score: 330 | [HN](https://news.ycombinator.com/item?id=48032265) | Link: https://yuanchuan.dev/multi-stroke-text-effect-in-css

### TL;DR
- Explores recreating a retro multi-stroke text effect in CSS by stacking multiple copies of the same glyph, each with different `-webkit-text-stroke-width` and colors, orchestrated via the css-doodle web component’s mini-language. The article investigates how browsers outline text differently (Firefox’s smoother distance-based expansion vs Chrome/Safari’s cusp-preserving spikes) and shows how font choice changes the final look. Due to heavy performance costs at large sizes, it’s framed as a playground for generative art, not production UI.

### Comment pulse
- css-doodle makes these cryptic @grid/@content rules usable → a custom element runs its own CSS-like language to generate visual patterns without app code.
- Stroke rendering differs by engine → Firefox uses distance-based expansion; Chrome/Safari retain cusps, creating spiky outlines—counterpoint: others feel Firefox’s rounding looks wrong for sharp shapes.
- Readers rediscover modern CSS → people who left frontend are surprised by today’s expressive power and praise the blog’s minimalist, experiment-focused design.

### LLM perspective
- View: Clever compositing of strokes shows how generative art can emerge from standard CSS primitives plus small DSLs.  
- Impact: Frontend tinkerers gain another alternative to Canvas/SVG for lightweight posters, logos, and procedural typography experiments.  
- Watch next: Standardized multi-stroke text properties, better GPU-accelerated text effects, or tooling that bakes these CSS artworks into static assets.
