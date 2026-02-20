# Don't Trust the Salt: AI Summarization, Multilingual Safety, and LLM Guardrails

- Score: 174 | [HN](https://news.ycombinator.com/item?id=47038032) | Link: https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails

### TL;DR
Author demonstrates how LLM summaries, especially in non‑English languages, can be quietly steered by hidden policies to downplay abuses or omit sensitive information while appearing neutral. Refugee/asylum case studies show large quality and safety gaps for Arabic, Farsi, Pashto, and Kurdish, and even guardrail tools inherit these multilingual biases, confidently mis‑scoring harmful outputs. HN commenters connect this to slanted summaries in products like YouTube AI and NotebookLM and to training‑data‑driven “voices” that can aid propaganda or radicalization.

### Comment pulse
- LLM persona mirrors training data → Arabic Gemini talks like 2000s religious forums, raising concerns about propaganda/radicalization—counterpoint: structural poverty and isolation matter more.  
- AI summarizers feel arbitrary or censored → NotebookLM fixates on minor details; YouTube AI omits controversial or clickbait‑revealing content, effectively editorializing for engagement.  
- Bias is unavoidable → system prompts and guardrails encode priorities like human executive summaries; one response advocates cryptographic third‑party audits instead of trusting models’ self‑reports.  

### LLM perspective
- View: Treat summarization and translation as high‑risk features; they silently reshape narratives users rarely cross‑check against sources.  
- Impact: Platform builders, NGOs, and regulators demand multilingual evaluations and expose or ban opaque “localized” wrappers with hidden policy layers.  
- Watch next: Benchmarks tying policy language to safety outcomes, plus guardrails hooked to search/RAG and independent logging for real‑world deployments.
