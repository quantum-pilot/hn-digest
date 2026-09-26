# Ollaya – Ollama for open-source, Jev-style decision models

- Score: 452 | [HN](https://news.ycombinator.com/item?id=49848269) | Link: https://ollaya.dev/

### TL;DR

Ollaya packages open-source, Jev-style decision models behind a local TypeSafe-compatible API for typed yes/no, choice, score, and classification tasks. It offers pinned model hashes, several model families, CPU and selected GPU support, and calibration through Modelfiles. Its RTX 4090 page reports roughly 8–10 ms for a five-question Laya request versus 236–276 ms hosted Jev medians, while explicitly warning that hardware and network conditions differ. Commenters emphasized that speed does not establish comparable decision quality.

### Comment pulse

- Local inference enables practical automation → commenters proposed smart grep, command selection, home control, and text classification.
- Quality remains the central uncertainty → posted comparisons and user impressions placed Laya below Jev on some evaluations.
- The moat is disputed → commenters debated whether Jev’s advantage lies in architecture, training data, or a reproducible recipe.

### LLM perspective

- View: Ollaya is a useful local runtime whose models must be evaluated separately from its API compatibility.
- Impact: Private, typed decision endpoints could make small classifiers easier to integrate without hosted inference.
- Watch next: Comparable task-specific evaluations should measure accuracy, calibration, latency, hardware, and custom fine-tuning together.
