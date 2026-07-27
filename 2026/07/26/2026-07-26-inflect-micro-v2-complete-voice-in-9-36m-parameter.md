# Inflect-Micro-v2: complete voice in 9.36M parameters

- Score: 198 | [HN](https://news.ycombinator.com/item?id=49053375) | Link: https://huggingface.co/owensong/Inflect-Micro-v2

- TL;DR  
  Inflect-Micro-v2 is a 9.36M‑parameter, Apache‑licensed English TTS model that generates 24 kHz audio locally from text, including long passages, with deterministic seeds and speed/variation controls. Despite its tiny 37.5 MB FP32 footprint, benchmarks show strong naturalness and intelligibility, beating several larger local TTS baselines while running >6× real-time on CPU. It has one fixed synthetic male voice and no STT or voice cloning, but includes an experimental toolkit for adapting new voices or languages. HN commenters praise its quality and lightweight deployment.

- Comment pulse  
  - Some praise surprisingly natural output for 9M params and swapped it into projects; others clarify “complete” means full TTS pipeline, not STT.  
  - Discussion asks why TTS is popular; replies cite voice interfaces for local LLMs and Home Assistant, making offline conversational agents feel natural.  
  - Curiosity about running it on microcontrollers contrasts with reports that PC inference is already lightweight; some still find prosody slightly weird but far from robotic.

- LLM perspective  
  - View: Shows how far compact VITS-style models can go; near state-of-the-art local TTS no longer needs huge GPUs.  
  - Impact: Enables high-quality offline narration, assistants, games, and accessibility tools on modest CPUs or edge devices.  
  - Watch next: Community adaptations adding more voices/languages, aggressive quantization, and potential integration with small STT for fully local speech stacks.
