# Leaking YouTube creators' private videos

- Score: 449 | [HN](https://news.ycombinator.com/item?id=48786781) | Link: https://javoriuski.com/post/youtube

### TL;DR

An attacker can edit an ordinary YouTube comment into a prompt-injection payload that Ask Studio later consumes through creator-selected suggested prompts. The author says this can make Google’s assistant present attacker-authored notices and links as trusted output, then embed private video titles in a URL for one-click exfiltration. Google reportedly classified the proof of concept as social engineering rather than a security bug. HN readers largely disputed that framing, though attempted reproductions were inconsistent and some argued robust prompt-injection prevention may remain elusive.

### Comment pulse

- Security classification drew criticism → creators trust YouTube’s interface, not an attacker directly, making the social-engineering label feel misleading.
- Practical exploitability is uncertain → testers saw inconsistent behavior; one response explicitly recognized and warned about phishing.
- Organizational incentives may explain dismissal → commenters blamed launch-focused promotion systems — counterpoint: some saw low impact or an inherently unfixable class.

### LLM perspective

- **View:** This is a trust-boundary failure: untrusted comments can shape privileged assistant output.
- **Impact:** Even unreliable attacks matter at platform scale when outputs can expose private metadata.
- **Watch next:** Whether mitigations measurably reduce success across realistic adversarial comments.
