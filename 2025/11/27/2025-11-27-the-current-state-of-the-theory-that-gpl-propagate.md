# The current state of the theory that GPL propagates to AI models

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46068777) | Link: https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/

### TL;DR
The article surveys whether GPL obligations “stick” to AI models trained on GPL code. Legally, the idea isn’t dead but has no precedent: the Copilot class action keeps open-source license–violation claims alive, while a German ruling (GEMA v. OpenAI) treats memorized works inside a model as copyright “reproduction,” potentially supporting propagation in extreme memorization cases. Counterarguments highlight copyright doctrine, GPL wording, technical realities, and impracticality. OSI favors open models plus data transparency; FSF wants freedom extended to data but treats it as an ethical, not yet legal, standard. HN discussion debates GPL’s purpose, feasibility of enforcement, and whether AI copyright rules should be relaxed or tightened.

---

### Comment pulse
- GPL’s spirit = user freedom, not “code sharing” → laundering GPL via AI betrays users; even one copied GPL function would infect a project—counterpoint: GPL also encodes a broader software–user relationship.  
- Enforcement doubts → proving training on copyleft data is hard, but leakage, inversion attacks, and discovery can expose it; bigger worry is outputs infringing third‑party copyrights.  
- Policy outlook → many cases seek a bright line on “when training/output infringes”; outcome may mirror Google v. Oracle, or be superseded by new legislation.

---

### LLM perspective
- View: Treat training on GPL as contract/compliance risk; focus on attribution, filters, and dataset curation rather than assuming “fair use solves everything.”  
- Impact: Model vendors, open‑source maintainers, and enterprises using AI coding tools need clearer internal policies and risk assessments around GPL‑tainted training.  
- Watch next: Appellate rulings in GEMA and Copilot, OSI/FSF follow‑on guidance, and any jurisdiction explicitly declaring models derivative or non‑derivative as a rule.
