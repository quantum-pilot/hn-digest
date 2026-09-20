# I built non-autoregressive decision models with RL a year ago

- Score: 1245 | [HN](https://news.ycombinator.com/item?id=49765348) | Link: https://laya.convaiinnovations.com/

### TL;DR

ConvAI founder Nandakishor Mukkunnoth argues his 2025 work anticipated TypeSafe’s Jev concept and introduces Laya, open-weight bidirectional models for typed classification, scoring, and boolean decisions. He reports 32.8ms single-question latency, multilingual routing, and stronger selected benchmarks than Jev. Important limitations temper those claims: Laya degrades beyond 20 choices, its 0.766 typed score requires fine-tuning on that benchmark, and domain temperature fitting improves calibration. Commenters disputed novelty, alleged leakage in earlier work, and distinguished Jev’s claimed zero-shot generality from specialized classifiers.

### Comment pulse

- Product framing created Jev’s visibility → commenters found its general API easier to understand than the author’s earlier sales-specific research.
- Comparability remains unresolved → Laya reports strong specialized results, while Jev’s differentiator may be broad in-context classification without fine-tuning.
- Priority claims face substantial prior art → commenters cited BERT classifiers and GLiNER while questioning the earlier model’s methodology.

### LLM perspective

- View: Open weights and disclosed weaknesses are valuable, but selected benchmarks cannot establish architectural equivalence or research priority.
- Impact: Teams with labeled data can self-host fast classifiers; rapidly changing schemas may still favor general hosted models.
- Watch next: Run independent zero-shot, leakage-controlled, multilingual, calibration, latency, and high-cardinality evaluations on identical tasks and hardware.
