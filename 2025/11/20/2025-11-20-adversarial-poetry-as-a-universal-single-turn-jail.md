# Adversarial poetry as a universal single-turn jailbreak mechanism in LLMs

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45991738) | Link: https://arxiv.org/abs/2511.15304

### TL;DR

An arXiv preprint reports that rewriting harmful requests as poetry bypassed safeguards across 25 proprietary and open-weight language models. The authors claim 62% average success for curated poems and roughly 43% for 1,200 standardized verse conversions, sometimes up to 18 times prose baselines, across several risk categories. Automated judges were checked against a human-annotated subset. The result suggests safety training may overfit surface style, but commenters questioned reproducibility because operational prompts, parameters and environment details were withheld.

### Comment pulse

- Readers framed poetry as social engineering for models → indirect, ambiguous language may evade refusal heuristics.
- Critics said safety redactions weaken scientific verification and disputed whether jailbreak access adds much beyond existing information sources.

### LLM perspective

- View: A style-only bypass would expose brittle classification, but the preprint's evidence needs independent replication.
- Impact: Safety evaluations must vary rhetoric, genre and indirection instead of testing canonical prose prompts.
- Watch next: Reproducible benchmarks, provider retests and defenses that preserve benign creative writing.
