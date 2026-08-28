# Claude for Chrome

- Score: 799 | [HN](https://news.ycombinator.com/item?id=45030760) | Link: https://www.anthropic.com/news/claude-for-chrome

### TL;DR

Anthropic is piloting a Chrome extension with 1,000 Max users that lets Claude inspect pages, click, and fill forms. The company openly identifies prompt injection as the central risk: in 123 adversarial tests, targeted attacks succeeded 23.6% of the time without new mitigations and 11.2% afterward in autonomous mode. Defenses include site permissions, confirmations, system instructions, blocked high-risk categories, and classifiers. A small browser-specific challenge set fell from 35.7% to zero, but Anthropic advises avoiding financial, legal, medical, and other sensitive use.

### Comment pulse

- Readers called browser agents a combination of private data, untrusted content, communication, and consequential action.
- Practitioners reported weak reliability from large DOMs, visual context loss, and long interaction loops.
- Some welcomed Anthropic’s disclosure while considering an 11.2% attack rate unacceptable.

### LLM perspective

- View: Limited rollout is warranted because prompt injection remains a systems problem, not a solved classifier task.
- Impact: Browser access magnifies ordinary model mistakes into data loss, disclosure, or unauthorized action.
- Watch next: Measure unseen attacks, permission bypasses, confirmation fatigue, and damage containment under realistic browsing.
