# Keyhive – Local-first access control

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45445114) | Link: https://www.inkandswitch.com/keyhive/notebook/

### TL;DR

Keyhive explores access control that travels with replicated data, works offline, and preserves familiar collaboration features without a central authorization server. It tracks capabilities and revocations through document history, then uses BeeKEM for group encryption with forward and post-compromise secrecy. BeeKEM adapts tree-based key agreement to causal, concurrent updates using standard cryptography; common operations are logarithmic, with linear worst cases. Commenters welcomed the research but challenged the claim that OAuth necessarily puts a central database on every request’s hot path.

### Comment pulse

- Architecture correction → signed OAuth access tokens can be validated offline, although the resource server still remains a centralized guard.
- Practical interest → one team evaluating Keyhive highlighted BeeKEM as a decentralized relative of TreeKEM used by MLS.
- Research appeal → readers valued Ink & Switch’s user-controlled alternative to subscription cloud architectures.

### LLM perspective

- View: Keyhive tackles the harder problem after offline sync: changing authority safely amid concurrent histories.
- Impact: Local-first applications could support sensitive collaboration without making one service the permanent trust bottleneck.
- Watch next: Formal BeeKEM analysis, adversarial audits, worst-case benchmarks, identity-layer integrations, and production deployments.
