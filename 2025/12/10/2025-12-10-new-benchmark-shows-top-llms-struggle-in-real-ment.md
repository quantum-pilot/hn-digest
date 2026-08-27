# New benchmark shows top LLMs struggle in real mental health care

- Score: 105 | [HN](https://news.ycombinator.com/item?id=46217578) | Link: https://swordhealth.com/newsroom/sword-introduces-mindeval

### TL;DR

Sword Health’s open-source MindEval simulates multi-turn therapy using a patient model, the clinician model under test, and an automated judge scoring five clinically derived dimensions. The company says its simulated patients resemble human role-play and its judge correlates moderately to highly with licensed psychologists. Across 12 models, average scores stayed below 4 on a six-point scale, worsening with severe symptoms and 40-turn sessions; larger reasoning models did not consistently lead. Critics question whether AI-generated patients and judgments can establish real clinical competence without field trials.

### Comment pulse

- Open prompts, code, rubrics, and validation data support scrutiny → commenters still ask how prompts and human baselines were controlled.
- AI-on-AI evaluation risks self-consistent errors → human judge correlation helps, but does not validate patient outcomes or therapeutic safety.
- Access shortages motivate supportive tools → clinicians and users resist treating simulated performance as evidence that human therapy is replaceable.

### LLM perspective

- View: MindEval is a useful preclinical filter, not evidence that any model safely delivers therapy to real patients.
- Impact: Developers gain a reproducible way to detect longitudinal and severe-case failures before costly human studies.
- Watch next: Randomized trials, crisis outcomes, demographic coverage, clinician baselines, judge drift, and independent replication are required.
