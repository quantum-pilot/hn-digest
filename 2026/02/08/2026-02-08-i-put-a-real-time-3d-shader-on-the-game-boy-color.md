# I put a real-time 3D shader on the Game Boy Color

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46935791) | Link: https://blog.otterstack.com/posts/202512-gbshader/

### TL;DR

Danny Spencer built a Game Boy Color demo that lights prerendered normal maps while the player moves an orbiting light. Without multiply or floating-point instructions, each pixel stores spherical coefficients in 8-bit linear/log space; multiplication becomes additions and lookups, reducing shading to three arithmetic operations and two reads. It processes at least 15 tiles per frame, consuming about 89% of the CPU budget, while self-modifying code saves roughly 10% of shader runtime. Commenters debated whether prerendered normals qualify as “3D,” praised the engineering and AI disclosure, and suggested environment maps.

### Comment pulse

- Visual plausibility beats numerical purity → lossy 8-bit math, tearing, LCD ghosting, and prerendered views are acceptable when the result reads correctly.
- Self-modification buys scarce cycles → patching an immediate subtraction avoids repeated memory loads across roughly 960 shaded pixels.
- AI helped at the edges → counterpoint: generated snippets worked, but the core assembly was slow, architecture-confused, error-prone, and rewritten.

### LLM perspective

- View: The project is a lesson in representation: precompute geometry, reformulate multiplication, and spend precision where perception notices.
- Impact: Retro developers gain a shading technique; modern engineers see how hardware limits drive algorithms, formats, and code structure.
- Watch next: Environment-map simplification, more objects, ROM-size tradeoffs, cycle measurements, hardware-display tests, and further lookup or empty-row optimizations.
