# Building reliable agentic AI systems

- Score: 177 | [HN](https://news.ycombinator.com/item?id=48615680) | Link: https://martinfowler.com/articles/reliable-llm-bayer.html

### TL;DR

Bayer and Thoughtworks’ PRINCE turns decades of preclinical reports and structured study data into an agentic research assistant using RAG, Text-to-SQL, and specialized planning, research, reflection, and writing stages. Reliability comes from selective context, cited evidence, read-only SQL, persisted workflow state, retries, model fallbacks, daily production evaluations, and mandatory expert approval for regulatory drafts. HN discussion focused less on orchestration than fundamentals: clean data, rigorous evaluation, and transparent control of loops. Critics cited a 3.1/5 user score and hallucination risk; the author said that score measured feature completeness, not accuracy.

### Comment pulse

- Data quality dominates agent tuning → one practitioner estimated a 99/1 effort split; centralized, well-designed schemas make retrieval and alignment dramatically easier.

- Large contexts do not replace retrieval architecture → production practitioners argued indiscriminate context harms steering, evaluation, and scale.

- Autonomous loops threaten transparency → critics questioned nondeterministic control flow — counterpoint: persisted steps, visible tools, citations, and expert review constrain outcomes.

### LLM perspective

- **View:** PRINCE’s reliability comes from conventional systems engineering around probabilistic models, not from making the models themselves deterministic.

- **Impact:** Scientists gain faster evidence synthesis, while qualified reviewers retain accountability for claims entering regulatory or safety decisions.

- **Watch next:** Publish stage-level accuracy, citation-error rates, loop distributions, failure-recovery metrics, updated satisfaction scores, and changes driven by daily evaluations.
