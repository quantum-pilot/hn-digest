# DNS-Persist-01: A New Model for DNS-Based Challenge Validation

- Score: 164 | [HN](https://news.ycombinator.com/item?id=47064047) | Link: https://letsencrypt.org/2026/02/18/dns-persist-01.html

### TL;DR

Let’s Encrypt is implementing DNS-PERSIST-01, a draft ACME challenge that replaces a fresh DNS TXT token for every issuance with a standing record authorizing one CA and ACME account. This removes DNS propagation and write credentials from renewal paths, helping private hosts, IoT fleets, and batch issuance. The tradeoff shifts risk to the account key and durable DNS authorization. Scope defaults to one FQDN, with optional wildcard/subdomain policy and expiration; Pebble already supports testing, with staging planned for late Q1 and production targeted for Q2 2026.

### Comment pulse

- Operators welcomed easier certificates for non-public LAN services and fewer distributed DNS credentials.
- Publishing account identifiers may aid breach correlation — counterpoint: CAA can already expose equivalent account bindings.
- Persistent services should cache certificates and monitor expiration because CA outages and rate limits still threaten just-in-time issuance.
