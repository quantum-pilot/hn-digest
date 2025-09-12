# Liquid Glass in the Browser: Refraction with CSS and SVG

- Score: 487 | [HN](https://news.ycombinator.com/item?id=45174297) | Link: https://kube.io/blog/liquid-glass-css-svg/

- TL;DR
    - The post recreates Apple’s “Liquid Glass” in the browser using physics-based refraction (Snell’s law), convex/squircle profiles, precomputed displacement fields, and SVG feDisplacementMap (RG channels) plus a rim-light highlight. It composes as a Chrome-only backdrop-filter; dynamic shape changes require regenerating maps. Demos include a magnifier, switch, slider, and a music panel. HN praises the clear explanations but flags jank and potential battery cost, debating WebGL shaders for portability versus CSS/SVG for immediate DOM integration and first-paint visibility.

- Comment pulse
    - WebGL shaders are faster and cross‑browser → require canvas re-rendering; weaker DOM integration and first paint. — counterpoint: SVG/CSS shows immediately and fits existing UIs.
    - Performance is rough → scrolling stutters and heavy battery use feared, even on high‑end Macs; author acknowledges and shipped quick optimizations.
    - Chrome‑only backdrop‑filter is frustrating → but acceptable for showcasing an unavailable feature; some report Firefox feels smoother despite missing effects.

- LLM perspective
    - View: Smart use of precomputed, normalized displacement maps to mimic Snell-based refraction with SVG constraints.
    - Impact: Practical for Electron/Chromium apps and marketing sites; risky for core UX due to performance and energy costs.
    - Watch next: Benchmark shader-based versions (WebGL/WebGPU), measure power and jank; track SVG filter backdrop support and potential shader-like filter proposals.
