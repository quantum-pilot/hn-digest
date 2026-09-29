# Parley: Federated, decentralised chat that speaks plain IRC

- Score: 322 | [HN](https://news.ycombinator.com/item?id=49875913) | Link: https://git.mills.io/prologic/parley

### TL;DR

Parley is a working, unhardened proof of concept for federated chat through ordinary IRC clients. Domain instances discover email-like identities using DNS and well-known documents, exchange signed HTTPS events, peer automatically, retain searchable history, and replicate global channels; local channels stay private to an instance. Global rooms deliberately lack owners, operators, topics, and kicks, replacing them with personal or instance-level blocks. Commenters argued this makes abuse, hostile-server spam, namespace governance, and divergent network views the design’s central unresolved problems.

### Comment pulse

- Operator-free global rooms alarmed commenters → abuse decisions fall to every instance administrator or potentially troublesome shared blocklists.
- Federation creates consistency ambiguity → rooms survive instance outages, but eventual replication may leave peers with divergent membership and history.
- Open federation invites abuse → commenters questioned hostile-server spam defenses, while the README acknowledges unbounded per-account message volume.

### LLM perspective

- View: Reusing IRC clients lowers adoption friction, but decentralizing ownership also decentralizes responsibility for shared spaces.
- Impact: IRC users could gain federation without plugins, while instance operators inherit difficult moderation, discovery, and abuse responsibilities.
- Watch next: Hardening needs bounded sending, adversarial federation tests, clearer moderation workflows, per-user keys, and encrypted direct messages.
