# Did Claude increase bugs in rsync?

- Score: 270 | [HN](https://news.ycombinator.com/item?id=48411635) | Link: https://alexispurslane.github.io/rsync-analysis/

## TL;DR

An rsync contributor analyzed 36 historical releases to test whether two Claude-assisted releases are unusually buggy. Using a severity‑weighted “bugs per 10 commits” metric and exact permutation plus Fisher tests, both Claude releases fall within the historical distribution; the pre‑Claude v3.4.1 is the clear outlier. The author argues the AI backlash stems from selection bias and a surge of AI-generated CVEs causing more churn, not Claude itself. HN debates the tiny sample size, attribution methodology, concrete AI mistakes, and norms around disclosing LLM use.

## Comment pulse

- AI commits show regressions → calloc-change commit hurt performance; surge of Claude commits looks rushed. — counterpoint: others blame maintainers and CVE churn, not Claude.  
- Stats and attribution questioned → Only two Claude releases; bug-to-release mapping and recency effects may undercount recent issues and overstate pre-Claude outlier v3.4.1.  
- Norms and ethics split → Some see LLMs as useful tools; others report unusable code, fear plagiarism, and argue hiding AI authorship is deceptive.  

## LLM perspective

- View: Evidence so far: Claude-assisted rsync releases look statistically ordinary; outrage is driven more by anecdotes and prior anti-AI beliefs.  
- Impact: Maintainers now face social risk for transparent AI use, potentially incentivizing hidden assistance instead of open discussion and review.  
- Watch next: More insight comes from longitudinal datasets: per-commit bug attribution, AI vs human diffs, and standardized tooling disclosure in projects.
