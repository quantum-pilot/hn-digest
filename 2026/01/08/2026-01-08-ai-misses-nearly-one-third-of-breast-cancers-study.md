# AI misses nearly one-third of breast cancers, study finds

- Score: 146 | [HN](https://news.ycombinator.com/item?id=46537983) | Link: https://www.emjreviews.com/radiology/news/ai-misses-nearly-one-third-of-breast-cancers-study-finds/

### TL;DR
A single-center retrospective study of 414 women already diagnosed with breast cancer found a commercial AI mammography/MRI system missed 30.7% of tumors, especially small ones and those in dense breasts. Diffusion‑weighted MRI (DWI) reviewed by two radiologists detected about 80% of these AI-missed lesions, suggesting DWI is a useful safety net. Hacker News discussion stresses that the study measures AI sensitivity only in cancer-positive cases, omits false-positive rates, doesn’t compare AI to radiologists, and uses an older (circa‑2021) convolutional model.

---

### Comment pulse
- Study is cancer-only → measures AI sensitivity, not specificity; no healthy controls, so no false-positive rate or AI-vs-radiologist comparison.  
  — counterpoint: still useful to bound best-case sensitivity for fully automated screening.

- AI system is an older commercial ConvNet from 2021 → results may understate current models; headline’s generic “AI misses” misleads by implying all AI systems.

- Methodology critiques: tiny sample of two radiologists, unblinded grading, biased case set (only positives) risks cognitive/anchoring bias; DWI evaluation not equivalent to real-world screening.

---

### LLM perspective
- View: Imaging AI should be treated like a medical device line, with explicit model/version labeling and regularly updated performance evidence.

- Impact: Hospital buyers, regulators, and malpractice insurers must demand prospective, multi-center trials with head‑to‑head AI vs radiologist performance.

- Watch next: Standardized “model cards” reporting sensitivity/specificity by breast density, tumor size, and modality, plus trials combining AI with targeted MRI sequences like DWI.
