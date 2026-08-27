# Dithering – Part 1

- Score: 448 | [HN](https://news.ycombinator.com/item?id=45750954) | Link: https://visualrambling.space/dithering-part-1/

### TL;DR

This interactive introduction explains ordered dithering by reducing grayscale images to black and white while preserving apparent tones through pixel density. Each input pixel is compared with a repeating threshold map: values above the local threshold become white, otherwise black. Strategically distributed outcomes retain shadows and gradients better than simply rounding every pixel to its nearest color. The article stops before explaining threshold-map construction or error diffusion, reserving those for later parts. Commenters praised its presentation while debating terminology and whether perceived gray is an illusion.

### Comment pulse

- One critique distinguished deterministic halftoning from noise-based dithering; replies noted “ordered dithering” remains accepted terminology.
- Others framed vision and viewing distance as a low-pass filter that turns binary spatial patterns into genuinely perceived intermediate intensity.

### LLM perspective

- View: The presentation succeeds by making the threshold decision spatial and visible before introducing algorithmic variants.
- Impact: Learners gain an intuitive bridge from quantization artifacts to pattern-based tone preservation.
- Watch next: Compare Bayer-style threshold maps, error diffusion, banding, resolution, and color-channel behavior in subsequent parts.
