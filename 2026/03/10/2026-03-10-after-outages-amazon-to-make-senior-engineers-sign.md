# After outages, Amazon to make senior engineers sign off on AI-assisted changes

- Score: 395 | [HN](https://news.ycombinator.com/item?id=47323017) | Link: https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/

- TL;DR  
    - Amazon’s retail and AWS systems have suffered several high-impact outages traced partly to AI code assistants, including a 6‑hour shopping-site failure and a 13‑hour AWS calculator issue. In response, Amazon will require senior engineers to approve AI-assisted changes from junior and mid-level staff and is using its weekly ops meeting for a root-cause deep dive. HN commenters argue that senior review alone won’t fix systemic problems: weak incentives, under-staffing, poor testing culture, and naive AI adoption.

- Comment pulse  
    - Media overhype vs routine ops: some say it’s just a weekly meeting; others note the new AI-approval policy is legitimately newsworthy.  
    - Senior review won’t magically sanitize AI code → deep review is as time-consuming as writing, so testing, simplification, and self-review workflows matter more.  
    - Amazon’s promo culture rewards volume and minimal PR friction → developers are pushed toward AI shortcuts; process tweaks fail unless performance metrics change—counterpoint: good upfront collaboration keeps PR noise low.

- LLM perspective  
    - View: AI coding in critical infra now needs governance similar to deployment of juniors at scale.  
    - Impact: SREs, senior engineers, and tooling teams will absorb more code-review and observability load.  
    - Watch next: concrete internal guardrails: AI usage flags in diffs, mandatory tests, rollback automation, and measured outage-rate improvements.
