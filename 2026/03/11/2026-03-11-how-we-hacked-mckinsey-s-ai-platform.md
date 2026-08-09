# How we hacked McKinsey's AI platform

- Score: 377 | [HN](https://news.ycombinator.com/item?id=47333627) | Link: https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform

### TL;DR

Security startup CodeWall says its autonomous agent found 22 unauthenticated Lilli endpoints and exploited SQL injection through concatenated JSON field names, obtaining production read-write access within two hours. It claims exposure of 46.5 million plaintext chats, 728,000 files, 57,000 accounts, RAG data, system prompts, and an IDOR enabling cross-user histories. CodeWall says McKinsey patched endpoints by March 2. HN noted this was ordinary authorization and SQL failure, not prompt injection, questioned independent confirmation, and blamed incentives that neglect long-lived internal software.

### Comment pulse

- Writable prompts could silently poison trusted answers → prompt integrity needs access control, versioning, and monitoring like code.
- AI found an injection missed by ZAP → counterpoint: publicly exposed unauthenticated APIs were already severe basic failures.
- Insider accounts described rotating teams and review-cycle incentives → unfinished internal products can outlive their owners without stewardship.

### LLM perspective

- **View:** Autonomous testing is noteworthy, but extraordinary exposure claims require independently verifiable evidence.
- **Impact:** Employees and clients may face confidentiality risk; organizations must segment data and verify authorization everywhere.
- **Watch next:** McKinsey confirmation, breach notices, technical proof, agent audit logs, and remediation details.
