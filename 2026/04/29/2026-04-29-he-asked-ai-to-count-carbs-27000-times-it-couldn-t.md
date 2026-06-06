# He asked AI to count carbs 27000 times. It couldn't give the same answer twice

- Score: 233 | [HN](https://news.ycombinator.com/item?id=47947490) | Link: https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/

### TL;DR
A diabetes technologist tested four multimodal LLMs (GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Pro, Gemini 3.1 Pro) on carb estimation from 13 real-meal photos, running each photo >500 times per model (26,904 queries). Even at minimum randomness, the same input produced wildly different carb counts—e.g., Gemini 2.5 Pro ranged 55–484g for one paella, implying up to 42.9 insulin units difference. Models also showed systematic bias (generally overdosing), frequent misidentification, and confidence scores uncorrelated with correctness, making them unsafe for autonomous insulin dosing despite slick carb-counting apps.

---

### Comment pulse
- Study is “astrology-level” because it just feeds photos to LLMs; real systems should use databases and portion models → but commercial apps already market exactly this photo-only behavior.  
- Value even if unsurprising: it quantifies variance, shows confidence is useless, and provides a concrete warning not to rely on LLMs for insulin dosing.  
- Task is fundamentally under-specified from pixels alone, yet humans and diabetics routinely make constrained, consistent estimates; LLMs’ huge spread plus overconfident tone misleads non-experts.

---

### LLM perspective
- View: Carb-from-photo should be treated as an ill-posed, safety-critical estimation problem requiring structured pipelines, not generic chat models.  
- Impact: Diabetes app vendors, clinicians, and regulators should prohibit single-shot LLM carb dosing and demand transparent error distributions.  
- Watch next: Benchmarks versus human raters, standards for medical AI marketing claims, and research on calibrated uncertainty and multi-sample aggregation.
