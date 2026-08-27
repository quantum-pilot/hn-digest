# New Apple Study Shows LLMs Can Tell What You're Doing from Audio and Motion Data

- Score: 64 | [HN](https://news.ycombinator.com/item?id=46015578) | Link: https://9to5mac.com/2025/11/21/apple-research-llm-study-audio-motion-activity/

### TL;DR

Apple researchers tested late multimodal fusion for recognizing 12 everyday activities from 20-second Ego4D samples. Specialized audio and motion models first converted raw signals into captions, labels, and activity predictions; Gemini 2.5 Pro and Qwen-32B then combined those textual outputs in zero- and one-shot settings, scoring above chance without task-specific training. The LLMs therefore did not directly interpret recordings. The approach may help when aligned training data is scarce, while commenters question whether an LLM adds enough value and warn that stored sensor data can enable later surveillance.

### Comment pulse

- Late fusion reuses specialist models → an LLM interprets their outputs without training a new joint embedding.
- Activity inference is not new → improved models expand what previously collected motion and audio metadata can reveal.
- Practical value remains unquantified here → commenters want comparison against simpler fusion and mature activity classifiers.

### LLM perspective

- View: The experiment demonstrates flexible semantic fusion, not that raw sensors inherently require language models.
- Impact: Wearables could add activities quickly, but richer inference raises consent, retention, and on-device-processing questions.
- Watch next: Compare baselines, per-class errors, unseen activities, compute cost, privacy leakage, and real-world wearable data.
