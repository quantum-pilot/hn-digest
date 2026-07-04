# 60% Fable cost cut by converting code to images and having the model OCR it

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48776464) | Link: https://github.com/teamchong/pxpipe

### TL;DR
Fable, a tool that uses Claude for code understanding, reportedly cut its API costs by ~60% by rendering code as images and sending those to the model’s vision endpoint instead of text. Commenters debate whether this is just exploiting token accounting or reflects a real efficiency: recent work like DeepSeek-OCR suggests visual “tokens” can compress documents dramatically with little quality loss. Others report mixed cost results with OpenAI, and criticize the project’s AI-written README as hard to understand and trust.  

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Vision/OCR tokens may be cheaper than text → DeepSeek-OCR shows ~90% fewer tokens with minor quality loss; image scaling adjusts compression level.  
- Pricing hack concern → Some expect OCR prices to rise as loophole closes — counterpoint: others say optical tokens are structurally cheaper, not wasteful.  
- AI-written ‘vibe’ README backlash → Readers find LLM-compressed explanations opaque and trust projects more when authors disclose AI help and write clear human summaries.  

---

### LLM perspective
- View: Vision-first code ingestion will spread if providers keep favorable pricing and quality parity with text prompts.  
- Impact: Tool builders can fit larger repos or logs into context windows, enabling more holistic refactors, audits, and debugging sessions.  
- Watch next: Benchmarks comparing visual-token compute cost, latency, and accuracy versus text for code, PDFs, and telemetry across major models.
