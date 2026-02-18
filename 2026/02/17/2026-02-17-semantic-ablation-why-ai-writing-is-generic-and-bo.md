# Semantic ablation: Why AI writing is generic and boring

- Score: 211 | [HN](https://news.ycombinator.com/item?id=47049088) | Link: https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/

### TL;DR
Models tuned with greedy decoding and RLHF tend to erase “high‑entropy” elements—unusual metaphors, precise jargon, and complex structure—when asked to “polish” text. The article calls this semantic ablation: a staged process (metaphor cleansing, lexical flattening, structural templating) that collapses vocabulary diversity and nuance into a smooth, generic “JPEG of thought.” Commenters widely recognize this in practice, blaming safety and preference tuning, while conceding AI still helps weaker writers and routine communications, but rarely produces great prose.

---

### Comment pulse
- AI polishing dulls distinctive voice → sharp metaphors, technical specificity gets sanded into generic, “polished” clichés; good editors add clarity, not erase personality.  
- AI voice feels ubiquitous and deadening → readers notice repeating cadences, buzzwords, and hedging, likening it to JPEG artifacts that seemed invisible but now dominate.  
- RLHF drives median, not originality → preference data rewards safe, expected answers; multi‑step LLM pipelines compound flattening—counterpoint: smaller, less‑tuned models can preserve more idiosyncrasy.

---

### LLM perspective
- View: Semantic ablation names a real optimization bias toward low‑entropy tokens created by decoding choices plus safety‑oriented fine‑tuning.  
- Impact: Overuse of AI polishing in media, academia, and policy risks homogenized language, shallower arguments, and loss of expert vocabulary.  
- Watch next: Benchmarks for entropy loss, RLHF knobs, routing creative tasks to base models, and tooling that flags over‑flattened revisions.
