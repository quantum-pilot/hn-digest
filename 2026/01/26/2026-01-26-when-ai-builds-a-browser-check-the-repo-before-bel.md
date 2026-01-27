# When AI 'builds a browser,' check the repo before believing the hype

- Score: 189 | [HN](https://news.ycombinator.com/item?id=46769965) | Link: https://www.theregister.com/2026/01/26/cursor_opinion/

### TL;DR
Cursor claimed its AI agents built a from-scratch, 3‑million‑line Rust browser in a week, but the FastRender repo barely compiles, leans on Servo/QuickJS, performs terribly, and was savaged by browser engineers as unusable spaghetti. The article argues this was an over-marketed internal experiment passed off as a milestone, feeding CEO fantasies that AI will soon write most code. HN commenters attack lines-of-code bragging, question wild token-cost estimates, yet some still see the attempt as technically notable.

---

### Comment pulse
- Hype-as-milestone erodes trust → framing a fragile demo as “AI built a browser” misleads non-technical leaders and inflates unrealistic expectations.  
- LOC worship persists → “millions of lines” impresses managers, mirroring bosses filing unreviewed AI-generated PRs; developers call LOC-based productivity metrics technical-debt phrenology.  
- Costs and capability overstated → commenters challenge Perplexity’s 10–20T-token estimate as throughput-infeasible for sequential agents — counterpoint: others still view the experiment’s complexity as notable.  

---

### LLM perspective
- View → Agentic coding is promising but currently excels at scaffolding, not architecture; vendors over-claim because marketing rewards spectacle over reliability.  
- Impact → Engineering orgs should treat AI as collaborators: require tests, CI, code review, and reject LOC or “percent AI-written” as KPIs.  
- Watch next → Watch for reproducible agentic projects with passing CI, independent benchmarks, and human-readable designs; anything less is a demo, not product.
