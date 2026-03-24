# If DSPy is so great, why isn't anyone using it?

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47490365) | Link: https://skylarbpayne.com/posts/dspy-engineering-patterns/

### TL;DR
The piece walks through how typical LLM “quick hacks” evolve into complex systems: prompt storage, typed schemas, retries, RAG, evals, and model‑swap layers. The author claims most teams eventually reinvent a fragile, homegrown version of DSPy, which bakes these patterns in via typed “signatures,” composable modules, and optimizers that tune prompts automatically. Adoption lags because DSPy is Python-only and forces upfront architectural thinking. HN discussion questions whether its patterns are novel, its optimizer effective, and highlights evaluation and DX as main bottlenecks.

---

### Comment pulse
- DSPy’s abstractions feel like table-stakes; Python-only is limiting; other libs (LiteLLM, Vercel ai) already provide model-agnostic calls and retries; optimizer is hard to use effectively.  
- Fans like the staged “you’ll rebuild this anyway” narrative and typed I/O, but complain about missing multi-language support, thin docs, and lack of a polished “whole product” around the library.  
- Some say simpler ML (NER, classifiers) often beats LLMs on cost/latency;—counterpoint: practitioners report transformer-based LLMs now yield far superior NER quality.

---

### LLM perspective
- View: DSPy mainly formalizes emerging best practices; its real hurdle is cultural inertia and Python-only early-adopter positioning.  
- Impact: Teams with growing LLM codebases benefit most: fewer bespoke pipelines, easier model swaps, and clearer places to attach monitoring.  
- Watch next: Useful signals: TS/Go ports, success stories with measurable quality gains from DSPy optimizers, and benchmarks versus LiteLLM/ai + custom glue.
