# A Decade of Slug

- Score: 363 | [HN](https://news.ycombinator.com/item?id=47416736) | Link: https://terathon.com/blog/decade-slug.html

### TL;DR

Ten years after creating Slug, Eric Lengyel explains how the GPU font renderer computes winding directly from Bézier curves, avoiding texture atlases while preserving antialiasing at any scale and perspective. He removed a modest band optimization, adaptive supersampling, and layered-emoji loops, simplifying shaders and halving band data; dynamic dilation now expands glyphs precisely half a viewport pixel. He also irrevocably disclaimed a patent otherwise lasting to 2038, dedicated the algorithm to the public domain, and released upgraded MIT reference shaders. HN celebrated the FOSS opening and its commercial success.

### Comment pulse

- FOSS barrier gone → developers who admired the technique can now implement it without patent risk, including terminals and game engines.
- Timed exclusivity found support → commercial licensing rewarded invention — counterpoint: some readers still oppose long software-patent terms.
- Product success impressed readers → the library served major game studios, Adobe, CAD, medical visualization, and Radical Pie.

### LLM perspective

- **View:** Releasing mature reference shaders makes the patent dedication actionable, not merely symbolic.
- **Impact:** Open-source renderers can adopt scale-independent GPU text without cached glyph images or license negotiations.
- **Watch next:** Independent ports, performance comparisons, font edge cases, and adoption beyond formerly licensed clients.
