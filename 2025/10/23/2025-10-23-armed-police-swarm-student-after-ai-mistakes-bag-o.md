# Armed police swarm student after AI mistakes bag of Doritos for a weapon

- Score: 405 | [HN](https://news.ycombinator.com/item?id=45684934) | Link: https://www.dexerto.com/entertainment/armed-police-swarm-student-after-ai-mistakes-bag-of-doritos-for-a-weapon-3273512/

- TL;DR
  - An AI gun-detection system at Baltimore County’s Kenwood High flagged a crumpled Doritos bag as a firearm, triggering an armed police response that handcuffed a 16-year-old. Vendor Omnilert called it a false positive that “worked as intended” with rapid human verification; the student reports trauma, the school offered counseling. HN readers question deploying opaque, unvalidated models in high-stakes contexts, press for human-in-the-loop review, transparency on accuracy/false positives, and legal/financial accountability; others note balancing false negatives versus false positives but say escalation costs here are extreme.

- Comment pulse
  - AI created unsafe armed escalation → false positive told officers teen had a gun, traumatizing students. — counterpoint: Higher recall acceptable only with low-cost verification.
  - Require transparency and human review → publish training data, ROC/false-positive rates; don’t dispatch on unvetted alerts; otherwise detectors get monetized into dangerous black boxes.
  - Enforce legal accountability and liability → armed stops require justified force; if no image review, it’s unreasonable; impose penalties for false positives to change incentives.

- LLM perspective
  - View: School safety AI needs a safety case: conservative thresholds, mandatory human gatekeeping, and staged, non-lethal verification before dispatch.
  - Impact: Procurement and insurers will demand independent audits, incident reporting, and kill-switches; vendors lacking transparent metrics will be deselected.
  - Watch next: BCPS incident report, Omnilert publishing ROC curves and datasets, NIST-style evaluations, policies requiring image review before police mobilization.
