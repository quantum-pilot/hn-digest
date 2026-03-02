# Decision trees – the unreasonable power of nested decision rules

- Score: 380 | [HN](https://news.ycombinator.com/item?id=47204964) | Link: https://mlu-explain.github.io/decision-tree/

## TL;DR
The article is a visual, intuitive walkthrough of decision trees: how they recursively split feature space (e.g., tree height/diameter) into regions using if-then rules, and how training chooses splits by maximizing information gain, computed from entropy as a measure of label impurity. It explains the ID3 algorithm, compares entropy with Gini impurity, and highlights key weaknesses: overfitting with deep trees and high variance from small data perturbations. Pruning and ensembling into random forests are presented as core remedies. Hacker News discussion adds practical tricks, concerns about explainability, and performance comparisons with neural networks.

---

## Comment pulse
- Hybrid pipelines: learn a good linear classifier, add its score as a feature, then train boosted trees → trees fix non-linear leftovers; feature engineering remains critical.  
- Explainability is overrated for deep trees: 10–15 levels become opaque like neural nets—counterpoint: shallow trees and per-path inspection still yield useful local explanations.  
- Performance: decision trees and boosted variants can be orders of magnitude faster at inference than small neural nets, crucial in low-latency or embedded settings.

---

## LLM perspective
- View: Decision trees shine on tabular data when paired with regularization, boosting, and simple diagnostics for local interpretability.  
- Impact: Most relevant to practitioners needing fast, inspectable models: finance, physics triggers, ads, industrial control, and embedded ML.  
- Watch next: Compare latency/accuracy of boosted trees vs compact NNs; tools to approximate NNs with trees; follow-up on random forests.
