# Claws are now a new layer on top of LLM agents

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47096253) | Link: https://twitter.com/karpathy/status/2024987174077432126

## TL;DR
"Claws" appear as a user-side orchestration layer atop LLM agents, giving them persistent identities, tools, and permissions. HN commenters split between seeing this as genuine user-controlled infrastructure versus just rebranded agent wrappers. Much discussion centers on security: OTPs, approval links, outer orchestration layers, and human-in-the-loop patterns to constrain powerful tools. Others imagine an "agent-first" internet of simple APIs instead of GUIs, while skeptics note business incentives and web history make that hard to realize.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- Claws are mostly agent rebranding → same basic functionality, lots of marketing, little novelty—counterpoint: user-owned orchestration and permissions might be a meaningful UX/security improvement.  
- Strong safety patterns are emerging → CLIs require OTPs, activity-approval links, or outer orchestration layers that ping humans before sensitive tool calls execute.  
- Agents could favor API-only services → Claws navigating simple text protocols might replace GUIs, but incumbents resist broad APIs to preserve lock-in and revenue.  

## LLM perspective
- View: Claws formalize personal-agent runtimes; success depends on transparent permissions, auditing, and easy customization, not novel LLM capabilities.  
- Impact: If standardized, they could become a de facto OS layer, mediating between cloud models, local data, and external services.  
- Watch next: concrete threat models, capability whitelists, and cross-vendor protocols for approvals and logging, analogous to OAuth scopes for agents.
