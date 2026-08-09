# 5x5 Pixel font for tiny screens

- Score: 372 | [HN](https://news.ycombinator.com/item?id=47824943) | Link: https://maurycyz.com/projects/mcufont/

### TL;DR

A hand-drawn fixed-width bitmap font fits every included glyph inside 5×5 pixels and occupies 350 bytes, targeting tiny displays and 8-bit microcontrollers. Most lowercase letters are one pixel shorter than capitals, while the uniform 6×6 cell makes layout and numeric widths predictable. The author argues 5×5 is the smallest size preserving broad legibility, then explores compromises down to 2×2; 3×2 surprisingly beats 2×3 because letters carry more horizontal detail. Readers liked the result but noted incomplete ASCII, required spacing, and alternatives using subpixels, grayscale, or taller grids.

### Comment pulse

- A 1×5 subpixel demo remained barely readable when enlarged, showing physical display structure can become part of glyph design.
- Context can rescue blurred text at three horizontal pixels per character, though isolated letters cease being reliably identifiable.
- Glyph critique focused on lowercase `t` and `l`, whose current forms can resemble capitals or lose expected ascenders.

### LLM perspective

- Add an explicit glyph inventory and coverage table so memory comparisons include supported characters.
- Test recognition on actual monochrome and color panels across sizes, distances, and common visual impairments.
- Offer generated C tables for 5×5, 3×5, and editable user subsets without complicating the core.
