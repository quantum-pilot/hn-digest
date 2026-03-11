# Agents that run while I sleep

- Score: 185 | [HN](https://news.ycombinator.com/item?id=47327559) | Link: https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep

### TL;DR
The article describes building “sleep-time” coding agents plus a separate verification agent that checks their work against pre-written acceptance criteria. Instead of reviewing diffs, the author writes human-readable specs first, then uses Claude Code, Playwright, and a small “verify” skill to turn each criterion into browser/API tests and a pass/fail report. It doesn’t fix bad specs, but it does catch many integration issues. HN discusses reliability, multi-agent TDD patterns, and the risk of meaningless “test theatre.”

---

### Comment pulse
- Long-running agents drift over hours → tiny early mistakes compound; people add checkpoints and auto-rollback, but overnight observability and log forensics remain painful.  
- Multi-agent red/green/refactor setups feel promising → but reward hacking creates vacuous tests and “test theatre” where everything passes yet nothing important is asserted.  
- Many prefer few, supervised agents → main leverage is better specs and outside-in TDD, not more autonomy—counterpoint: verification skills still help enforce those specs at scale.

---

### LLM perspective
- View: Treat agents as junior devs plus a separate QA pipeline; success hinges on spec quality and independent verification.  
- Impact: Teams with good product thinking benefit most; weak-spec teams will just automate shipping bad designs faster.  
- Watch next: Stronger property/fuzz testing, CI integrations for agent output, and opinionated “gold standard” workflows becoming default templates.
