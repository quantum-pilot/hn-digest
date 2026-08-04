# Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor

- Score: 413 | [HN](https://news.ycombinator.com/item?id=48894752) | Link: https://get-inscribe.com/blog/apple-speech-api-benchmark.html

### TL;DR

On 5,559 English LibriSpeech clips run fully on-device on an M2 Pro, Apple’s SpeechAnalyzer scored 2.12% word error on clean audio and 4.56% on noisy audio, beating Whisper Small’s 3.74% and 7.95% while running roughly three times faster. It also cut legacy SFSpeechRecognizer errors by 3.5–4×. The reproducible harness publishes transcripts and matches OpenAI’s Whisper results closely, but covers only read English. HN welcomed the speed yet said newer Parakeet, Nemotron, Voxtral, and Cohere models, multilingual use, meetings, jargon, and poor audio are needed comparisons.

### Comment pulse

- The baseline was contested → readers preferred Parakeet or newer commercial systems; Whisper v3 may still excel on degraded audio despite hallucinations.
- Real-world trials were encouraging → one math-lecture test was much faster but slightly worse than Whisper-Large-V2; podcast processing reached 60× realtime.
- Transcription remains weak for developers → recognizers need project context or LSP integration to preserve identifiers such as `useSuspenseQuery`.

### LLM perspective

- **View:** Built-in accuracy plus speed changes the default for Apple-only English apps; portability remains Whisper’s moat.
- **Impact:** Wrapper apps must compete on editing, workflow, jargon adaptation, and cross-platform support rather than raw transcription.
- **Watch next:** Benchmark spontaneous multilingual meetings, far-field accents, diarization, hallucinations, energy use, and Parakeet under identical scoring.
