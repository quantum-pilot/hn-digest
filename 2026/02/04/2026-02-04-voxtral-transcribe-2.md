# Voxtral Transcribe 2

- Score: 670 | [HN](https://news.ycombinator.com/item?id=46886735) | Link: https://mistral.ai/news/voxtral-transcribe-2

- TL;DR  
    Mistral’s Voxtral Transcribe 2 introduces two ASR models: a streaming Realtime model and a batch Mini Transcribe V2, with strong multilingual accuracy, diarization, timestamps, and very low pricing. Realtime uses a streaming architecture for near-instant transcripts and ships as open weights. Hacker News testers praise its real-time quality versus existing ASR, especially on accents and jargon, but hit demo glitches, complain about missing languages (e.g., Polish/Ukrainian), and debate multilingual vs single-language models and how pricing really compares to cloud incumbents.

- Comment pulse  
    Users find the realtime demo astonishingly accurate on fast speech, jargon, and mixed languages, though some report Hugging Face space errors and non-functioning microphone input.  
    Slavic speakers see Polish/Ukrainian utterances transcribed as Russian, causing frustration and expectations for broader European support—counterpoint: others note the docs only promise 13 specific languages.  
    Practitioners report Voxtral beating Deepgram and Assembly on UK-accent call data, with big cost gaps vs AWS but uncertainty over billing units and latency variability.

- LLM perspective  
    View: A compact, high-quality streaming ASR model with permissive licensing will likely reset expectations for “good enough” voice infrastructure.  
    Impact: Low-cost, realtime transcription enables smaller teams to build voice agents, subtitle tools, and analytics that previously needed big-vendor budgets.  
    Watch next: Independent evaluations on non-listed languages, fine-tuned domain models, and comparisons with Whisper-based “per compute second” pricing schemes.
