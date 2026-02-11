# Pure C, CPU-only inference with Mistral Voxtral Realtime 4B speech to text model

- Score: 281 | [HN](https://news.ycombinator.com/item?id=46954049) | Link: https://github.com/antirez/voxtral.c

- TL;DR  
A self-contained C implementation of Mistral’s 4B Voxtral Realtime speech-to-text model runs on CPU (BLAS) or Apple Silicon GPUs (MPS) with no nonstandard dependencies. It supports streaming transcription, stdin piping via ffmpeg, a C streaming API, and a small Python reference script. Benchmarks show real-time or better performance on high-end Apple Silicon, but HN users report it’s currently too slow on typical CPUs, comparing it with Whisper.cpp, Parakeet V3, voxtype, and Mistral’s own hosted Voxtral API.

- Comment pulse  
  - Local STT options compared: Handy+Parakeet, Whisper.cpp, voxtype, and Mistral Voxtral API; many find Voxtral.c too slow on CPU-only setups — counterpoint: MPS backend is notably faster.  
  - Several see Voxtral 4B as oversized for everyday local use; author suggests smaller models like Qwen 0.6 plus 8‑bit quantization as better CPU targets.  
  - Users want continuous, on-screen, real-time transcription and easy mic/monitor capture; Linux users struggle to replicate macOS `--from-mic` flow using ffmpeg.

- LLM perspective  
  - View: Pure-C, no-deps inference pipelines are valuable reference implementations and baselines for optimization, independent of heavyweight runtimes.  
  - Impact: Benefits embedded, on-prem, and regulated environments where Python stacks, CUDA, or cloud APIs are undesirable or impossible.  
  - Watch next: Optimized CPU kernels, quantized variants, official smaller models, and better cross-platform audio capture/streaming glue around these runtimes.
