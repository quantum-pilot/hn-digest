# Krea 2: SOTA open-weights 12B image model

- Score: 324 | [HN](https://news.ycombinator.com/item?id=48646659) | Link: https://www.krea.ai/blog/krea-2-technical-report

### TL;DR

Krea 2 is a 12B open-weights image-generation family built for aesthetic breadth and steerability rather than one polished house style. Krea releases hackable RAW and eight-step Turbo variants, including mid- and post-training checkpoints, with weights and inference under permissive licenses. Training spans curated nonsynthetic pretraining data, SFT, preference optimization, RL, prompt expansion, and multi-image style references. The model ranks among the top 10 text-to-image systems. HN praised Turbo’s local speed and unusually detailed report, while questioning whether text-to-image gains matter as much as robust editing, consistency, and agentic composition.

### Comment pulse

- Turbo punches above its speed class → an independent 15-test comparison placed it highest among locally hostable models except slower Ideogram 4.
- Open checkpoints expand experimentation → RAW targets fine-tuning, while separate mid- and post-training states expose stages rarely released by image-model labs.
- The frontier may have shifted → diverse text generation helps moodboarding — counterpoint: critics prioritize editing, character consistency, and general image-to-image control.

### LLM perspective

- **View:** The release’s durable value is reproducibility: checkpoints plus infrastructure detail let outsiders study not only outputs but training decisions.
- **Impact:** Creators gain local control and style mixing; researchers inherit a baseline; closed providers face transparency and pricing pressure.
- **Watch next:** Benchmark editing, prompt fidelity, style-content leakage, multilingual text, VRAM needs, Turbo latency, and community fine-tunes within license terms.
