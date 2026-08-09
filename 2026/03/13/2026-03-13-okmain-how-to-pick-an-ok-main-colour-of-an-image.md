# Okmain: How to pick an OK main colour of an image

- Score: 237 | [HN](https://news.ycombinator.com/item?id=47309397) | Link: https://dgroshev.com/blog/okmain/

### TL;DR

Okmain extracts a visually pleasing representative image colour by clustering pixels in Oklab instead of averaging an entire sRGB image. It uses at most four clusters, weights central pixels, favors chroma, and retries with fewer clusters when colours are too similar. Images are downsampled below 250,000 pixels; Rust auto-vectorization helps reach roughly 100 milliseconds, with Python bindings available. HN praised the perceptual approach, discussed defensive image decoding and memory use, and suggested applications from album-art dashboards to distant-object rendering.

### Comment pulse

- Averaging in gamma-corrected sRGB creates muddy results → perceptual-space clustering preserves more convincing mixtures.
- Thumbnailing reduces noise and computation → counterpoint: callers still need safe decoders and input-size controls against hostile images.
- LLM agents accelerated scaffolding and debug tools → the author rewrote hot paths after subtle errors and poor abstractions.

### LLM perspective

- **View:** The heuristics are transparent enough to tune, unlike semantic black-box colour selection.
- **Impact:** UI and rendering systems gain better defaults without a heavy vision model.
- **Watch next:** Memory benchmarks, adversarial-image tests, SIMD dispatch, and comparisons with Android Palette and ColorThief.
