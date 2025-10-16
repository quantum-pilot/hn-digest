# I almost got hacked by a 'job interview'

- Score: 707 | [HN](https://news.ycombinator.com/item?id=45591707) | Link: https://blog.daviddodda.com/how-i-almost-got-hacked-by-a-job-interview

- TL;DR
    - A developer nearly executed malware from a polished “coding test” sent by a LinkedIn “Chief Blockchain Officer” at a real-seeming company. An AI scan flagged obfuscated code in a server controller that fetched a short‑lived payload; VirusTotal showed wallet/credential-stealing behavior. The op used urgency, authority, and social proof to push execution before scrutiny. Takeaways: treat interview repos as untrusted, run in sandboxes, verify identities, and use AI/code review before running. HN debates AI-written tone, LinkedIn “verification,” and how easily LLM scans can be bypassed.

- Comment pulse
    - Post likely AI-written → repetitive hooks, cliché cadence; calls to flag AI-generated blogspam.
    - LinkedIn verification isn’t trustable → badges can be gamed; check profile age/history; viewing profiles reveals you to scammers; NFC ID verification can be abused.
    - LLM scans help but aren’t security → attackers can misname variables, obfuscate strings, or prompt-inject to evade detection — counterpoint: still a useful preflight alongside sandboxing.

- LLM perspective
    - View: Treat take-home projects as malware until proven safe; default to sandboxed, no-network execution and manual diffing.
    - Impact: Hiring pipelines and dev workflows must add isolation, secret hygiene, ephemeral dev envs, and wallet separation.
    - Watch next: Repo host malware scanning, LinkedIn/Persona verification hardening, standardized interview sandboxes, shared IOCs for short‑lived payload infra.
