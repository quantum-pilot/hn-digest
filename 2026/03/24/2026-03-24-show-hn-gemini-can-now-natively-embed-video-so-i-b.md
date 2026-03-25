# Show HN: Gemini can now natively embed video, so I built sub-second video search

- Score: 228 | [HN](https://news.ycombinator.com/item?id=47503617) | Link: https://github.com/ssrajadh/sentrysearch

- TL;DR  
  - Open-source tool SentrySearch uses Google’s Gemini Embedding 2 to chunk dashcam footage, embed raw video into a shared vector space with text, and deliver sub‑second semantic search results and auto-trimmed clips via a simple CLI. It explains costs (~$2.50/hour), preprocessing tradeoffs, and limitations like heuristic scene detection. HN commenters are excited about practical uses and editing workflows but deeply worried about how scalable AI video search accelerates police, commercial, and drone-enabled panopticon-style surveillance.

- Comment pulse  
  - AI video search enables panopticon-style surveillance via natural-language queries over city, police, and consumer cameras—counterpoint: current costs, latency, and fragmented ownership slow real-time surveillance.  
  - Makers want to integrate this into custom dashcam viewers and other embedding experiments, validating demand for turnkey “describe it, find it” tooling.  
  - People speculate about creative tools: video editors powered by semantic queries that auto-generate edit decision lists to remove or isolate specific content.

- LLM perspective  
  - View: Direct video-text embeddings make many niche “needle-in-haystack” video search problems suddenly tractable without transcription pipelines.  
  - Impact: Most immediate adopters: fleet operators, security teams, editors, quantified-self folks with wearables or dashcams drowning in unstructured footage.  
  - Watch next: Key questions: evaluation benchmarks, robustness to adversarial scenes, on-device or open-weight models that reduce cloud dependency and privacy risk.
