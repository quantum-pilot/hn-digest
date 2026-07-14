# Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor

- Score: 413 | [HN](https://news.ycombinator.com/item?id=48894752) | Link: https://get-inscribe.com/blog/apple-speech-api-benchmark.html

### TL;DR
Apple’s new on-device SpeechAnalyzer API appears significantly faster than OpenAI’s Whisper (especially Large-V2) while matching or beating Whisper Small on standard LibriSpeech benchmarks. Developers report real-time math-lecture and podcast transcription on iPhone with roughly 60× real‑time throughput. HN discussion questions benchmarking only against Whisper when newer ASR models exist, highlights Whisper v3’s superiority on very noisy audio, and notes that while general dictation is close to “solved,” domain-specific jargon and developer workflows remain challenging.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Whisper is an incomplete baseline → People cite Nemotron, Parakeet, Voxtral, Cohere and multilingual auto‑detect as stronger comparators; Whisper v3 still best for low‑quality audio.  
- On‑device speed is impressive → Users see it faster than Whisper‑Large‑V2; one iPhone 17 Pro processed an hour‑long podcast in about a minute.  
- Speech‑to‑text feels almost solved → Tools like Willow give cleaned‑up transcripts; harder problems are domain jargon and IDE‑aware symbol/file names for developer workflows.

---

### LLM perspective
- View: Apple is turning high‑quality, private, on‑device ASR into a default OS capability rather than a premium cloud feature.  
- Impact: Wrapper apps and generic transcription SaaS lose differentiation; value shifts to workflow integration, editing UX, and domain‑specific customization.  
- Watch next: Multilingual and noisy‑audio benchmarks, user‑modifiable vocabularies for jargon, and integration of speech directly into coding/agent workflows.
