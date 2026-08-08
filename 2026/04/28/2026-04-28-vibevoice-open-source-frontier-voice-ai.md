# VibeVoice: Open-source frontier voice AI

- Score: 311 | [HN](https://news.ycombinator.com/item?id=47933236) | Link: https://github.com/microsoft/VibeVoice

### TL;DR

Microsoft’s VibeVoice repository groups open-weight speech models using 7.5Hz continuous tokenizers and next-token diffusion: a 7B ASR model transcribes 60-minute audio with speakers, timestamps, hotwords, and 50-plus languages; a 1.5B TTS model generates up to 90 minutes with four speakers; and a 0.5B streaming model targets 300ms first audio. Microsoft removed the original TTS code after misuse but later released newer components. Hacker News questioned the open source label because training remains proprietary and reported ASR hallucinations, slow inference, high memory use, and weak multilingual quality.

### Comment pulse

- Some users preferred Voxtral, Chatterbox Turbo, or Qwen TTS for speed and quality, treating repository attention as renewed hype.
- MIT-licensed weights permit broad use — counterpoint: absent training code and data prevent reproducibility and justify calling it open-weight.
- The repository mixes withdrawn and newer ASR/TTS variants, making its safety history and current offering easy to confuse.

### LLM perspective

- **View:** Model-family branding obscures component-specific maturity; ASR and TTS claims need separate evaluation.
- **Impact:** Local developers gain long-context speech tools, but resource demands may exclude ordinary hardware.
- **Watch next:** Independent word-error, diarization, hallucination, multilingual, latency, memory, and quantization tests across every published checkpoint.
