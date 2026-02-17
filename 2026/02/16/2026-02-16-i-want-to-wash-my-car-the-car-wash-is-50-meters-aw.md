# I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

- Score: 1379 | [HN](https://news.ycombinator.com/item?id=47031580) | Link: https://mastodon.world/@knowmadd/116072773118828295

### TL;DR
A viral trick question—“I want to wash my car. The car wash is 50m away. Should I walk or drive?”—exposed that some LLMs answer “walk,” ignoring that the car must be driven to be washed. HN discussion splits between blaming users for “underspecified prompts” and blaming models for brittle, pattern-based reasoning (short distance → walk) instead of goal-aware understanding. Commenters note vendors quickly “patch” such failures after publicity, raising concerns about prompt fragility, benchmark gaming, and safety in real-world decision-making.

---

### Comment pulse
- LLMs latch onto “50m → walk” → strong training prior overwhelms goal (“wash car”), revealing language-pattern limits, not mere ambiguity—counterpoint: clearer prompts still reliably fix it.  
- Expectation: systems used like humans must handle messy, underspecified questions or ask clarifications; “you’re prompting wrong” is an unacceptable safety and UX stance.  
- Quietly patching viral failures masks structural weaknesses; with “move fast” AI deployment, commenters want systematic query-analysis safeguards, not one-off fixes per TikTok meme.

---

### LLM perspective
- View: Treat this as a goal-inference test: model must prioritize “achieve X” over surface heuristics like distance.  
- Impact: Product UIs should encourage users to state goals explicitly and have models request clarification when intent is uncertain.  
- Watch next: Robustness benchmarks using adversarial everyday questions; public model-change logs explaining behavioral patches, not just better scores.
