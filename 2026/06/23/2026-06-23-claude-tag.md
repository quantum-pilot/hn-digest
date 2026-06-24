# Claude Tag

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48648039) | Link: https://www.anthropic.com/news/introducing-claude-tag

- TL;DR  
  Anthropic’s Claude Tag appears to be a Slack-native, shared “teammate” agent that watches channels, builds long-lived context, and can draft code and PRs. Commenters expect big token costs and potential platform lock-in, so some are building model-agnostic, cost-controlled alternatives. Others highlight problems with what Claude “learns,” from misreading marketing claims to persisting wrong assumptions. Enterprise folks debate whether permissions, privacy, and multiplayer context can be made safe, while some see strong potential for collaborative todos and project management.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Claude Tag risks high token costs and lock-in → always-on Slack parsing favors Anthropic’s stack; builders push model-agnostic agents with tight usage and spend limits.  
  - Learning quality is brittle → Claude mis-generalizes from marketing or experiments, then reuses wrong assumptions despite memory resets, forcing teams to discard generated work.  
  - Enterprise fit hinges on permissions/privacy → shared agent complicates access control; OAuth-per-user designs exist — counterpoint: LDAP-controlled Slack groups can mirror enterprise permissions cleanly.

- LLM perspective  
  - View: Multiplayer agents in chat are natural but need clear boundaries between shared workspace memory and per-user private context.  
  - Impact: If reliable, Claude Tag could shift coding, triage, and documentation into Slack-first workflows, reducing context-switching for technical teams.  
  - Watch next: Key tests: token-cost transparency, configurable retention/learning controls, fine-grained enterprise permission models, and benchmarks against cheaper open-source or local agent stacks.
