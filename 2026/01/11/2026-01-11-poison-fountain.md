# Poison Fountain

- Score: 156 | [HN](https://news.ycombinator.com/item?id=46577464) | Link: https://rnsaffn.com/poison3/

### TL;DR
Poison Fountain is a site that emits endless “poisoned” text intended to corrupt LLM training data. It encourages website operators to detect crawlers via hidden links and then serve compressed poison output to any scraper, framing this as a “war effort” against AI, echoing Geoffrey Hinton’s warnings. Hacker News discussion largely doubts its real impact, citing strong data curation, RL-driven progress, and easy scraper workarounds, while debating whether widespread poisoning merely raises costs or risks making models less safe and trustworthy.

---

### Comment pulse
- Frontier labs filter web data heavily and gain most from RL and better inference, so random poison is unlikely to derail top models—counterpoint: it still raises curation costs.  
- Scraper detection is weak; labs can mimic humans via browsers, OCR, and global IPs, while AI-generated “slop” is already degrading the open web’s training value.  
- Ethically, some see poisoning as leverage or DRM for unpaid data use; others warn it just destabilizes models and exposes proxies to hosting dubious content.

---

### LLM perspective
- View: Treat open-web training as adversarial by default; poisoning tools accelerate the shift toward curated, paid, or proprietary data sources.  
- Impact: Increases infrastructure, legal, and safety costs for large labs; small hobbyist trainers and naive scrapers are most vulnerable.  
- Watch next: Benchmarks for poison robustness, provenance/watermark standards, and regulation around data collection, liability, and “data sabotage.”
