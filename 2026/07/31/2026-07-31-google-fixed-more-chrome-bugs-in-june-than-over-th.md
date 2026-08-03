# Google fixed more Chrome bugs in June than over the past two years, thanks to AI

- Score: 478 | [HN](https://news.ycombinator.com/item?id=49120097) | Link: https://blog.google/security/chrome-stronger-with-every-update/

### TL;DR

Chrome says LLM-based agents now assist vulnerability discovery, triage, candidate patches, review, and tests. Chrome 149 and 150 fixed 1,072 security bugs—more than the prior 23 milestones combined—while automation reportedly saves hundreds of developer hours monthly. Google pairs locked-down scanning with faster releases, dynamic patching research, C++ hardening, and targeted Rust adoption. HN debate centered on whether the surge demonstrates useful automation or reflects backlog and KPI effects, whether C++ remains tenable, and whether Google disclosed enough failures to assess net security.

### Comment pulse

- Rust advocates blame C++ → manual memory hazards scale poorly — counterpoint: wholesale ports discard institutional knowledge and overlook browser-specific complexity.
- Skeptics reject raw fix counts → missing false-positive, revert, regression, and AI-introduced-bug rates prevent judging net security improvement.
- Supporters distinguish assisted security from blind generation → adversarial analysis gains value when harnesses, critics, tests, and human review constrain outputs.

### LLM perspective

- View: Discovery scale only improves safety when validated fixes reach users before public patches reveal exploitable details.
- Impact: External researchers must target additive findings as automated pipelines absorb routine discovery, while developers increasingly review machine-generated patches.
- Watch next: Compare severity-adjusted fix rates, regressions, patch-gap duration, and restart latency before and after Chrome 149.
