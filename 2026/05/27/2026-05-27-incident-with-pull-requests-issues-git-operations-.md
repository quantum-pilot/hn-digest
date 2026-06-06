# Incident with Pull Requests, Issues, Git Operations and API Requests

- Score: 252 | [HN](https://news.ycombinator.com/item?id=48293080) | Link: https://www.githubstatus.com/incidents/xy1tt3hs572m

## TL;DR
GitHub experienced a brief but serious incident on May 27, 2026, degrading core functionality: pull requests, issues, git operations, and API calls. It lasted a bit over an hour from initial investigation to resolution, with a root-cause analysis promised later. Hacker News commenters are far more focused on the broader pattern: a spike in critical outages over the last month, subtle PR inconsistencies that risk faulty code review, and speculation that Azure migration, AI-driven traffic, and looser engineering standards are eroding reliability.

---

## Comment pulse
- Reliability is trending down → Third‑party uptime trackers show a sharp rise in critical GitHub incidents recently, especially May 2026—counterpoint: some suspect changing incident classification/recording.
- Functional correctness is wobbling → PRs sometimes miss commits or lag branch updates, forcing multi‑minute delays and risking merges without a full, accurate diff.
- Why more outages? → Theories mix Azure capacity strain from AI workloads, AI-driven user growth, and teams relying on LLMs while cutting process and QA discipline.

---

## LLM perspective
- View: The worrying part isn’t minutes of downtime; it’s inconsistency in PR state, which undermines trust in code review as a safety mechanism.
- Impact: Heavy GitHub users, CI/CD pipelines, and AI coding agents become more fragile when the “single source of truth” is intermittently wrong.
- Watch next: GitHub’s postmortem details, any concrete SLO/SLA tightening, and whether they separate “AI load” infrastructure from core git/PR paths.
