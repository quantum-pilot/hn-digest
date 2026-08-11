# Google API keys weren't secrets, but then Gemini changed the rules

- Score: 1194 | [HN](https://news.ycombinator.com/item?id=47156925) | Link: https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules

### TL;DR

Truffle Security says Google reused one API-key format for public project identification and sensitive Gemini authentication. When a project owner enables the Generative Language API, older unrestricted keys embedded in Maps, Firebase, websites, or apps can silently gain access to Gemini files and cached content, consume quotas, and incur charges. A Common Crawl scan found 2,863 live affected keys, including Google’s. Google reclassified the report as a bug and began blocking discovered keys, planning scoped AI Studio defaults and notifications. HN called retroactive remediation technically disruptive.

### Comment pulse

- The API itself is not enabled automatically → exposure begins when one teammate enables Gemini on a reused project containing public keys.
- Blanket privilege removal may be safest → commenters warned it would also break legitimate Gemini applications at enormous scale.
- Calling historical public keys leaked shifts responsibility → Google’s own earlier guidance encouraged client-side exposure.

### LLM perspective

- **View:** Credentials must never gain new sensitive privileges without explicit reauthorization.
- **Impact:** GCP teams should inventory enabled APIs, scope every key, and rotate exposed Gemini-capable credentials.
- **Watch next:** Root-cause separation, retrospective notices, false-positive blocking, and treatment of pre-Gemini keys.
