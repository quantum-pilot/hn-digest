# Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting

- Score: 213 | [HN](https://news.ycombinator.com/item?id=48995213) | Link: https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git

### TL;DR

Buzz is Block’s Apache-licensed, self-hostable attempt to unify team chat, Git repositories, workflows, search, and first-class AI agents. Humans and agents use Nostr key pairs; messages, patches, approvals, and other actions become signed, auditable events, with harnesses for Goose, Codex, and Claude Code. Despite decentralized branding, each workspace currently relies on one authoritative relay, shifting uptime, security, backups, and upgrades to operators. The unfinished v0.4.21 release drew interest as a Slack/GitHub alternative, but commenters questioned access controls, protocol scale, product scope, and durability.

### Comment pulse

- Agent permissions are core → shared assistants need precise resource ACLs and exfiltration barriers, while user-scoped agents inherit a clearer trust boundary.
- Bundling chat and Git divides opinion → shared context can align people and agents — counterpoint: integration expands complexity and migration blast radius.
- AI-built software weakens early-adopter confidence → lower creation friction suggests abandonment risk, though commenters noted neglected projects long predate LLMs.

### LLM perspective

- **View:** Cryptographic signatures establish who acted, not whether an agent’s action was authorized, safe, or contextually appropriate.
- **Impact:** Developers may replace integration glue with a shared event model, but tool substitution becomes an all-at-once organizational decision.
- **Watch next:** Test multi-relay replication, large-enterprise authorization, agent-secret isolation, recovery procedures, mobile clients, and completion of workflow approval gates.
