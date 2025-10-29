# Poker Tournament for LLMs

- Score: 297 | [HN](https://news.ycombinator.com/item?id=45730094) | Link: https://pokerbattle.ai/event

- TL;DR
  An LLM-only poker tournament is fun but not a measure of poker skill. Experts note strong poker needs mixed strategies, calibrated randomness, online search, and consistency—areas where general LLMs lag. State-of-the-art poker uses CFR with real-time search (e.g., Pluribus); current models even misread boards. Commenters flagged one-off results, luck, and logging inconsistencies. Others propose letting models talk to bluff. Prior runs used TEEs and public logs. Practical path: LLMs orchestrate tools, not play unaided.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - LLMs can’t play strong poker → need mixed strategies, randomness, and online search; token sampling isn’t proper RNG — counterpoint: external RNG and engines mitigate.
  - Tournament validity questioned → one event, LLMs vs LLMs, luck swings, missing hands, pot/stack inconsistencies; may show rule-following, not skill.
  - Specialized poker AI dominates → CFR plus real-time search (Pluribus); LLMs misread boards/hands; imperfect-information multiplayer is harder — counterpoint: allow table talk to test persuasion/bluffing.

- LLM perspective
  - View: Use LLM as orchestrator—rules, narration, and tool-calls for RNG and a poker engine; avoid unaided bet selection.
  - Impact: Better evaluations of planning under uncertainty than board strength; specialized CFR bots remain state-of-the-art for actual winning play.
  - Watch next: multi-table events, repeated matches with seed control, open logs, human baselines, ablations for RNG, memory, tool access.
