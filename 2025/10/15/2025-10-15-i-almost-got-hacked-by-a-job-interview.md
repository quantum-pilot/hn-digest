# I almost got hacked by a 'job interview'

- Score: 707 | [HN](https://news.ycombinator.com/item?id=45591707) | Link: https://blog.daviddodda.com/how-i-almost-got-hacked-by-a-job-interview

### TL;DR

A developer says a fake blockchain recruiter sent a professional-looking Node/React interview repository containing obfuscated server-side code that fetched a remote payload. He nearly ran it unsandboxed under time pressure, but asked an AI coding assistant to inspect the project; it flagged the byte-encoded URL, whose payload he says targeted wallets, files, and credentials. HN readers treated the attack pattern as credible but questioned the article’s AI-shaped prose, noted suspicious LinkedIn account history, and warned that AI review itself can be manipulated.

### Comment pulse

- Interview code is untrusted input → run it in a disposable environment without personal credentials or host access.
- Verified profiles do not establish recruiter identity → recent account creation and urgent execution requests deserve scrutiny.
- AI found this payload but is not a security boundary → prompt injection and stronger obfuscation could defeat inspection.

### LLM perspective

- View: The decisive safeguard is isolation; automated review is a useful secondary check, not proof of safety.
- Impact: Developer machines expose production secrets and wallets, making recruitment workflows attractive supply-chain targets.
- Watch next: Standardize disposable interview environments, recruiter verification, network blocking, and malicious-code scanning.
