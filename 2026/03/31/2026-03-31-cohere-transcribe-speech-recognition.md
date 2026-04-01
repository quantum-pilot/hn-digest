# Cohere Transcribe: Speech Recognition

- Score: 150 | [HN](https://news.ycombinator.com/item?id=47589818) | Link: https://cohere.com/blog/transcribe

## TL;DR

Cohere Transcribe is a 2B-parameter, conformer-based, open‑weights ASR model (Apache 2.0) trained from scratch on 14 languages. It currently tops Hugging Face’s Open ASR Leaderboard with the lowest reported English WER among ≥1B-parameter models, while also pushing the speed/accuracy Pareto frontier for production throughput. Cohere is positioning it as the speech front-end for its enterprise stack (via API and Model Vault), though the initial release omits diarization and timestamps, drawing mixed but engaged reactions from HN.

---

## Comment pulse

- Benchmarks vs reality → HN users want timestamps, overlapping speakers, literal transcripts, and non‑verbal tags for accessibility; many models silently drop sentences—counterpoint: benchmark leadership still matters for core accuracy.

- ASR vs multimodal LLMs → Some expect multimodal LLMs with domain context to displace standalone ASR; others emphasize local/on‑device STT for bandwidth, privacy, and latency.

- Tooling and APIs → Frustration with major ASR APIs (Google, AWS, OpenAI) lacking reliable diarization + word timestamps; hope Cohere spurs WhisperX‑style ecosystems, but absence of prompts/custom vocabulary is a dealbreaker for some.

---

## LLM perspective

- View: Dedicated ASR will likely persist as a fast, cheap front‑end, feeding richer multimodal or domain‑tuned LLMs when deeper understanding is needed.

- Impact: Enterprises with call centers, meetings, and compliance logging gain more control via open weights and private deployments versus pure SaaS ASR.

- Watch next: Compare real-world latency/cost vs Whisper+WhisperX and GPT‑4o‑style transcription; track if Cohere adds diarization, timestamps, and contextual prompting.
