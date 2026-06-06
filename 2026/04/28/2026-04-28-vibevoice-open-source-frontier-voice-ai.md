# VibeVoice: Open-source frontier voice AI

- Score: 311 | [HN](https://news.ycombinator.com/item?id=47933236) | Link: https://github.com/microsoft/VibeVoice

## TL;DR
Microsoft’s VibeVoice is a family of MIT‑licensed voice models for long‑form ASR, multi‑speaker TTS, and lightweight realtime TTS. It uses ultra‑low‑rate continuous audio tokenizers plus an LLM‑driven diffusion decoder to handle hour‑scale sequences, structured transcripts (who/when/what), hot‑word steering, and multilingual audio. Hacker News discussion is cautious: several users report hallucinations, slow and heavy inference and weak multilingual ASR, question branding it as “open source” without training code, and point to alternatives like Mistral’s Voxtral.

## Comment pulse
- ASR quality criticized → users see frequent hallucinations, noisy training effects, large memory use and slow inference; some note slightly more expressive behavior than competitors.  
- Not truly open source → only weights/inference are MIT; training pipeline opaque, prompting calls for “open‑weights” term — counterpoint: usage rights trump methodology disclosure.  
- Alternatives and history → some recommend Mistral’s Voxtral for lighter realtime use; others flag past Microsoft takedown and a security researcher’s critical backstory.  

## LLM perspective
- View: Feels like a research showcase for ultra‑long‑context speech, not yet a drop‑in for production assistants or transcription services.  
- Impact: Raises expectations that future voice stacks will unify recognition, speaker attribution, and synthesis, instead of today’s brittle multi‑component pipelines.  
- Watch next: Independent benchmarks including latency/VRAM, rigorous hallucination studies, and clearer norms around using “open‑source” versus “open‑weights” in model marketing.
