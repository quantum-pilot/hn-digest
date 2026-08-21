# Vomit: Clean up Claude 5's token output with a separate LLM

- Score: 169 | [HN](https://news.ycombinator.com/item?id=49375996) | Link: https://github.com/zachahn/vomit

## TL;DR
Vomit is a small Go CLI that taps into your local Claude Code session, captures its verbose “token vomit,” and pipes it through a separate local LLM (via OpenAI-style API, Llama.app, or Ollama). That second model rewrites Claude’s meandering, self-congratulatory prose into clear, conversational English while preserving intent. HN discussion splits between people desperate for relief from unreadable “Claude-speak,” those who see multi-model stacks and prompt scaffolding as more direct fixes, and skeptics of the growing AI Rube Goldberg machine.

---

## Comment pulse
- Core pain: baked-in “Claude dialect” feels obfuscated, verbose, and resistant to AGENTS.md-style instructions; some users literally post-process everything just to stay productive.  
- Multi-model stacks debated: critics ask why not switch vendors; supporters say “reasoning vs style” and use cross-model review to boost reliability — counterpoint: feels like needless complexity.  
- Meta-frustration: the ecosystem is accreting layers of tools-on-tools, undermining the promise that AI should simplify work rather than require elaborate orchestration.

---

## LLM perspective
- View: Vomit encodes a reusable “LLM-to-human translation” pattern, separating reasoning from communication style via a fixed editor prompt.  
- Impact: Heavy Claude Code users, and anyone drowning in agentic tool output, gain a drop-in readability layer without changing their primary model.  
- Watch next: Native “style control” knobs, IDE-integrated de-jargonizers, and benchmarks measuring readability vs. accuracy for agent-code and reasoning streams.
