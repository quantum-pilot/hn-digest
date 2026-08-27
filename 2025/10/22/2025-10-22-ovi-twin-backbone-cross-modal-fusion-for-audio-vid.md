# Ovi: Twin backbone cross-modal fusion for audio-video generation

- Score: 224 | [HN](https://news.ycombinator.com/item?id=45674166) | Link: https://github.com/character-ai/Ovi

### TL;DR

Ovi is an open audio-video generation model from Character AI and Yale researchers that simultaneously produces synchronized sound and five-second video from text or text-plus-image inputs. Its video branch starts from Wan2.2, while the team says it pretrained a five-billion-parameter audio branch on in-house data. The released tooling supports varied aspect ratios, prompt tags for speech and sound, quantized configurations, Gradio, and multi-GPU inference. Current requirements remain heavy, and planned work includes training code, longer clips, voice conditioning, distillation, and efficiency improvements.

### Comment pulse

- Readers welcomed open models built on Wan2.2 as competition for closed video generators.
- Demo reactions mixed amazement with uncanny-valley criticism, including visible anatomical artifacts.
- Some discussion warned that unrelated sites may appropriate new model names for opportunistic hosting.

### LLM perspective

- View: Joint generation is compelling, but five-second demos and substantial GPU needs keep the release research-oriented.
- Impact: Open weights and runnable code let creators inspect, adapt, and integrate synchronized generation locally.
- Watch next: Longer coherent clips, lower memory use, training-code release, and independent quality comparisons.
