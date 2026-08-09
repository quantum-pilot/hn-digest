# Measuring Claude 4.7's tokenizer costs

- Score: 518 | [HN](https://news.ycombinator.com/item?id=47807006) | Link: https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you

### TL;DR

An independent test found Claude Opus 4.7’s tokenizer used 1.325× as many tokens as 4.6 across seven real-world Claude Code samples, rising to 1.445× for a CLAUDE.md file and 1.47× for technical documentation. A 20-prompt IFEval sample showed strict prompt-level compliance improving from 85% to 90%, but no loose-mode gain. Modeling an 80-turn cached session estimated costs rising 20–30%, though the author cautions that tokenizer, model weights, output length, and post-training effects cannot be isolated.

### Comment pulse

- Several readers said cost-per-task matters more than tokenizer counts — counterpoint: organizations face explicit quota multipliers and rate limits.
- Businesses argued engineer time dwarfs subscriptions, while hobbyists and autonomous-agent users feel usage charges acutely.
- Discussion favored task-aware model routing as frontier performance yields increasingly expensive, uneven returns.

### LLM perspective

- Rebenchmark complete tasks, because shorter reasoning can offset denser input tokenization.
- Cache-heavy sessions mute dollar impact but not quota pressure or cold-start and compaction costs.
- The tiny benchmark supports a hypothesis, not a reliable estimate of instruction-following gains.
