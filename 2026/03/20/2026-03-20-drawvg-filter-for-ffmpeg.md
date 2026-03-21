# Drawvg Filter for FFmpeg

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47413879) | Link: https://ayosec.github.io/ffmpeg-drawvg/

### TL;DR
drawvg is a new FFmpeg filter (since 8.1) that renders vector graphics over video using a small purpose-built language, VGS (Vector Graphics Script), rasterized via Cairo. VGS gives FFmpeg a programmable 2D drawing layer: you can use expressions tied to time, frame size, metadata, or pixel colors to build progress indicators, smart crop overlays, custom transitions, pixelation, and displacement maps. HN discussion focuses on practical uses like censoring overlays, future ML-powered masking, and programmable annotations.

---

### Comment pulse
- Practical killer use: mask/censor talking‑head picture‑in‑picture overlays, including circular ones → drawvg beats older drawbox; scripting makes per‑video tuning easy.  
- Desire for ML integration: YOLO/SAM-style models could automate face censoring and content-aware edits → big concern about binary bloat; prefer pluggable, accelerated backends.  
- New vector layer suggests scripted annotations and effects in instructional videos → reproducible, text-based workflows beat GUI editors — counterpoint: some users just want simple runtime overlays or cropping.

---

### LLM perspective
- View: drawvg makes FFmpeg closer to a programmable compositor, not just a filter chain runner.  
- Impact: power users, automators, and tool vendors can ship shareable, text-based overlays, transitions, and visualizations.  
- Watch next: community VGS script libraries, wrappers in Python/Rust, and any move toward plugin ML filters for automatic masks.
