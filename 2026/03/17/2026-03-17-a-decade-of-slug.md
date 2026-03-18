# A Decade of Slug

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47416736) | Link: https://terathon.com/blog/decade-slug.html

## TL;DR
Slug is a GPU font and vector rendering algorithm that draws directly from Bézier outlines—no glyph texture atlases—while remaining robust to floating‑point errors and fast enough for consoles. Over ten years it dropped rarely-useful optimizations (band splitting, tiny-text supersampling, emoji layering in one shader) to simplify shaders and reduce memory. The major new feature, dynamic dilation, analytically adjusts glyph bounds per-vertex to guarantee half‑pixel coverage with minimal overdraw. The author has now disclaimed the patent and published MIT‑licensed reference shaders, enabling unrestricted use, including FOSS.

---

## Comment pulse
- Patent dedication welcomed → previously, licensing blocked FOSS; 8-ish-year practical exclusivity feels fair to many—counterpoint: some still oppose software patents entirely.  
- Slug’s engineering praised → users report high quality and elegance in production, calling it a model of carefully designed graphics software.  
- Radical Pie noted → commercial Windows equation editor showcases Slug, but some see the market as niche and increasingly non-Windows-centric.

---

## LLM perspective
- View: A mature, production-proven GPU text algorithm becoming patent-free plus MIT shaders lowers the barrier to high-end font rendering.  
- Impact: Game engines, scientific/CAD tools, terminal emulators, and FOSS UI stacks can adopt outline-on-GPU text without legal friction.  
- Watch next: Independent reimplementations, benchmarks against SDF/MSDF pipelines, and possible integration into libraries like Skia, FreeType frontends, or ImGui-like toolkits.
