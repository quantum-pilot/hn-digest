# Hacking Moltbook

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46857615) | Link: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys

### TL;DR

Wiz researchers say Moltbook’s misconfigured Supabase Row Level Security exposed roughly 4.75 million records, including 1.5 million agent tokens, tens of thousands of emails, 4,060 private conversations, and some third-party credentials. Unauthenticated users could also alter posts until several rounds of responsible-disclosure fixes closed the access. The database showed 1.5 million agents tied to about 17,000 owners, with no proof posts came from autonomous AI. Commenters focused on insecure defaults, prompt-injection exposure, and the risks of giving unattended agents data and network access.

### Comment pulse

- Viral accessibility expands the threat surface → prepackaged agents attract nontechnical operators before security practices catch up.
- Database failure was conventional → an exposed client key became catastrophic only because Row Level Security policies were missing.
- Agent design adds a second risk → untrusted posts can become instructions when systems combine private data, autonomy, and outbound access.

### LLM perspective

- View: The incident joins ordinary authorization failure with uniquely scalable agent impersonation and prompt-manipulation risks.
- Impact: Owners, email subscribers, agent identities, and connected third-party accounts faced privacy or integrity exposure.
- Watch next: Verify token rotation, audit logs, RLS tests, rate limits, identity controls, and sandboxed agent permissions.
