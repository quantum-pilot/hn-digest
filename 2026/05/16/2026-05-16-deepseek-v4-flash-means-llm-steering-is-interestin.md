# DeepSeek-V4-Flash means LLM steering is interesting again

- Score: 199 | [HN](https://news.ycombinator.com/item?id=48160807) | Link: https://www.seangoedecke.com/steering-vectors/

### TL;DR
The post argues that DeepSeek-V4-Flash, via the DwarfStar 4 project, finally makes serious “steering” experiments viable on a strong local model. Steering means identifying activation patterns that encode concepts (e.g., terseness) and adding or suppressing them at inference time, instead of relying on prompts or retraining. The author explains simple vector-difference steering and feature-based methods, but is skeptical it can unlock deep traits like “intelligence” or “codebase knowledge,” predicting prompting and fine-tuning will usually win—while still expecting rapid experimentation now that tooling exists.

---

### LLM perspective
- View: Treat steering as targeted, reversible, runtime fine-tuning rather than magic dials for “intelligence” or broad skills.  
- Impact: Most useful for niche behaviors—refusal removal, style control, domain quirks—on locally run open models.  
- Watch next: Standardized steering-vector libraries, benchmarks comparing steering vs prompts/fine-tunes, and safety work on de-refusal and uncensoring techniques.
