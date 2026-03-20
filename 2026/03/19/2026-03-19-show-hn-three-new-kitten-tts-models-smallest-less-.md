# Show HN: Three new Kitten TTS models – smallest less than 25MB

- Score: 295 | [HN](https://news.ycombinator.com/item?id=47441546) | Link: https://github.com/KittenML/KittenTTS

### TL;DR
Kitten TTS is a tiny, CPU-only, open‑source text‑to‑speech library built on ONNX, with 15M–80M parameter English models that fit in 25–80MB. It ships with 8 expressive voices, 24kHz output, simple Python APIs, and a browser demo. HN discussion praises its quality‑to‑size ratio and easy experimentation via tools like OpenClaw, but flags dependency bloat from a Spacy transformer chain, numeric pronunciation issues, unclear training data sources, and interest in additional languages like Japanese and more neutral voices.

---

### Comment pulse
- Lightweight TTS, heavy deps → installing via Python pulls Spacy transformers, Torch, and CUDA, wasting gigabytes for a CPU‑only model — counterpoint: can be wrapped via a thin CLI.
- Quality vs size impresses; 80M runs ~1.5× realtime on i7‑9700, but GPU gains unclear; some dislike current “cartoonish” voices, want more professional options.
- Users report poor number/units pronunciation and ask for preprocessing and model‑level fixes, plus transparency about training data and a dedicated Japanese model.

---

### LLM perspective
- View: Ultra‑small, CPU‑optimized TTS narrows the gap between cloud voices and fully offline, embeddable systems suitable for apps and devices.
- Impact: Indie devs and edge/IoT products gain viable on‑device speech without GPU or online APIs, easing privacy and latency concerns.
- Watch next: Numeric/text normalization benchmarks, multilingual releases, dependency slimming, and clear dataset/licensing disclosures for safe commercial adoption.
