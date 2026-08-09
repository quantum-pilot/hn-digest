# €54k spike in 13h from unrestricted Firebase browser key accessing Gemini APIs

- Score: 375 | [HN](https://news.ycombinator.com/item?id=47791871) | Link: https://discuss.ai.google.dev/t/unexpected-54k-billing-spike-in-13-hours-firebase-browser-key-without-api-restrictions-used-for-gemini-requests/140262

### TL;DR

A Firebase project used for Authentication exposed an unrestricted browser API key; after Firebase AI Logic enabled Gemini, automated traffic generated more than €54,000 in 13 hours. An €80 budget alert arrived only after charges reached €28,000, and delayed reporting doubled the final total. Google initially deemed the usage valid and denied adjustment. Google cited new account/project caps, leaked-key detection, planned rejection of unrestricted keys, and prepaid billing, while warning against client-side secrets. Hacker News blamed “keys are not secrets” guidance and delayed alerts that cannot act as hard brakes.

### Comment pulse

- Budget alerts are notifications, not limits — counterpoint: commenters argued offering delayed alerts as protection creates a dangerously misleading control.
- Billing aggregation cannot be perfectly real-time, but a 13-hour anomaly immediately following new permissions should trigger provider-side fraud detection.
- Legacy cross-service browser keys changed risk when Gemini became billable, exposing a documentation and secure-default migration failure.

### LLM perspective

- **View:** Browser keys became financial secrets when costly inference accepted them; secure defaults should have preceded cross-service enablement.
- **Impact:** Small developers face existential bill shock, Google absorbs trust damage, and frontend architectures must move inference behind controlled servers.
- **Watch next:** Adjustment appeal, unrestricted-key shutdown, prepaid rollout, cap enforcement latency, anomaly auto-blocking, alert semantics, and treatment of compromised usage.
