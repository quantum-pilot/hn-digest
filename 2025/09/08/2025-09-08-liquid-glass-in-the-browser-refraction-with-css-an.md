# Liquid Glass in the Browser: Refraction with CSS and SVG

- Score: 487 | [HN](https://news.ycombinator.com/item?id=45174297) | Link: https://kube.io/blog/liquid-glass-css-svg/

### TL;DR

The tutorial recreates Apple-like refractive interface elements using refraction calculations, generated SVG displacement maps, CSS filters, and a separate specular-highlight layer. It models several curved surface profiles, precomputes symmetric displacement magnitudes, encodes X and Y offsets into image color channels, and applies the result behind ordinary HTML. The approach can render on the first frame without moving the page into a canvas, but true backdrop refraction currently depends on a Chromium-only extension. Dynamic resizing is expensive, and the author labels the prototype experimental and under-optimized.

### Comment pulse

- WebGL alternatives offer wider browser support and faster shaders, but cannot directly refract existing DOM content without re-rendering it.
- Readers reported heavy scrolling jank; the author acknowledged several unoptimized visualizations and made an initial performance fix.

### LLM perspective

- View: The technique is strongest as an optics lesson and constrained enhancement, not a production-wide design system.
- Impact: Precomputed SVG maps preserve normal HTML composition, trading shader flexibility for DOM integration and first-frame rendering.
- Watch next: Standardized backdrop filters, resizing costs, GPU acceleration, accessibility fallbacks, battery use, and open-source cleanup.
