# Changes in the system prompt between Claude Opus 4.6 and 4.7

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47823270) | Link: https://simonwillison.net/2026/Apr/18/opus-system-prompt/

### TL;DR
Anthropic publicly diffs its Claude chat system prompts; Opus 4.7 adds stronger safety (child protection, disordered eating, controversial questions), encourages concise replies, tool_search, and more autonomous “act before asking” behavior, while dropping some style micromanagement and Trump-specific clarifications thanks to a later knowledge cutoff. HN commenters like the transparency but criticize non-configurable tradeoffs: many want explicit clarification phases, richer, longer explanations, or fewer options. Others debate whether ever-growing safety sections are necessary harm reduction or creeping, opaque censorship.

### Comment pulse
- Users dislike new “act-don't-ask” rule → prefer mandatory clarification phases to avoid harmful or low-quality assumptions—counterpoint: others report Gemini handles keywordy, underspecified prompts well.  
- Expanded disordered-eating guardrails worry some → fear creeping censorship, extra latency, over-refusals; others say targeting at-risk users is common sense and liability-reducing.  
- Conciseness and option-listing tweaks divide users → some need long, didactic answers and fewer choices, arguing verbosity and style should be a user-tunable setting.  

### LLM perspective
- Expose these behaviors as per-conversation knobs → “clarification level”, “verbosity”, “risk sensitivity” instead of hardcoded, one-size-fits-all system prompts.  
- Tool_search plus richer safety tags implies more autonomous agents, but also more hidden policy complexity that developers must debug around.  
- Watch whether Anthropic documents internal tools and persona variants; transparency here will determine how reliably teams can build atop Claude.
