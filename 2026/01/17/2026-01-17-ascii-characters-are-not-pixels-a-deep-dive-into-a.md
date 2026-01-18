# ASCII characters are not pixels: a deep dive into ASCII rendering

- Score: 774 | [HN](https://news.ycombinator.com/item?id=46657122) | Link: https://alexharri.com/blog/ascii-rendering

- TL;DR  
  The author builds an image‑to‑ASCII renderer that treats characters as shaped glyphs rather than pixel-like blocks. They sample each cell with multiple “sampling circles” to create 6‑dimensional shape vectors, then choose characters via nearest‑neighbor search in that space. Two stages of contrast enhancement—global and directional, using exponents and neighboring samples—sharpen edges between regions. Performance comes from kd‑trees, aggressive caching with quantized keys, and GPU-based sampling. HN readers discuss math tweaks, related rendering work, and AI-generated imagery.

- Comment pulse  
  - Distance math and speedups → use cosine / matrix multiply, skip square roots; author already caches and GPUs, but readers note further micro-optimizations.  
  - Craft of rendering deep-dives → comparisons to Obra Dinn’s dithering post; others adapting ideas to braille graphics where contrast and edge alignment matter.  
  - Synthetic Saturn image debate → some decry fake astronomy; others predict frictionless AI asset generation will replace manual searching like calculators and the web did.

- LLM perspective  
  - View: Treat glyphs as high-dimensional shapes, not grayscale tiles, enabling smarter symbol choices than naive luminance mapping.  
  - Impact: Terminal art, low-res displays, and accessibility tech (braille, e-ink) can gain apparent resolution without extra pixels or bandwidth.  
  - Watch next: Learn sampling patterns automatically, benchmark against human perception, and experiment with learned glyph embeddings plus approximate nearest-neighbor search.
