# ChatGPT now knows what you do on other websites via ad collector

- Score: 707 | [HN](https://news.ycombinator.com/item?id=49776729) | Link: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/

### TL;DR

An investigator reports that ChatGPT creates a year-long `__obi` cookie tied to an account or persistent anonymous device, which OpenAI advertising tags then send from participating websites alongside page paths, events, and sometimes hashed contact data. Testing covered Chrome on Android and hundreds of observed pixels; Safari blocks the mechanism, desktop Chrome was untested, and the server-side account join was inferred rather than observed. HN viewed this as familiar third-party ad tracking made more sensitive by intimate chatbot use.

### Comment pulse

- Standard adtech remains invasive → attaching cross-site behavior to a conversational identity combines browsing signals with unusually sensitive user disclosures.
- Regulation provides incomplete protection → EU rules and consent interfaces constrain some practices, but commenters report persistent tracking and dark patterns.

### LLM perspective

- View: The central concern is consent mismatch: an analytics choice appears to enable marketing-adjacent cross-site identification.
- Impact: Chatbot users and advertisers may unknowingly participate in cross-site measurement potentially resolvable to an account.
- Watch next: OpenAI should explain classification, consent behavior, retention, account joining, and browser-specific reach.
