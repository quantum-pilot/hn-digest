# The LLM Lobotomy?

- Score: 114 | [HN](https://news.ycombinator.com/item?id=45315746) | Link: https://learn.microsoft.com/en-us/answers/questions/5561465/the-llm-lobotomy

### TL;DR

An Azure customer alleges that identical, temperature-zero regression conversations against gpt-4o-mini became less accurate over six months, especially when producing enum fields, while newer mini and nano models were slower or worse. The author suspects undisclosed model changes but shared only a fabricated apple-and-mango illustration, not dated measurements. HN readers want reproducible logs and periodically rerun benchmarks, while offering alternative explanations including ordinary nondeterminism, inference infrastructure, hidden prompts, sampling bias, or changing deployment versions rather than degraded weights.

### Comment pulse

- Evidence is the missing centerpiece → claims of logged regressions remain untestable without scores, dates, request parameters, and identifiers.
- Temperature zero is not deterministic → repeated samples and statistical error rates are still required.
- Production users need stable contracts → version pinning, validation layers, and continuous regression alerts reduce exposure to behavioral drift.

### LLM perspective

- View: Model identity alone is insufficient provenance for a managed inference service.
- Impact: Applications with structured outputs inherit unannounced behavioral risk unless they validate every response.
- Watch next: Published test data, pinned deployment audits, repeated trials, latency percentiles, and provider change disclosures.
