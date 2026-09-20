# Alibaba open-sources AI model that can detect cancer and nearly 150 conditions

- Score: 148 | [HN](https://news.ycombinator.com/item?id=49761840) | Link: https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions

### TL;DR

Alibaba’s Damo Academy open-sourced Damo Radar, a vision-language model trained on contrast-enhanced CT scans and reports to identify findings across 18 abdominal organs. Alibaba reports an average ROC-AUC of 0.913 across 146 findings in nearly 40,000 examinations, plus better accuracy than 23 of 26 radiologists and improved speed and missed-diagnosis prevention when assisting them. HN readers welcomed the breadth but questioned whether ROC-AUC under class imbalance obscures clinically important precision and false-positive behavior.

### Comment pulse

- ROC-AUC is insufficient evidence → rare findings can yield impressive curves while precision and false-positive burdens remain poor.
- The encoder choice deserves attention → one reader found the convolutional feature extractor outperforming vision transformers more notable than the headline comparison.

### LLM perspective

- View: A broad abdominal model is promising, but aggregate discrimination does not establish safe diagnostic performance.
- Impact: Radiologists could gain faster triage and fewer misses if independent studies reproduce the assisted-workflow results.
- Watch next: Seek per-condition precision-recall curves, calibration, external cohorts, and prospective clinical evaluations.
