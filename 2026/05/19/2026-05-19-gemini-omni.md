# Gemini Omni

- Score: 268 | [HN](https://news.ycombinator.com/item?id=48196609) | Link: https://deepmind.google/models/gemini-omni/

### TL;DR
Gemini Omni is Google DeepMind’s new multimodal model focused on conversational video creation and editing: you describe changes in natural language and it transforms or remixes input videos, images, audio, and text while preserving scene coherence, style, and motion. It aims to respect real‑world physics and domain knowledge for explainers, supports multi‑step edits, style/motion transfer, and character swapping, and ships with watermarking (SynthID, C2PA) plus extensive red‑teaming. HN finds the visuals striking but questions physical/spatial fidelity and non‑video performance.

---

### Comment pulse
- Rigid‑body test prompts (e.g., Jenga tower collapse) reveal discontinuous, nonphysical motion; videos feel like “dreams” of dynamics—counterpoint: better 3D pipelines might let transformers learn realistic physics.

- Viewers notice geometry popping or changing when re‑entering view, suggesting no robust 3D scene model; some want “ugly but accurate” floorplan‑driven flythrough models and more curated, hierarchical training.

- On an Agentic SQL benchmark Omni scores 19/25 and is slower and costlier than earlier Gemini/Gemma; several users say Seedance 2 currently produces stronger video, albeit under heavy copyright censorship.

---

### LLM perspective
- View: The differentiator is unified, conversational control over complex video edits, not absolute state‑of‑the‑art in dynamics or text reasoning.

- Impact: Short‑form creators, marketers, and educators gain rapid prototyping; high‑precision simulation, graphics, and data‑heavy workflows still favor specialized tools.

- Watch next: Independent tests of long, uncut sequences, occlusion handling, physics benchmarks, and clear pricing/limits versus rivals will determine real adoption.
