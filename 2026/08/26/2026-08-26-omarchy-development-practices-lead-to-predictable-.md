# Omarchy development practices lead to predictable security issues

- Score: 281 | [HN](https://news.ycombinator.com/item?id=49447682) | Link: https://blog.happyfellow.dev/merchants-of-insecurity/

### TL;DR

The author argues Omarchy’s development culture makes severe security bugs predictable, citing shell injection through video titles and notifications capable of executing arbitrary commands. Rapid fixes and a security team do not compensate, they say, for AI-generated bash handling untrusted input without adequate review. HN split between treating those flaws as evidence of systemic negligence and defending Omarchy’s polished, fast, opinionated Arch experience. Others objected that political hostility toward DHH and an editorialized submission title overwhelmed technical analysis.

### Comment pulse

- Bug class matters more than fix speed → injection flaws suggest missing basic threat modeling and review.
- Users value decisive UX → simple installation and coherent defaults can outweigh customization or perceived risk.
- Culture-war framing obscures evidence → commenters wanted deeper technical detail and less personal antagonism.

### LLM perspective

- View: Security credibility depends on preventing recurring bug classes, not counting rapidly closed reports.
- Impact: Enthusiastic users and employers must reassess whether convenience justifies machine-wide execution risk.
- Watch next: Audit input boundaries, AI-generated patches, review requirements, regression tests, and disclosure quality.
