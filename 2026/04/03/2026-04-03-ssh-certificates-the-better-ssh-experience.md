# SSH certificates: the better SSH experience

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47624811) | Link: https://jpmens.net/2026/04/03/ssh-certificates-the-better-ssh-experience/

### TL;DR

OpenSSH certificates replace per-host trust and per-user key distribution with an SSH certificate authority, not X.509. Servers trust the CA for signed user keys; clients trust it for signed host keys. Certificates expire automatically and encode principals, source networks, forced commands, and forwarding or PTY permissions, eliminating `authorized_keys` edits, TOFU prompts, and host-key-rotation alarms across managed fleets. The walkthrough includes manual setup and a prototype signer. HN agreed payoff grows with fleet churn, while ordinary keys and verified TOFU remain simpler for a few stable machines.

### Comment pulse

- Some physically verify keys or publish fingerprints internally — counterpoint: others said real-world TOFU usually means typing “yes” without checking.
- Centralized certificates add issuance infrastructure and administrative trust, worthwhile mainly when organizations control many dynamic hosts.
- Hardware-backed private keys can complement either approach; unmanaged key copying, not public-key authentication itself, enables lateral movement.

### LLM perspective

- **View:** Certificates primarily improve authorization lifecycle and fleet operations; they do not eliminate secure trust bootstrapping.
- **Impact:** Teams gain time-bounded, auditable access without distributing and later removing individual keys everywhere.
- **Watch next:** CA-key protection, separate host/user authorities, authenticated issuance, clock drift, renewal availability, serial tracking, and migration tooling.
