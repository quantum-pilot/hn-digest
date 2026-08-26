# TimeCapsuleLLM: LLM trained only on data from 1800-1875

- Score: 446 | [HN](https://news.ycombinator.com/item?id=46590280) | Link: https://github.com/haykgrigo3/TimeCapsuleLLM

### TL;DR

TimeCapsuleLLM trains small models from scratch on London texts dated 1800–1875, aiming to reproduce period vocabulary and worldview without modern pretraining. Versions grew from 16 million to 700 million parameters; a 300-million-parameter experiment used 15 GB from a planned 90 GB corpus. Outputs improved from incoherent pseudo-archaic text to grammatical but hallucination-prone prose, with OCR and tokenization defects. HN saw historical cutoffs as a test of model innovation, but questioned linguistic expertise, data leakage, corpus bias, scarce training volume, and the absence of period-appropriate instruction tuning.

### Comment pulse

- Scientific rediscovery is an appealing benchmark → success before known discoveries could test synthesis — counterpoint: later experiments supplied indispensable evidence.
- Temporal purity is difficult → misdated texts, annotations, metadata, modern OCR, and fine-tuning datasets can leak future knowledge.
- Historical corpora are selective → preserved newspapers and elite writing offer less volume and diversity than modern internet-scale text.

### LLM perspective

- View: The project is more convincing as a bias laboratory than as evidence models can independently discover science.
- Impact: Historians gain experimental tools, but conclusions depend on provenance, linguistic validation, and transparent corpus construction.
- Watch next: Publish contamination audits, held-out future tests, matched modern baselines, ablations, and expert historical-language scoring.
