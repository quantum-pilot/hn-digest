# Where the goblins came from

- Score: 1012 | [HN](https://news.ycombinator.com/item?id=47957688) | Link: https://openai.com/index/where-the-goblins-came-from/

### TL;DR

OpenAI traced models’ multiplying goblin and gremlin metaphors to a reward signal built for ChatGPT’s “Nerdy” personality. Although Nerdy produced only 2.5% of responses, it accounted for 66.7% of goblin mentions; reinforcement learning and reused model-generated data spread the tic beyond that setting. OpenAI retired Nerdy, removed the reward, filtered creature-heavy training data, and added a Codex instruction for GPT-5.5. Hacker News praised the candid debugging account, joked about prompt engineering as machine ritual, and debated whether the episode demonstrates opacity or effective empirical control.

### Comment pulse

- Some saw training unpredictability as sorcery and an AGI limit — counterpoint: others said isolating the reward and mitigation showed engineering works.
- Commenters welcomed this transparency and wanted similar postmortems for recurring visual tints and recognizable phrases.
- A blanket creature prohibition may suppress legitimate topics such as the Goblins programming environment, illustrating brittle prompt-level fixes.

### LLM perspective

- **View:** Local style rewards can leak into default behavior when generated rollouts return to shared training pipelines.
- **Impact:** Lexical quirks reveal broader risks in reward design, data reuse, and conditional behavior separation.
- **Watch next:** Whether root-cause filters reduce tics without blocking relevant creature discussions or merely shifting them elsewhere.
