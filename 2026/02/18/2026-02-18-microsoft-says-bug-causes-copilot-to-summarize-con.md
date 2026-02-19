# Microsoft says bug causes Copilot to summarize confidential emails

- Score: 227 | [HN](https://news.ycombinator.com/item?id=47060202) | Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/

- TL;DR  
Microsoft disclosed that a bug in Microsoft 365 Copilot’s “work” chat has, since late January, been summarizing users’ confidential emails in Sent and Drafts folders, ignoring sensitivity labels and configured DLP policies. A fix has been rolling out since early February, but the impact and number of affected tenants remain unclear, and Microsoft framed it only as a limited-scope advisory. Discussion centers on failed data-loss controls, over‑aggressive “AI everywhere” strategies, weak transparency, and whether sensitive data should ever reach LLM services.

- Comment pulse  
  - Bug shows “AI everywhere” risk: labels/DLP failed, other similar leaks may lurk unnoticed.  
  - LLMs with screen-wide access can't be constrained by tags or prompts; denying access is the only real protection.  
  - Microsoft labeling this as an “advisory” highlights preference to downplay incidents and avoid full incident reports with regulatory scrutiny.  

- LLM perspective  
  - View: Treat Copilot-like AIs as separate services; enforce strict least-privilege access and fail-closed behavior rather than trusting labels.  
  - Impact: Organizations handling regulated data should pause or narrow Copilot rollout for email until DLP interactions are independently validated.  
  - Watch next: Diagnostic logs for AI data flows, red-team prompt-injection tests, and contractual guarantees about training versus inference data use.
