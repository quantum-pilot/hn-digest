# Don't Trust the Salt: AI Summarization, Multilingual Safety, and LLM Guardrails

- Score: 174 | [HN](https://news.ycombinator.com/item?id=47038032) | Link: https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails

### TL;DR

Three linked projects show that LLM summaries and their guardrails can change meaning across hidden policies and languages. A customized Farsi policy shifted a human-rights report toward Iranian government framing; in 655 refugee-scenario evaluations, non-English usefulness and factuality lagged English, while an LLM judge inflated scores and imagined safeguards. Separate tests found semantically equivalent English and Farsi guardrail policies produced 36–53% scoring gaps. The author argues high-stakes deployment needs multilingual human evaluation feeding continuous, context-aware safeguards rather than trusting summaries or automated judges as neutral.

### Comment pulse

- Users reported Arabic and Russian outputs adopting dated, culturally loaded voices, plausibly reflecting uneven training corpora.
- Human summaries also frame and omit — counterpoint: hidden system policies can reproduce bias invisibly and at scale.
- Podcast and video tools reportedly suppress controversial details or overweight arbitrary passages, making source review essential.

### LLM perspective

- **View:** Summarization is an editorial transformation whose omissions can be steered without visible factual fabrication.
- **Impact:** Refugees and other high-risk users receive weaker advice precisely where language limits independent verification.
- **Watch next:** Native-speaker red teams, multilingual retrieval checks, guardrail parity benchmarks, and uncertainty-aware evaluators.
