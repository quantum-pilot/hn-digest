# Recall for Linux

- Score: 505 | [HN](https://news.ycombinator.com/item?id=45718231) | Link: https://github.com/rolflobker/recall-for-linux

- TL;DR
  - A satirical “Recall for Linux” repo mocks Microsoft Recall yet actually works: a tiny local loop takes 5‑second screenshots, OCRs them with tesseract, and saves text/images to ~/.recall. HN splits between “useful if open, local, encrypted” and “inherently risky surveillance.” People cite real uses (audits, memory, cross‑app search) and point to alternatives and caveats: unencrypted stores, unauthenticated UIs, Wayland gaps, and hefty disk/CPU needs. Some view this as a minimal, transparent pattern rather than a product.

- Comment pulse
  - Useful if local, open, encrypted → aids memory, billing, and cross-app search; examples include ActivityWatch, Dayflow, screenpipe.
  - Inherent privacy risk → continuous screenshots capture others’ data; open/local builds still ship unencrypted stores, unauthenticated UIs — counterpoint: strict locality reduces exposure.
  - Practicalities → storage/compute heavy (e.g., 10+ GB per 8h), Wayland gaps; the repo’s bash loop with grim+tesseract shows a minimal working pattern.

- LLM perspective
  - View: OS-level recall is acceptable only if opt-in, local-first, encrypted-by-default, and easily paused with visible indicators.
  - Impact: Expect growth in personal search pipelines using OCR+embeddings; better PKM tools and desktop portals will follow.
  - Watch next: benchmarks for disk/CPU/privacy tradeoffs, default encryption schemes, Wayland/X11 APIs, and audited local models for on-device indexing.
