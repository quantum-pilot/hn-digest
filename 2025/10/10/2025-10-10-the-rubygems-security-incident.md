# The RubyGems "Security Incident"

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45535149) | Link: https://andre.arko.net/2025/10/09/the-rubygems-security-incident/

### TL;DR

Former RubyGems.org operator André Arko disputes Ruby Central's account of an AWS access incident. He says contradictory permission changes made him suspect compromise, so he locked down AWS while on call, then withdrew once he understood the takeover was authorized. He later discovered Ruby Central had left him root, GitHub-owner, monitoring, password-vault, and shared production access, which he disclosed. Ruby Central reportedly alleged unauthorized access. HN commenters saw severe offboarding failures but questioned why Arko did not immediately report his password change; the competing accounts remain unresolved.

### Comment pulse

- Offboarding controls plainly failed if Arko's account is accurate → former operators retained root and shared credentials after an announced security audit.
- Intent does not settle procedure → commenters asked why a suspected attack and root-password change were not communicated immediately.
- Trust deteriorated on all sides → governance conflict, alleged commercial log ideas, legal threats, and selective disclosures cloud infrastructure stewardship.

### LLM perspective

- View: Independent of motive, privileged access required an immediate inventory, rotation, ownership transfer, and documented incident channel.
- Impact: Ruby developers must trust infrastructure managed amid unresolved governance and operational-control disputes.
- Watch next: Seek both timelines, access logs, credential-rotation evidence, communication records, postmortem findings, and governance reforms.
