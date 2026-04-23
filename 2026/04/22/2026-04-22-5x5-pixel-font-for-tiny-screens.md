# 5x5 Pixel font for tiny screens

- Score: 372 | [HN](https://news.ycombinator.com/item?id=47824943) | Link: https://maurycyz.com/projects/mcufont/

### TL;DR
Author designs a 5x5 monospaced pixel font optimized for tiny OLEDs and 8‑bit microcontrollers, arguing it’s the smallest grid that preserves clear Latin letters, digits, and case distinction. The font fits a 6x6 layout, occupies ~350 bytes, and beats tiny vector fonts in sharpness and resource use. They systematically explore progressively smaller grids (3x5 down to 2x2), showing how glyph distinctiveness collapses. HN comments add subpixel/grayscale tricks, ASCII-coverage concerns, CJK constraints, and minor glyph‑shape suggestions.

---

### Comment pulse
- 5x5 and 3x5 praised → but lack full ASCII and require extra spacing; some prefer existing 4x8/5x8 bitmap sets like Spleen for completeness.  
- Subpixel and grayscale rendering → 1x5 or 3‑pixels‑wide text becomes surprisingly readable using RGB subpixels and multi‑level brightness—counterpoint: demands ideal screens and careful viewing distance.  
- Typography details and scripts → readers suggest tweaking lowercase t and l shapes, and note separate challenges designing ultra‑small CJK bitmap fonts.

---

### LLM perspective
- View: Meticulous low‑pixel font design still matters, outperforming generic vector fonts on constrained hardware and preserving human legibility limits.  
- Impact: Encourages microcontroller, retro, and wearable projects to ship sharper UIs by investing hundreds of bytes in custom bitmap typefaces.  
- Watch next: Empirical tests of reading speed and accuracy across 5x5, 3x5, and subpixel/grayscale approaches on OLED and LCD panels.
