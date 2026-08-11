# Decision trees – the unreasonable power of nested decision rules

- Score: 380 | [HN](https://news.ycombinator.com/item?id=47204964) | Link: https://mlu-explain.github.io/decision-tree/

### TL;DR

The explainer builds a decision tree by repeatedly splitting trunk height and diameter until leaves predict apple, cherry, or oak. Information gain greedily chooses feature thresholds using entropy to measure impurity; regression leaves instead average values. Unrestricted splitting makes deep trees memorize noise, while small data perturbations can radically change their structure. Depth, leaf-size, and leaf-count constraints reduce overfitting; ensembles such as random forests reduce variance. HN highlighted fast inference and hybrid features, but warned that deep or boosted trees lose their celebrated interpretability and depend heavily on feature engineering.

### Comment pulse

- Adding a linear classifier’s score as a feature lets shallow trees capture residual structure; specialized oblique and model trees formalize related ideas.
- CERN users valued boosted trees’ speed and explainability — counterpoint: beyond a few levels, traced decisions can become another opaque jungle.
- For low-latency inference, one commenter found small neural networks more accurate but roughly two orders of magnitude slower.

### LLM perspective

- **View:** Trees are strongest when axis-aligned rules match engineered features and operational constraints reward speed and inspectability.
- **Impact:** They remain compelling for structured, latency-sensitive problems, but brittle single trees need regularization or ensembles.
- **Watch next:** Cross-validation, calibration, perturbation tests, feature drift, inference budgets, and whether explanations remain useful at deployed depth.
