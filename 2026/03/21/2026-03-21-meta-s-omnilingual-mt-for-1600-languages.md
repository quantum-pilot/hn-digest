# Meta's Omnilingual MT for 1,600 Languages

- Score: 112 | [HN](https://news.ycombinator.com/item?id=47421749) | Link: https://ai.meta.com/research/publications/omnilingual-mt-machine-translation-for-1600-languages/?_fb_noscript=1

### TL;DR

Meta’s Omnilingual Machine Translation expands claimed coverage beyond 1,600 languages, targeting the gap between recognizing low-resource text and generating it faithfully. Its data mix combines public corpora, manually curated MeDLEY bitext, mining, synthetic backtranslation, and new evaluation sets for quality and toxicity. Two specialized families—decoder-only OMT-LLaMA and encoder–decoder OMT-NLLB—span 1B to 8B parameters and reportedly match or beat a 70B baseline. Commenters welcomed the scale but questioned real-world quality, downloadable weights, and whether the underlying long-tail data is clean enough.

### Comment pulse

- Khmer users reported sharply different experiences, from superior paragraph-level context to formal, robotic output and weak Chinese performance.
- Low-resource builders say language identification and mixed-language documents are harder bottlenecks than merely collecting more web text.
- Free evaluation datasets are explicit, but readers could not find a clear promise or direct release of model weights.

### LLM perspective

- **View:** Language count is a coverage metric, not proof that each direction is useful or culturally natural.
- **Impact:** Small specialized models could bring translation to constrained devices and communities excluded by dominant-language LLMs.
- **Watch next:** Native-speaker evaluation, per-language errors, weight licensing, and reproducible comparisons against commercial systems.
