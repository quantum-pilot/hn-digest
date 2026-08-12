# Microsoft says bug causes Copilot to summarize confidential emails

- Score: 227 | [HN](https://news.ycombinator.com/item?id=47060202) | Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/

### TL;DR

Microsoft says a Microsoft 365 Copilot code bug bypassed sensitivity labels and data-loss-prevention policies, allowing Work Tab Chat to read and summarize confidential messages in the current user’s Sent Items and Drafts folders. The issue was detected January 21, and a fix began rolling out in early February, but Microsoft had not given a completion date or affected-user count. The company was contacting a subset of users to verify remediation and classified the event as an advisory, indicating limited reported scope rather than proving no privacy impact.

### Comment pulse

- Commenters argue access controls must prevent AI from seeing restricted data, because labels and prompts are weaker than architectural isolation.
- Some fear confidential text trained models — counterpoint: others note Microsoft says Copilot customer data is not used for model training.
- Several distinguish a DLP policy failure within one mailbox from cross-user access, while still viewing it as a serious trust breach.

### LLM perspective

- **View:** DLP controls designed for data movement need explicit semantics for same-user AI retrieval and cloud processing.
- **Impact:** Compliance teams must validate enforcement paths rather than assume labels automatically constrain newly integrated agents.
- **Watch next:** Fix completion, affected-tenant counts, audit logs for prior summaries, and regression tests beyond Sent Items and Drafts.
