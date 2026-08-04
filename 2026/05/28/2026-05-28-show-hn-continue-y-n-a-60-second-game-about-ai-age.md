# Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48308376) | Link: https://llmgame.scalex.dev

### TL;DR

This one-minute browser game simulates permission fatigue: an AI coding agent presents shell commands under time pressure, and players must approve or deny as many as possible while spotting harmful actions. Its premise is that rushed humans may trust plausible descriptions instead of reading commands. HN found the exercise memorable but exposed design gaps: deny-all initially yielded a near-win, the results omitted the descriptions that misled players, several safe/unsafe labels were disputed, and rapidly changing contexts felt less realistic than a sequence of routine approvals hiding one dangerous request.

### Comment pulse

- Post-game feedback needs evidence → players wanted every mistaken approval paired with its original description to diagnose exactly how time pressure fooled them.
- The scoring could reward blanket denial → an early deny-all strategy looked victorious — counterpoint: the creator added a distinct title after feedback.
- Risk labels and sequencing need realism → commenters disputed zshrc and lsof judgments and proposed task packs that bury one dangerous action among routine approvals.

### LLM perspective

- **View:** Permission UX fails when users must repeatedly perform semantic code review under interruption, urgency, and asymmetric consequences.
- **Impact:** Agent tools should minimize prompts, scope capabilities, preview effects, and make denial recoverable without encouraging reflexive approval.
- **Watch next:** Measure false approvals, overblocking, decision time, learning after explanations, and performance on realistic multi-step command sequences.
