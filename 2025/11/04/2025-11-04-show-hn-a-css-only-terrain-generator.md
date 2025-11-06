# Show HN: A CSS-Only Terrain Generator

- Score: 312 | [HN](https://news.ycombinator.com/item?id=45811093) | Link: https://terra.layoutit.com

- TL;DR
  - Layoutit Terra is a browser-based terrain generator whose final output is pure HTML/CSS: isometric tiles, biomes, camera controls, and exports (heightmap, PNG, VOX, CSS). The site uses JavaScript for the editor and interactivity; with JS disabled you see a loader, but downloaded or CodePen exports render without scripts. HN loved the SimCity/Populous/TTD nostalgia, while some criticized the “CSS-only” title as misleading. Net: impressive CSS rendering, clear generator-vs-artifact split, and a polished UI.

- Comment pulse
  - Not truly CSS-only → demo page relies on JS; disabling it shows a loader — counterpoint: exported HTML/CSS or CodePen renders terrain without scripts.
  - Rendering vs tooling → CSS handles isometric tiles; JS powers editing, camera, and drag tools; a more accurate name: “Generator for CSS‑only terrain”.
  - Nostalgia factor → evokes RollerCoaster Tycoon, SimCity 2000/3000, Populous, OpenTTD; the raise/lower mechanic especially triggers classic isometric vibes.

- LLM perspective
  - View: Clean separation: JS for UX; CSS for final artifact. Demonstrates CSS 3D transforms and layered tiles at scale.
  - Impact: Handy for education, design previews, and no-script embeds; export to PNG/VOX/heightmaps enables workflows beyond web.
  - Watch next: Add JS-free demo fallback, colorblind-safe palettes, large-map performance numbers, mobile gestures, browser compatibility matrix.
