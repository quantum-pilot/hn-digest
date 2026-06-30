# HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No – 88

- Score: 943 | [HN](https://news.ycombinator.com/item?id=48713832) | Link: https://danunparsed.com/p/hackerrank-open-source-ats

### TL;DR
HackerRank’s newly open-sourced, LLM-based applicant tracking system scores the same resume very differently across runs (e.g., 90, 74, 88/100), exposing how stochastic and fragile AI screening can be. Hacker News discussion focuses on how temperature and infrastructure affect determinism, the legal risk of biased automated hiring (GDPR, EU AI Act, US discrimination law), and whether such noisy filters are justified by overwhelming applicant volume. Commenters also worry these systems overweight side projects/OSS, structurally favoring wealthy or unconstrained candidates.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- LLM resume scoring is highly variable; temperature only reshapes the sampling distribution, not a true determinism switch—counterpoint: temperature 0 with local, deterministic kernels can be stable.  

- AI hiring filters likely breach GDPR Article 22 and risk discrimination claims via correlated features—counterpoint: proving unlawful bias in court remains technically and evidentially hard.  

- Massive applicant volume makes noisy gates tempting, but ATSes overvalue OSS/personal projects, disadvantaging caregivers and poorer candidates; random lotteries might be similarly effective and fairer.  

---

### LLM perspective
- View: Open-sourcing exposes ATS logic, enabling scrutiny of variance and bias that proprietary systems usually hide.  

- Impact: HR teams and vendors must treat LLM screeners as advisory tools, not decision-makers, especially in regulated jurisdictions.  

- Watch next: Rigorous experiments comparing LLM ATS, structured human review, and partial randomization on hire quality and demographic impact.
