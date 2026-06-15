# Claude Fable is relentlessly proactive

- Score: 769 | [HN](https://news.ycombinator.com/item?id=48498573) | Link: https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/

- TL;DR  
Simon Willison recounts Claude Fable 5 acting like an ultra-proactive coding agent. From a single screenshot and a vague prompt, it spun up his Datasette dev server, drove Playwright and real browsers, worked around macOS restrictions with Quartz, injected JavaScript into templates, built a tiny CORS web server, and navigated shadow DOM to reproduce and fix a minor textarea scrollbar bug—spending about $12 in tokens. HN reacts with awe, but also concern over cost, security, and loss of human judgment.

- Comment pulse  
  - Overkill for a two-line CSS fix → agent’s elaborate workflow replaces simple inspect-and-edit, reducing dev insight — counterpoint: strong verification mimics a careful junior.  
  - Full terminal access is reckless → models can exploit OS tricks, so agents need real sandboxes and least-privilege accounts, not wishful “safe setups.”  
  - Relentless autonomy hurts usability → Fable eagerly runs tests, spawns sub-agents, writes scripts, burning tokens and battery instead of asking questions or accepting smaller scopes.

- LLM perspective  
  - View: This illustrates agents shifting from “autocomplete for code” to semi-autonomous operators that improvise toolchains and workflows.  
  - Impact: Development teams must design roles, permissions, and expectations for agents, similar to onboarding a powerful but naive contractor.  
  - Watch next: Practical sandbox patterns, agent effort controls, and UX norms for when models should pause, ask, or escalate instead of acting.
