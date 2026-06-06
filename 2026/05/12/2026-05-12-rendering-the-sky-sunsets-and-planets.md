# Rendering the Sky, Sunsets, and Planets

- Score: 392 | [HN](https://news.ycombinator.com/item?id=48107997) | Link: https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/

### TL;DR
Heckel walks through building a physically based sky and planetary-atmosphere renderer in WebGL/React Three Fiber, starting from first principles of atmospheric scattering. He models Rayleigh, Mie, and ozone effects via raymarching and lightmarching, adds depth-aware post-processing so the atmosphere interacts with scene geometry, and extends it to spherical planet shells with eclipses and Martian skies. To make it performant, he experiments with Sebastian Hillaire–style LUTs for transmittance, sky color, and aerial perspective, trading some accuracy and generality for speed.

---

### Comment pulse
- Technical inspiration → Readers link related work by Sebastian Lague, Nishita et al., and personal engine experiments, reinforcing that Rayleigh/Mie models give huge visual payoff.
- Physical accuracy nit → Twilight shouldn’t vanish as soon as the sun sets; real sky stays lit until ~18° below horizon — counterpoint: might be out-of-scope for a demo.
- Practical excitement → People praise the depth and polish, noting how browsers/phones now handle atmospheric scattering once limited to offline or desktop engines.

---

### LLM perspective
- View: The article is a rare full-stack walkthrough: physics, GLSL, engine integration, and performance engineering in one coherent pipeline.
- Impact: Web/indie graphics devs gain a reusable blueprint for “AAA-looking” skies and planets without custom engines or C++.
- Watch next: Benchmarks of LUT vs full raymarch, WebGPU compute-based versions, and more accurate twilight/eclipses would round this out into a reference implementation.
