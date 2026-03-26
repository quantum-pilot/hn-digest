# Apple randomly closes bug reports unless you "verify" the bug remains unfixed

- Score: 239 | [HN](https://news.ycombinator.com/item?id=47521876) | Link: https://lapcatsoftware.com/articles/2026/3/11.html

### TL;DR
Apple developer Jeff Johnson describes Feedback Assistant closing long-standing bug reports unless reporters “verify” the bug on the latest beta, even when Apple appears not to have tried reproducing or fixing them. He cites a 3‑year‑old, fully reproducible network privacy bug and a pinned-tabs Safari bug marked “Unable to diagnose” despite sample projects and steps. Hacker News commenters say this isn’t unique to Apple: enterprise vendors and open source often offload QA to users, auto-stale issues, and optimize metrics over actual fixes.

---

### Comment pulse
- This is standard industry behavior → enterprises and open source ask users to re-test on latest, then close as stale or “can’t repro” to hit metrics.  
- Users resent being unpaid QA → they already provide repros/logs, but vendors (Apple, Microsoft, etc.) still demand extensive verification work.  
- Some engineers justify closing old or hard bugs as pragmatic triage → others argue leaving them open is costless and more honest about product quality — counterpoint: huge backlogs become unmanageable.

---

### LLM perspective
- View: Apple’s workflow optimizes for clean dashboards, not reporter experience, undermining trust in Feedback Assistant as a serious engineering input.  
- Impact: Power users and third‑party devs disengage from formal reporting, reducing Apple’s visibility into real-world defects, especially nuanced networking/privacy issues.  
- Watch next: Evidence of process change—public bug states, SLAs, or engineering blogs explaining triage criteria—would show Apple treating reports as assets, not liabilities.
