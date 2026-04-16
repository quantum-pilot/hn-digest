# Open Source Isn't Dead

- Score: 309 | [HN](https://news.ycombinator.com/item?id=47780712) | Link: https://www.strix.ai/blog/cal-com-is-closing-its-code-due-to-ai-threats

## TL;DR
Cal.com is closing its core source, citing AI-powered vulnerability discovery that makes code transparency a liability. Strix, an open-source AI security agent vendor, counters that attackers can probe black-box services just as effectively, so hiding code mainly removes benevolent reviewers. They advocate “AI versus AI”: continuous, automated testing wired into CI/CD while remaining open source. Hacker News broadly agrees AI shifts security economics, but many see Cal.com’s rationale as business-driven and Strix’s post as polished product marketing.

## Comment pulse
- AI tools flood open-source projects with vuln reports; some valuable, much junk. Closing code removes scrutiny, but firms can run scanners and bug bounties themselves.  
- Many suspect Cal.com’s move is about monetization and open-core, with AI as convenient PR cover; founder insists open source was profitable but customer data trumped.  
- Some argue obscurity is a valid extra layer that raises attacker costs; open vs closed remains a trade-off in where scarce security attention comes from.

## LLM perspective
- View: Treat security justifications for de-open-sourcing skeptically; demand concrete threat models and comparative risk analyses, not slogans.  
- Impact: Cheap automated testing will normalize frequent published security reports, raising expectations for even small projects’ hygiene and responsiveness.  
- Watch next: independent benchmarks of AI pentest tools on common targets; possible standards or regulations mandating continuous automated security testing.
