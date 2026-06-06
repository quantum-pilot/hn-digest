# Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency

- Score: 236 | [HN](https://news.ycombinator.com/item?id=48414653) | Link: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/

### TL;DR
Google is releasing quantization‑aware training (QAT) checkpoints for Gemma 4, targeting 4‑bit Q4_0 and a new mobile‑specialized format. By simulating quantization during training, they preserve more quality than standard post‑training quantization while greatly shrinking memory: the E2B edge model can run text‑only in under 1 GB, with multimodal variants around a few GB. HN discussion focuses on real on‑device usage, QAT vs other quant schemes (like Unsloth’s), and VRAM/benchmark transparency.

---

### Comment pulse
- On‑device is here → Users run 2B Gemma locally on Macs/phones; ~0.8–3.2GB multimodal models handle audio, images, basic coding and SVG generation.  
- Quantization details matter → Debate over Google QAT vs Unsloth quants, BF16 vs 4‑bit metrics, and missing 4–8‑bit benchmarks — counterpoint: QAT Q4_0 isn’t trivial repacking.  
- Strategy and positioning → People praise Gemma’s fast ecosystem growth, note awkward staggered 12B/Q4_0 releases, speculate about WWDC/Siri tie‑ins, and question Google’s RAM support messaging.

---

### LLM perspective
- View: QAT + mobile‑specific schemes show big labs now optimizing for real consumer hardware, not just datacenter benchmarks.  
- Impact: Enables serious multimodal assistants on laptops/phones without cloud, shifting some workloads and privacy expectations to on‑device.  
- Watch next: Side‑by‑side 4/6/8‑bit benchmarks, community quants vs official QAT, and tighter integration into OS‑level assistants and app stores.
