# Claude Fable 5

- Score: 1667 | [HN](https://news.ycombinator.com/item?id=48463808) | Link: https://www.anthropic.com/news/claude-fable-5-mythos-5

### TL;DR

Anthropic released Fable 5, its first general Mythos-class model, claiming gains in long-horizon coding, vision, knowledge work, memory, and science. It costs $10 per million input tokens and $50 per million output. Classifiers can visibly route cybersecurity, biology, chemistry, or distillation requests to Opus 4.8; Anthropic says fewer than 5% of sessions trigger fallback and requires 30-day retention of business traffic. HN testers often found cleaner, more efficient code and stronger hard-task performance, but results varied. Hidden degradation of frontier-model-development requests drew fierce criticism as anti-competitive self-protection.

### Comment pulse

- Coding gains look task-dependent → users praised surgical diffs, frontend design, refactors, and reverse engineering, while Stockfish optimization still defeated it.
- Token efficiency can offset price → some testers reported half the tokens and fewer loops, bringing hard-task costs near Opus 4.8.
- Safety controls are polarized → visible fallbacks handled benign false positives — counterpoint: covert suppression of competing-model work destroys trust.

### LLM perspective

- **View:** Capability and product integrity are inseparable: users must know which model answered and whether policy altered its reasoning.
- **Impact:** Developers gain stronger autonomy but face higher costs, retention, classifier uncertainty, and potential benchmark contamination from undisclosed interventions.
- **Watch next:** Measure fallback rates by domain, effective cost per accepted task, reproducibility, and performance on model-development work.
