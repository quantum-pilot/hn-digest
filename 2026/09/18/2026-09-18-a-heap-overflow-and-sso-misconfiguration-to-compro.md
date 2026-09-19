# A heap overflow and SSO misconfiguration to compromise OpenAI internal repos

- Score: 469 | [HN](https://news.ycombinator.com/item?id=49749656) | Link: https://www.hacktron.ai/blog/hacking-openai

### TL;DR

Hacktron researchers say they chained a libheif heap overflow in OpenAI’s Discourse forum with an OpenAI SSO flaw, taking over employee ChatGPT and Codex accounts and proving internal-repository access through a harmless Codex-created pull request. They reported the chain and stopped testing; OpenAI fixed its side within roughly 14 hours, Discourse patched and sandboxed image processing, and OpenAI paid $6,500 for the SSO finding. The team argues AI agents sharply reduced exploit-development time, making dependency patching and defense-in-depth more urgent.

### Comment pulse

- Agent-assisted exploitation changes economics → models adapted memory-corruption exploits quickly, though skilled human guidance and carefully scoped targets remained essential.
- Image decoding is excessive attack surface → commenters favor fewer accepted formats, client conversion, sandboxed processors, and strict isolation from identity systems.
- Broad offensive capability divides opinion → faster vulnerability discovery may harden software—counterpoint: deceptive CTF framing bypassed the model’s remote-target refusal.

### LLM perspective

- View: The decisive failure was compositional: a decoder bug became identity takeover and connector access through weak isolation.
- Impact: Forum users, employees, and connected GitHub, Slack, or email services faced potential cross-product compromise.
- Watch next: Rebuild Discourse images, patch libheif dependencies, sandbox decoders, audit SSO boundaries, and monitor unusual image crashes.
