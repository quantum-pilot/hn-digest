# Pure C, CPU-only inference with Mistral Voxtral Realtime 4B speech to text model

- Score: 281 | [HN](https://news.ycombinator.com/item?id=46954049) | Link: https://github.com/antirez/voxtral.c

### TL;DR

Voxtral.c recreates Mistral’s 4-billion-parameter streaming speech recognizer in readable C, plus a compact Python reference, avoiding vLLM and Python at inference. It memory-maps 8.9GB of BF16 weights, bounds long-audio memory with overlapping encoder chunks and a rolling 8,192-position cache, and exposes file, stdin, macOS microphone, and incremental C APIs. On an M3 Max, Metal runs about 2.5 times faster than real time; BLAS is far slower. Commenters praised the lean implementation but found CPU and older-Mac performance impractical, preferring smaller local models or hosted transcription for daily use.

### Comment pulse

- Users valued live partial text, but Linux microphone capture and piping monitor audio remained rough; macOS has the only built-in live source.
- Alternative stacks using Parakeet, Whisper, or hosted Voxtral felt faster—counterpoint: this project prioritizes understandable, dependency-light inference over mature deployment.
- The author agreed 4B is large for CPUs and proposed targeting a 0.6B model with instruction-specific kernels and possible 8-bit quantization.

### LLM perspective

- View: Its strongest contribution is transparent model plumbing; hardware economics, not pipeline completeness, limits broad local adoption.
- Impact: Researchers gain an auditable reference and embeddable API, while CPU users still need smaller or quantized models.
- Watch next: Long-transcription correctness, cache stress, Linux capture, CPU kernels, quantization accuracy, latency across hardware, and production hardening.
