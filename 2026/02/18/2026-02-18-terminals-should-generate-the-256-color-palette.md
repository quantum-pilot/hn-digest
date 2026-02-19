# Terminals should generate the 256-color palette

- Score: 455 | [HN](https://news.ycombinator.com/item?id=47057824) | Link: https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783

### TL;DR
The author argues terminals should auto-generate the 256‑color palette from the user’s existing 16‑color (base16) theme. Today, 16 colors are too limiting, while truecolor needs per‑app configs and has weaker compatibility. The default 256 palette clashes with themes, has bad interpolation, and inconsistent contrast. Using LAB/OKLAB interpolation between base16 colors can create a consistent, readable, theme‑aware 256 palette, letting apps safely use richer color without custom theming. Discussion centers on stability vs dynamism, accessibility, and opt‑in/opt‑out/detection.

---

### Comment pulse
- Fixed 16–255 mappings aid cross‑terminal consistency; auto‑generated palettes make 256 colors as unpredictable as base16 — counterpoint: users, not apps, should own palette choice.  
- Many dislike apps inventing their own colors; they want semantic, sparse color that respects terminal themes. If you want “pretty,” use GUIs/web frontends.  
- Others see auto‑generation as obvious; related work uses HSV/OKLAB and tinted-theming. Practical worries: opt‑out, detection, and avoiding double‑transforming carefully themed apps.

---

### LLM perspective
- View: Treat 256 colors as a themeable palette layer, generated from user base16, while CLIs stick to indices instead of raw RGB.  
- Impact: Terminal emulators, TUI libraries, and theme ecosystems; users get consistent theming and better contrast without per‑app config sprawl.  
- Watch next: Convergence on LAB vs OKLAB, a standard env/OSC flag for “generated 256,” and adoption in major terminals plus shell‑level shims.
