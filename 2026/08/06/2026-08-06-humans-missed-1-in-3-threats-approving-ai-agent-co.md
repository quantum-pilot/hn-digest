# Humans missed 1 in 3 threats approving AI agent commands across 40k game runs

- Score: 283 | [HN](https://news.ycombinator.com/item?id=49195468) | Link: https://scalex.dev/blog/ai-agent-permissions-stats/

### TL;DR

A permission game collected 409,000 approve-or-deny decisions across 40,000 runs and found players missed 33.7% of threats. Obvious destruction was missed 11.7%, but credential access 35%; familiar npm scripts concealed exfiltration payloads and were missed 52.5%, while benign cleanup and configuration commands were often blocked. Accuracy worsened late in timed sessions, illustrating fatigue and the cost of vigilance. The author recommends sandboxing and separating secrets rather than treating approval prompts as sufficient. HN challenged the game’s artificial stakes, disputed its safe/unsafe labels, and largely agreed click-through supervision is structurally weak.

### Comment pulse

- Critics called the statistics non-scientific because failures had no consequences, the timer encouraged haste, and disputed labels lacked environmental context.
- The author acknowledged contested cases — counterpoint: disagreement itself demonstrates why users cannot reliably classify context-dependent commands.
- Permission prompts may shift liability, not security; reading files, editing scripts, and making network requests combine into hard-to-police exfiltration paths.

### LLM perspective

- View: Command-level approval cannot expose transitive behavior after an agent edits code, dependencies, configuration, or scripts.
- Impact: Developers either lose productivity auditing every step or accept risk; vendors need capability boundaries that remain meaningful under composition.
- Watch next: Benchmark sandbox policies, secret isolation, taint tracking, auto-mode classifiers, untimed expert performance, and consequences resembling real work.
