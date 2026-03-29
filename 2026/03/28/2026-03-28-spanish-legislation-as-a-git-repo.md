# Spanish legislation as a Git repo

- Score: 684 | [HN](https://news.ycombinator.com/item?id=47553798) | Link: https://github.com/EnriqueLop/legalize-es

### TL;DR
A project mirrors Spanish state legislation into a public Git repo: each law is a Markdown file and every reform is a dated git commit. Using the official consolidated BOE API, it encodes 8,600+ laws with full change history so you can `git log` and `git diff` instead of reading amending clauses. HN discussion explores extensions (overlaying court rulings, tagging lawmakers, unit-test-like checks), comparisons to France/UK, legal-tech business potential, and institutional resistance to making law truly computable.

---

### Comment pulse
- Make law executable/structured → Catala and similar efforts show tax and benefits rules can be encoded for precise computation—counterpoint: this doesn’t “prove” the law, only implementations.
- Next layer of value → link judgments and citations over time to show how text is interpreted, which provisions are fragile, and where drafting patterns fail.
- Structural change vs. cool mirror → real impact needs governments to treat repos as canonical (Open Law Library example); incumbents may resist transparent, efficiency-boosting tooling that erodes billable hours.

---

### LLM perspective
- View: This repo is a near-ideal corpus for experimenting with version-aware legal reasoning and automatic redlining tools.
- Impact: Legaltech startups, researchers, and civic hackers gain a clean, historical dataset without scraping PDFs or reverse-engineering formats.
- Watch next: Coverage of regulations and case law, official adoptions like Maryland’s, and stable APIs for cross-country, machine-readable legislative datasets.
