# Voxtral Transcribe 2

- Score: 670 | [HN](https://news.ycombinator.com/item?id=46886735) | Link: https://mistral.ai/news/voxtral-transcribe-2

### TL;DR

Mistral released Voxtral Transcribe 2 as separate batch and streaming speech-to-text models. Mini Transcribe V2 adds speaker diarization, word timestamps, context biasing, noise robustness and three-hour requests across 13 languages; Mistral prices its API at $0.003 per minute and claims roughly 4% FLEURS word error. Apache-licensed Voxtral Realtime streams as audio arrives, with configurable delay below 200 milliseconds, edge deployment and a $0.006-per-minute API. Mistral also launched an audio playground, while its performance and cost comparisons remain company-reported benchmark claims.

### Comment pulse

- Several users reported striking real-time accuracy, including jargon and language switching; others could not make the hosted demo transcribe.
- Polish and Ukrainian tests exposed unsupported-language confusion, while replies noted the announced list covers only 13 specified languages.
- Commenters debated multilingual overhead, code-switching benefits and whether quoted API pricing means audio time or compute time.

### LLM perspective

- View: Separating streaming and batch models lets latency-sensitive and accuracy-focused workloads choose different tradeoffs.
- Impact: Low claimed prices and open realtime weights could make private, responsive transcription broadly accessible.
- Watch next: Independent multilingual benchmarks, tail-latency measurements and fixes for demo reliability and unsupported-language misclassification.
