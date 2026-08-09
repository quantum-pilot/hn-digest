# Changes in the system prompt between Claude Opus 4.6 and 4.7

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47823270) | Link: https://simonwillison.net/2026/Apr/18/opus-system-prompt/

### TL;DR

Anthropic’s published Claude.ai prompt diff shows Opus 4.7 being pushed toward action, completion, and brevity: resolve minor ambiguity with reasonable assumptions or tools, search deferred capabilities before claiming no access, finish tasks, respect conversation endings, and avoid long caveats. Safety guidance expands substantially for child protection and disordered eating, while contested yes/no questions may receive nuance instead. The prompt also adds PowerPoint integration and removes obsolete style and presidential-context instructions. Anthropic publishes system prompts, but tool descriptions remain outside the archive.

### Comment pulse

- Many developers prefer mandatory clarification because silent assumptions create costly or dangerous rework.
- Others accept action-first behavior for underspecified everyday requests, especially where tools can cheaply resolve uncertainty.
- Users welcomed concision — counterpoint: hardcoded brevity can reduce learning value and safety in low-level technical work.

### LLM perspective

- A single default interaction style cannot fit casual chat, exploratory learning, and high-risk code changes equally.
- Modular, user-selectable policies could expose tradeoffs without requiring repeated prompt overrides.
- Watch whether these instructions reach Claude Code and whether behavioral evaluations measure assumption-related rework.
