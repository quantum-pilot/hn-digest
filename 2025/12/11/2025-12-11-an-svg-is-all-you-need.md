# An SVG is all you need

- Score: 336 | [HN](https://news.ycombinator.com/item?id=46235959) | Link: https://jon.recoil.org/blog/2025/12/an-svg-is-all-you-need.html

### TL;DR
The post argues that a single self-contained SVG file can be a durable, portable container for interactive scientific figures: it can embed or fetch data, run client‑side computation, and provide sliders/buttons for exploration, all served from static hosting. A 20‑year‑old fungal‑network visualization still working in modern browsers is used as proof of SVG’s longevity. The author maps this to permanence, provenance, permission, and placement, and frames SVGs as one more tool alongside notebooks for remixable, reproducible research.

---

### Comment pulse
- SVG as application UI → People report success building full interfaces (choreography tools, chart sites) by emitting SVG from Python/JS, praising its math‑driven simplicity and crisp output.
- SVG’s rough edges → Inconsistent rendering, awkward text wrapping, font embedding, performance, and security concerns limit complex use—counterpoint: specs (SVG 2, WOFF, `<font>`) exist, but browser support lags.
- Interactive papers → Commenters like SVG‑backed, browser‑reproducible figures and note Distill‑style examples, but stress that only model‑based or light‑compute experiments are realistically rerun in‑browser.

---

### LLM perspective
- View: Treat SVG as a “portable lab bench” for specific figures: self‑contained, text‑diffable, and easy to archive, not a universal app platform.
- Impact: Most valuable for computational sciences, teaching materials, and exploratory data analysis where small, focused simulations accompany static papers.
- Watch next: Shared libraries/templates for “reproducible SVG figures,” guidance on safe embedding (no JS), and cross‑browser conformance tests for scientific publishers.
