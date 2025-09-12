# Claude's memory architecture is the opposite of ChatGPT's

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45214908) | Link: https://www.shloked.com/writing/claude-memory

- TL;DR
    - The article dissects Claude’s opt-in memory: it starts blank, only activates on explicit prompts, and searches raw chat history by keyword or time before synthesizing answers. ChatGPT’s memory is always-on, builds summaries/profiles, and personalizes automatically. HN frames this as strategy: ChatGPT targets mass-market stickiness; Claude optimizes professional control and privacy. Users split on convenience vs control; critics say Claude’s search misses non-keyword intents. Others expect future abstraction layers, and note Anthropic is changing memory soon.

- Comment pulse
    - Memory split maps to business goals → ChatGPT auto-profiles for consumer UX; Claude opts for explicit, privacy-leaning tools — counterpoint: subscriptions suffice; ads not required.
    - Users divided → Some disable ChatGPT memory for bleed/hallucination carryover; others prefer effortless recall. Claude’s manual retrieval praised for control and avoiding unwanted associations.
    - Claude’s raw-history search criticized → Lacks summaries/knowledge graphs; misses non-keyword queries. Others expect RL-derived abstractions and note Anthropic announced upcoming memory changes.

- LLM perspective
    - View: Opposite memory stacks are rational: Claude optimizes controllability/latency tradeoffs; ChatGPT maximizes seamless personalization and lock‑in.
    - Impact: Enterprise and regulated teams prefer explicit retrieval traces; consumers and education benefit from frictionless defaults that remember preferences.
    - Watch next: Measure retrieval precision/recall, latency, and privacy guarantees; watch Anthropic’s new memory; expect hybrid profiles plus searchable logs and non‑linguistic state.
