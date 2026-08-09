# Cohere Transcribe: Speech Recognition

- Score: 150 | [HN](https://news.ycombinator.com/item?id=47589818) | Link: https://cohere.com/blog/transcribe

### TL;DR

Cohere released Transcribe, an Apache 2.0, open-weights speech-recognition model trained from scratch across 14 languages. Its 2-billion-parameter design combines a Conformer encoder with a lightweight Transformer decoder and can run locally, through a rate-limited API, or on Cohere’s managed platform. Cohere reports a 5.42% average word-error rate atop the Open ASR Leaderboard, plus strong throughput and human evaluations. HN questioned production completeness: no native timestamps or speaker diarization, limited contextual customization, and benchmarks that may miss overlapping speech, nonverbal sounds, omissions, and plausible hallucinations.

### Comment pulse

- Multimodal models can use domain prompts for names — counterpoint: stronger priors may replace rare, correct speech with plausible errors.
- Missing timestamps and diarization block many subtitle and podcast workflows, though external alignment and separation tools could wrap the model.
- Local recognition preserves privacy and reduces microphone bandwidth, giving dedicated ASR an advantage even if multimodal systems understand more context.

### LLM perspective

- **View:** This is a strong base recognizer, not yet a complete transcription product for demanding media workflows.
- **Impact:** Self-hosters gain a permissively licensed multilingual option with manageable inference and full infrastructure control.
- **Watch next:** Independent multilingual tests, hardware-specific throughput, omissions, hallucinations, timestamps, diarization, and custom vocabulary or prompt support.
