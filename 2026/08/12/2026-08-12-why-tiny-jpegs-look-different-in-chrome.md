# Why tiny JPEGs look different in Chrome

- Score: 302 | [HN](https://news.ycombinator.com/item?id=49272549) | Link: https://guillaumetech.github.io/posts/jpg-scaling-chrome/

### TL;DR

Chrome can render a heavily downscaled JPEG differently because Skia and libjpeg-turbo perform partial inverse DCT decoding before final resampling. At one-eighth size, only each 8×8 block’s constant component is decoded, discarding gradients and edges; this saves substantial memory and work but made the example icon appear thicker. The author later emphasized that the final scaling algorithm also matters. The practical fix was SVG: JPEG’s photograph-oriented compression and browser-specific resizing behavior make it a poor format for tiny interface graphics.

### Comment pulse

- Similar PNG differences likely reflect resampling rather than partial IDCT, and one Electron upgrade visibly changed icons.
- Commenters recommended supplying appropriately sized sources instead of shrinking a 2000-pixel image to 20 pixels.
- Firefox is exploring partial-IDCT scaling; edge cases may expose malformed trailing JPEG block data.

### LLM perspective

- View: A decode optimization becomes visible semantics when assets are far outside their format’s intended use.
- Impact: Browser and app upgrades can silently alter icons, demanding cross-engine visual tests or vector assets.
- Watch next: Watch Firefox’s implementation, malformed-edge handling, and how resampler choices trade sharpness against blur and ringing.
