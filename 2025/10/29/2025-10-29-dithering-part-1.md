# Dithering – Part 1

- Score: 448 | [HN](https://news.ycombinator.com/item?id=45750954) | Link: https://visualrambling.space/dithering-part-1/

- TL;DR
    - Interactive explainer shows how ordered dithering turns grayscale into black/white patterns whose densities read as shades. It contrasts hard thresholding with threshold-map patterns and tees up future parts on matrix design and error diffusion. Commenters debate terminology (halftone vs dithering) and whether the shades are an "illusion" or simply low‑pass averaged by human vision. Several note banding in ordered methods and point to error diffusion/noise as a fix. Others share learning resources and applaud the execution.

- Comment pulse
    - This is halftoning, not dithering → deterministic matrices band; dithering uses noise to hide banding — counterpoint: ordered dithering is widely accepted terminology.
    - Illusion vs reality → low‑pass filtering reveals true average tones; vision is the filter — counterpoint: up close, you still see only black/white pixels.
    - Banding and methods → ordered patterns show bands; error diffusion reduces them but adds grain and computational cost.

- LLM perspective
    - View: Treat ordered dithering as deterministic halftoning; reserve 'dithering' for noise/error-diffusion when clarity matters.
    - Impact: Useful for e‑ink, two‑color UIs, retro games, and print; algorithm choice trades banding, grain, and performance.
    - Watch next: Publish threshold-matrix generation and code; compare algorithms on MTF/PSNR and perceptual tests; include colored dithering, blue-noise masks.
