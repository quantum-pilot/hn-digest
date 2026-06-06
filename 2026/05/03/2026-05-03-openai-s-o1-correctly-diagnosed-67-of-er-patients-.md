# OpenAI's o1 correctly diagnosed 67% of ER patients vs. 50-55% by triage doctors

- Score: 248 | [HN](https://news.ycombinator.com/item?id=47991981) | Link: https://www.theguardian.com/technology/2026/apr/30/ai-outperforms-doctors-in-harvard-trial-of-emergency-triage-diagnoses

### TL;DR
Harvard researchers tested OpenAI’s o1 reasoning model against ER doctors using only text from patient records for triage-style diagnosis. With minimal data (nurse notes, vitals), o1 matched or nearly matched the correct diagnosis in 67% of 76 real ER cases, versus 50–55% for doctors; with full notes, the gap shrank and lost statistical significance. In vignette-based treatment-planning tasks, o1 scored far higher. The study and coverage sparked debate over biased benchmarks, safety, accountability, and how AI should fit into real-world clinical workflows.

---

### Comment pulse
- Study design likely favors LLMs → doctors were restricted to text summaries, unlike real ER practice where history-taking and exams are central — counterpoint: it still shows value as a “paperwork second opinion.”
- Accuracy isn’t the only metric → safe medicine sometimes chooses conservative options and rule-outs over the numerically likeliest diagnosis; error type and harm profile matter more than raw percentage.
- LLMs already help patients and clinicians brainstorm diagnoses → but without healthcare reform they may be used to speed throughput, worsening care rather than improving access and safety.

---

### LLM perspective
- View: Treat frontier medical LLMs as always-on consultants that surface missed differentials, not autonomous diagnosticians.
- Impact: ER and primary care workflows, training, and malpractice standards must adapt to “doctor + AI” joint decision-making.
- Watch next: Prospective trials with full clinical context, bias/over-deference audits, and clear liability frameworks for AI-augmented care.
