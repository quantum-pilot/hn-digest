# It looks like the status/need-triage label was removed

- Score: 269 | [HN](https://news.ycombinator.com/item?id=46721179) | Link: https://github.com/google-gemini/gemini-cli/issues/16728

### TL;DR
A GitHub issue about adding native JetBrains IDE detection to Google’s `gemini-cli` accidentally exposed a runaway labeling loop: the `gemini-cli` bot kept adding and removing the `status/need-triage` label thousands of times. Two conflicting GitHub Actions workflows—one removing the label, another re-adding it whenever a “non-maintainer” removed it—failed to recognize the bot as automation, spamming notifications and burning API calls. HN readers relate similar automation feedback loops and discuss ownership, costs, and why “AI agents” need guardrails and self-awareness.

---

### Comment pulse
- Runaway loop → Two workflows fought over one label, generating ~4.6k events, lots of notification email, and unnecessary Gemini inference calls—counterpoint: this is basic automation, not advanced AI.  
- Automation horror stories → Commenters recount email/helpdesk/Salesforce loops that flooded ticket systems or even took down servers, showing how tiny rules can cascade.  
- Governance and ownership → GitHub staff note the app lives under a personal account, not a Google org, and describe upcoming support for org-owned apps and better permissions.

---

### LLM perspective
- View: Event-driven agents need explicit self-identity, exemptions for other bots, and loop-detection (idempotency, rate caps, circuit breakers).  
- Impact: Any team wiring AI or rules into CI, issue triage, or support queues risks silent cost overruns and noisy spam storms.  
- Watch next: Expect patterns like “bot policies,” standardized agent metadata, and dashboards that surface abnormal automation churn in real time.
