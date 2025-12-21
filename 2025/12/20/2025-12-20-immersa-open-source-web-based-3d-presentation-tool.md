# Immersa: Open-source Web-based 3D Presentation Tool

- Score: 123 | [HN](https://news.ycombinator.com/item?id=46336097) | Link: https://github.com/ertugrulcetin/immersa

### TL;DR
Immersa is an open-source, browser-based 3D presentation editor built with ClojureScript and Babylon.js. You arrange 3D models, images, and text in a 3D scene; each “slide” is a keyframe, and Immersa interpolates positions, rotations, and scales between slides to create smooth transitions. It runs fully client-side using IndexedDB for persistence and supports GLB models, 3D text, undo/redo, keyboard shortcuts, and export/import. HN commenters compare it to Keynote’s Magic Move, suggest 3D video use, and discuss UX and implementation choices.

---

### Comment pulse
- Similarity to Keynote → Magic Move already offers object-interpolated slide transitions; this is a web/open alternative focused on explicit 3D scenes.
- Use cases → People want a “3D PowerPoint” and see potential as a simple 3D movie maker with autoplay, durations, and interpolation controls.
- Architecture/implementation → Slide-per-transition UX might explode slide count; author is open to PRs. Commenters praise the small, clean ClojureScript/re-frame codebase versus larger TS editors.

---

### LLM perspective
- View: Treat slides as animation keyframes; consider adding intra-slide timelines for complex sequences without slide bloat.
- Impact: Lowers barrier for educators, product teams, and 3D artists to build lightweight 3D explainer content without full DCC tools.
- Watch next: Benchmarks on large decks, richer easing/timing controls, and templates for common 3D storytelling patterns.
