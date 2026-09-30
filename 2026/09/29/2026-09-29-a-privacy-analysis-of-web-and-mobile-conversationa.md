# A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]

- Score: 419 | [HN](https://news.ycombinator.com/item?id=49890226) | Link: https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf

### TL;DR

A May 2026 study tested nine consumer AI assistants on the web and eight on Android from Spain, finding 124 third-party domains linked to 44 organizations. Six web clients and three Android clients disclosed conversation-derived artifacts, sometimes alongside persistent identifiers; consent rejection reduced but did not eliminate tracking, and paid tiers changed little. Shared permalinks also created exposure risks. The authors frame their results as a point-in-time lower bound, not a legal verdict: tests were black-box, mostly single-run and excluded enterprise tiers and several client types.

### Comment pulse

- Readers treated UUID-based sharing links as fragile privacy boundaries → Link leakage can turn nominal obscurity into broad conversation exposure.
- Some disputed whether observed integrations were deliberate disclosure or rushed implementation → The measurements establish flows, not every recipient’s purpose.
- Others favored local models to reduce platform trust → Convenience was weighed against handing sensitive conversations to complex tracking ecosystems.

### LLM perspective

- View: Conversational data inherits familiar web-tracking risks while carrying unusually revealing context.
- Impact: Consent controls and subscriptions alone appear insufficient safeguards in the tested configurations.
- Watch next: Provider remediations and repeated multi-region measurements should test whether these May findings persist.
