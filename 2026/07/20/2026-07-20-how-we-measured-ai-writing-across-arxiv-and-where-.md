# How we measured AI writing across arXiv, and where the measurement breaks

- Score: 188 | [HN](https://news.ycombinator.com/item?id=48981206) | Link: https://unslop.run/blog/measuring-ai-writing-on-arxiv

## TL;DR
- A custom detector scored 12,750 arXiv papers (2021–2026), calibrated so that pre-ChatGPT papers show only 0.4% false positives, then tracked how many later papers look “machine-written.”  
- The flagged share jumps after ChatGPT’s release, peaking around 39% overall and ~65% in computer science; math stays near zero but likely reflects a detector blind spot.  
- The author stresses limits: small controls, uneven coverage, and that “machine-like” text ≠ proof of AI use.  
- HN readers largely question detector reliability, share high scores on pre-LLM work, and warn against using such tools for accusations, arguing text-only detection is inherently shaky.

---

## Comment pulse
- AI-text detectors are unreliable → many pre-LLM theses and papers score highly; historic documents misclassified; dangerous when used to accuse students and authors.  
- Methodology draws interest but skepticism → calibration and time series look strong, yet closed-source scoring, formatting sensitivity, and possible training leakage undermine trust.  
- Text-only attribution seen as fundamentally limited → overlapping human/LLM styles and shifting “tells” make per-document judgments dubious—counterpoint: combinatorial phrasing space is vast; difficulty comes from other factors.

---

## LLM perspective
- View: Use such detectors only for aggregate trend analysis, never as forensic tools against specific authors or submissions.  
- Impact: Scientific writing norms, review practices, and credit models must assume pervasive AI assistance regardless of precise detector estimates.  
- Watch next: Open, benchmarked detectors; longitudinal studies of style and citation shifts; institutional rules restricting detector use in misconduct cases.
